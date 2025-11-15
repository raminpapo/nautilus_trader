# Documentation: `nautilus_trader/test_kit/mocks/engines.py`
**Generated:** 2025-11-15T19:40:05.340433Z
**File Size:** 2976 bytes
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

- **Path:** `nautilus_trader/test_kit/mocks/engines.py`
- **Size:** 2,976 bytes
- **Lines:** 117
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 3
- **Functions:** 10

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

from nautilus_trader.live.data_engine import LiveDataEngine
from nautilus_trader.live.execution_engine import LiveExecutionEngine
from nautilus_trader.live.risk_engine import LiveRiskEngine


class MockLiveDataEngine(LiveDataEngine):
    """
    Provides a mock live data engine for testing.
    """

    def __init__(
        self,
        loop,
        msgbus,
        cache,
        clock,
        config=None,
    ):
        super().__init__(
            loop=loop,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            config=config,
        )

        self.commands = []
        self.events = []
        self.responses = []

    def execute(self, command):
        self.commands.append(command)

    def process(self, data):
        self.events.append(data)

    def receive(self, response):
        self.responses.append(response)


class MockLiveExecutionEngine(LiveExecutionEngine):
    """
    Provides a mock live execution engine for testing.
    """

    def __init__(
        self,
        loop,
        msgbus,
        cache,
        clock,
        config=None,
    ):
        super().__init__(
            loop=loop,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            config=config,
        )

        self.commands = []
        self.events = []

    def execute(self, command):
        self.commands.append(command)

    def process(self, event):
        self.events.append(event)


class MockLiveRiskEngine(LiveRiskEngine):
    """
    Provides a mock live risk engine for testing.
    """

    def __init__(
        self,
        loop,
        portfolio,
        msgbus,
        cache,
        clock,
        config=None,
    ):
        super().__init__(
            loop=loop,
            portfolio=portfolio,
            msgbus=msgbus,
            cache=cache,
            clock=clock,
            config=config,
        )

        self.commands = []
        self.events = []

    def execute(self, command):
        self.commands.append(command)

    def process(self, event):
        self.events.append(event)
```


---

## Overview

This file is located at `nautilus_trader/test_kit/mocks/engines.py` within the repository.

**Classes defined:** MockLiveDataEngine, MockLiveExecutionEngine, MockLiveRiskEngine

**Functions defined:** __init__, execute, process, receive, __init__, execute, process, __init__, execute, process

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `MockLiveDataEngine`

**Inherits from:** LiveDataEngine


#### `MockLiveExecutionEngine`

**Inherits from:** LiveExecutionEngine


#### `MockLiveRiskEngine`

**Inherits from:** LiveRiskEngine


### Functions

#### `__init__(
        self,
        loop,
        msgbus,
        cache,
        clock,
        config=None,
    )`


#### `execute(self, command)`


#### `process(self, data)`


#### `receive(self, response)`


#### `__init__(
        self,
        loop,
        msgbus,
        cache,
        clock,
        config=None,
    )`


#### `execute(self, command)`


#### `process(self, event)`


#### `__init__(
        self,
        loop,
        portfolio,
        msgbus,
        cache,
        clock,
        config=None,
    )`


#### `execute(self, command)`


#### `process(self, event)`


### Imports

- `from nautilus_trader.live.data_engine import LiveDataEngine`
- `from nautilus_trader.live.execution_engine import LiveExecutionEngine`
- `from nautilus_trader.live.risk_engine import LiveRiskEngine`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.mocks.engines import MockLiveDataEngine
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.live.data_engine import LiveDataEngine`
- `from nautilus_trader.live.execution_engine import LiveExecutionEngine`
- `from nautilus_trader.live.risk_engine import LiveRiskEngine`

**Directory:** `nautilus_trader/test_kit/mocks`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


