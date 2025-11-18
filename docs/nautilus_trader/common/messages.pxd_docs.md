# Documentation: messages.pxd

## File Metadata

- **Path**: `nautilus_trader/common/messages.pxd`
- **Size**: 3,338 bytes
- **Lines**: 89
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 37


**Identifiers**: `ANY`, `All`, `Any`, `BASIS`, `CONDITIONS`, `Command`, `ComponentId`, `ComponentState`, `ComponentStateChanged`, `Copyright`, `Event`, `GNU`, `General`, `Identifier`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `None`, `Pty`, `Public`, `RiskEvent`, `See`, `ShutdownSystem`, `Systems`, `The`, `TraderId`, `TradingState` *(+7 more)*

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
*Generated on 2025-11-18T21:55:05.258707Z*
