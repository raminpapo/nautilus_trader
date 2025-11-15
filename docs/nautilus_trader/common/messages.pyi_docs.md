# Documentation: `nautilus_trader/common/messages.pyi`
**Generated:** 2025-11-15T19:40:04.702611Z
**File Size:** 3044 bytes
**Extension:** .pyi
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

- **Path:** `nautilus_trader/common/messages.pyi`
- **Size:** 3,044 bytes
- **Lines:** 89
- **Extension:** `.pyi`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `nautilus_trader/common/messages.pyi` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


