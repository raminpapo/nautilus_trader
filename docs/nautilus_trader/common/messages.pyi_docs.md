# Documentation: messages.pyi

## File Metadata

- **Path**: `nautilus_trader/common/messages.pyi`
- **Size**: 3,044 bytes
- **Lines**: 90
- **Language**: Unknown

## Original Source

```
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

from typing import Any

from nautilus_trader.common.component import ComponentState
from nautilus_trader.core.message import Command
from nautilus_trader.core.message import Event
from nautilus_trader.core.uuid import UUID4
from nautilus_trader.model.enums import TradingState
from nautilus_trader.model.identifiers import ComponentId
from nautilus_trader.model.identifiers import TraderId


class ShutdownSystem(Command):
    @property
    def trader_id(self) -> TraderId: ...
    @property
    def component_id(self) -> ComponentId: ...
    @property
    def reason(self) -> str | None: ...
    @property
    def id(self) -> UUID4: ...
    @property
    def ts_init(self) -> int: ...
    @staticmethod
    def from_dict(values: dict[str, Any]) -> ShutdownSystem: ...
    @staticmethod
    def to_dict(obj: ShutdownSystem) -> dict[str, Any]: ...

class ComponentStateChanged(Event):
    @property
    def trader_id(self) -> TraderId: ...
    @property
    def component_id(self) -> ComponentId: ...
    @property
    def component_type(self) -> str: ...
    @property
    def state(self) -> ComponentState: ...
    @property
    def config(self) -> dict[str, Any]: ...
    @property
    def id(self) -> UUID4: ...
    @property
    def ts_event(self) -> int: ...
    @property
    def ts_init(self) -> int: ...
    @staticmethod
    def from_dict(values: dict[str, Any]) -> ComponentStateChanged: ...
    @staticmethod
    def to_dict(obj: ComponentStateChanged) -> dict[str, Any]: ...

class RiskEvent(Event):
    @property
    def trader_id(self) -> TraderId: ...
    @property
    def id(self) -> UUID4: ...
    @property
    def ts_event(self) -> int: ...
    @property
    def ts_init(self) -> int: ...

class TradingStateChanged(RiskEvent):
    @property
    def state(self) -> TradingState: ...
    @property
    def config(self) -> dict[str, Any]: ...
    @property
    def id(self) -> UUID4: ...
    @property
    def ts_event(self) -> int: ...
    @property
    def ts_init(self) -> int: ...
    @staticmethod
    def from_dict(values: dict[str, Any]) -> TradingStateChanged: ...
    @staticmethod
    def to_dict(obj: TradingStateChanged) -> dict[str, Any]: ...

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 35


**Identifiers**: `ANY`, `All`, `Any`, `BASIS`, `CONDITIONS`, `Command`, `ComponentId`, `ComponentState`, `ComponentStateChanged`, `Copyright`, `Event`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `None`, `Pty`, `Public`, `RiskEvent`, `See`, `ShutdownSystem`, `Systems`, `TraderId`, `TradingState`, `TradingStateChanged`, `UUID4` *(+5 more)*

## Related Files

This file is located in `nautilus_trader/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.260028Z*
