# Documentation: `nautilus_trader/model/orders/list.pyx`
**Generated:** 2025-11-15T19:40:05.184155Z
**File Size:** 3032 bytes
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

- **Path:** `nautilus_trader/model/orders/list.pyx`
- **Size:** 3,032 bytes
- **Lines:** 86
- **Extension:** `.pyx`
- **Type:** text
- **Functions:** 5

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

from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.model.identifiers cimport OrderListId
from nautilus_trader.model.orders.base cimport Order


cdef class OrderList:
    """
    Represents a list of bulk or related contingent orders.

    All orders must be for the same instrument ID.

    Parameters
    ----------
    order_list_id : OrderListId
        The order list ID.
    orders : list[Order]
        The contained orders list.

    Raises
    ------
    ValueError
        If `orders` is empty.
    ValueError
        If `orders` contains a type other than `Order`.
    ValueError
        If orders contain different instrument IDs (must all be the same instrument).

    """

    def __init__(
        self,
        OrderListId order_list_id not None,
        list orders not None,
    ) -> None:
        Condition.not_empty(orders, "orders")
        Condition.list_type(orders, Order, "orders")
        cdef Order first = orders[0]
        cdef Order order
        for order in orders:
            # First condition check avoids creating an f-string for performance reasons
            if order.instrument_id != first.instrument_id:
                Condition.is_true(
                    order.instrument_id == first.instrument_id,
                    f"order.instrument_id {order.instrument_id} != instrument_id {first.instrument_id}; "
                    "all orders in the list must be for the same instrument ID",
                )

        self.id = order_list_id
        self.instrument_id = first.instrument_id
        self.strategy_id = first.strategy_id
        self.orders = orders
        self.first = first
        self.ts_init = first.ts_init

    def __eq__(self, OrderList other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __len__(self) -> int:
        return len(self.orders)

    def __repr__(self) -> str:
        return (
            f"OrderList("
            f"id={self.id.to_str()}, "
            f"instrument_id={self.instrument_id}, "
            f"strategy_id={self.strategy_id}, "
            f"orders={self.orders})"
        )
```


---

## Overview

This file is located at `nautilus_trader/model/orders/list.pyx` within the repository.

**Functions defined:** __init__, __eq__, __hash__, __len__, __repr__


---

## Detailed Analysis

### Functions

#### `__init__(
        self,
        OrderListId order_list_id not None,
        list orders not None,
    )`


#### `__eq__(self, OrderList other)`


#### `__hash__(self)`


#### `__len__(self)`


#### `__repr__(self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `nautilus_trader/model/orders`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


