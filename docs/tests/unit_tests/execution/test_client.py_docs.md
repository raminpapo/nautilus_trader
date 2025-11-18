# Documentation: test_client.py

## File Metadata

- **Path**: `tests/unit_tests/execution/test_client.py`
- **Size**: 5,569 bytes
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

from nautilus_trader.common.component import MessageBus
from nautilus_trader.common.component import TestClock
from nautilus_trader.common.factories import OrderFactory
from nautilus_trader.execution.client import ExecutionClient
from nautilus_trader.execution.engine import ExecutionEngine
from nautilus_trader.model.currencies import USD
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.enums import OmsType
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.events import OrderDenied
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.portfolio.portfolio import Portfolio
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.component import TestComponentStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


USDJPY_SIM = TestInstrumentProvider.default_fx_ccy("USD/JPY")
AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


class TestExecutionClient:
    def setup(self):
        # Fixture Setup
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

        self.exec_engine = ExecutionEngine(
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.venue = Venue("SIM")

        self.client = ExecutionClient(
            client_id=ClientId(self.venue.value),
            venue=self.venue,
            oms_type=OmsType.HEDGING,
            account_type=AccountType.MARGIN,
            base_currency=USD,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        self.order_factory = OrderFactory(
            trader_id=TraderId("TESTER-000"),
            strategy_id=StrategyId("S-001"),
            clock=TestClock(),
        )

    def test_venue_when_brokerage_returns_client_id_value_as_venue(self):
        assert self.client.venue == self.venue

    def test_venue_when_routing_venue_returns_none(self):
        # Arrange
        client = ExecutionClient(
            client_id=ClientId("IB"),
            venue=None,  # Multi-venue
            oms_type=OmsType.HEDGING,
            account_type=AccountType.MARGIN,
            base_currency=USD,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        # Act, Assert
        assert client.venue is None

    def test_generate_order_denied_emits_order_denied_event(self):
        # Arrange
        clock = TestClock()
        trader_id = TestIdStubs.trader_id()
        msgbus = MessageBus(trader_id=trader_id, clock=clock)
        cache = TestComponentStubs.cache()
        client = ExecutionClient(
            client_id=ClientId(self.venue.value),
            venue=self.venue,
            oms_type=OmsType.HEDGING,
            account_type=AccountType.MARGIN,
            base_currency=USD,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
        )

        captured: dict[str, OrderDenied] = {}

        def handler(event):
            captured["event"] = event

        msgbus.register("ExecEngine.process", handler)

        order_factory = OrderFactory(
            trader_id=trader_id,
            strategy_id=StrategyId("S-UNIT"),
            clock=TestClock(),
        )
        order = order_factory.market(
            instrument_id=AUDUSD_SIM.id,
            order_side=OrderSide.BUY,
            quantity=AUDUSD_SIM.make_qty(1.0),
        )

        reason = "quote quantity required"
        ts_event = 123456789

        # Act
        client.generate_order_denied(
            strategy_id=order.strategy_id,
            instrument_id=order.instrument_id,
            client_order_id=order.client_order_id,
            reason=reason,
            ts_event=ts_event,
        )

        # Assert
        event = captured.get("event")
        assert event is not None
        assert isinstance(event, OrderDenied)
        assert event.instrument_id == order.instrument_id
        assert event.client_order_id == order.client_order_id
        assert event.reason == reason
        assert event.ts_event == ts_event
        msgbus.deregister("ExecEngine.process", handler)

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestExecutionClient`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Classs**: `TestExecutionClient`
**Imports**: `nautilus_trader.common.component`, `nautilus_trader.common.factories`, `nautilus_trader.execution.client`, `nautilus_trader.execution.engine`, `nautilus_trader.model.currencies`, `nautilus_trader.model.enums`, `nautilus_trader.model.events`, `nautilus_trader.model.identifiers`, `nautilus_trader.portfolio.portfolio`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.component`, `nautilus_trader.test_kit.stubs.identifiers`

## Related Files

This file is located in `tests/unit_tests/execution/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/execution/test_client.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.365741Z*
