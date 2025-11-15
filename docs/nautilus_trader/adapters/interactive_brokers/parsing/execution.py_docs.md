# Documentation: `nautilus_trader/adapters/interactive_brokers/parsing/execution.py`
**Generated:** 2025-11-15T19:40:04.390565Z
**File Size:** 4250 bytes
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

- **Path:** `nautilus_trader/adapters/interactive_brokers/parsing/execution.py`
- **Size:** 4,250 bytes
- **Lines:** 114
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Functions:** 1

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

from collections.abc import Callable

import pandas as pd

from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.enums import OrderStatus
from nautilus_trader.model.enums import OrderType
from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.enums import TriggerType


MAP_TRIGGER_METHOD: dict[int, int] = {
    TriggerType.DEFAULT: 0,
    TriggerType.DOUBLE_BID_ASK: 1,
    TriggerType.LAST_PRICE: 2,
    TriggerType.DOUBLE_LAST: 3,
    TriggerType.BID_ASK: 4,
    TriggerType.LAST_OR_BID_ASK: 7,
    TriggerType.MID_POINT: 8,
}

MAP_TIME_IN_FORCE: dict[int, str] = {
    TimeInForce.DAY: "DAY",
    TimeInForce.GTC: "GTC",
    TimeInForce.IOC: "IOC",
    TimeInForce.GTD: "GTD",
    TimeInForce.AT_THE_OPEN: "OPG",
    TimeInForce.AT_THE_CLOSE: "DAY",
    TimeInForce.FOK: "FOK",
    # unsupported: 'DTC',
}

MAP_ORDER_ACTION: dict[int, str] = {
    OrderSide.BUY: "BUY",
    OrderSide.SELL: "SELL",
}

ORDER_SIDE_TO_ORDER_ACTION: dict[str, str] = {
    "BOT": "BUY",
    "SLD": "SELL",
}

MAP_ORDER_TYPE: dict[int | tuple[int, int], str] = {
    OrderType.LIMIT: "LMT",
    OrderType.LIMIT_IF_TOUCHED: "LIT",
    OrderType.MARKET: "MKT",
    OrderType.MARKET_IF_TOUCHED: "MIT",
    OrderType.MARKET_TO_LIMIT: "MTL",
    OrderType.STOP_LIMIT: "STP LMT",
    OrderType.STOP_MARKET: "STP",
    OrderType.TRAILING_STOP_LIMIT: "TRAIL LIMIT",
    OrderType.TRAILING_STOP_MARKET: "TRAIL",
    (OrderType.MARKET, TimeInForce.AT_THE_CLOSE): "MOC",
    (OrderType.LIMIT, TimeInForce.AT_THE_CLOSE): "LOC",
}


MAP_ORDER_FIELDS: set[tuple[str, str, Callable]] = {
    # ref: (nautilus_order_field, ib_order_field, value_fn)
    ("client_order_id", "orderRef", lambda x: x.value),
    ("display_qty", "displaySize", lambda x: x.as_double()),
    ("expire_time", "goodTillDate", lambda x: x.strftime("%Y%m%d %H:%M:%S %Z")),
    ("limit_offset", "lmtPriceOffset", float),
    ("order_type", "orderType", lambda x: MAP_ORDER_TYPE[x]),
    ("price", "lmtPrice", lambda x: x.as_double()),
    ("quantity", "totalQuantity", lambda x: x.as_decimal()),
    ("side", "action", lambda x: MAP_ORDER_ACTION[x]),
    ("time_in_force", "tif", lambda x: MAP_TIME_IN_FORCE[x]),
    # ("trailing_offset", "trailStopPrice", lambda x: float(x)),
    # ("trigger_price", "auxPrice", lambda x: x.as_double()),
    # ("trigger_type", "triggerMethod", lambda x: map_trigger_method[x]),
    ("parent_order_id", "parentId", lambda x: x.value),
}


MAP_ORDER_STATUS = {
    "ApiPending": OrderStatus.SUBMITTED,
    "PendingSubmit": OrderStatus.SUBMITTED,
    "PendingCancel": OrderStatus.PENDING_CANCEL,
    "PreSubmitted": OrderStatus.SUBMITTED,
    "Submitted": OrderStatus.ACCEPTED,
    "ApiCancelled": OrderStatus.CANCELED,
    "Cancelled": OrderStatus.CANCELED,
    "Filled": OrderStatus.FILLED,
    "Inactive": OrderStatus.DENIED,
}


def timestring_to_timestamp(timestring: str) -> pd.Timestamp:
    # Support string conversion not supported directly by pd.to_datetime
    # 20230223 00:43:36 America/New_York
    # 20230223 00:43:36 Universal
    # When the tz is Universal, and mode is live (not paper) and only in this case, IB can also send it with this format : "20250225-15:15:00"
    if " " in timestring:
        dt, tz = timestring.rsplit(" ", 1)
    else:
        dt, tz = timestring.replace("-", " "), "Universal"

    return pd.Timestamp(dt, tz=tz)
```


---

## Overview

This file is located at `nautilus_trader/adapters/interactive_brokers/parsing/execution.py` within the repository.

**Functions defined:** timestring_to_timestamp

**Import statements:** 7


---

## Detailed Analysis

### Functions

#### `timestring_to_timestamp(timestring: str)`


### Imports

- `from collections.abc import Callable`
- `import pandas as pd`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.enums import OrderStatus`
- `from nautilus_trader.model.enums import OrderType`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.enums import TriggerType`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.interactive_brokers.parsing.execution import timestring_to_timestamp
```


---

## Related Files

This file imports from the following modules:

- `from collections.abc import Callable`
- `import pandas as pd`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.enums import OrderStatus`
- `from nautilus_trader.model.enums import OrderType`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.enums import TriggerType`

**Directory:** `nautilus_trader/adapters/interactive_brokers/parsing`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


