# Documentation: base.pyx

## File Metadata

- **Path**: `nautilus_trader/portfolio/base.pyx`
- **Size**: 5,236 bytes
- **Lines**: 97
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 34


**Identifiers**: `ANY`, `Abstract`, `Account`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `InstrumentId`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Money`, `Nautech`, `None`, `NotImplementedError`, `Portfolio`, `PortfolioFacade`, `Price`, `Provides`, `Pty`, `Public`, `QUERIES`, `See`, `Systems`, `Unless`, `Venue` *(+4 more)*

## Related Files

This file is located in `nautilus_trader/portfolio/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.883603Z*
