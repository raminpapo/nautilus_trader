# Documentation: `nautilus_trader/backtest/node_builder.py`
**Generated:** 2025-11-15T19:40:04.600035Z
**File Size:** 4722 bytes
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

- **Path:** `nautilus_trader/backtest/node_builder.py`
- **Size:** 4,722 bytes
- **Lines:** 133
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 1
- **Functions:** 3

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

from nautilus_trader.backtest.engine import BacktestEngine
from nautilus_trader.common.component import Logger
from nautilus_trader.config import ImportableConfig
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.live.config import LiveDataClientConfig
from nautilus_trader.live.factories import LiveDataClientFactory
from nautilus_trader.model.identifiers import Venue


class BacktestNodeBuilder:
    """
    Provides building services for a backtest node.

    Parameters
    ----------
    engine : BacktestEngine
        The backtest engine for the node.
    logger : Logger
        The logger for building clients.

    """

    def __init__(
        self,
        engine: BacktestEngine,
        logger: Logger,
    ) -> None:
        self._engine = engine
        self._log = logger
        self._data_factories: dict[str, type[LiveDataClientFactory]] = {}

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
        if not issubclass(factory, LiveDataClientFactory):
            self._log.error(f"Factory was not of type `LiveDataClientFactory`, was {factory}")
            return

        self._data_factories[name] = factory

    def build_data_clients(
        self,
        config: dict[str, type[LiveDataClientConfig]],
    ) -> None:
        """
        Build the data clients with the given configuration.

        Parameters
        ----------
        config : dict[str, ImportableConfig | LiveExecClientConfig]
            The execution clients configuration.

        """
        PyCondition.not_none(config, "config")

        if not config:
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

            # We create an event loop here only to satisfy the linters, it won't be used
            client = factory.create(
                loop=asyncio.new_event_loop(),
                name=name,
                config=client_config,
                msgbus=self._engine.kernel.msgbus,
                cache=self._engine.kernel.cache,
                clock=self._engine.kernel.clock,
            )
            client._is_sync = True
            self._engine.kernel.data_engine.register_client(client)

            # Default client config
            if client_config.routing.default:
                self._engine.kernel.data_engine.register_default_client(client)

            # Venue routing config
            venues: frozenset[str] = client_config.routing.venues or frozenset()

            for venue in venues:
                if not isinstance(venue, Venue):
                    venue = Venue(venue)

                self._engine.kernel.data_engine.register_venue_routing(client, venue)
```


---

## Overview

This file is located at `nautilus_trader/backtest/node_builder.py` within the repository.

**Classes defined:** BacktestNodeBuilder

**Functions defined:** __init__, add_data_client_factory, build_data_clients

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `BacktestNodeBuilder`


### Functions

#### `__init__(
        self,
        engine: BacktestEngine,
        logger: Logger,
    )`


#### `add_data_client_factory(self, name: str, factory: type[LiveDataClientFactory])`


#### `build_data_clients(
        self,
        config: dict[str, type[LiveDataClientConfig]],
    )`


### Imports

- `import asyncio`
- `from nautilus_trader.backtest.engine import BacktestEngine`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.config import ImportableConfig`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.live.config import LiveDataClientConfig`
- `from nautilus_trader.live.factories import LiveDataClientFactory`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from nautilus_trader.backtest.node_builder import BacktestNodeBuilder
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.backtest.engine import BacktestEngine`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.config import ImportableConfig`
- `from nautilus_trader.core.correctness import PyCondition`
- `from nautilus_trader.live.config import LiveDataClientConfig`
- `from nautilus_trader.live.factories import LiveDataClientFactory`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `nautilus_trader/backtest`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


