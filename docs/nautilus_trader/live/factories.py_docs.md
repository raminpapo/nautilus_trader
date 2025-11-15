# Documentation: `nautilus_trader/live/factories.py`
**Generated:** 2025-11-15T19:40:05.005440Z
**File Size:** 3395 bytes
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

- **Path:** `nautilus_trader/live/factories.py`
- **Size:** 3,395 bytes
- **Lines:** 108
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 2
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

import asyncio

from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.config import LiveDataClientConfig
from nautilus_trader.config import LiveExecClientConfig
from nautilus_trader.live.data_client import LiveDataClient
from nautilus_trader.live.execution_client import LiveExecutionClient


class LiveDataClientFactory:
    """
    Provides a factory for creating `LiveDataClient` instances.
    """

    @staticmethod
    def create(
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: LiveDataClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> LiveDataClient:
        """
        Return a new data client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        config : dict[str, object]
            The configuration for the client.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock : LiveClock
            The clock for the client.

        Returns
        -------
        LiveDataClient

        """
        raise NotImplementedError(
            "method `create` must be implemented in the subclass",
        )  # pragma: no cover


class LiveExecClientFactory:
    """
    Provides a factory for creating `LiveExecutionClient` instances.
    """

    @staticmethod
    def create(
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: LiveExecClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> LiveExecutionClient:
        """
        Return a new execution client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        config : dict[str, object]
            The configuration for the client.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock : LiveClock
            The clock for the client.

        Returns
        -------
        LiveExecutionClient

        """
        raise NotImplementedError(
            "method `create' must be implemented in the subclass",
        )  # pragma: no cover
```


---

## Overview

This file is located at `nautilus_trader/live/factories.py` within the repository.

**Classes defined:** LiveDataClientFactory, LiveExecClientFactory

**Functions defined:** create, create

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `LiveDataClientFactory`


#### `LiveExecClientFactory`


### Functions

#### `create(
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: LiveDataClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


#### `create(
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: LiveExecClientConfig,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


### Imports

- `import asyncio`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.config import LiveDataClientConfig`
- `from nautilus_trader.config import LiveExecClientConfig`
- `from nautilus_trader.live.data_client import LiveDataClient`
- `from nautilus_trader.live.execution_client import LiveExecutionClient`


---

## Usage Examples

### Importing

```python
from nautilus_trader.live.factories import LiveDataClientFactory
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.config import LiveDataClientConfig`
- `from nautilus_trader.config import LiveExecClientConfig`
- `from nautilus_trader.live.data_client import LiveDataClient`
- `from nautilus_trader.live.execution_client import LiveExecutionClient`

**Directory:** `nautilus_trader/live`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


