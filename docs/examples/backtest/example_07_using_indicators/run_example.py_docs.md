# Documentation: `examples/backtest/example_07_using_indicators/run_example.py`
**Generated:** 2025-11-15T19:40:03.839077Z
**File Size:** 3907 bytes
**Extension:** .py
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `examples/backtest/example_07_using_indicators/run_example.py`
- **Size:** 3,907 bytes
- **Lines:** 91
- **Extension:** `.py`
- **Type:** text
- **Imports:** 14

---

## Source Code

```python
#!/usr/bin/env python3
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

from decimal import Decimal

from strategy import DemoStrategy

from examples.utils.data_provider import prepare_demo_data_eurusd_futures_1min
from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.config import BacktestEngineConfig
from nautilus_trader.config import LoggingConfig
from nautilus_trader.model import Bar
from nautilus_trader.model import TraderId
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.instruments.base import Instrument
from nautilus_trader.model.objects import Money


if __name__ == "__main__":

    # ----------------------------------------------------------------------------------
    # 1. Configure and create backtest engine
    # ----------------------------------------------------------------------------------

    engine_config = BacktestEngineConfig(
        trader_id=TraderId("BACKTEST-INDICATOR-001"),  # Unique identifier for this backtest
        logging=LoggingConfig(
            log_level="INFO",  # Set to INFO to see indicator values
        ),
    )
    engine = BacktestEngine(config=engine_config)

    # ----------------------------------------------------------------------------------
    # 2. Prepare market data
    # ----------------------------------------------------------------------------------

    prepared_data: dict = prepare_demo_data_eurusd_futures_1min()
    venue_name: str = prepared_data["venue_name"]
    eurusd_instrument: Instrument = prepared_data["instrument"]
    eurusd_1min_bartype = prepared_data["bar_type"]
    eurusd_1min_bars: list[Bar] = prepared_data["bars_list"]

    # ----------------------------------------------------------------------------------
    # 3. Configure trading environment
    # ----------------------------------------------------------------------------------

    # Set up the trading venue with a margin account
    engine.add_venue(
        venue=Venue(venue_name),
        oms_type=OmsType.NETTING,  # Use a netting order management system
        account_type=AccountType.MARGIN,  # Use a margin trading account
        starting_balances=[Money(1_000_000, USD)],  # Set initial capital
        base_currency=USD,  # Account currency
        default_leverage=Decimal(1),  # No leverage (1:1)
    )

    # Register the trading instrument
    engine.add_instrument(eurusd_instrument)

    # Load historical market data
    engine.add_data(eurusd_1min_bars)

    # ----------------------------------------------------------------------------------
    # 4. Configure and run strategy
    # ----------------------------------------------------------------------------------

    # Create and register the strategy
    strategy = DemoStrategy(bar_type=eurusd_1min_bartype)
    engine.add_strategy(strategy)

    # Execute the backtest
    engine.run()

    # Clean up resources
    engine.dispose()
```


---

## Overview

This file is located at `examples/backtest/example_07_using_indicators/run_example.py` within the repository.

**Import statements:** 14


---

## Detailed Analysis

### Imports

- `from decimal import Decimal`
- `from strategy import DemoStrategy`
- `from examples.utils.data_provider import prepare_demo_data_eurusd_futures_1min`
- `from nautilus_trader.backtest.engine import BacktestEngine`
- `from nautilus_trader.config import BacktestEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.model import Bar`
- `from nautilus_trader.model import TraderId`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.enums import AccountType`
- `from nautilus_trader.model.enums import OmsType`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.instruments.base import Instrument`
- `from nautilus_trader.model.objects import Money`


---

## Usage Examples

### Importing

```python
import examples.backtest.example_07_using_indicators.run_example
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from strategy import DemoStrategy`
- `from examples.utils.data_provider import prepare_demo_data_eurusd_futures_1min`
- `from nautilus_trader.backtest.engine import BacktestEngine`
- `from nautilus_trader.config import BacktestEngineConfig`
- `from nautilus_trader.config import LoggingConfig`
- `from nautilus_trader.model import Bar`
- `from nautilus_trader.model import TraderId`
- `from nautilus_trader.model.currencies import USD`
- `from nautilus_trader.model.enums import AccountType`

*... and 4 more*

**Directory:** `examples/backtest/example_07_using_indicators`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


