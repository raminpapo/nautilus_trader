# Documentation: controller.py

## File Metadata

- **Path**: `nautilus_trader/test_kit/mocks/controller.py`
- **Size**: 1,790 bytes
- **Lines**: 41
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

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`ControllerConfig`**: Class defined in this file
- **`MyController`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Classs**: `ControllerConfig`, `MyController`
**Imports**: `nautilus_trader.config`, `nautilus_trader.examples.strategies.signal_strategy`, `nautilus_trader.trading.config`, `nautilus_trader.trading.controller`

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
pytest nautilus_trader/test_kit/mocks/controller.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.964556Z*
