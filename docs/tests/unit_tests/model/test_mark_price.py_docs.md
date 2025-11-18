# Documentation: test_mark_price.py

## File Metadata

- **Path**: `tests/unit_tests/model/test_mark_price.py`
- **Size**: 3,780 bytes
- **Lines**: 115
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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.data import MarkPriceUpdate
from nautilus_trader.model.objects import Price
from nautilus_trader.test_kit.providers import TestInstrumentProvider


BTCUSDT_BINANCE = TestInstrumentProvider.btcusdt_binance()


class TestTradeTick:
    def test_fully_qualified_name(self):
        # Arrange, Act, Assert
        assert (
            MarkPriceUpdate.fully_qualified_name() == "nautilus_trader.model.data:MarkPriceUpdate"
        )

    def test_hash_str_and_repr(self):
        # Arrange
        mark_price = MarkPriceUpdate(
            instrument_id=BTCUSDT_BINANCE.id,
            value=Price.from_str("100_000.00"),
            ts_event=1,
            ts_init=2,
        )

        # Act, Assert
        assert isinstance(hash(mark_price), int)
        assert str(mark_price) == "BTCUSDT.BINANCE,100000.00,1,2"
        assert repr(mark_price) == "MarkPriceUpdate(BTCUSDT.BINANCE,100000.00,1,2)"

    def test_to_dict_returns_expected_dict(self):
        # Arrange
        mark_price = MarkPriceUpdate(
            instrument_id=BTCUSDT_BINANCE.id,
            value=Price.from_str("100_000.00"),
            ts_event=1,
            ts_init=2,
        )

        # Act
        result = MarkPriceUpdate.to_dict(mark_price)

        # Assert
        assert result == {
            "type": "MarkPriceUpdate",
            "instrument_id": "BTCUSDT.BINANCE",
            "value": "100000.00",
            "ts_event": 1,
            "ts_init": 2,
        }

    def test_from_dict_returns_expected_tick(self):
        # Arrange
        mark_price = MarkPriceUpdate(
            instrument_id=BTCUSDT_BINANCE.id,
            value=Price.from_str("100_000.00"),
            ts_event=1,
            ts_init=2,
        )

        # Act
        result = MarkPriceUpdate.from_dict(MarkPriceUpdate.to_dict(mark_price))

        # Assert
        assert result == mark_price

    def test_from_pyo3(self):
        # Arrange
        mark_price = MarkPriceUpdate(
            instrument_id=BTCUSDT_BINANCE.id,
            value=Price.from_str("100_000.00"),
            ts_event=1,
            ts_init=2,
        )

        # Act
        pyo3_mark_price = mark_price.to_pyo3()
        result = MarkPriceUpdate.from_pyo3(pyo3_mark_price)

        # Assert
        assert result == mark_price

    def test_to_pyo3(self):
        # Arrange
        mark_price = MarkPriceUpdate(
            instrument_id=BTCUSDT_BINANCE.id,
            value=Price.from_str("100_000.00"),
            ts_event=1,
            ts_init=2,
        )

        # Act
        pyo3_mark_price = mark_price.to_pyo3()

        # Assert
        assert isinstance(pyo3_mark_price, nautilus_pyo3.MarkPriceUpdate)
        assert pyo3_mark_price.value == nautilus_pyo3.Price.from_str("100_000.00")
        assert pyo3_mark_price.ts_event == 1
        assert pyo3_mark_price.ts_init == 2

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestTradeTick`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `TestTradeTick`
**Imports**: `nautilus_trader.core`, `nautilus_trader.model.data`, `nautilus_trader.model.objects`, `nautilus_trader.test_kit.providers`

## Related Files

This file is located in `tests/unit_tests/model/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/model/test_mark_price.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.623484Z*
