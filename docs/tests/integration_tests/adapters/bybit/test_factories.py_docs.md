# Documentation: test_factories.py

## File Metadata

- **Path**: `tests/integration_tests/adapters/bybit/test_factories.py`
- **Size**: 5,962 bytes
- **Lines**: 148
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

        return

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

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestBybitFactories`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Classs**: `TestBybitFactories`
**Imports**: `nautilus_trader.adapters.bybit.config`, `nautilus_trader.adapters.bybit.data`, `nautilus_trader.adapters.bybit.execution`, `nautilus_trader.adapters.bybit.factories`, `nautilus_trader.cache.cache`, `nautilus_trader.common.component`, `nautilus_trader.core`, `nautilus_trader.test_kit.mocks.cache_database`, `nautilus_trader.test_kit.stubs.identifiers`, `pytest`

## Related Files

This file is located in `tests/integration_tests/adapters/bybit/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/bybit/test_factories.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:06.802976Z*
