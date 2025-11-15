# Documentation: `nautilus_trader/portfolio/base.pyx`
**Generated:** 2025-11-15T19:40:05.272170Z
**File Size:** 5236 bytes
**Extension:** .pyx
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

- **Path:** `nautilus_trader/portfolio/base.pyx`
- **Size:** 5,236 bytes
- **Lines:** 96
- **Extension:** `.pyx`
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
    """
    Provides a read-only facade for a `Portfolio`.
    """

# -- QUERIES --------------------------------------------------------------------------------------

    cpdef Account account(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `account` must be implemented in the subclass")  # pragma: no cover

    cpdef dict balances_locked(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `balances_locked` must be implemented in the subclass")  # pragma: no cover

    cpdef dict margins_init(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `margins_init` must be implemented in the subclass")  # pragma: no cover

    cpdef dict margins_maint(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `margins_maint` must be implemented in the subclass")  # pragma: no cover

    cpdef dict realized_pnls(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `realized_pnls` must be implemented in the subclass")  # pragma: no cover

    cpdef dict unrealized_pnls(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `unrealized_pnls` must be implemented in the subclass")  # pragma: no cover

    cpdef dict total_pnls(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `total_pnls` must be implemented in the subclass")  # pragma: no cover

    cpdef dict net_exposures(self, Venue venue):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `net_exposure` must be implemented in the subclass")  # pragma: no cover

    cpdef Money realized_pnl(self, InstrumentId instrument_id):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `realized_pnl` must be implemented in the subclass")  # pragma: no cover

    cpdef Money unrealized_pnl(self, InstrumentId instrument_id, Price price=None):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `unrealized_pnl` must be implemented in the subclass")  # pragma: no cover

    cpdef Money total_pnl(self, InstrumentId instrument_id, Price price=None):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `total_pnl` must be implemented in the subclass")  # pragma: no cover

    cpdef Money net_exposure(self, InstrumentId instrument_id, Price price=None):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `next_exposure` must be implemented in the subclass")  # pragma: no cover

    cpdef object net_position(self, InstrumentId instrument_id):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `net_position` must be implemented in the subclass")  # pragma: no cover

    cpdef bint is_net_long(self, InstrumentId instrument_id):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `is_net_long` must be implemented in the subclass")  # pragma: no cover

    cpdef bint is_net_short(self, InstrumentId instrument_id):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `is_net_short` must be implemented in the subclass")  # pragma: no cover

    cpdef bint is_flat(self, InstrumentId instrument_id):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `is_flat` must be implemented in the subclass")  # pragma: no cover

    cpdef bint is_completely_flat(self):
        """Abstract method (implement in subclass)."""
        raise NotImplementedError("method `is_completely_flat` must be implemented in the subclass")  # pragma: no cover
```


---

## Overview

This file is located at `nautilus_trader/portfolio/base.pyx` within the repository.


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


