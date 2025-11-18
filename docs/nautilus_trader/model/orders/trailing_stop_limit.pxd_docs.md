# Documentation: trailing_stop_limit.pxd

## File Metadata

- **Path**: `nautilus_trader/model/orders/trailing_stop_limit.pxd`
- **Size**: 2,861 bytes
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

from libc.stdint cimport uint64_t

from nautilus_trader.core.rust.model cimport TrailingOffsetType
from nautilus_trader.core.rust.model cimport TriggerType
from nautilus_trader.model.events.order cimport OrderInitialized
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity
from nautilus_trader.model.orders.base cimport Order


cdef class TrailingStopLimitOrder(Order):
    cdef readonly Price price
    """The order price (LIMIT).\n\n:returns: `Price` or ``None``"""
    cdef readonly Price activation_price
    """The order activation price (STOP).\n\n:returns: `Price` or ``None``"""
    cdef readonly Price trigger_price
    """The order trigger price (STOP).\n\n:returns: `Price` or ``None``"""
    cdef readonly TriggerType trigger_type
    """The trigger type for the order.\n\n:returns: `TriggerType`"""
    cdef readonly object limit_offset
    """The trailing offset for the orders limit price.\n\n:returns: `Decimal`"""
    cdef readonly object trailing_offset
    """The trailing offset for the orders trigger price (STOP).\n\n:returns: `Decimal`"""
    cdef readonly TrailingOffsetType trailing_offset_type
    """The trailing offset type.\n\n:returns: `TrailingOffsetType`"""
    cdef readonly uint64_t expire_time_ns
    """The order expiration (UNIX epoch nanoseconds), zero for no expiration.\n\n:returns: `uint64_t`"""
    cdef readonly Quantity display_qty
    """The quantity of the ``LIMIT`` order to display on the public book (iceberg).\n\n:returns: `Quantity` or ``None``"""  # noqa
    cdef readonly bint is_activated
    """If the order has been activated.\n\n:returns: `bool`"""
    cdef readonly bint is_triggered
    """If the order has been triggered.\n\n:returns: `bool`"""
    cdef readonly uint64_t ts_triggered
    """UNIX timestamp (nanoseconds) when the order was triggered (0 if not triggered).\n\n:returns: `uint64_t`"""

    @staticmethod
    cdef TrailingStopLimitOrder create_c(OrderInitialized init)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 35


**Identifiers**: `ANY`, `All`, `BASIS`, `CONDITIONS`, `Copyright`, `Decimal`, `GNU`, `General`, `KIND`, `LIMIT`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `None`, `Order`, `OrderInitialized`, `Price`, `Pty`, `Public`, `Quantity`, `STOP`, `See`, `Systems`, `The`, `TrailingOffsetType`, `TrailingStopLimitOrder`, `TriggerType`, `UNIX` *(+5 more)*

## Related Files

This file is located in `nautilus_trader/model/orders/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.815699Z*
