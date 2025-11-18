# Documentation: base.pxd

## File Metadata

- **Path**: `nautilus_trader/indicators/base.pxd`
- **Size**: 1,701 bytes
- **Lines**: 41
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

from nautilus_trader.model.data cimport Bar
from nautilus_trader.model.data cimport QuoteTick
from nautilus_trader.model.data cimport TradeTick


cdef class Indicator:
    cdef list _params

    cdef readonly str name
    """The name of the indicator.\n\n:returns: `str`"""
    cdef readonly bint has_inputs
    """If the indicator has received inputs.\n\n:returns: `bool`"""
    cdef readonly bint initialized
    """If the indicator is warmed up and initialized.\n\n:returns: `bool`"""

    cdef str _params_str(self)

    cpdef void handle_quote_tick(self, QuoteTick tick)
    cpdef void handle_trade_tick(self, TradeTick tick)
    cpdef void handle_bar(self, Bar bar)
    cpdef void reset(self)

    cpdef void _set_has_inputs(self, bint setting)
    cpdef void _set_initialized(self, bint setting)
    cpdef void _reset(self)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 27


**Identifiers**: `ANY`, `All`, `BASIS`, `Bar`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `Indicator`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `QuoteTick`, `See`, `Systems`, `The`, `TradeTick`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/indicators/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.535521Z*
