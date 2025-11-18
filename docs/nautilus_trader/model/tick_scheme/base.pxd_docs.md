# Documentation: base.pxd

## File Metadata

- **Path**: `nautilus_trader/model/tick_scheme/base.pxd`
- **Size**: 2,252 bytes
- **Lines**: 54
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

from libc.math cimport fabs
from libc.math cimport fmax
from libc.math cimport fmin

from nautilus_trader.model.objects cimport Price


cdef dict[str, TickScheme] TICK_SCHEMES

cdef class TickScheme:
    cdef readonly str name
    """The name of the scheme.\n\n:returns: `str`"""
    cdef readonly Price min_price
    """The minimum valid price for the scheme.\n\n:returns: `Price`"""
    cdef readonly Price max_price
    """The maximum valid price for the scheme.\n\n:returns: `Price`"""

    cpdef Price next_ask_price(self, double value, int n=*)
    cpdef Price next_bid_price(self, double value, int n=*)


cpdef double round_down(double value, double base)
cpdef double round_up(double value, double base)

cpdef void register_tick_scheme(TickScheme tick_scheme)
cpdef TickScheme get_tick_scheme(str name)


cdef inline bint is_close(double a, double b) noexcept nogil:
    # Check if two floating point values are approximately equal:
    # uses relative tolerance scaled with magnitude but capped to prevent
    # treating values multiple ticks away as "on boundary".
    cdef double diff = fabs(a - b)
    cdef double largest = fmax(fabs(a), fabs(b))
    cdef double rel_tol = 1e-12 * largest  # RELATIVE_TOLERANCE
    cdef double tolerance = fmin(rel_tol, 0.001)  # MAX_TICK_DELTA
    tolerance = fmax(tolerance, 1e-14)  # ABSOLUTE_TOLERANCE
    return diff <= tolerance

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 30


**Identifiers**: `ABSOLUTE_TOLERANCE`, `ANY`, `All`, `BASIS`, `CONDITIONS`, `Check`, `Copyright`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `MAX_TICK_DELTA`, `Nautech`, `Price`, `Pty`, `Public`, `RELATIVE_TOLERANCE`, `See`, `Systems`, `TICK_SCHEMES`, `The`, `TickScheme`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/model/tick_scheme/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.834906Z*
