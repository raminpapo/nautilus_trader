# Documentation: `nautilus_trader/adapters/bybit/factories.py`
**Generated:** 2025-11-15T19:40:04.194207Z
**File Size:** 9594 bytes
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

- **Path:** `nautilus_trader/adapters/bybit/factories.py`
- **Size:** 9,594 bytes
- **Lines:** 280
- **Extension:** `.py`
- **Type:** text
- **Imports:** 16
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

import asyncio
from functools import lru_cache

from nautilus_trader.adapters.bybit.config import BybitDataClientConfig
from nautilus_trader.adapters.bybit.config import BybitExecClientConfig
from nautilus_trader.adapters.bybit.constants import BYBIT_ALL_PRODUCTS
from nautilus_trader.adapters.bybit.data import BybitDataClient
from nautilus_trader.adapters.bybit.execution import BybitExecutionClient
from nautilus_trader.adapters.bybit.providers import BybitInstrumentProvider
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.config import InstrumentProviderConfig
from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.core.nautilus_pyo3 import BybitProductType
from nautilus_trader.live.factories import LiveDataClientFactory
from nautilus_trader.live.factories import LiveExecClientFactory


@lru_cache(1)
def get_cached_bybit_http_client(
    api_key: str | None = None,
    api_secret: str | None = None,
    base_url: str | None = None,
    demo: bool = False,
    testnet: bool = False,
    timeout_secs: int | None = None,
    max_retries: int | None = None,
    retry_delay_ms: int | None = None,
    retry_delay_max_ms: int | None = None,
    recv_window_ms: int | None = None,
    proxy_url: str | None = None,
) -> nautilus_pyo3.BybitHttpClient:
    """
    Cache and return a Bybit HTTP client with the given key and secret.

    If ``api_key`` and ``api_secret`` are ``None``, then they will be sourced from the
    environment variables ``BYBIT_API_KEY`` and ``BYBIT_API_SECRET`` for production,
    ``BYBIT_DEMO_API_KEY`` and ``BYBIT_DEMO_API_SECRET`` when ``demo=True``,
    or ``BYBIT_TESTNET_API_KEY`` and ``BYBIT_TESTNET_API_SECRET`` when ``testnet=True``.

    If a cached client with matching parameters already exists, the cached client will be returned.

    Parameters
    ----------
    api_key : str, optional
        The API key for the client.
    api_secret : str, optional
        The API secret for the client.
    base_url : str, optional
        The base URL for the API endpoints.
    demo : bool, default False
        If the client is connecting to the demo API.
    testnet : bool, default False
        If the client is connecting to the testnet API.
    timeout_secs : int, optional
        The timeout for HTTP requests in seconds.
    max_retries : int, optional
        The maximum number of retry attempts for failed requests.
    retry_delay_ms : int, optional
        The initial delay (milliseconds) between retries.
    retry_delay_max_ms : int, optional
        The maximum delay (milliseconds) between retries.
    recv_window_ms : int, optional
        The receive window (milliseconds) for Bybit HTTP requests.
    proxy_url : str, optional
        The proxy URL for HTTP requests.

    Returns
    -------
    BybitHttpClient

    """
    if base_url is None:
        # Priority: demo > testnet > mainnet
        if demo:
            environment = nautilus_pyo3.BybitEnvironment.DEMO
        elif testnet:
            environment = nautilus_pyo3.BybitEnvironment.TESTNET
        else:
            environment = nautilus_pyo3.BybitEnvironment.MAINNET
        base_url = nautilus_pyo3.get_bybit_http_base_url(environment)

    return nautilus_pyo3.BybitHttpClient(
        api_key=api_key,
        api_secret=api_secret,
        base_url=base_url,
        demo=demo,
        testnet=testnet,
        timeout_secs=timeout_secs,
        max_retries=max_retries,
        retry_delay_ms=retry_delay_ms,
        retry_delay_max_ms=retry_delay_max_ms,
        recv_window_ms=recv_window_ms,
        proxy_url=proxy_url,
    )


@lru_cache(1)
def get_cached_bybit_instrument_provider(
    client: nautilus_pyo3.BybitHttpClient,
    product_types: tuple[BybitProductType, ...],
    config: InstrumentProviderConfig | None = None,
) -> BybitInstrumentProvider:
    """
    Cache and return a Bybit instrument provider.

    If a cached provider already exists, then that provider will be returned.

    Parameters
    ----------
    client : BybitHttpClient
        The Bybit HTTP client.
    product_types : tuple[BybitProductType, ...]
        The product types to load.
    config : InstrumentProviderConfig, optional
        The instrument provider configuration, by default None.

    Returns
    -------
    BybitInstrumentProvider

    """
    return BybitInstrumentProvider(
        client=client,
        product_types=product_types,
        config=config,
    )


class BybitLiveDataClientFactory(LiveDataClientFactory):
    """
    Provides a Bybit live data client factory.
    """

    @staticmethod
    def create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: BybitDataClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> BybitDataClient:
        """
        Create a new Bybit data client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        config : BybitDataClientConfig
            The client configuration.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock: LiveClock
            The clock for the instrument provider.

        Returns
        -------
        BybitDataClient

        """
        product_types = config.product_types or BYBIT_ALL_PRODUCTS
        client: nautilus_pyo3.BybitHttpClient = get_cached_bybit_http_client(
            api_key=config.api_key,
            api_secret=config.api_secret,
            base_url=config.base_url_http,
            demo=config.demo,
            testnet=config.testnet,
            timeout_secs=None,  # Use Rust default (60s)
            max_retries=config.max_retries,
            retry_delay_ms=config.retry_delay_initial_ms,
            retry_delay_max_ms=config.retry_delay_max_ms,
            recv_window_ms=config.recv_window_ms,
            proxy_url=config.http_proxy_url,
        )
        provider = get_cached_bybit_instrument_provider(
            client=client,
            product_types=tuple(product_types),
            config=config.instrument_provider,
        )
        return BybitDataClient(
            loop=loop,
            client=client,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            instrument_provider=provider,
            config=config,
            name=name,
        )


class BybitLiveExecClientFactory(LiveExecClientFactory):
    """
    Provides a Bybit live execution client factory.
    """

    @staticmethod
    def create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: BybitExecClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> BybitExecutionClient:
        """
        Create a new Bybit execution client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        config : BybitExecClientConfig
            The client configuration.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock : LiveClock
            The clock for the client.

        Returns
        -------
        BybitExecutionClient

        """
        product_types = config.product_types or BYBIT_ALL_PRODUCTS
        # Use Rust HTTP client
        client: nautilus_pyo3.BybitHttpClient = get_cached_bybit_http_client(
            api_key=config.api_key,
            api_secret=config.api_secret,
            base_url=config.base_url_http,
            demo=config.demo,
            testnet=config.testnet,
            timeout_secs=None,  # Use Rust default (60s)
            max_retries=config.max_retries,
            retry_delay_ms=config.retry_delay_initial_ms,
            retry_delay_max_ms=config.retry_delay_max_ms,
            recv_window_ms=config.recv_window_ms,
            proxy_url=config.http_proxy_url,
        )
        provider = get_cached_bybit_instrument_provider(
            client=client,
            product_types=tuple(product_types),
            config=config.instrument_provider,
        )
        return BybitExecutionClient(
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

This file is located at `nautilus_trader/adapters/bybit/factories.py` within the repository.

**Classes defined:** BybitLiveDataClientFactory, BybitLiveExecClientFactory

**Functions defined:** get_cached_bybit_http_client, get_cached_bybit_instrument_provider, create, create

**Import statements:** 16


---

## Detailed Analysis

### Classes

#### `BybitLiveDataClientFactory`

**Inherits from:** LiveDataClientFactory


#### `BybitLiveExecClientFactory`

**Inherits from:** LiveExecClientFactory


### Functions

#### `get_cached_bybit_http_client(
    api_key: str | None = None,
    api_secret: str | None = None,
    base_url: str | None = None,
    demo: bool = False,
    testnet: bool = False,
    timeout_secs: int | None = None,
    max_retries: int | None = None,
    retry_delay_ms: int | None = None,
    retry_delay_max_ms: int | None = None,
    recv_window_ms: int | None = None,
    proxy_url: str | None = None,
)`


#### `get_cached_bybit_instrument_provider(
    client: nautilus_pyo3.BybitHttpClient,
    product_types: tuple[BybitProductType, ...],
    config: InstrumentProviderConfig | None = None,
)`


#### `create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: BybitDataClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


#### `create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: BybitExecClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


### Imports

- `import asyncio`
- `from functools import lru_cache`
- `from nautilus_trader.adapters.bybit.config import BybitDataClientConfig`
- `from nautilus_trader.adapters.bybit.config import BybitExecClientConfig`
- `from nautilus_trader.adapters.bybit.constants import BYBIT_ALL_PRODUCTS`
- `from nautilus_trader.adapters.bybit.data import BybitDataClient`
- `from nautilus_trader.adapters.bybit.execution import BybitExecutionClient`
- `from nautilus_trader.adapters.bybit.providers import BybitInstrumentProvider`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.config import InstrumentProviderConfig`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.nautilus_pyo3 import BybitProductType`
- `from nautilus_trader.live.factories import LiveDataClientFactory`
- `from nautilus_trader.live.factories import LiveExecClientFactory`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.bybit.factories import BybitLiveDataClientFactory
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from functools import lru_cache`
- `from nautilus_trader.adapters.bybit.config import BybitDataClientConfig`
- `from nautilus_trader.adapters.bybit.config import BybitExecClientConfig`
- `from nautilus_trader.adapters.bybit.constants import BYBIT_ALL_PRODUCTS`
- `from nautilus_trader.adapters.bybit.data import BybitDataClient`
- `from nautilus_trader.adapters.bybit.execution import BybitExecutionClient`
- `from nautilus_trader.adapters.bybit.providers import BybitInstrumentProvider`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`

*... and 6 more*

**Directory:** `nautilus_trader/adapters/bybit`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.


