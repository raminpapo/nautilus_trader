# Documentation: `nautilus_trader/model/tick_scheme/implementations/fixed.pxd`
**Generated:** 2025-11-15T19:40:05.227010Z
**File Size:** 1425 bytes
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

- **Path:** `nautilus_trader/model/tick_scheme/implementations/fixed.pxd`
- **Size:** 1,425 bytes
- **Lines:** 31
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

from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.tick_scheme.base cimport TickScheme


cdef class FixedTickScheme(TickScheme):
    cdef double _increment
    cdef double _min_price
    cdef double _max_price

    cdef readonly int price_precision
    """The tick scheme price precision.\n\n:returns: `int`"""
    cdef readonly Price increment
    """The tick scheme price increment.\n\n:returns: `Price`"""

    cpdef Price next_ask_price(self, double value, int n=*)
    cpdef Price next_bid_price(self, double value, int n=*)
```


---

## Overview

This file is located at `nautilus_trader/model/tick_scheme/implementations/fixed.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/model/tick_scheme/implementations`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


