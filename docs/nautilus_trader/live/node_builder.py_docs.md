# Documentation: `nautilus_trader/live/node_builder.py`
**Generated:** 2025-11-15T19:40:05.009468Z
**File Size:** 9566 bytes
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

- **Path:** `nautilus_trader/live/node_builder.py`
- **Size:** 9,566 bytes
- **Lines:** 268
- **Extension:** `.py`
- **Type:** text
- **Imports:** 15
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

import asyncio

from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import Logger
from nautilus_trader.common.component import MessageBus
from nautilus_trader.config import ImportableConfig
from nautilus_trader.config import LiveDataClientConfig
from nautilus_trader.config import LiveExecClientConfig
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.live.data_engine import LiveDataEngine
from nautilus_trader.live.execution_engine import LiveExecutionEngine
from nautilus_trader.live.factories import LiveDataClientFactory
from nautilus_trader.live.factories import LiveExecClientFactory
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.portfolio.portfolio import Portfolio


class TradingNodeBuilder:
    """
    Provides building services for a trading node.

    Parameters
    ----------
    loop : asyncio.AbstractEventLoop
        The event loop for the clients.
    data_engine : LiveDataEngine
        The data engine for the trading node.
    exec_engine : LiveExecutionEngine
        The execution engine for the trading node.
    portfolio : Portfolio
        The portfolio for the trading node.
    msgbus : MessageBus
        The message bus for the trading node.
    cache : Cache
        The cache for building clients.
    clock : LiveClock
        The clock for building clients.
    logger : Logger
        The logger for building clients.
    log : Logger
        The trading nodes logger.

    """

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        data_engine: LiveDataEngine,
        exec_engine: LiveExecutionEngine,
        portfolio: Portfolio,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
        logger: Logger,
    ) -> None:
        self._msgbus = msgbus
        self._cache = cache
        self._clock = clock
        self._log = logger

        self._loop = loop
        self._data_engine = data_engine
        self._exec_engine = exec_engine
        self._portfolio = portfolio

        self._data_factories: dict[str, type[LiveDataClientFactory]] = {}
        self._exec_factories: dict[str, type[LiveExecClientFactory]] = {}

    def add_data_client_factory(self, name: str, factory: type[LiveDataClientFactory]) -> None:
        """
        Add the given data client factory to the builder.

        Parameters
        ----------
        name : str
            The name of the client.
        factory : type[LiveDataClientFactory]
            The factory to add.

        Raises
        ------
        ValueError
            If `name` is not a valid string.
        KeyError
            If `name` has already been added.

        """
        PyCondition.valid_string(name, "name")
        PyCondition.not_none(factory, "factory")
        PyCondition.not_in(name, self._data_factories, "name", "_data_factories")

        if not issubclass(factory, LiveDataClientFactory):
            self._log.error(f"Factory was not of type `LiveDataClientFactory`, was {factory}")
            return

        self._data_factories[name] = factory

    def add_exec_client_factory(self, name: str, factory: type[LiveExecClientFactory]) -> None:
        """
        Add the given client factory to the builder.

        Parameters
        ----------
        name : str
            The name of the client.
        factory : type[LiveExecClientFactory]
            The factory to add.

        Raises
        ------
        ValueError
            If `name` is not a valid string.
        KeyError
            If `name` has already been added.

        """
        PyCondition.valid_string(name, "name")
        PyCondition.not_none(factory, "factory")
        PyCondition.not_in(name, self._exec_factories, "name", "_exec_factories")

        if not issubclass(factory, LiveExecClientFactory):
            self._log.error(f"Factory was not of type `LiveExecClientFactory`, was {factory}")
            return

        self._exec_factories[name] = factory

    def build_data_clients(
        self,
        config: dict[str, LiveDataClientConfig],
    ) -> None:
        """
        Build the data clients with the given configuration.

        Parameters
        ----------
        config : dict[str, ImportableConfig | LiveDataClientConfig]
            The data clients configuration.

        """
        PyCondition.not_none(config, "config")

        if not config and not self._data_engine.get_external_client_ids():
            self._log.warning("No `data_clients` configuration found")

        for parts, cfg in config.items():
            name = parts.partition("-")[0]
            self._log.info(f"Building data client for {name}")

            if isinstance(cfg, ImportableConfig):
                if name not in self._data_factories and cfg.factory is not None:
                    self._data_factories[name] = cfg.factory.create()

                client_config: LiveDataClientConfig = cfg.create()
            else:
                client_config: LiveDataClientConfig = cfg  # type: ignore

            if name not in self._data_factories:
                self._log.error(f"No `LiveDataClientFactory` registered for {name}")
                continue

            factory = self._data_factories[name]
            client = factory.create(
                loop=self._loop,
                name=name,
                config=client_config,
                msgbus=self._msgbus,
                cache=self._cache,
                clock=self._clock,
            )
            self._data_engine.register_client(client)

            # Default client config
            if client_config.routing.default:
                self._data_engine.register_default_client(client)

            # Venue routing config
            venues: frozenset[str] = client_config.routing.venues or frozenset()

            for venue in venues:
                if not isinstance(venue, Venue):
                    venue = Venue(venue)

                self._data_engine.register_venue_routing(client, venue)

    def build_exec_clients(  # noqa: C901 (too complex)
        self,
        config: dict[str, LiveExecClientConfig],
    ) -> None:
        """
        Build the execution clients with the given configuration.

        Parameters
        ----------
        config : dict[str, ImportableConfig | LiveExecClientConfig]
            The execution clients configuration.

        """
        PyCondition.not_none(config, "config")

        if not config and not self._exec_engine.get_external_client_ids():
            self._log.warning("No `exec_clients` configuration found")

        for parts, cfg in config.items():
            name = parts.partition("-")[0]
            self._log.info(f"Building execution client for {name}")

            if isinstance(cfg, ImportableConfig):
                if name not in self._exec_factories and cfg.factory is not None:
                    self._exec_factories[name] = cfg.factory.create()

                client_config: LiveExecClientConfig = cfg.create()
            else:
                client_config: LiveExecClientConfig = cfg  # type: ignore

            if name not in self._exec_factories:
                self._log.error(f"No `LiveExecClientFactory` registered for {name}")
                continue

            factory = self._exec_factories[name]

            factory_kws = {
                "loop": self._loop,
                "name": name,
                "config": client_config,
                "msgbus": self._msgbus,
                "cache": self._cache,
                "clock": self._clock,
            }

            if factory.__name__ == "SandboxLiveExecClientFactory":
                factory_kws["portfolio"] = self._portfolio

            client = factory.create(**factory_kws)
            self._exec_engine.register_client(client)

            # Default client config
            if client_config.routing.default:
                self._exec_engine.register_default_client(client)

            # Venue routing config
            venues: frozenset[str] = client_config.routing.venues or frozenset()

            for venue in venues:
                if not isinstance(venue, Venue):
                    venue = Venue(venue)

                self._exec_engine.register_venue_routing(client, venue)

            # Temporary handling for setting specific 'venue' for portfolio
            if factory.__name__ == "InteractiveBrokersLiveExecClientFactory":
                # We initialize a new IB venue to avoid importing from the adapter subpackage
                self._cache.set_specific_venue(Venue("INTERACTIVE_BROKERS"))
```


---

## Overview

This file is located at `nautilus_trader/live/node_builder.py` within the repository.

**Classes defined:** TradingNodeBuilder

**Functions defined:** __init__, add_data_client_factory, add_exec_client_factory, build_data_clients, build_exec_clients

**Import statements:** 15


---

## Detailed Analysis

### Classes

#### `TradingNodeBuilder`


### Functions

#### `__init__(
        self,
        loop: asyncio.AbstractEventLoop,
        data_engine: LiveDataEngine,
        exec_engine: LiveExecutionEngine,
        portfolio: Portfolio,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
        logger: Logger,
    )`


#### `add_data_client_factory(self, name: str, factory: type[LiveDataClientFactory])`


#### `add_exec_client_factory(self, name: str, factory: type[LiveExecClientFactory])`


#### `build_data_clients(
        self,
        config: dict[str, LiveDataClientConfig],
    )`


#### `build_exec_clients(  # noqa: C901 (too complex)`


### Imports

- `import asyncio`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.config import ImportableConfig`
- `from nautilus_trader.config import LiveDataClientConfig`
- `from nautilus_trader.config import LiveExecClientConfig`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.live.data_engine import LiveDataEngine`
- `from nautilus_trader.live.execution_engine import LiveExecutionEngine`
- `from nautilus_trader.live.factories import LiveDataClientFactory`
- `from nautilus_trader.live.factories import LiveExecClientFactory`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.portfolio.portfolio import Portfolio`


---

## Usage Examples

### Importing

```python
from nautilus_trader.live.node_builder import TradingNodeBuilder
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.config import ImportableConfig`
- `from nautilus_trader.config import LiveDataClientConfig`
- `from nautilus_trader.config import LiveExecClientConfig`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.live.data_engine import LiveDataEngine`

*... and 5 more*

**Directory:** `nautilus_trader/live`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


