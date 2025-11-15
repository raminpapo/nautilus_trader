# Documentation: `nautilus_trader/common/messages.pxd`
**Generated:** 2025-11-15T19:40:04.701461Z
**File Size:** 3338 bytes
**Extension:** .pxd
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

- **Path:** `nautilus_trader/common/messages.pxd`
- **Size:** 3,338 bytes
- **Lines:** 88
- **Extension:** `.pxd`
- **Type:** text

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

from libc.stdint cimport uint64_t

from nautilus_trader.core.message cimport Command
from nautilus_trader.core.message cimport Event
from nautilus_trader.core.rust.common cimport ComponentState
from nautilus_trader.core.rust.model cimport TradingState
from nautilus_trader.core.uuid cimport UUID4
from nautilus_trader.model.identifiers cimport ComponentId
from nautilus_trader.model.identifiers cimport Identifier
from nautilus_trader.model.identifiers cimport TraderId


cdef class ShutdownSystem(Command):
    cdef UUID4 _command_id
    cdef uint64_t _ts_init

    cdef readonly TraderId trader_id
    """The trader ID associated with the event.\n\n:returns: `TraderId`"""
    cdef readonly Identifier component_id
    """The component ID associated with the event.\n\n:returns: `Identifier`"""
    cdef readonly str reason
    """The reason for the shutdown command.\n\n:returns: `str` or ``None``"""

    @staticmethod
    cdef ShutdownSystem from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(ShutdownSystem obj)


cdef class ComponentStateChanged(Event):
    cdef UUID4 _event_id
    cdef uint64_t _ts_event
    cdef uint64_t _ts_init

    cdef readonly TraderId trader_id
    """The trader ID associated with the event.\n\n:returns: `TraderId`"""
    cdef readonly Identifier component_id
    """The component ID associated with the event.\n\n:returns: `Identifier`"""
    cdef readonly str component_type
    """The component type associated with the event.\n\n:returns: `str`"""
    cdef readonly ComponentState state
    """The component state.\n\n:returns: `ComponentState`"""
    cdef readonly dict config
    """The component configuration.\n\n:returns: `dict[str, Any]`"""

    @staticmethod
    cdef ComponentStateChanged from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(ComponentStateChanged obj)


cdef class RiskEvent(Event):
    cdef UUID4 _event_id
    cdef uint64_t _ts_event
    cdef uint64_t _ts_init

    cdef readonly TraderId trader_id
    """The trader ID associated with the event.\n\n:returns: `TraderId`"""


cdef class TradingStateChanged(RiskEvent):
    cdef readonly TradingState state
    """The trading state for the event.\n\n:returns: `TradingState`"""
    cdef readonly dict config
    """The risk engine configuration.\n\n:returns: `dict[str, Any]`"""

    @staticmethod
    cdef TradingStateChanged from_dict_c(dict values)

    @staticmethod
    cdef dict to_dict_c(TradingStateChanged obj)
```


---

## Overview

This file is located at `nautilus_trader/common/messages.pxd` within the repository.


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


