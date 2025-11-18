# Documentation: fill.pxd

## File Metadata

- **Path**: `nautilus_trader/backtest/models/fill.pxd`
- **Size**: 1,874 bytes
- **Lines**: 39
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

from nautilus_trader.model.book cimport BookOrder
from nautilus_trader.model.book cimport OrderBook
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.orders.base cimport Order


cdef class FillModel:
    cdef readonly double prob_fill_on_limit
    """The probability of limit orders filling on the limit price.\n\n:returns: `bool`"""
    cdef readonly double prob_fill_on_stop
    """The probability of stop orders filling on the stop price.\n\n:returns: `bool`"""
    cdef readonly double prob_slippage
    """The probability of aggressive order execution slipping.\n\n:returns: `bool`"""

    cpdef bint is_limit_filled(self)
    cpdef bint is_stop_filled(self)
    cpdef bint is_slipped(self)
    cpdef OrderBook get_orderbook_for_fill_simulation(self, Instrument instrument, Order order, Price best_bid, Price best_ask)

    cdef bint _event_success(self, double probability)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 29


**Identifiers**: `ANY`, `All`, `BASIS`, `BookOrder`, `CONDITIONS`, `Copyright`, `FillModel`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `Order`, `OrderBook`, `Price`, `Pty`, `Public`, `See`, `Systems`, `The`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/backtest/models/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest nautilus_trader/backtest/models/fill.pxd

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:05.094157Z*
