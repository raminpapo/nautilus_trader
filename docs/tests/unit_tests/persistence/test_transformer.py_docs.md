# Documentation: test_transformer.py

## File Metadata

- **Path**: `tests/unit_tests/persistence/test_transformer.py`
- **Size**: 6,457 bytes
- **Lines**: 189
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

from io import BytesIO

import pandas as pd
import pyarrow as pa
import pytest

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import IndexPriceUpdate
from nautilus_trader.model.data import MarkPriceUpdate
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.objects import FIXED_PRECISION_BYTES
from nautilus_trader.persistence.wranglers import TradeTickDataWrangler
from nautilus_trader.persistence.wranglers_v2 import QuoteTickDataWranglerV2
from nautilus_trader.test_kit.providers import TestDataProvider
from nautilus_trader.test_kit.providers import TestInstrumentProvider


def test_pyo3_quotes_to_record_batch_reader() -> None:
    # Arrange
    path = TEST_DATA_DIR / "truefx" / "audusd-ticks.csv"
    df = pd.read_csv(path)
    instrument = TestInstrumentProvider.default_fx_ccy("AUD/USD")

    # Act
    wrangler = QuoteTickDataWranglerV2.from_instrument(instrument)
    quotes = wrangler.from_pandas(df)

    # Act
    batch_bytes = nautilus_pyo3.quotes_to_arrow_record_batch_bytes(quotes)
    reader = pa.ipc.open_stream(BytesIO(batch_bytes))

    # Assert
    assert len(quotes) == 100_000
    assert len(reader.read_all()) == len(quotes)
    reader.close()


def test_legacy_trades_to_record_batch_reader() -> None:
    # Arrange
    instrument = TestInstrumentProvider.ethusdt_binance()
    wrangler = TradeTickDataWrangler(instrument=instrument)
    trades = wrangler.process(TestDataProvider().read_csv_ticks("binance/ethusdt-trades.csv"))

    # Act
    batch_bytes = nautilus_pyo3.pyobjects_to_arrow_record_batch_bytes(trades)
    reader = pa.ipc.open_stream(BytesIO(batch_bytes))

    # Assert
    assert len(trades) == 69_806
    assert len(reader.read_all()) == len(trades)
    reader.close()


def test_legacy_deltas_to_record_batch_reader() -> None:
    # Arrange
    deltas = [
        OrderBookDelta.from_dict(
            {
                "action": "CLEAR",
                "flags": 0,
                "instrument_id": "1.166564490-237491-0.0.BETFAIR",
                "order": {
                    "order_id": 0,
                    "price": "0",
                    "side": "NO_ORDER_SIDE",
                    "size": "0",
                },
                "sequence": 0,
                "ts_event": 1576840503572000000,
                "ts_init": 1576840503572000000,
                "type": "OrderBookDelta",
            },
        ),
    ]

    # Act
    batch_bytes = nautilus_pyo3.pyobjects_to_arrow_record_batch_bytes(deltas)
    reader = pa.ipc.open_stream(BytesIO(batch_bytes))

    # Assert
    assert len(deltas) == 1
    assert len(reader.read_all()) == len(deltas)
    reader.close()


def test_get_schema_map_with_unsupported_type() -> None:
    # Arrange, Act, Assert
    with pytest.raises(TypeError):
        nautilus_pyo3.get_arrow_schema_map(str)


@pytest.mark.parametrize(
    ("data_type", "expected_map"),
    [
        [
            OrderBookDelta,
            {
                "action": "UInt8",
                "side": "UInt8",
                "price": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "size": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "order_id": "UInt64",
                "sequence": "UInt64",
                "flags": "UInt8",
                "ts_event": "UInt64",
                "ts_init": "UInt64",
            },
        ],
        [
            QuoteTick,
            {
                "bid_price": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "ask_price": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "bid_size": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "ask_size": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "ts_event": "UInt64",
                "ts_init": "UInt64",
            },
        ],
        [
            TradeTick,
            {
                "price": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "size": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "aggressor_side": "UInt8",
                "trade_id": "Utf8",
                "ts_event": "UInt64",
                "ts_init": "UInt64",
            },
        ],
        [
            Bar,
            {
                "open": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "high": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "low": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "close": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "volume": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "ts_event": "UInt64",
                "ts_init": "UInt64",
            },
        ],
        [
            MarkPriceUpdate,
            {
                "value": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "ts_event": "UInt64",
                "ts_init": "UInt64",
            },
        ],
        [
            IndexPriceUpdate,
            {
                "value": f"FixedSizeBinary({FIXED_PRECISION_BYTES})",
                "ts_event": "UInt64",
                "ts_init": "UInt64",
            },
        ],
    ],
)
def test_get_schema_map_for_all_implemented_types(
    data_type: type,
    expected_map: dict[str, str],
) -> None:
    # Arrange, Act
    schema_map = nautilus_pyo3.get_arrow_schema_map(data_type)

    # Assert
    assert schema_map == expected_map

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`test_pyo3_quotes_to_record_batch_reader()`**: Function defined in this file
- **`test_legacy_trades_to_record_batch_reader()`**: Function defined in this file
- **`test_legacy_deltas_to_record_batch_reader()`**: Function defined in this file
- **`test_get_schema_map_with_unsupported_type()`**: Function defined in this file
- **`test_get_schema_map_for_all_implemented_types()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Functions**: `test_get_schema_map_for_all_implemented_types`, `test_get_schema_map_with_unsupported_type`, `test_legacy_deltas_to_record_batch_reader`, `test_legacy_trades_to_record_batch_reader`, `test_pyo3_quotes_to_record_batch_reader`
**Imports**: `io`, `nautilus_trader`, `nautilus_trader.core`, `nautilus_trader.model.data`, `nautilus_trader.model.objects`, `nautilus_trader.persistence.wranglers`, `nautilus_trader.persistence.wranglers_v2`, `nautilus_trader.test_kit.providers`, `pandas`, `pyarrow`, `pytest`

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
pytest tests/unit_tests/persistence/test_transformer.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.717149Z*
