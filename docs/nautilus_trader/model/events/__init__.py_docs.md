# Documentation: `nautilus_trader/model/events/__init__.py`
**Generated:** 2025-11-15T19:40:05.049785Z
**File Size:** 2920 bytes
**Extension:** .py
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

- **Path:** `nautilus_trader/model/events/__init__.py`
- **Size:** 2,920 bytes
- **Lines:** 68
- **Extension:** `.py`
- **Type:** text
- **Imports:** 23

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


---

## Overview

This file is located at `nautilus_trader/model/events/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 23


---

## Detailed Analysis

### Imports

- `from nautilus_trader.model.events.account import AccountState`
- `from nautilus_trader.model.events.order import OrderAccepted`
- `from nautilus_trader.model.events.order import OrderCanceled`
- `from nautilus_trader.model.events.order import OrderCancelRejected`
- `from nautilus_trader.model.events.order import OrderDenied`
- `from nautilus_trader.model.events.order import OrderEmulated`
- `from nautilus_trader.model.events.order import OrderEvent`
- `from nautilus_trader.model.events.order import OrderExpired`
- `from nautilus_trader.model.events.order import OrderFilled`
- `from nautilus_trader.model.events.order import OrderInitialized`
- `from nautilus_trader.model.events.order import OrderModifyRejected`
- `from nautilus_trader.model.events.order import OrderPendingCancel`
- `from nautilus_trader.model.events.order import OrderPendingUpdate`
- `from nautilus_trader.model.events.order import OrderRejected`
- `from nautilus_trader.model.events.order import OrderReleased`
- `from nautilus_trader.model.events.order import OrderSubmitted`
- `from nautilus_trader.model.events.order import OrderTriggered`
- `from nautilus_trader.model.events.order import OrderUpdated`
- `from nautilus_trader.model.events.position import PositionAdjusted`
- `from nautilus_trader.model.events.position import PositionChanged`
- `from nautilus_trader.model.events.position import PositionClosed`
- `from nautilus_trader.model.events.position import PositionEvent`
- `from nautilus_trader.model.events.position import PositionOpened`


---

## Usage Examples

### Importing

```python
import nautilus_trader.model.events.__init__
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.events.account import AccountState`
- `from nautilus_trader.model.events.order import OrderAccepted`
- `from nautilus_trader.model.events.order import OrderCanceled`
- `from nautilus_trader.model.events.order import OrderCancelRejected`
- `from nautilus_trader.model.events.order import OrderDenied`
- `from nautilus_trader.model.events.order import OrderEmulated`
- `from nautilus_trader.model.events.order import OrderEvent`
- `from nautilus_trader.model.events.order import OrderExpired`
- `from nautilus_trader.model.events.order import OrderFilled`
- `from nautilus_trader.model.events.order import OrderInitialized`

*... and 13 more*

**Directory:** `nautilus_trader/model/events`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


