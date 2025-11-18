# Documentation: test_wranglers_v2.py

## File Metadata

- **Path**: `tests/unit_tests/persistence/test_wranglers_v2.py`
- **Size**: 2,716 bytes
- **Lines**: 68
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

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.persistence.wranglers_v2 import QuoteTickDataWranglerV2
from nautilus_trader.persistence.wranglers_v2 import TradeTickDataWranglerV2
from nautilus_trader.test_kit.providers import TestInstrumentProvider


def test_quote_tick_data_wrangler() -> None:
    # Arrange
    path = TEST_DATA_DIR / "truefx" / "audusd-ticks.csv"
    df = pd.read_csv(path)
    instrument = TestInstrumentProvider.default_fx_ccy("AUD/USD")

    # Act
    wrangler = QuoteTickDataWranglerV2.from_instrument(instrument)
    pyo3_quotes = wrangler.from_pandas(df)

    quotes = QuoteTick.from_pyo3_list(pyo3_quotes)

    # Assert
    assert len(pyo3_quotes) == 100_000
    assert len(quotes) == 100_000
    assert isinstance(quotes[0], QuoteTick)
    assert str(pyo3_quotes[0]) == "AUD/USD.SIM,0.67067,0.67070,1000000,1000000,1580398089820000000"
    assert str(pyo3_quotes[-1]) == "AUD/USD.SIM,0.66934,0.66938,1000000,1000000,1580504394501000000"


def test_trade_tick_data_wrangler() -> None:
    # Arrange
    path = TEST_DATA_DIR / "binance" / "ethusdt-trades.csv"
    df = pd.read_csv(path)
    instrument = TestInstrumentProvider.ethusdt_binance()

    # Act
    wrangler = TradeTickDataWranglerV2.from_instrument(instrument)
    pyo3_trades = wrangler.from_pandas(df)

    trades = TradeTick.from_pyo3_list(pyo3_trades)

    # Assert
    assert len(pyo3_trades) == 69806
    assert len(trades) == 69806
    assert isinstance(trades[0], TradeTick)
    assert (
        str(pyo3_trades[0]) == "ETHUSDT.BINANCE,423.76,2.67900,BUYER,148568980,1597399200223000000"
    )
    assert (
        str(pyo3_trades[-1]) == "ETHUSDT.BINANCE,426.89,0.16100,BUYER,148638715,1597417198693000000"
    )

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`test_quote_tick_data_wrangler()`**: Function defined in this file
- **`test_trade_tick_data_wrangler()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `test_quote_tick_data_wrangler`, `test_trade_tick_data_wrangler`
**Imports**: `nautilus_trader`, `nautilus_trader.model.data`, `nautilus_trader.persistence.wranglers_v2`, `nautilus_trader.test_kit.providers`, `pandas`

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
pytest tests/unit_tests/persistence/test_wranglers_v2.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.720127Z*
