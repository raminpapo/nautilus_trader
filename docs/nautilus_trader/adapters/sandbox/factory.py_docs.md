# Documentation: `nautilus_trader/adapters/sandbox/factory.py`
**Generated:** 2025-11-15T19:40:04.496994Z
**File Size:** 2676 bytes
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

- **Path:** `nautilus_trader/adapters/sandbox/factory.py`
- **Size:** 2,676 bytes
- **Lines:** 75
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 1
- **Functions:** 1

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

from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig
from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient
from nautilus_trader.cache.cache import Cache
from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import MessageBus
from nautilus_trader.live.factories import LiveExecClientFactory
from nautilus_trader.portfolio import PortfolioFacade


class SandboxLiveExecClientFactory(LiveExecClientFactory):
    """
    Provides a `Sandbox` live execution client factory.
    """

    @staticmethod
    def create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: SandboxExecutionClientConfig,
        portfolio: PortfolioFacade,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    ) -> SandboxExecutionClient:
        """
        Create a new Sandbox execution client.

        Parameters
        ----------
        loop : asyncio.AbstractEventLoop
            The event loop for the client.
        name : str
            The custom client ID.
        portfolio : PortfolioFacade
            The read-only portfolio for the client.
        msgbus : MessageBus
            The message bus for the client.
        cache : Cache
            The cache for the client.
        clock : LiveClock
            The clock for the client.
        config : dict[str, object]
            The configuration for the client.

        Returns
        -------
        SandboxExecutionClient

        """
        exec_client = SandboxExecutionClient(
            loop=loop,
            clock=clock,
            portfolio=portfolio,
            msgbus=msgbus,
            cache=cache,
            config=config,
        )
        return exec_client
```


---

## Overview

This file is located at `nautilus_trader/adapters/sandbox/factory.py` within the repository.

**Classes defined:** SandboxLiveExecClientFactory

**Functions defined:** create

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `SandboxLiveExecClientFactory`

**Inherits from:** LiveExecClientFactory


### Functions

#### `create(  # type: ignore
        loop: asyncio.AbstractEventLoop,
        name: str,
        config: SandboxExecutionClientConfig,
        portfolio: PortfolioFacade,
        msgbus: MessageBus,
        cache: Cache,
        clock: LiveClock,
    )`


### Imports

- `import asyncio`
- `from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig`
- `from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.live.factories import LiveExecClientFactory`
- `from nautilus_trader.portfolio import PortfolioFacade`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.sandbox.factory import SandboxLiveExecClientFactory
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from nautilus_trader.adapters.sandbox.config import SandboxExecutionClientConfig`
- `from nautilus_trader.adapters.sandbox.execution import SandboxExecutionClient`
- `from nautilus_trader.cache.cache import Cache`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import MessageBus`
- `from nautilus_trader.live.factories import LiveExecClientFactory`
- `from nautilus_trader.portfolio import PortfolioFacade`

**Directory:** `nautilus_trader/adapters/sandbox`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


