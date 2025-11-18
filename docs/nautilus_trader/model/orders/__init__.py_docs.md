# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/model/orders/__init__.py`
- **Size**: 2,094 bytes
- **Lines**: 48
- **Language**: Python

## Original Source

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
"""
Provides a full range of standard order types, as well as more advanced types and order
lists.
"""

from nautilus_trader.model.orders.base import Order
from nautilus_trader.model.orders.limit import LimitOrder
from nautilus_trader.model.orders.limit_if_touched import LimitIfTouchedOrder
from nautilus_trader.model.orders.list import OrderList
from nautilus_trader.model.orders.market import MarketOrder
from nautilus_trader.model.orders.market_if_touched import MarketIfTouchedOrder
from nautilus_trader.model.orders.market_to_limit import MarketToLimitOrder
from nautilus_trader.model.orders.stop_limit import StopLimitOrder
from nautilus_trader.model.orders.stop_market import StopMarketOrder
from nautilus_trader.model.orders.trailing_stop_limit import TrailingStopLimitOrder
from nautilus_trader.model.orders.trailing_stop_market import TrailingStopMarketOrder
from nautilus_trader.model.orders.unpacker import OrderUnpacker


__all__ = [
    "LimitIfTouchedOrder",
    "LimitOrder",
    "MarketIfTouchedOrder",
    "MarketOrder",
    "MarketToLimitOrder",
    "Order",
    "OrderList",
    "OrderUnpacker",
    "StopLimitOrder",
    "StopMarketOrder",
    "TrailingStopLimitOrder",
    "TrailingStopMarketOrder",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 12


**Imports**: `nautilus_trader.model.orders.base`, `nautilus_trader.model.orders.limit`, `nautilus_trader.model.orders.limit_if_touched`, `nautilus_trader.model.orders.list`, `nautilus_trader.model.orders.market`, `nautilus_trader.model.orders.market_if_touched`, `nautilus_trader.model.orders.market_to_limit`, `nautilus_trader.model.orders.stop_limit`, `nautilus_trader.model.orders.stop_market`, `nautilus_trader.model.orders.trailing_stop_limit`, `nautilus_trader.model.orders.trailing_stop_market`, `nautilus_trader.model.orders.unpacker`

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
*Generated on 2025-11-18T21:55:05.775162Z*
