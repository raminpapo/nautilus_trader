# Documentation: component.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/stubs/component.py`
- **Size**: 5,926 bytes
- **Lines**: 159
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


from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.backtest.engine import BacktestEngineConfig
from nautilus_trader.backtest.models import FillModel
from nautilus_trader.backtest.node import BacktestNode
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.common.factories import OrderFactory
from nautilus_trader.common.functions import get_event_loop
from nautilus_trader.core.data import Data
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.instruments import Instrument
from nautilus_trader.model.objects import Currency
from nautilus_trader.model.objects import Money
from nautilus_trader.persistence.catalog.parquet import ParquetDataCatalog
from nautilus_trader.portfolio.portfolio import Portfolio
from nautilus_trader.test_kit.mocks.engines import MockLiveDataEngine
from nautilus_trader.test_kit.mocks.engines import MockLiveExecutionEngine
from nautilus_trader.test_kit.mocks.engines import MockLiveRiskEngine
from nautilus_trader.test_kit.stubs.config import TestConfigStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs
from nautilus_trader.trading.strategy import Strategy


class TestComponentStubs:
    @staticmethod
    def clock() -> LiveClock:
        return LiveClock()

    @staticmethod
    def msgbus() -> MessageBus:
        return MessageBus(
            trader_id=TestIdStubs.trader_id(),
            clock=TestComponentStubs.clock(),
        )

    @staticmethod
    def cache() -> Cache:
        return Cache(database=None)

    @staticmethod
    def portfolio() -> Portfolio:
        return Portfolio(
            msgbus=TestComponentStubs.msgbus(),
            clock=TestComponentStubs.clock(),
            cache=TestComponentStubs.cache(),
        )

    @staticmethod
    def trading_strategy() -> Strategy:
        strategy = Strategy()
        strategy.register(
            trader_id=TraderId("TESTER-000"),
            portfolio=TestComponentStubs.portfolio(),
            msgbus=TestComponentStubs.msgbus(),
            cache=TestComponentStubs.cache(),
            clock=TestComponentStubs.clock(),
        )
        return strategy

    @staticmethod
    def mock_live_data_engine() -> MockLiveDataEngine:
        loop = get_event_loop()

        return MockLiveDataEngine(
            loop=loop,
            msgbus=TestComponentStubs.msgbus(),
            cache=TestComponentStubs.cache(),
            clock=TestComponentStubs.clock(),
        )

    @staticmethod
    def mock_live_exec_engine() -> MockLiveExecutionEngine:
        loop = get_event_loop()

        return MockLiveExecutionEngine(
            loop=loop,
            msgbus=TestComponentStubs.msgbus(),
            cache=TestComponentStubs.cache(),
            clock=TestComponentStubs.clock(),
        )

    @staticmethod
    def mock_live_risk_engine() -> MockLiveRiskEngine:
        loop = get_event_loop()

        return MockLiveRiskEngine(
            loop=loop,
            portfolio=TestComponentStubs.portfolio(),
            msgbus=TestComponentStubs.msgbus(),
            cache=TestComponentStubs.cache(),
            clock=TestComponentStubs.clock(),
        )

    @staticmethod
    def order_factory() -> OrderFactory:
        return OrderFactory(
            trader_id=TestIdStubs.trader_id(),
            strategy_id=TestIdStubs.strategy_id(),
            clock=TestComponentStubs.clock(),
        )

    @staticmethod
    def backtest_node(
        catalog: ParquetDataCatalog,
        engine_config: BacktestEngineConfig,
    ) -> BacktestNode:
        run_config = TestConfigStubs.backtest_run_config(catalog=catalog, config=engine_config)
        node = BacktestNode(configs=[run_config])
        return node

    @staticmethod
    def backtest_engine(
        config: BacktestEngineConfig | None = None,
        instrument: Instrument | None = None,
        ticks: list[Data] | None = None,
        venue: Venue | None = None,
        oms_type: OmsType | None = None,
        account_type: AccountType | None = None,
        base_currency: Currency | None = None,
        starting_balances: list[Money] | None = None,
        fill_model: FillModel | None = None,
    ) -> BacktestEngine:
        engine = BacktestEngine(config=config)
        engine.add_venue(
            venue=venue or Venue("SIM"),
            oms_type=oms_type or OmsType.HEDGING,
            account_type=account_type or AccountType.MARGIN,
            base_currency=base_currency or USD,
            starting_balances=starting_balances or [Money(1_000_000, USD)],
            fill_model=fill_model or FillModel(),
        )
        engine.add_instrument(instrument)

        if ticks:
            engine.add_data(ticks)

        return engine

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestComponentStubs`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 20


**Classs**: `TestComponentStubs`
**Imports**: `nautilus_trader.backtest.engine`, `nautilus_trader.backtest.models`, `nautilus_trader.backtest.node`, `nautilus_trader.cache.cache`, `nautilus_trader.common.component`, `nautilus_trader.common.factories`, `nautilus_trader.common.functions`, `nautilus_trader.core.data`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.instruments`, `nautilus_trader.model.objects`, `nautilus_trader.persistence.catalog.parquet`, `nautilus_trader.portfolio.portfolio`, `nautilus_trader.test_kit.mocks.engines`, `nautilus_trader.test_kit.stubs.config`, `nautilus_trader.test_kit.stubs.identifiers`, `nautilus_trader.trading.strategy`

## Related Files

This file is located in `nautilus_trader/test_kit/stubs/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/stubs/component.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.003636Z*
