# Documentation: math.pyx

## File Metadata

- **Path**: `nautilus_trader/core/math.pyx`
- **Size**: 2,455 bytes
- **Lines**: 70
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

import numpy as np

cimport numpy as np


cdef inline double linear_weight(double x1, double x2, double x):
    return (x - x1) / (x2 - x1)


cdef inline double linear_weighting(double y1, double y2, double x1_diff):
    return y1 + x1_diff * (y2 - y1)


cdef inline int pos_search(double x, np.ndarray xs):
    cdef int n_elem = xs.shape[0]
    cdef int pos = max(min(int(np.searchsorted(xs, x, side='right')), n_elem - 1) - 1, 0)
    return pos


cdef inline double quad_polynomial(double x, double x0, double x1, double x2, double y0, double y1, double y2):
    return (y0 * (x - x1) * (x - x2) / ((x0 - x1) * (x0 - x2))
            + y1 * (x - x0) * (x - x2) / ((x1 - x0) * (x1 - x2))
            + y2 * (x - x0) * (x - x1) / ((x2 - x0) * (x2 - x1)))


cpdef double quadratic_interpolation(double x, np.ndarray xs, np.ndarray ys):
    cdef int n_elem = xs.shape[0]
    cdef int pos
    cdef double w

    if x <= xs[0]:
        return ys[0]

    if x >= xs[n_elem-1]:
        return ys[n_elem-1]

    pos = pos_search(x, xs)

    if xs[pos] == x:
        return ys[pos]

    if pos == 0:
        return quad_polynomial(x, xs[0], xs[1], xs[2], ys[0], ys[1], ys[2])

    if pos == n_elem - 2:
        return quad_polynomial(x, xs[n_elem-3], xs[n_elem-2], xs[n_elem-1], ys[n_elem-3], ys[n_elem-2], ys[n_elem-1])

    w = linear_weight(xs[pos], xs[pos+1], x)

    return linear_weighting(
        quad_polynomial(x, xs[pos-1], xs[pos], xs[pos+1], ys[pos-1], ys[pos], ys[pos+1]),
        quad_polynomial(x, xs[pos], xs[pos+1], xs[pos+2], ys[pos], ys[pos+1], ys[pos+2]),
        w
    )

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 22


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Pty`, `Public`, `See`, `Systems`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/core/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.310975Z*
