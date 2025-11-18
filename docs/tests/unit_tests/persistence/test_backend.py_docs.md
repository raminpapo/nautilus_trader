# Documentation: test_backend.py

## File Metadata

- **Path**: `tests/unit_tests/persistence/test_backend.py`
- **Size**: 6,868 bytes
- **Lines**: 201
- **Language**: Python

## Original Source

```python
# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

import pandas as pd
import pytest

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.core.nautilus_pyo3 import DataBackendSession
from nautilus_trader.core.nautilus_pyo3 import NautilusDataType
from nautilus_trader.model.data import capsule_to_list
from nautilus_trader.model.objects import HIGH_PRECISION


def test_backend_session_order_book_deltas() -> None:
    # Arrange
    if HIGH_PRECISION:
        data_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "deltas.parquet"
    else:
        data_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "deltas.parquet"

    session = DataBackendSession()
    session.add_file(NautilusDataType.OrderBookDelta, "order_book_deltas", str(data_path))

    # Act
    result = session.to_query_result()

    deltas = []
    for chunk in result:
        deltas.extend(capsule_to_list(chunk))

    # Assert
    assert pd.read_parquet(data_path).shape[0] == 1_077
    assert len(deltas) == 1_077
    # TODO: deltas.parquet does not have non decreasing timestamps and so would fail the
    # is_ascending check (bad data file)


def test_backend_session_quotes() -> None:
    # Arrange
    if HIGH_PRECISION:
        data_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "quotes.parquet"
    else:
        data_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "quotes.parquet"

    session = DataBackendSession()
    session.add_file(NautilusDataType.QuoteTick, "quote_ticks", str(data_path))

    # Act
    result = session.to_query_result()

    quotes = []
    for chunk in result:
        quotes.extend(capsule_to_list(chunk))

    # TODO: Quote tick test data currently uses incorrectly scaled prices and sizes and needs repair
    # Assert
    assert len(quotes) == 9_500
    assert (
        str(quotes[-1]) == "EUR/USD.SIM,112.13000,112.13200,10000000,10000000,1577919652000000125"
    )
    is_ascending = all(quotes[i].ts_init <= quotes[i + 1].ts_init for i in range(len(quotes) - 1))
    assert is_ascending


def test_backend_session_trades() -> None:
    # Arrange
    if HIGH_PRECISION:
        data_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "trades.parquet"
    else:
        data_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "trades.parquet"

    session = DataBackendSession()
    session.add_file(NautilusDataType.TradeTick, "trade_ticks", str(data_path))

    # Act
    result = session.to_query_result()

    trades = []
    for chunk in result:
        trades.extend(capsule_to_list(chunk))

    # Assert
    assert len(trades) == 100
    is_ascending = all(trades[i].ts_init <= trades[i + 1].ts_init for i in range(len(trades) - 1))
    assert is_ascending


def test_backend_session_bars() -> None:
    # Arrange
    if HIGH_PRECISION:
        data_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "bars.parquet"
    else:
        data_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "bars.parquet"

    session = DataBackendSession()
    session.add_file(NautilusDataType.Bar, "bars_01", str(data_path))

    # Act
    result = session.to_query_result()

    bars = []
    for chunk in result:
        bars.extend(capsule_to_list(chunk))

    # Assert
    assert len(bars) == 10
    is_ascending = all(bars[i].ts_init <= bars[i + 1].ts_init for i in range(len(bars) - 1))
    assert is_ascending


def test_backend_session_multiple_types() -> None:
    # Arrange
    if HIGH_PRECISION:
        trades_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "trades.parquet"
        quotes_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "quotes.parquet"
    else:
        trades_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "trades.parquet"
        quotes_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "quotes.parquet"

    session = DataBackendSession()
    session.add_file(NautilusDataType.TradeTick, "trades_01", str(trades_path))
    session.add_file(NautilusDataType.QuoteTick, "quotes_01", str(quotes_path))

    # Act
    result = session.to_query_result()

    data = []
    for chunk in result:
        data.extend(capsule_to_list(chunk))

    # Assert
    assert len(data) == 9_600
    is_ascending = all(data[i].ts_init <= data[i + 1].ts_init for i in range(len(data) - 1))
    assert is_ascending


def test_backend_session_register_object_store_from_uri_local_file() -> None:
    """
    Test registering object store from local file URI.
    """
    # Arrange
    if HIGH_PRECISION:
        data_path = TEST_DATA_DIR / "nautilus" / "128-bit" / "trades.parquet"
    else:
        data_path = TEST_DATA_DIR / "nautilus" / "64-bit" / "trades.parquet"

    session = DataBackendSession()

    # Act - register object store from local file URI
    file_uri = f"file://{data_path.parent}"
    session.register_object_store_from_uri(file_uri)

    # Add file using the registered object store
    session.add_file(NautilusDataType.TradeTick, "trade_ticks", str(data_path))
    result = session.to_query_result()

    trades = []
    for chunk in result:
        trades.extend(capsule_to_list(chunk))

    # Assert
    assert len(trades) == 100
    is_ascending = all(trades[i].ts_init <= trades[i + 1].ts_init for i in range(len(trades) - 1))
    assert is_ascending


def test_backend_session_register_object_store_from_uri_invalid_uri() -> None:
    """
    Test registering object store from invalid URI raises appropriate error.
    """
    # Arrange
    session = DataBackendSession()

    # Act & Assert - invalid URI should raise an error
    with pytest.raises(Exception):  # The specific exception type may vary
        session.register_object_store_from_uri("invalid://not-a-real-uri")


def test_backend_session_register_object_store_from_uri_nonexistent_path() -> None:
    """
    Test registering object store from non-existent path URI.
    """
    # Arrange
    session = DataBackendSession()

    # Act & Assert - non-existent path should raise an error
    with pytest.raises(Exception):  # The specific exception type may vary
        session.register_object_store_from_uri("file:///nonexistent/path")

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`test_backend_session_order_book_deltas()`**: Function defined in this file
- **`test_backend_session_quotes()`**: Function defined in this file
- **`test_backend_session_trades()`**: Function defined in this file
- **`test_backend_session_bars()`**: Function defined in this file
- **`test_backend_session_multiple_types()`**: Function defined in this file
- **`test_backend_session_register_object_store_from_uri_local_file()`**: Function defined in this file
- **`test_backend_session_register_object_store_from_uri_invalid_uri()`**: Function defined in this file
- **`test_backend_session_register_object_store_from_uri_nonexistent_path()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `test_backend_session_bars`, `test_backend_session_multiple_types`, `test_backend_session_order_book_deltas`, `test_backend_session_quotes`, `test_backend_session_register_object_store_from_uri_invalid_uri`, `test_backend_session_register_object_store_from_uri_local_file`, `test_backend_session_register_object_store_from_uri_nonexistent_path`, `test_backend_session_trades`
**Imports**: `nautilus_trader`, `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.model.data`, `nautilus_trader.model.objects`, `pandas`, `pytest`

## Related Files

This file is located in `tests/unit_tests/persistence/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/persistence/test_backend.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.696382Z*
