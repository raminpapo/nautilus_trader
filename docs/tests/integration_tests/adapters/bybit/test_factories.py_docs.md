# Documentation: `tests/integration_tests/adapters/bybit/test_factories.py`
**Generated:** 2025-11-15T19:40:07.728037Z
**File Size:** 5961 bytes
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

- **Path:** `tests/integration_tests/adapters/bybit/test_factories.py`
- **Size:** 5,961 bytes
- **Lines:** 147
- **Extension:** `.py`
- **Type:** text
- **Imports:** 13
- **Classes:** 1
- **Functions:** 5

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

from nautilus_trader.adapters.bybit.config import BybitDataClientConfig
from nautilus_trader.adapters.bybit.config import BybitExecClientConfig
from nautilus_trader.adapters.bybit.data import BybitDataClient
from nautilus_trader.adapters.bybit.execution import BybitExecutionClient
from nautilus_trader.adapters.bybit.factories import BybitLiveDataClientFactory
from nautilus_trader.adapters.bybit.factories import BybitLiveExecClientFactory
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.test_kit.mocks.cache_database import MockCacheDatabase
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


class TestBybitFactories:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.loop = request.getfixturevalue("event_loop")
        self.clock = LiveClock()

        self.trader_id = TestIdStubs.trader_id()
        self.strategy_id = TestIdStubs.strategy_id()
        self.account_id = TestIdStubs.account_id()

        self.msgbus = MessageBus(
            trader_id=self.trader_id,
            clock=self.clock,
        )

        self.cache_db = MockCacheDatabase()
        self.cache = Cache(database=self.cache_db)

        yield

    @pytest.mark.parametrize(
        ("environment", "expected"),
        [
            [nautilus_pyo3.BybitEnvironment.MAINNET, "https://api.bybit.com"],
            [nautilus_pyo3.BybitEnvironment.TESTNET, "https://api-testnet.bybit.com"],
            [nautilus_pyo3.BybitEnvironment.DEMO, "https://api-demo.bybit.com"],
        ],
    )
    def test_get_http_base_url(self, environment, expected):
        base_url = nautilus_pyo3.get_bybit_http_base_url(environment)
        assert base_url == expected

    @pytest.mark.parametrize(
        ("product_type", "environment", "expected"),
        [
            [
                nautilus_pyo3.BybitProductType.SPOT,
                nautilus_pyo3.BybitEnvironment.MAINNET,
                "wss://stream.bybit.com/v5/public/spot",
            ],
            [
                nautilus_pyo3.BybitProductType.SPOT,
                nautilus_pyo3.BybitEnvironment.TESTNET,
                "wss://stream-testnet.bybit.com/v5/public/spot",
            ],
            [
                nautilus_pyo3.BybitProductType.SPOT,
                nautilus_pyo3.BybitEnvironment.DEMO,
                "wss://stream-demo.bybit.com/v5/public/spot",
            ],
            [
                nautilus_pyo3.BybitProductType.LINEAR,
                nautilus_pyo3.BybitEnvironment.MAINNET,
                "wss://stream.bybit.com/v5/public/linear",
            ],
            [
                nautilus_pyo3.BybitProductType.LINEAR,
                nautilus_pyo3.BybitEnvironment.TESTNET,
                "wss://stream-testnet.bybit.com/v5/public/linear",
            ],
            [
                nautilus_pyo3.BybitProductType.LINEAR,
                nautilus_pyo3.BybitEnvironment.DEMO,
                "wss://stream-demo.bybit.com/v5/public/linear",
            ],
            [
                nautilus_pyo3.BybitProductType.INVERSE,
                nautilus_pyo3.BybitEnvironment.MAINNET,
                "wss://stream.bybit.com/v5/public/inverse",
            ],
            [
                nautilus_pyo3.BybitProductType.INVERSE,
                nautilus_pyo3.BybitEnvironment.TESTNET,
                "wss://stream-testnet.bybit.com/v5/public/inverse",
            ],
            [
                nautilus_pyo3.BybitProductType.INVERSE,
                nautilus_pyo3.BybitEnvironment.DEMO,
                "wss://stream-demo.bybit.com/v5/public/inverse",
            ],
        ],
    )
    def test_get_ws_base_url(self, product_type, environment, expected):
        base_url = nautilus_pyo3.get_bybit_ws_url_public(product_type, environment)
        assert base_url == expected

    def test_create_bybit_live_data_client(self):
        data_client = BybitLiveDataClientFactory.create(
            loop=self.loop,
            name="BYBIT",
            config=BybitDataClientConfig(
                api_key="SOME_BYBIT_API_KEY",
                api_secret="SOME_BYBIT_API_SECRET",
                product_types=[nautilus_pyo3.BybitProductType.LINEAR],
            ),
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )
        assert isinstance(data_client, BybitDataClient)

    def test_create_bybit_live_exec_client(self):
        data_client = BybitLiveExecClientFactory.create(
            loop=self.loop,
            name="BYBIT",
            config=BybitExecClientConfig(
                api_key="SOME_BYBIT_API_KEY",
                api_secret="SOME_BYBIT_API_SECRET",
                product_types=[nautilus_pyo3.BybitProductType.LINEAR],
            ),
            msgbus=self.msgbus,
            cache=self.cache,
            clock=self.clock,
        )
        assert isinstance(data_client, BybitExecutionClient)
```


---

## Overview

This file is located at `tests/integration_tests/adapters/bybit/test_factories.py` within the repository.

**Classes defined:** TestBybitFactories

**Functions defined:** setup, test_get_http_base_url, test_get_ws_base_url, test_create_bybit_live_data_client, test_create_bybit_live_exec_client

**Import statements:** 13


---

## Detailed Analysis

### Classes

#### `TestBybitFactories`


### Functions

#### `setup(self, request)`


#### `test_get_http_base_url(self, environment, expected)`


#### `test_get_ws_base_url(self, product_type, environment, expected)`


#### `test_create_bybit_live_data_client(self)`


#### `test_create_bybit_live_exec_client(self)`


### Imports

- `import pytest`
- `from nautilus_trader.adapters.bybit.config import BybitDataClientConfig`
- `from nautilus_trader.adapters.bybit.config import BybitExecClientConfig`
- `from nautilus_trader.adapters.bybit.data import BybitDataClient`
- `from nautilus_trader.adapters.bybit.execution import BybitExecutionClient`
- `from nautilus_trader.adapters.bybit.factories import BybitLiveDataClientFactory`
- `from nautilus_trader.adapters.bybit.factories import BybitLiveExecClientFactory`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.test_kit.mocks.cache_database import MockCacheDatabase`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.bybit.test_factories import TestBybitFactories
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.adapters.bybit.config import BybitDataClientConfig`
- `from nautilus_trader.adapters.bybit.config import BybitExecClientConfig`
- `from nautilus_trader.adapters.bybit.data import BybitDataClient`
- `from nautilus_trader.adapters.bybit.execution import BybitExecutionClient`
- `from nautilus_trader.adapters.bybit.factories import BybitLiveDataClientFactory`
- `from nautilus_trader.adapters.bybit.factories import BybitLiveExecClientFactory`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`

*... and 3 more*

**Directory:** `tests/integration_tests/adapters/bybit`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


