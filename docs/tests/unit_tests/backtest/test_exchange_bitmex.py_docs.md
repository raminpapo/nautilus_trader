# Documentation: `tests/unit_tests/backtest/test_exchange_bitmex.py`
**Generated:** 2025-11-15T19:40:08.964696Z
**File Size:** 6901 bytes
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

- **Path:** `tests/unit_tests/backtest/test_exchange_bitmex.py`
- **Size:** 6,901 bytes
- **Lines:** 192
- **Extension:** `.py`
- **Type:** text
- **Imports:** 27
- **Classes:** 1
- **Functions:** 2

---

## Source Code

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

from decimal import Decimal

from nautilus_trader.backtest.engine import SimulatedExchange
from nautilus_trader.backtest.execution_client import BacktestExecClient
from nautilus_trader.backtest.models import FillModel
from nautilus_trader.backtest.models import LatencyModel
from nautilus_trader.backtest.models import MakerTakerFeeModel
from nautilus_trader.common.component import MessageBus
from nautilus_trader.common.component import TestClock
from nautilus_trader.data.engine import DataEngine
from nautilus_trader.execution.engine import ExecutionEngine
from nautilus_trader.model.currencies import BTC
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import LiquiditySide
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Money
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.portfolio.portfolio import Portfolio
from nautilus_trader.risk.engine import RiskEngine
from nautilus_trader.test_kit.mocks.strategies import MockStrategy
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.component import TestComponentStubs
from nautilus_trader.test_kit.stubs.data import TestDataStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


XBTUSD_BITMEX = TestInstrumentProvider.xbtusd_bitmex()


class TestBitmexExchange:
    """
    Various tests which are more specific to market making with maker rebates.
    """

    def setup(self):
        # Fixture Setup
        self.strategies = [MockStrategy(TestDataStubs.bartype_btcusdt_binance_100tick_last())]

        self.clock = TestClock()
        self.trader_id = TestIdStubs.trader_id()

        self.msgbus = MessageBus(
            trader_id=self.trader_id,
            clock=self.clock,
        )

        self.cache = TestComponentStubs.cache()

        self.portfolio = Portfolio(
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.data_engine = DataEngine(
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.exec_engine = ExecutionEngine(
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.risk_engine = RiskEngine(
            portfolio=self.portfolio,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.exchange = SimulatedExchange(
            venue=Venue("BITMEX"),
            oms_type=OmsType.NETTING,
            account_type=AccountType.MARGIN,
            base_currency=BTC,
            starting_balances=[Money(20, BTC)],
            default_leverage=Decimal(50),
            leverages={},
            portfolio=self.portfolio,
            msgbus=self.msgbus,
            cache=self.cache,
            modules=[],
            fill_model=FillModel(),
            fee_model=MakerTakerFeeModel(),
            clock=self.clock,
            latency_model=LatencyModel(0),
        )
        self.exchange.add_instrument(XBTUSD_BITMEX)

        self.exec_client = BacktestExecClient(
            exchange=self.exchange,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        # Wire up components
        self.exec_engine.register_client(self.exec_client)
        self.exchange.register_client(self.exec_client)

        self.cache.add_instrument(XBTUSD_BITMEX)

        self.strategy = MockStrategy(bar_type=TestDataStubs.bartype_btcusdt_binance_100tick_last())
        self.strategy.register(
            trader_id=self.trader_id,
            portfolio=self.portfolio,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.exchange.reset()
        self.data_engine.start()
        self.exec_engine.start()
        self.strategy.start()

    def test_commission_maker_taker_order(self):
        # Arrange
        # Prepare market
        quote1 = QuoteTick(
            instrument_id=XBTUSD_BITMEX.id,
            bid_price=Price.from_str("11493.0"),
            ask_price=Price.from_str("11493.5"),
            bid_size=Quantity.from_int(1_500_000),
            ask_size=Quantity.from_int(1_500_000),
            ts_event=0,
            ts_init=0,
        )

        self.data_engine.process(quote1)
        self.exchange.process_quote_tick(quote1)

        order_market = self.strategy.order_factory.market(
            XBTUSD_BITMEX.id,
            OrderSide.BUY,
            Quantity.from_int(100_000),
        )

        order_limit = self.strategy.order_factory.limit(
            XBTUSD_BITMEX.id,
            OrderSide.BUY,
            Quantity.from_int(100_000),
            Price.from_str("11492.5"),
        )

        # Act
        self.strategy.submit_order(order_market)
        self.exchange.process(0)
        self.strategy.submit_order(order_limit)
        self.exchange.process(0)

        quote2 = QuoteTick(
            instrument_id=XBTUSD_BITMEX.id,
            bid_price=Price.from_str("11491.0"),
            ask_price=Price.from_str("11491.5"),
            bid_size=Quantity.from_int(1_500_000),
            ask_size=Quantity.from_int(1_500_000),
            ts_event=0,
            ts_init=0,
        )

        self.exchange.process_quote_tick(quote2)  # Fill the limit order
        self.portfolio.update_quote_tick(quote2)

        # Assert
        assert order_limit.avg_px == 11492.5
        assert self.strategy.store[2].liquidity_side == LiquiditySide.TAKER
        assert self.strategy.store[7].liquidity_side == LiquiditySide.MAKER
        assert self.strategy.store[2].commission == Money(0.00652543, BTC)
        assert self.strategy.store[7].commission == Money(-0.00217533, BTC)
```


---

## Overview

This file is located at `tests/unit_tests/backtest/test_exchange_bitmex.py` within the repository.

**Classes defined:** TestBitmexExchange

**Functions defined:** setup, test_commission_maker_taker_order

**Import statements:** 27


---

## Detailed Analysis

### Classes

#### `TestBitmexExchange`


### Functions

#### `setup(self)`


#### `test_commission_maker_taker_order(self)`


### Imports

- `from decimal import Decimal`
- `from nautilus_trader.backtest.engine import SimulatedExchange`
- `from nautilus_trader.backtest.execution_client import BacktestExecClient`
- `from nautilus_trader.backtest.models import FillModel`
- `from nautilus_trader.backtest.models import LatencyModel`
- `from nautilus_trader.backtest.models import MakerTakerFeeModel`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.data.engine import DataEngine`
- `from nautilus_trader.execution.engine import ExecutionEngine`
- `from nautilus_trader.model.currencies import BTC`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.enums import AccountType`
- `from nautilus_trader.model.enums import LiquiditySide`
- `from nautilus_trader.model.enums import OmsType`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Money`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.portfolio.portfolio import Portfolio`
- `from nautilus_trader.risk.engine import RiskEngine`
- `from nautilus_trader.test_kit.mocks.strategies import MockStrategy`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.component import TestComponentStubs`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.backtest.test_exchange_bitmex import TestBitmexExchange
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from nautilus_trader.backtest.engine import SimulatedExchange`
- `from nautilus_trader.backtest.execution_client import BacktestExecClient`
- `from nautilus_trader.backtest.models import FillModel`
- `from nautilus_trader.backtest.models import LatencyModel`
- `from nautilus_trader.backtest.models import MakerTakerFeeModel`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.data.engine import DataEngine`
- `from nautilus_trader.execution.engine import ExecutionEngine`

*... and 17 more*

**Directory:** `tests/unit_tests/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


