# Documentation: `nautilus_trader/model/tick_scheme/base.pxd`
**Generated:** 2025-11-15T19:40:05.223254Z
**File Size:** 2252 bytes
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

- **Path:** `nautilus_trader/model/tick_scheme/base.pxd`
- **Size:** 2,252 bytes
- **Lines:** 53
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


---

## Overview

This file is located at `nautilus_trader/model/tick_scheme/base.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/model/tick_scheme`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


