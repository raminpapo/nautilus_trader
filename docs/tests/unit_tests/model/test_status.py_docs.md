# Documentation: test_status.py

## File Metadata

- **Path**: `tests/unit_tests/model/test_status.py`
- **Size**: 4,637 bytes
- **Lines**: 121
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
from nautilus_trader.model.data import InstrumentClose
from nautilus_trader.model.data import InstrumentStatus
from nautilus_trader.model.enums import InstrumentCloseType
from nautilus_trader.model.enums import MarketStatusAction
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.objects import Price
from nautilus_trader.test_kit.providers import TestInstrumentProvider


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestVenue:
    def test_instrument_status(self):
        # Arrange
        status = InstrumentStatus(
            instrument_id=InstrumentId.from_str("MSFT.XNAS"),
            action=MarketStatusAction.TRADING,
            ts_event=0,
            ts_init=0,
            is_trading=True,
            is_quoting=True,
            is_short_sell_restricted=False,
        )

        # Act, Assert
        assert InstrumentStatus.from_dict(InstrumentStatus.to_dict(status)) == status
        assert (
            repr(status)
            == "InstrumentStatus(instrument_id=MSFT.XNAS, action=TRADING, reason=None, trading_event=None, is_trading=True, is_quoting=True, is_short_sell_restricted=False, ts_event=0)"
        )

    def test_instrument_status_to_pyo3(self):
        # Arrange
        status = InstrumentStatus(
            instrument_id=InstrumentId.from_str("ESM4.GLBX"),
            action=MarketStatusAction.TRADING,
            ts_event=1,
            ts_init=2,
            reason="Scheduled",
            trading_event=None,
            is_trading=True,
            is_quoting=True,
            is_short_sell_restricted=None,
        )

        # Act
        pyo3_status = status.to_pyo3()

        # Assert
        assert isinstance(pyo3_status, nautilus_pyo3.InstrumentStatus)
        assert pyo3_status.action == nautilus_pyo3.MarketStatusAction.TRADING
        assert pyo3_status.ts_event == 1
        assert pyo3_status.ts_init == 2
        assert pyo3_status.reason == "Scheduled"
        assert pyo3_status.trading_event is None
        assert pyo3_status.is_trading
        assert pyo3_status.is_quoting
        assert pyo3_status.is_short_sell_restricted is None

    def test_instrument_status_from_pyo3(self):
        # Arrange
        pyo3_status = nautilus_pyo3.InstrumentStatus(
            instrument_id=nautilus_pyo3.InstrumentId.from_str("ESM4.GLBX"),
            action=nautilus_pyo3.MarketStatusAction.TRADING,
            ts_event=1,
            ts_init=2,
            reason="Scheduled",
            trading_event=None,
            is_trading=True,
            is_quoting=True,
            is_short_sell_restricted=None,
        )

        # Act
        status = InstrumentStatus.from_pyo3(pyo3_status)

        # Assert
        assert isinstance(status, InstrumentStatus)
        assert status.action == MarketStatusAction.TRADING
        assert status.ts_event == 1
        assert status.ts_init == 2
        assert status.reason == "Scheduled"
        assert status.trading_event is None
        assert status.is_trading
        assert status.is_quoting
        assert status.is_short_sell_restricted is None

    def test_instrument_close(self):
        # Arrange
        update = InstrumentClose(
            instrument_id=InstrumentId.from_str("BTCUSDT.BINANCE"),
            close_price=Price(100.0, precision=0),
            close_type=InstrumentCloseType.CONTRACT_EXPIRED,
            ts_event=0,
            ts_init=0,
        )

        # Act, Assert
        assert InstrumentClose.from_dict(InstrumentClose.to_dict(update)) == update
        assert (
            repr(update)
            == "InstrumentClose(instrument_id=BTCUSDT.BINANCE, close_price=100, close_type=CONTRACT_EXPIRED)"
        )

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestVenue`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Classs**: `TestVenue`
**Imports**: `nautilus_trader.core`, `nautilus_trader.model.data`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `nautilus_trader.test_kit.providers`

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
pytest tests/unit_tests/model/test_status.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.677828Z*
