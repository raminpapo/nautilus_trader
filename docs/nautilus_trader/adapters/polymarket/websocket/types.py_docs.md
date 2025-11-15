# Documentation: `nautilus_trader/adapters/polymarket/websocket/types.py`
**Generated:** 2025-11-15T19:40:04.491875Z
**File Size:** 1621 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/websocket/types.py`
- **Size:** 1,621 bytes
- **Lines:** 33
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7

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

from nautilus_trader.adapters.polymarket.schemas.book import PolymarketBookSnapshot
from nautilus_trader.adapters.polymarket.schemas.book import PolymarketQuotes
from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTickSizeChange
from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTrade
from nautilus_trader.adapters.polymarket.schemas.user import PolymarketUserOrder
from nautilus_trader.adapters.polymarket.schemas.user import PolymarketUserTrade


MARKET_WS_MESSAGE: Final = (
    list[PolymarketBookSnapshot]
    | PolymarketBookSnapshot
    | PolymarketQuotes
    | PolymarketTrade
    | PolymarketTickSizeChange
)
USER_WS_MESSAGE: Final = PolymarketUserOrder | PolymarketUserTrade
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/websocket/types.py` within the repository.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `from typing import Final`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketBookSnapshot`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketQuotes`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTickSizeChange`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTrade`
- `from nautilus_trader.adapters.polymarket.schemas.user import PolymarketUserOrder`
- `from nautilus_trader.adapters.polymarket.schemas.user import PolymarketUserTrade`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.polymarket.websocket.types
```


---

## Related Files

This file imports from the following modules:

- `from typing import Final`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketBookSnapshot`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketQuotes`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTickSizeChange`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTrade`
- `from nautilus_trader.adapters.polymarket.schemas.user import PolymarketUserOrder`
- `from nautilus_trader.adapters.polymarket.schemas.user import PolymarketUserTrade`

**Directory:** `nautilus_trader/adapters/polymarket/websocket`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


