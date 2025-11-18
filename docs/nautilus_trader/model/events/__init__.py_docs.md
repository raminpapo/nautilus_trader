# Documentation: __init__.py

## File Metadata

- **Path**: `nautilus_trader/model/events/__init__.py`
- **Size**: 2,920 bytes
- **Lines**: 69
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
Defines the fundamental event types represented within the trading domain.
"""

from nautilus_trader.model.events.account import AccountState
from nautilus_trader.model.events.order import OrderAccepted
from nautilus_trader.model.events.order import OrderCanceled
from nautilus_trader.model.events.order import OrderCancelRejected
from nautilus_trader.model.events.order import OrderDenied
from nautilus_trader.model.events.order import OrderEmulated
from nautilus_trader.model.events.order import OrderEvent
from nautilus_trader.model.events.order import OrderExpired
from nautilus_trader.model.events.order import OrderFilled
from nautilus_trader.model.events.order import OrderInitialized
from nautilus_trader.model.events.order import OrderModifyRejected
from nautilus_trader.model.events.order import OrderPendingCancel
from nautilus_trader.model.events.order import OrderPendingUpdate
from nautilus_trader.model.events.order import OrderRejected
from nautilus_trader.model.events.order import OrderReleased
from nautilus_trader.model.events.order import OrderSubmitted
from nautilus_trader.model.events.order import OrderTriggered
from nautilus_trader.model.events.order import OrderUpdated
from nautilus_trader.model.events.position import PositionAdjusted
from nautilus_trader.model.events.position import PositionChanged
from nautilus_trader.model.events.position import PositionClosed
from nautilus_trader.model.events.position import PositionEvent
from nautilus_trader.model.events.position import PositionOpened


__all__ = [
    "AccountState",
    "OrderAccepted",
    "OrderCancelRejected",
    "OrderCanceled",
    "OrderDenied",
    "OrderEmulated",
    "OrderEvent",
    "OrderExpired",
    "OrderFilled",
    "OrderInitialized",
    "OrderModifyRejected",
    "OrderPendingCancel",
    "OrderPendingUpdate",
    "OrderRejected",
    "OrderReleased",
    "OrderSubmitted",
    "OrderTriggered",
    "OrderUpdated",
    "PositionAdjusted",
    "PositionChanged",
    "PositionClosed",
    "PositionEvent",
    "PositionOpened",
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Imports**: `nautilus_trader.model.events.account`, `nautilus_trader.model.events.order`, `nautilus_trader.model.events.position`

## Related Files

This file is located in `nautilus_trader/model/events/`. Related files may include:
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
*Generated on 2025-11-18T21:55:05.649519Z*
