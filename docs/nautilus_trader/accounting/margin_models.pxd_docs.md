# Documentation: `nautilus_trader/accounting/margin_models.pxd`
**Generated:** 2025-11-15T19:40:04.005325Z
**File Size:** 1726 bytes
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

- **Path:** `nautilus_trader/accounting/margin_models.pxd`
- **Size:** 1,726 bytes
- **Lines:** 51
- **Extension:** `.pxd`
- **Type:** text
- **Imports:** 1

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

from decimal import Decimal

from nautilus_trader.core.rust.model cimport PositionSide
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cdef class MarginModel:
    cpdef Money calculate_margin_init(
        self,
        Instrument instrument,
        Quantity quantity,
        Price price,
        leverage,
        bint use_quote_for_inverse=*,
    )

    cpdef Money calculate_margin_maint(
        self,
        Instrument instrument,
        PositionSide side,
        Quantity quantity,
        Price price,
        leverage,
        bint use_quote_for_inverse=*,
    )


cdef class StandardMarginModel(MarginModel):
    pass


cdef class LeveragedMarginModel(MarginModel):
    pass
```


---

## Overview

This file is located at `nautilus_trader/accounting/margin_models.pxd` within the repository.

**Import statements:** 1


---

## Detailed Analysis

### Imports

- `from decimal import Decimal`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`

**Directory:** `nautilus_trader/accounting`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


