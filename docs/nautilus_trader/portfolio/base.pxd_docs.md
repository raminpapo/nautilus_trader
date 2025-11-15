# Documentation: `nautilus_trader/portfolio/base.pxd`
**Generated:** 2025-11-15T19:40:05.270912Z
**File Size:** 2442 bytes
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

- **Path:** `nautilus_trader/portfolio/base.pxd`
- **Size:** 2,442 bytes
- **Lines:** 52
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

from nautilus_trader.accounting.accounts.base cimport Account
from nautilus_trader.model.identifiers cimport InstrumentId
from nautilus_trader.model.identifiers cimport Venue
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price


cdef class PortfolioFacade:

# -- QUERIES --------------------------------------------------------------------------------------  # noqa

    cdef readonly bint initialized
    """If the portfolio is initialized.\n\n:returns: `bool`"""

    cdef readonly analyzer
    """The portfolios analyzer.\n\n:returns: `PortfolioAnalyzer`"""

    cpdef Account account(self, Venue venue)

    cpdef dict balances_locked(self, Venue venue)
    cpdef dict margins_init(self, Venue venue)
    cpdef dict margins_maint(self, Venue venue)
    cpdef dict realized_pnls(self, Venue venue)
    cpdef dict unrealized_pnls(self, Venue venue)
    cpdef dict total_pnls(self, Venue venue)
    cpdef dict net_exposures(self, Venue venue)

    cpdef Money realized_pnl(self, InstrumentId instrument_id)
    cpdef Money unrealized_pnl(self, InstrumentId instrument_id, Price price=*)
    cpdef Money total_pnl(self, InstrumentId instrument_id, Price price=*)
    cpdef Money net_exposure(self, InstrumentId instrument_id, Price price=*)
    cpdef object net_position(self, InstrumentId instrument_id)

    cpdef bint is_net_long(self, InstrumentId instrument_id)
    cpdef bint is_net_short(self, InstrumentId instrument_id)
    cpdef bint is_flat(self, InstrumentId instrument_id)
    cpdef bint is_completely_flat(self)
```


---

## Overview

This file is located at `nautilus_trader/portfolio/base.pxd` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/portfolio`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


