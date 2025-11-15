# Documentation: `nautilus_trader/risk/sizing.pxd`
**Generated:** 2025-11-15T19:40:05.293307Z
**File Size:** 1747 bytes
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

- **Path:** `nautilus_trader/risk/sizing.pxd`
- **Size:** 1,747 bytes
- **Lines:** 45
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

from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cdef class PositionSizer:
    cdef readonly Instrument instrument
    """The instrument for position sizing.\n\n:returns: `Instrument`"""

    cpdef void update_instrument(self, Instrument instrument)
    cpdef Quantity calculate(
        self,
        Price entry,
        Price stop_loss,
        Money equity,
        risk,
        commission_rate=*,
        exchange_rate=*,
        hard_limit=*,
        unit_batch_size=*,
        int units=*,
    )

    cdef object _calculate_risk_ticks(self, Price entry, Price stop_loss)
    cdef object _calculate_riskable_money(self, equity, risk, commission_rate)


cdef class FixedRiskSizer(PositionSizer):
    pass
```


---

## Overview

This file is located at `nautilus_trader/risk/sizing.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/risk`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


