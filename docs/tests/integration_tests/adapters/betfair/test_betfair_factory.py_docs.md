# Documentation: `tests/integration_tests/adapters/betfair/test_betfair_factory.py`
**Generated:** 2025-11-15T19:40:07.560237Z
**File Size:** 3432 bytes
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

- **Path:** `tests/integration_tests/adapters/betfair/test_betfair_factory.py`
- **Size:** 3,432 bytes
- **Lines:** 87
- **Extension:** `.py`
- **Type:** text
- **Imports:** 12
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

import pytest

from nautilus_trader.adapters.betfair.config import BetfairDataClientConfig
from nautilus_trader.adapters.betfair.config import BetfairExecClientConfig
from nautilus_trader.adapters.betfair.constants import BETFAIR_VENUE
from nautilus_trader.adapters.betfair.data import BetfairDataClient
from nautilus_trader.adapters.betfair.execution import BetfairExecutionClient
from nautilus_trader.adapters.betfair.factories import BetfairLiveDataClientFactory
from nautilus_trader.adapters.betfair.factories import BetfairLiveExecClientFactory
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.test_kit.stubs.component import TestComponentStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


class TestBetfairFactory:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        # Fixture Setup
        self.loop = request.getfixturevalue("event_loop")
        self.loop.set_debug(True)

        self.clock = LiveClock()

        self.trader_id = TestIdStubs.trader_id()
        self.venue = BETFAIR_VENUE

        self.msgbus = MessageBus(
            trader_id=self.trader_id,
            clock=self.clock,
        )
        self.cache = TestComponentStubs.cache()

        yield

    @pytest.mark.asyncio()
    def test_create(self):
        data_config = BetfairDataClientConfig(
            account_currency="GBP",
            username="SOME_BETFAIR_USERNAME",
            password="SOME_BETFAIR_PASSWORD",
            app_key="SOME_BETFAIR_APP_KEY",
            certs_dir="SOME_BETFAIR_CERTS_DIR",
        )
        exec_config = BetfairExecClientConfig(
            account_currency="GBP",
            username="SOME_BETFAIR_USERNAME",
            password="SOME_BETFAIR_PASSWORD",
            app_key="SOME_BETFAIR_APP_KEY",
            certs_dir="SOME_BETFAIR_CERTS_DIR",
        )

        data_client = BetfairLiveDataClientFactory.create(
            loop=self.loop,
            name=BETFAIR_VENUE.value,
            config=data_config,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )
        exec_client = BetfairLiveExecClientFactory.create(
            loop=self.loop,
            name=BETFAIR_VENUE.value,
            config=exec_config,
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )

        # Assert
        assert BetfairDataClient is type(data_client)
        assert BetfairExecutionClient is type(exec_client)
```


---

## Overview

This file is located at `tests/integration_tests/adapters/betfair/test_betfair_factory.py` within the repository.

**Classes defined:** TestBetfairFactory

**Functions defined:** setup, test_create

**Import statements:** 12


---

## Detailed Analysis

### Classes

#### `TestBetfairFactory`


### Functions

#### `setup(self, request)`


#### `test_create(self)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.betfair.config import BetfairDataClientConfig`
- `from nautilus_trader.adapters.betfair.config import BetfairExecClientConfig`
- `from nautilus_trader.adapters.betfair.constants import BETFAIR_VENUE`
- `from nautilus_trader.adapters.betfair.data import BetfairDataClient`
- `from nautilus_trader.adapters.betfair.execution import BetfairExecutionClient`
- `from nautilus_trader.adapters.betfair.factories import BetfairLiveDataClientFactory`
- `from nautilus_trader.adapters.betfair.factories import BetfairLiveExecClientFactory`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.test_kit.stubs.component import TestComponentStubs`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.betfair.test_betfair_factory import TestBetfairFactory
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.betfair.config import BetfairDataClientConfig`
- `from nautilus_trader.adapters.betfair.config import BetfairExecClientConfig`
- `from nautilus_trader.adapters.betfair.constants import BETFAIR_VENUE`
- `from nautilus_trader.adapters.betfair.data import BetfairDataClient`
- `from nautilus_trader.adapters.betfair.execution import BetfairExecutionClient`
- `from nautilus_trader.adapters.betfair.factories import BetfairLiveDataClientFactory`
- `from nautilus_trader.adapters.betfair.factories import BetfairLiveExecClientFactory`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`

*... and 2 more*

**Directory:** `tests/integration_tests/adapters/betfair`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


