# Documentation: test_betfair_backtest.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/test_betfair_backtest.py`
- **Size**: 4,008 bytes
- **Lines**: 101
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

from nautilus_trader.adapters.betfair.constants import BETFAIR_VENUE
from nautilus_trader.adapters.betfair.parsing.core import BetfairParser
from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.backtest.engine import BacktestEngineConfig
from nautilus_trader.backtest.engine import Decimal
from nautilus_trader.config import LoggingConfig
from nautilus_trader.examples.strategies.orderbook_imbalance import OrderBookImbalance
from nautilus_trader.examples.strategies.orderbook_imbalance import OrderBookImbalanceConfig
from nautilus_trader.model.currencies import GBP
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import BookType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.objects import Money
from tests.integration_tests.adapters.betfair.test_kit import BetfairDataProvider
from tests.integration_tests.adapters.betfair.test_kit import betting_instrument


def test_betfair_backtest():
    # Arrange
    config = BacktestEngineConfig(
        trader_id=TraderId("BACKTESTER-001"),
        logging=LoggingConfig(bypass_logging=True),
    )

    # Build the backtest engine
    engine = BacktestEngine(config=config)

    # Add a trading venue (multiple venues possible)
    engine.add_venue(
        venue=BETFAIR_VENUE,
        oms_type=OmsType.NETTING,
        account_type=AccountType.CASH,  # Spot CASH account (not for perpetuals or futures)
        base_currency=GBP,  # Multi-currency account
        starting_balances=[Money(100_000, GBP)],
        book_type=BookType.L1_MBP,
    )

    # Add instruments
    min_notional = Money(1, GBP)
    instruments = [
        betting_instrument(
            market_id="1-166811431",
            selection_id=19248890,
            selection_handicap=None,
        ),
        betting_instrument(
            market_id="1-166811431",
            selection_id=38848248,
            selection_handicap=None,
        ),
    ]
    engine.add_instrument(instruments[0])
    engine.add_instrument(instruments[1])

    # Add data
    raw = list(BetfairDataProvider.market_updates())
    parser = BetfairParser(currency="GBP")
    updates = [upd for update in raw for upd in parser.parse(update, min_notional=min_notional)]
    engine.add_data(updates, client_id=ClientId("BETFAIR"))

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

    # Act
    engine.run()

    # Assert
    account = engine.trader.generate_account_report(BETFAIR_VENUE)
    fills = engine.trader.generate_order_fills_report()
    positions = engine.trader.generate_positions_report()
    assert account.iloc[-1]["total"] == "98257.24"
    assert len(fills) == 1049
    assert len(positions) == 4

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_betfair_backtest()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `test_betfair_backtest`
**Imports**: `nautilus_trader.adapters.betfair.constants`, `nautilus_trader.adapters.betfair.parsing.core`, `nautilus_trader.backtest.engine`, `nautilus_trader.config`, `nautilus_trader.examples.strategies.orderbook_imbalance`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `tests.integration_tests.adapters.betfair.test_kit`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/test_betfair_backtest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.558218Z*
