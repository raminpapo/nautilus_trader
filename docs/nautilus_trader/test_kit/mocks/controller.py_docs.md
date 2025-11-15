# Documentation: `nautilus_trader/test_kit/mocks/controller.py`
**Generated:** 2025-11-15T19:40:05.337502Z
**File Size:** 1790 bytes
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

- **Path:** `nautilus_trader/test_kit/mocks/controller.py`
- **Size:** 1,790 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5
- **Classes:** 2
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

from nautilus_trader.config import ActorConfig
from nautilus_trader.examples.strategies.signal_strategy import SignalStrategy
from nautilus_trader.examples.strategies.signal_strategy import SignalStrategyConfig
from nautilus_trader.trading.config import ImportableStrategyConfig
from nautilus_trader.trading.controller import Controller


class ControllerConfig(ActorConfig, frozen=True):
    pass


class MyController(Controller):
    def start(self):
        """
        Dynamically add a new strategy after startup.
        """
        instruments = self.cache.instruments()
        strategy_config = ImportableStrategyConfig(
            strategy_path=SignalStrategy.fully_qualified_name(),
            config_path=SignalStrategyConfig.fully_qualified_name(),
            config={
                "instrument_id": instruments[0].id,
            },
        )
        self.create_strategy_from_config(strategy_config)
```


---

## Overview

This file is located at `nautilus_trader/test_kit/mocks/controller.py` within the repository.

**Classes defined:** ControllerConfig, MyController

**Functions defined:** start

**Import statements:** 5


---

## Detailed Analysis

### Classes

#### `ControllerConfig`

**Inherits from:** ActorConfig, frozen=True


#### `MyController`

**Inherits from:** Controller


### Functions

#### `start(self)`


### Imports

- `from nautilus_trader.config import ActorConfig`
- `from nautilus_trader.examples.strategies.signal_strategy import SignalStrategy`
- `from nautilus_trader.examples.strategies.signal_strategy import SignalStrategyConfig`
- `from nautilus_trader.trading.config import ImportableStrategyConfig`
- `from nautilus_trader.trading.controller import Controller`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.mocks.controller import ControllerConfig
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.config import ActorConfig`
- `from nautilus_trader.examples.strategies.signal_strategy import SignalStrategy`
- `from nautilus_trader.examples.strategies.signal_strategy import SignalStrategyConfig`
- `from nautilus_trader.trading.config import ImportableStrategyConfig`
- `from nautilus_trader.trading.controller import Controller`

**Directory:** `nautilus_trader/test_kit/mocks`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


