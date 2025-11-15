# Documentation: `tests/unit_tests/portfolio/conftest.py`
**Generated:** 2025-11-15T19:40:09.437917Z
**File Size:** 2768 bytes
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

- **Path:** `tests/unit_tests/portfolio/conftest.py`
- **Size:** 2,768 bytes
- **Lines:** 97
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9
- **Functions:** 9

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
"""
Common fixtures for portfolio tests.
"""

import pytest

from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import MessageBus
from nautilus_trader.common.component import TestClock
from nautilus_trader.execution.engine import ExecutionEngine
from nautilus_trader.portfolio.portfolio import Portfolio
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs
from nautilus_trader.trading.strategy import Strategy


AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD")


@pytest.fixture(name="clock")
def fixture_clock():
    return TestClock()


@pytest.fixture(name="trader_id")
def fixture_trader_id():
    return TestIdStubs.trader_id()


@pytest.fixture(name="strategy_id")
def fixture_strategy_id():
    return TestIdStubs.strategy_id()


@pytest.fixture(name="account_id")
def fixture_account_id():
    return TestIdStubs.account_id()


@pytest.fixture(name="msgbus")
def fixture_msgbus(trader_id, clock):
    return MessageBus(
        trader_id=trader_id,
        clock=clock,
    )


@pytest.fixture(name="cache")
def fixture_cache():
    cache = Cache()
    cache.add_instrument(AUDUSD_SIM)
    return cache


@pytest.fixture(name="portfolio")
def fixture_portfolio(msgbus, cache, clock):
    return Portfolio(
        msgbus=msgbus,
        cache=cache,
        clock=clock,
    )


@pytest.fixture(name="exec_engine")
def fixture_exec_engine(msgbus, cache, clock):
    return ExecutionEngine(
        msgbus=msgbus,
        cache=cache,
        clock=clock,
    )


@pytest.fixture(name="strategy")
def fixture_strategy(trader_id, portfolio, msgbus, cache, clock):
    strategy = Strategy()
    strategy.register(
        trader_id=trader_id,
        portfolio=portfolio,
        msgbus=msgbus,
        cache=cache,
        clock=clock,
    )
    return strategy
```


---

## Overview

This file is located at `tests/unit_tests/portfolio/conftest.py` within the repository.

**Functions defined:** fixture_clock, fixture_trader_id, fixture_strategy_id, fixture_account_id, fixture_msgbus, fixture_cache, fixture_portfolio, fixture_exec_engine, fixture_strategy

**Import statements:** 9


---

## Detailed Analysis

### Functions

#### `fixture_clock()`


#### `fixture_trader_id()`


#### `fixture_strategy_id()`


#### `fixture_account_id()`


#### `fixture_msgbus(trader_id, clock)`


#### `fixture_cache()`


#### `fixture_portfolio(msgbus, cache, clock)`


#### `fixture_exec_engine(msgbus, cache, clock)`


#### `fixture_strategy(trader_id, portfolio, msgbus, cache, clock)`


### Imports

- `import pytest`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.execution.engine import ExecutionEngine`
- `from nautilus_trader.portfolio.portfolio import Portfolio`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.portfolio.conftest import fixture_clock
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.execution.engine import ExecutionEngine`
- `from nautilus_trader.portfolio.portfolio import Portfolio`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`
- `from nautilus_trader.trading.strategy import Strategy`

**Directory:** `tests/unit_tests/portfolio`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


