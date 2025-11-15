# Documentation: `nautilus_trader/adapters/betfair/orderbook.pyx`
**Generated:** 2025-11-15T19:40:04.035926Z
**File Size:** 1770 bytes
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

- **Path:** `nautilus_trader/adapters/betfair/orderbook.pyx`
- **Size:** 1,770 bytes
- **Lines:** 41
- **Extension:** `.pyx`
- **Type:** text
- **Imports:** 4

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


---

## Overview

This file is located at `nautilus_trader/adapters/betfair/orderbook.pyx` within the repository.

**Import statements:** 4


---

## Detailed Analysis

### Imports

- `from nautilus_trader.adapters.betfair.common import BETFAIR_FLOAT_TO_PRICE`
- `from nautilus_trader.adapters.betfair.constants import BETFAIR_PRICE_PRECISION`
- `from nautilus_trader.adapters.betfair.constants import BETFAIR_QUANTITY_PRECISION`
- `from nautilus_trader.core.rust.model import BookType`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.adapters.betfair.common import BETFAIR_FLOAT_TO_PRICE`
- `from nautilus_trader.adapters.betfair.constants import BETFAIR_PRICE_PRECISION`
- `from nautilus_trader.adapters.betfair.constants import BETFAIR_QUANTITY_PRECISION`
- `from nautilus_trader.core.rust.model import BookType`

**Directory:** `nautilus_trader/adapters/betfair`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


