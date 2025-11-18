# Documentation: betfair_backtest_orderbook_imbalance.py

## File Metadata

- **Path**: `examples/backtest/betfair_backtest_orderbook_imbalance.py`
- **Size**: 4,182 bytes
- **Lines**: 115
- **Language**: Python

## Original Source

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

import time
from decimal import Decimal

import pandas as pd

from nautilus_trader.adapters.betfair import BETFAIR_CLIENT_ID
from nautilus_trader.adapters.betfair import BETFAIR_VENUE
from nautilus_trader.adapters.betfair import BetfairParser
from nautilus_trader.backtest.config import BacktestEngineConfig
from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.examples.strategies.orderbook_imbalance import OrderBookImbalance
from nautilus_trader.examples.strategies.orderbook_imbalance import OrderBookImbalanceConfig
from nautilus_trader.model.currencies import GBP
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import BookType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.objects import Money
from tests.integration_tests.adapters.betfair.test_kit import BetfairDataProvider
from tests.integration_tests.adapters.betfair.test_kit import betting_instrument


if __name__ == "__main__":
    # Configure backtest engine
    config = BacktestEngineConfig(trader_id=TraderId("BACKTESTER-001"))

    # Build the backtest engine
    engine = BacktestEngine(config=config)

    # Add a trading venue (multiple venues possible)
    engine.add_venue(
        venue=BETFAIR_VENUE,
        oms_type=OmsType.NETTING,
        account_type=AccountType.CASH,  # Spot CASH account (not for perpetuals or futures)
        base_currency=GBP,  # Multi-currency account
        starting_balances=[Money(100_000, GBP)],
        book_type=BookType.L2_MBP,
    )

    # Add instruments
    instruments = [
        betting_instrument(
            market_id="1-166811431",
            selection_id=19248890,
            selection_handicap=0.0,
        ),
        betting_instrument(
            market_id="1-166811431",
            selection_id=38848248,
            selection_handicap=0.0,
        ),
    ]
    engine.add_instrument(instruments[0])
    engine.add_instrument(instruments[1])

    # Add data
    raw = list(BetfairDataProvider.market_updates())
    parser = BetfairParser(currency=GBP.code)
    updates = [upd for update in raw for upd in parser.parse(update)]
    engine.add_data(updates, client_id=BETFAIR_CLIENT_ID)

    # Configure your strategy
    strategies = [
        OrderBookImbalance(
            config=OrderBookImbalanceConfig(
                instrument_id=instrument.id,
                max_trade_size=Decimal(10),
                order_id_tag=instrument.selection_id,
            ),
        )
        for instrument in instruments
    ]
    engine.add_strategies(strategies)

    time.sleep(0.1)
    input("Press Enter to continue...")

    # Run the engine (from start to end of data)
    engine.run()

    # Optionally view reports
    with pd.option_context(
        "display.max_rows",
        100,
        "display.max_columns",
        None,
        "display.width",
        300,
    ):
        print(engine.trader.generate_account_report(BETFAIR_VENUE))
        print(engine.trader.generate_order_fills_report())
        print(engine.trader.generate_positions_report())

    # For repeated backtest runs make sure to reset the engine
    engine.reset()

    # Good practice to dispose of the object
    engine.dispose()

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 12


**Imports**: `decimal`, `nautilus_trader.adapters.betfair`, `nautilus_trader.backtest.config`, `nautilus_trader.backtest.engine`, `nautilus_trader.examples.strategies.orderbook_imbalance`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `pandas`, `tests.integration_tests.adapters.betfair.test_kit`, `time`

## Related Files

This file is located in `examples/backtest/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/betfair_backtest_orderbook_imbalance.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.203631Z*
