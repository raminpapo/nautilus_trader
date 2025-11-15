# Documentation: `nautilus_trader/adapters/coinbase_intx/constants.py`
**Generated:** 2025-11-15T19:40:04.203944Z
**File Size:** 1581 bytes
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

- **Path:** `nautilus_trader/adapters/coinbase_intx/constants.py`
- **Size:** 1,581 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 5

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

from typing import Final

from nautilus_trader.model.enums import OrderType
from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue


COINBASE_INTX: Final[str] = "COINBASE_INTX"
COINBASE_INTX_VENUE: Final[Venue] = Venue(COINBASE_INTX)
COINBASE_INTX_CLIENT_ID: Final[ClientId] = ClientId(COINBASE_INTX)

COINBASE_INTX_SUPPORTED_ORDER_TYPES: Final[set[OrderType]] = {
    OrderType.MARKET,
    OrderType.LIMIT,
    OrderType.STOP_MARKET,
    OrderType.STOP_LIMIT,
}

COINBASE_INTX_SUPPORTED_TIF: Final[set[TimeInForce]] = {
    TimeInForce.GTC,
    TimeInForce.GTD,
    TimeInForce.IOC,
    TimeInForce.FOK,
}
```


---

## Overview

This file is located at `nautilus_trader/adapters/coinbase_intx/constants.py` within the repository.

**Import statements:** 5


---

## Detailed Analysis

### Imports

- `from typing import Final`
- `from nautilus_trader.model.enums import OrderType`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.coinbase_intx.constants
```


---

## Related Files

This file imports from the following modules:

- `from typing import Final`
- `from nautilus_trader.model.enums import OrderType`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `nautilus_trader/adapters/coinbase_intx`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


