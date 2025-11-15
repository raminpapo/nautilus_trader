# Documentation: `nautilus_trader/adapters/polymarket/http/conversion.py`
**Generated:** 2025-11-15T19:40:04.466519Z
**File Size:** 1554 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/http/conversion.py`
- **Size:** 1,554 bytes
- **Lines:** 34
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
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

from py_clob_client.clob_types import OrderType

from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.enums import time_in_force_to_str


def convert_tif_to_polymarket_order_type(time_in_force) -> str:
    match time_in_force:
        case TimeInForce.GTC:
            return OrderType.GTC
        case TimeInForce.GTD:
            return OrderType.GTD
        case TimeInForce.FOK:
            return OrderType.FOK
        case TimeInForce.IOC:
            return OrderType.FAK
        case _:
            time_in_force_str = time_in_force_to_str(time_in_force)
            raise ValueError(f"invalid `TimeInForce` for conversion, was {time_in_force_str}")
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/http/conversion.py` within the repository.

**Functions defined:** convert_tif_to_polymarket_order_type

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `convert_tif_to_polymarket_order_type(time_in_force)`


### Imports

- `from py_clob_client.clob_types import OrderType`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.enums import time_in_force_to_str`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.http.conversion import convert_tif_to_polymarket_order_type
```


---

## Related Files

This file imports from the following modules:

- `from py_clob_client.clob_types import OrderType`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.enums import time_in_force_to_str`

**Directory:** `nautilus_trader/adapters/polymarket/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


