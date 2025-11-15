# Documentation: `nautilus_trader/adapters/hyperliquid/factories.py`
**Generated:** 2025-11-15T19:40:04.329792Z
**File Size:** 8087 bytes
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

- **Path:** `nautilus_trader/adapters/hyperliquid/factories.py`
- **Size:** 8,087 bytes
- **Lines:** 241
- **Extension:** `.py`
- **Type:** text
- **Imports:** 17
- **Classes:** 2
- **Functions:** 4

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

from __future__ import annotations

import asyncio
from functools import lru_cache
from typing import TYPE_CHECKING

from nautilus_trader.adapters.hyperliquid.config import HyperliquidDataClientConfig
from nautilus_trader.adapters.hyperliquid.config import HyperliquidExecClientConfig
from nautilus_trader.adapters.hyperliquid.data import HyperliquidDataClient
from nautilus_trader.adapters.hyperliquid.execution import HyperliquidExecutionClient
from nautilus_trader.adapters.hyperliquid.providers import HyperliquidInstrumentProvider
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.config import InstrumentProviderConfig
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.live.factories import LiveDataClientFactory
from nautilus_trader.live.factories import LiveExecClientFactory


if TYPE_CHECKING:
    from typing import Any

    # PyO3 types from Rust (temporary namespace qualification)
    HyperliquidHttpClient = Any  # nautilus_pyo3.HyperliquidHttpClient (stub not yet available)


@lru_cache(1)
def get_cached_hyperliquid_http_client(
    private_key: str | None = None,
    vault_address: str | None = None,
    base_url: str | None = None,
    timeout_secs: int = 10,
    testnet: bool = False,
    proxy_url: str | None = None,
) -> HyperliquidHttpClient:
    """
    Cache and return a Hyperliquid HTTP client with the given parameters.

    If a cached client with matching parameters already exists, the cached client will be returned.

    Parameters
    ----------
    private_key : str, optional
        The EVM private key for the client.
        If ``None`` then will source the `HYPERLIQUID_PK` or `HYPERLIQUID_TESTNET_PK`
        environment variable (depending on the `testnet` setting).
        Note: The PyO3 client handles credentials internally.
    vault_address : str, optional
        The vault address for vault trading.
        If ``None`` then will source the `HYPERLIQUID_VAULT` or `HYPERLIQUID_TESTNET_VAULT`
        environment variable (depending on the `testnet` setting).
        Note: The PyO3 client handles credentials internally.
    base_url : str, optional
        The base URL for the API endpoints.
        Note: Currently not supported by PyO3 client.
    timeout_secs : int, default 10
        The timeout (seconds) for HTTP requests to Hyperliquid.
    testnet : bool, default False
        If the client is connecting to the testnet API.
    proxy_url : str, optional
        Optional HTTP proxy URL.

    Returns
    -------
    nautilus_pyo3.HyperliquidHttpClient
        The Hyperliquid HTTP client instance.

    """
    # The constructor will read credentials from environment variables if not provided
    # This ensures proxy_url is always honored regardless of credential source
    return nautilus_pyo3.HyperliquidHttpClient(
        private_key=private_key,
        vault_address=vault_address,
        is_testnet=testnet,
        timeout_secs=timeout_secs,
        proxy_url=proxy_url,
    )


@lru_cache(1)
def get_cached_hyperliquid_instrument_provider(
    client: HyperliquidHttpClient,
    config: InstrumentProviderConfig | None = None,
) -> HyperliquidInstrumentProvider:
    """
    Cache and return a Hyperliquid instrument provider.

    If a cached provider already exists, then that provider will be returned.

    Parameters
    ----------
    client : HyperliquidHttpClient
        The Hyperliquid HTTP client.
    config : InstrumentProviderConfig, optional
        The instrument provider configuration, by default None.

    Returns
    -------
    HyperliquidInstrumentProvider

    """
    return HyperliquidInstrumentProvider(
        client=client,
        config=config,
    )


class HyperliquidLiveDataClientFactory(LiveDataClientFactory):
    """
    Provides a Hyperliquid live data client factory.
    """

    @staticmethod
    def create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: HyperliquidDataClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> HyperliquidDataClient:
        """
        Create a new Hyperliquid data client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        config : HyperliquidDataClientConfig
            The client configuration.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock: LiveClock
            The clock for the instrument provider.

        Returns
        -------
        HyperliquidDataClient

        """
        client = get_cached_hyperliquid_http_client(
            base_url=config.base_url_http,
            timeout_secs=config.http_timeout_secs,
            testnet=config.testnet,
            proxy_url=config.http_proxy_url,
        )
        provider = get_cached_hyperliquid_instrument_provider(
            client=client,
            config=config.instrument_provider,
        )
        return HyperliquidDataClient(
            loop=loop,
            client=client,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            instrument_provider=provider,
            config=config,
            name=name,
        )


class HyperliquidLiveExecClientFactory(LiveExecClientFactory):
    """
    Provides a Hyperliquid live execution client factory.
    """

    @staticmethod
    def create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: HyperliquidExecClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> HyperliquidExecutionClient:
        """
        Create a new Hyperliquid execution client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        config : HyperliquidExecClientConfig
            The client configuration.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock : LiveClock
            The clock for the client.

        Returns
        -------
        HyperliquidExecutionClient

        """
        client = get_cached_hyperliquid_http_client(
            private_key=config.private_key,
            vault_address=config.vault_address,
            base_url=config.base_url_http,
            timeout_secs=config.http_timeout_secs,
            testnet=config.testnet,
            proxy_url=config.http_proxy_url,
        )
        provider = get_cached_hyperliquid_instrument_provider(
            client=client,
            config=config.instrument_provider,
        )
        return HyperliquidExecutionClient(
            loop=loop,
            client=client,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            instrument_provider=provider,
            config=config,
            name=name,
        )
```


---

## Overview

This file is located at `nautilus_trader/adapters/hyperliquid/factories.py` within the repository.

**Classes defined:** HyperliquidLiveDataClientFactory, HyperliquidLiveExecClientFactory

**Functions defined:** get_cached_hyperliquid_http_client, get_cached_hyperliquid_instrument_provider, create, create

**Import statements:** 17


---

## Detailed Analysis

### Classes

#### `HyperliquidLiveDataClientFactory`

**Inherits from:** LiveDataClientFactory


#### `HyperliquidLiveExecClientFactory`

**Inherits from:** LiveExecClientFactory


### Functions

#### `get_cached_hyperliquid_http_client(
    private_key: str | None = None,
    vault_address: str | None = None,
    base_url: str | None = None,
    timeout_secs: int = 10,
    testnet: bool = False,
    proxy_url: str | None = None,
)`


#### `get_cached_hyperliquid_instrument_provider(
    client: HyperliquidHttpClient,
    config: InstrumentProviderConfig | None = None,
)`


#### `create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: HyperliquidDataClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


#### `create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: HyperliquidExecClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


### Imports

- `from __future__ import annotations`
- `import asyncio`
- `from functools import lru_cache`
- `from typing import TYPE_CHECKING`
- `from nautilus_trader.adapters.hyperliquid.config import HyperliquidDataClientConfig`
- `from nautilus_trader.adapters.hyperliquid.config import HyperliquidExecClientConfig`
- `from nautilus_trader.adapters.hyperliquid.data import HyperliquidDataClient`
- `from nautilus_trader.adapters.hyperliquid.execution import HyperliquidExecutionClient`
- `from nautilus_trader.adapters.hyperliquid.providers import HyperliquidInstrumentProvider`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.live.factories import LiveDataClientFactory`
- `from nautilus_trader.live.factories import LiveExecClientFactory`
- `from typing import Any`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.hyperliquid.factories import HyperliquidLiveDataClientFactory
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `import asyncio`
- `from functools import lru_cache`
- `from typing import TYPE_CHECKING`
- `from nautilus_trader.adapters.hyperliquid.config import HyperliquidDataClientConfig`
- `from nautilus_trader.adapters.hyperliquid.config import HyperliquidExecClientConfig`
- `from nautilus_trader.adapters.hyperliquid.data import HyperliquidDataClient`
- `from nautilus_trader.adapters.hyperliquid.execution import HyperliquidExecutionClient`
- `from nautilus_trader.adapters.hyperliquid.providers import HyperliquidInstrumentProvider`
- `from nautilus_trader.cache.cache import Cache`

*... and 7 more*

**Directory:** `nautilus_trader/adapters/hyperliquid`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: private_key, credential. Ensure proper handling of secrets.


