# Documentation: engines.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/mocks/engines.py`
- **Size**: 2,976 bytes
- **Lines**: 118
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

## High-Level Overview

This file is part of the NautilusTrader repository. 3 class(es).

## Detailed Walkthrough


### Classes
- **`MockLiveDataEngine`**: Class defined in this file
- **`MockLiveExecutionEngine`**: Class defined in this file
- **`MockLiveRiskEngine`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `MockLiveDataEngine`, `MockLiveExecutionEngine`, `MockLiveRiskEngine`
**Imports**: `nautilus_trader.live.data_engine`, `nautilus_trader.live.execution_engine`, `nautilus_trader.live.risk_engine`

## Related Files

This file is located in `nautilus_trader/test_kit/mocks/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/test_kit/mocks/engines.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.967841Z*
