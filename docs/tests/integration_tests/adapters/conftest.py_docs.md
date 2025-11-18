# Documentation: conftest.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/conftest.py`
- **Size**: 8,115 bytes
- **Lines**: 311
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

from typing import Any

import pytest
from pytest_mock import MockerFixture

from nautilus_trader.accounting.factory import AccountFactory
from nautilus_trader.common import Environment
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.common.component import TestClock
from nautilus_trader.core.message import Event
from nautilus_trader.core.uuid import UUID4
from nautilus_trader.data.engine import DataEngine
from nautilus_trader.execution.engine import ExecutionEngine
from nautilus_trader.live.execution_engine import LiveExecutionEngine
from nautilus_trader.model.events import AccountState
from nautilus_trader.model.events import OrderCanceled
from nautilus_trader.model.events import OrderFilled
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.portfolio.portfolio import Portfolio
from nautilus_trader.risk.engine import RiskEngine
from nautilus_trader.test_kit.stubs.component import TestComponentStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs
from nautilus_trader.trading.strategy import Strategy
from nautilus_trader.trading.strategy import StrategyConfig
from nautilus_trader.trading.trader import Trader


@pytest.fixture
def account_id(venue):
    return AccountId(f"{venue.value}-001")


def has_live_components_marker(request) -> bool:
    marker_names = [mark.name for mark in request.node.iter_markers()]
    return "live_components" in marker_names


@pytest.fixture
def clock(request):
    if has_live_components_marker(request):
        clock = LiveClock()
    else:
        clock = TestClock()
        clock.set_time(0)
    return clock


@pytest.fixture
def live_clock():
    clock = LiveClock()
    return clock


@pytest.fixture
def trader_id():
    return TestIdStubs.trader_id()


@pytest.fixture
def instance_id():
    return UUID4()


@pytest.fixture
def msgbus(trader_id, clock):
    return MessageBus(
        trader_id,
        clock,
    )


@pytest.fixture
def cache(instrument):
    cache = TestComponentStubs.cache()
    if instrument is not None:
        cache.add_instrument(instrument)
    return cache


@pytest.fixture
def portfolio(clock, cache, msgbus, account_state):
    portfolio = Portfolio(
        msgbus,
        cache,
        clock,
    )
    if account_state is not None:
        portfolio.update_account(account_state)
    return portfolio


@pytest.fixture
def data_engine(msgbus, cache, clock, data_client):
    engine = DataEngine(
        msgbus,
        cache,
        clock,
    )
    if data_client is not None:
        engine.register_client(data_client)
    return engine


@pytest.fixture
def exec_engine(request, event_loop, msgbus, cache, clock, exec_client):
    if has_live_components_marker(request):
        engine = LiveExecutionEngine(
            event_loop,
            msgbus,
            cache,
            clock,
        )
    else:
        engine = ExecutionEngine(
            msgbus,
            cache,
            clock,
        )
    if exec_client is not None:
        engine.register_client(exec_client)
    return engine


@pytest.fixture
def risk_engine(portfolio, msgbus, cache, clock):
    risk_engine = RiskEngine(
        portfolio,
        msgbus,
        cache,
        clock,
    )
    return risk_engine


@pytest.fixture(autouse=True)
def trader(
    trader_id,
    instance_id,
    msgbus,
    cache,
    portfolio,
    data_engine,
    risk_engine,
    exec_engine,
    clock,
    event_loop,
):
    return Trader(
        trader_id=trader_id,
        instance_id=instance_id,
        msgbus=msgbus,
        cache=cache,
        portfolio=portfolio,
        data_engine=data_engine,
        risk_engine=risk_engine,
        exec_engine=exec_engine,
        clock=clock,
        environment=Environment.BACKTEST,
        loop=event_loop,
    )


@pytest.fixture
def mock_data_engine_process(mocker: MockerFixture, msgbus, data_engine):
    mock = mocker.MagicMock()
    msgbus.deregister(endpoint="DataEngine.process", handler=data_engine.process)
    msgbus.register(
        endpoint="DataEngine.process",
        handler=mock,
    )
    return mock


@pytest.fixture
def mock_exec_engine_process(mocker: MockerFixture, msgbus, exec_engine):
    mock = mocker.MagicMock()
    msgbus.deregister(endpoint="ExecEngine.process", handler=exec_engine.process)
    msgbus.register(
        endpoint="ExecEngine.process",
        handler=mock,
    )
    return mock


@pytest.fixture
def strategy(trader_id, portfolio, msgbus, cache, clock):
    strategy = Strategy(config=StrategyConfig(strategy_id="S", order_id_tag="001"))
    strategy.register(
        trader_id,
        portfolio,
        msgbus,
        cache,
        clock,
    )
    return strategy


@pytest.fixture
def strategy_id(strategy):
    return strategy.id


@pytest.fixture
def client_order_id(strategy):
    return TestIdStubs.client_order_id()


@pytest.fixture
def venue_order_id(strategy):
    return TestIdStubs.venue_order_id()


@pytest.fixture
def trade_id(strategy):
    return TestIdStubs.trade_id()


@pytest.fixture(autouse=True)
def components(data_engine, exec_engine, risk_engine, strategy):
    # Ensures components are created and running for every test
    return


def _collect_events(msgbus, filter_types: tuple[type, ...] | None = None):
    events = []

    def handler(event: Event) -> None:
        if filter_types is None or isinstance(event, filter_types):
            events.append(event)

    msgbus.subscribe("events.order.*", handler=handler)
    msgbus.subscribe("events.position.*", handler=handler)
    return events


@pytest.fixture
def events(msgbus: MessageBus) -> list[Event]:
    return _collect_events(msgbus, filter_types=None)


@pytest.fixture
def fill_events(msgbus: MessageBus) -> list[Event]:
    return _collect_events(msgbus, filter_types=(OrderFilled,))


@pytest.fixture
def cancel_events(msgbus: MessageBus) -> list[Event]:
    return _collect_events(msgbus, filter_types=(OrderCanceled,))


@pytest.fixture
def messages(msgbus: MessageBus) -> list[Any]:
    messages: list[Any] = []
    msgbus.subscribe("*", handler=messages.append)
    return messages


@pytest.fixture
def account(account_state, cache):
    return AccountFactory.create(account_state)


# TO BE IMPLEMENTED IN ADAPTER conftest.py
@pytest.fixture
def venue() -> Venue:
    raise NotImplementedError("`venue` needs to be implemented in adapter `conftest.py`")


@pytest.fixture
def instrument_provider():
    raise NotImplementedError(
        "`instrument_provider` needs to be implemented in adapter `conftest.py`",
    )


@pytest.fixture
def data_client():
    raise NotImplementedError("`data_client` needs to be implemented in adapter `conftest.py`")


@pytest.fixture
def exec_client():
    raise NotImplementedError("`exec_client` needs to be implemented in adapter `conftest.py`")


@pytest.fixture
def instrument():
    raise NotImplementedError("`instrument` needs to be implemented in adapter `conftest.py`")


@pytest.fixture
def account_state() -> AccountState:
    raise NotImplementedError("`account_state` needs to be implemented in adapter `conftest.py`")

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 33 function(s).

## Detailed Walkthrough

### Functions
- **`account_id()`**: Function defined in this file
- **`has_live_components_marker()`**: Function defined in this file
- **`clock()`**: Function defined in this file
- **`live_clock()`**: Function defined in this file
- **`trader_id()`**: Function defined in this file
- **`instance_id()`**: Function defined in this file
- **`msgbus()`**: Function defined in this file
- **`cache()`**: Function defined in this file
- **`portfolio()`**: Function defined in this file
- **`data_engine()`**: Function defined in this file
- **`exec_engine()`**: Function defined in this file
- **`risk_engine()`**: Function defined in this file
- **`trader()`**: Function defined in this file
- **`mock_data_engine_process()`**: Function defined in this file
- **`mock_exec_engine_process()`**: Function defined in this file
- **`strategy()`**: Function defined in this file
- **`strategy_id()`**: Function defined in this file
- **`client_order_id()`**: Function defined in this file
- **`venue_order_id()`**: Function defined in this file
- **`trade_id()`**: Function defined in this file

*...and 13 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 52


**Functions**: `_collect_events`, `account`, `account_id`, `account_state`, `cache`, `cancel_events`, `client_order_id`, `clock`, `components`, `data_client`, `data_engine`, `events`, `exec_client`, `exec_engine`, `fill_events`, `has_live_components_marker`, `instance_id`, `instrument`, `instrument_provider`, `live_clock`, `messages`, `mock_data_engine_process`, `mock_exec_engine_process`, `msgbus`, `portfolio`, `risk_engine`, `strategy`, `strategy_id`, `trade_id`, `trader` *(+3 more)*
**Imports**: `nautilus_trader.accounting.factory`, `nautilus_trader.common`, `nautilus_trader.common.component`, `nautilus_trader.core.message`, `nautilus_trader.core.uuid`, `nautilus_trader.data.engine`, `nautilus_trader.execution.engine`, `nautilus_trader.live.execution_engine`, `nautilus_trader.model.events`, `nautilus_trader.model.identifiers`, `nautilus_trader.portfolio.portfolio`, `nautilus_trader.risk.engine`, `nautilus_trader.test_kit.stubs.component`, `nautilus_trader.test_kit.stubs.identifiers`, `nautilus_trader.trading.strategy`, `nautilus_trader.trading.trader`, `pytest`, `pytest_mock`, `typing`

## Related Files

This file is located in `tests/integration_tests/adapters/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/conftest.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.816880Z*
