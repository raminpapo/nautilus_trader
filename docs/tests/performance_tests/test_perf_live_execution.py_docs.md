# Documentation: `tests/performance_tests/test_perf_live_execution.py`
**Generated:** 2025-11-15T19:40:08.046057Z
**File Size:** 5892 bytes
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

- **Path:** `tests/performance_tests/test_perf_live_execution.py`
- **Size:** 5,892 bytes
- **Lines:** 178
- **Extension:** `.py`
- **Type:** text
- **Imports:** 22
- **Classes:** 1
- **Functions:** 6

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

import asyncio

import pytest

from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.core.uuid import UUID4
from nautilus_trader.execution.messages import SubmitOrder
from nautilus_trader.live.data_engine import LiveDataEngine
from nautilus_trader.live.execution_engine import LiveExecutionEngine
from nautilus_trader.live.risk_engine import LiveRiskEngine
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Quantity
from nautilus_trader.portfolio.portfolio import Portfolio
from nautilus_trader.test_kit.mocks.exec_clients import MockExecutionClient
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.component import TestComponentStubs
from nautilus_trader.test_kit.stubs.events import TestEventStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs
from nautilus_trader.trading.strategy import Strategy


BINANCE = Venue("BINANCE")
BTCUSDT_BINANCE = TestInstrumentProvider.btcusdt_binance()


class TestLiveExecutionPerformance:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        # Fixture Setup
        self.loop = request.getfixturevalue("event_loop")
        self.loop.set_debug(True)

        self.clock = LiveClock()

        self.trader_id = TestIdStubs.trader_id()
        self.account_id = AccountId(f"{BINANCE.value}-001")

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

        self.data_engine = LiveDataEngine(
            loop=self.loop,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.exec_engine = LiveExecutionEngine(
            loop=self.loop,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.risk_engine = LiveRiskEngine(
            loop=self.loop,
            portfolio=self.portfolio,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.exec_client = MockExecutionClient(
            client_id=ClientId("BINANCE"),
            venue=BINANCE,
            account_type=AccountType.CASH,
            base_currency=None,  # Multi-currency account
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )
        self.portfolio.update_account(TestEventStubs.margin_account_state())
        self.exec_engine.register_client(self.exec_client)

        self.strategy = Strategy()
        self.strategy.register(
            trader_id=self.trader_id,
            portfolio=self.portfolio,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        yield

    def submit_order(self):
        order = self.strategy.order_factory.market(
            BTCUSDT_BINANCE.id,
            OrderSide.BUY,
            Quantity.from_str("1.00000000"),
        )

        self.strategy.submit_order(order)

    @pytest.mark.asyncio()
    def test_execute_command(self, benchmark):
        order = self.strategy.order_factory.market(
            BTCUSDT_BINANCE.id,
            OrderSide.BUY,
            Quantity.from_str("1.00000000"),
        )

        command = SubmitOrder(
            trader_id=self.trader_id,
            strategy_id=self.strategy.id,
            position_id=None,
            order=order,
            command_id=UUID4(),
            ts_init=self.clock.timestamp_ns(),
        )

        def execute_command():
            self.exec_engine.execute(command)

        benchmark(execute_command)

    @pytest.mark.asyncio()
    async def test_submit_order(self, benchmark):
        self.exec_engine.start()
        await asyncio.sleep(1)

        def submit_order():
            order = self.strategy.order_factory.market(
                BTCUSDT_BINANCE.id,
                OrderSide.BUY,
                Quantity.from_str("1.00000000"),
            )

            self.strategy.submit_order(order)

        benchmark(submit_order)

    @pytest.mark.asyncio()
    async def test_submit_order_end_to_end(self, benchmark):
        self.exec_engine.start()
        await asyncio.sleep(1)

        def run():
            for _ in range(1000):
                order = self.strategy.order_factory.market(
                    BTCUSDT_BINANCE.id,
                    OrderSide.BUY,
                    Quantity.from_str("1.00000000"),
                )

                self.strategy.submit_order(order)

        benchmark(run)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_live_execution.py` within the repository.

**Classes defined:** TestLiveExecutionPerformance

**Functions defined:** setup, submit_order, test_execute_command, execute_command, submit_order, run

**Import statements:** 22


---

## Detailed Analysis

### Classes

#### `TestLiveExecutionPerformance`


### Functions

#### `setup(self, request)`


#### `submit_order(self)`


#### `test_execute_command(self, benchmark)`


#### `execute_command()`


#### `submit_order()`


#### `run()`


### Imports

- `import asyncio`
- `import pytest`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.execution.messages import SubmitOrder`
- `from nautilus_trader.live.data_engine import LiveDataEngine`
- `from nautilus_trader.live.execution_engine import LiveExecutionEngine`
- `from nautilus_trader.live.risk_engine import LiveRiskEngine`
- `from nautilus_trader.model.enums import AccountType`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.portfolio.portfolio import Portfolio`
- `from nautilus_trader.test_kit.mocks.exec_clients import MockExecutionClient`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.component import TestComponentStubs`
- `from nautilus_trader.test_kit.stubs.events import TestEventStubs`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_live_execution import TestLiveExecutionPerformance
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `import pytest`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.execution.messages import SubmitOrder`
- `from nautilus_trader.live.data_engine import LiveDataEngine`
- `from nautilus_trader.live.execution_engine import LiveExecutionEngine`
- `from nautilus_trader.live.risk_engine import LiveRiskEngine`
- `from nautilus_trader.model.enums import AccountType`

*... and 12 more*

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


