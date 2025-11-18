# Documentation: orderbook.pyx

## File Metadata

- **Path**: `nautilus_trader/adapters/betfair/orderbook.pyx`
- **Size**: 1,770 bytes
- **Lines**: 42
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

from nautilus_trader.adapters.betfair.common import BETFAIR_FLOAT_TO_PRICE
from nautilus_trader.adapters.betfair.constants import BETFAIR_PRICE_PRECISION
from nautilus_trader.adapters.betfair.constants import BETFAIR_QUANTITY_PRECISION
from nautilus_trader.core.rust.model import BookType

from nautilus_trader.model.identifiers cimport InstrumentId
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cpdef inline OrderBook create_betfair_order_book(InstrumentId instrument_id):
    return OrderBook(
        instrument_id,
        BookType.L2_MBP,
    )


cpdef Price betfair_float_to_price(double value):
    try:
        return BETFAIR_FLOAT_TO_PRICE[value]
    except KeyError:
        return Price(value, BETFAIR_PRICE_PRECISION)


cpdef Quantity betfair_float_to_quantity(double value):
    return Quantity(value, BETFAIR_QUANTITY_PRECISION)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 32


**Identifiers**: `ANY`, `All`, `BASIS`, `BETFAIR_FLOAT_TO_PRICE`, `BETFAIR_PRICE_PRECISION`, `BETFAIR_QUANTITY_PRECISION`, `BookType`, `CONDITIONS`, `Copyright`, `GNU`, `General`, `InstrumentId`, `KIND`, `KeyError`, `L2_MBP`, `Lesser`, `License`, `Licensed`, `Ltd`, `Nautech`, `OrderBook`, `Price`, `Pty`, `Public`, `Quantity`, `See`, `Systems`, `Unless`, `Version`, `WARRANTIES` *(+2 more)*

## Related Files

This file is located in `nautilus_trader/adapters/betfair/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.477439Z*
