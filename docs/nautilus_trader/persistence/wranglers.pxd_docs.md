# Documentation: wranglers.pxd

## File Metadata

- **Path**: `nautilus_trader/persistence/wranglers.pxd`
- **Size**: 2,729 bytes
- **Lines**: 84
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

from libc.stdint cimport int64_t
from libc.stdint cimport uint8_t
from libc.stdint cimport uint64_t

from nautilus_trader.core.rust.model cimport AggressorSide
from nautilus_trader.core.rust.model cimport BookAction
from nautilus_trader.core.rust.model cimport OrderSide
from nautilus_trader.core.rust.model cimport PriceRaw
from nautilus_trader.core.rust.model cimport QuantityRaw
from nautilus_trader.model.data cimport Bar
from nautilus_trader.model.data cimport BarType
from nautilus_trader.model.data cimport OrderBookDelta
from nautilus_trader.model.data cimport QuoteTick
from nautilus_trader.model.data cimport TradeTick
from nautilus_trader.model.instruments.base cimport Instrument


cdef class OrderBookDeltaDataWrangler:
    cdef readonly Instrument instrument

    cpdef OrderBookDelta _build_delta(
        self,
        BookAction action,
        OrderSide side,
        double price,
        double size,
        uint64_t order_id,
        uint8_t flags,
        uint64_t sequence,
        uint64_t ts_event,
        uint64_t ts_init,
    )


cdef class QuoteTickDataWrangler:
    cdef readonly Instrument instrument

    cpdef QuoteTick _build_tick(
        self,
        double bid_price,
        double ask_price,
        double bid_size,
        double ask_size,
        uint64_t ts_event,
        uint64_t ts_init,
    )


cdef class TradeTickDataWrangler:
    cdef readonly Instrument instrument
    cdef readonly processed_data

    cpdef TradeTick _build_tick(
        self,
        double price,
        double size,
        AggressorSide aggressor_side,
        str trade_id,
        uint64_t ts_event,
        uint64_t ts_init,
    )


cdef class BarDataWrangler:
    cdef readonly BarType bar_type
    cdef readonly Instrument instrument

    cpdef Bar _build_bar(self, double[:] values, uint64_t ts_event, uint64_t ts_init_delta)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 37


**Identifiers**: `ANY`, `AggressorSide`, `All`, `BASIS`, `Bar`, `BarDataWrangler`, `BarType`, `BookAction`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `OrderBookDelta`, `OrderBookDeltaDataWrangler`, `OrderSide`, `PriceRaw`, `Pty`, `Public`, `QuantityRaw`, `QuoteTick`, `QuoteTickDataWrangler`, `See`, `Systems` *(+7 more)*

## Related Files

This file is located in `nautilus_trader/persistence/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.868240Z*
