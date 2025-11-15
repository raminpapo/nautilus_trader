# Documentation: `nautilus_trader/adapters/betfair/constants.py`
**Generated:** 2025-11-15T19:40:04.022644Z
**File Size:** 2240 bytes
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

- **Path:** `nautilus_trader/adapters/betfair/constants.py`
- **Size:** 2,240 bytes
- **Lines:** 46
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

from betfair_parser.spec.betting import MarketStatus as BetfairMarketStatus

from nautilus_trader.model.enums import BookType
from nautilus_trader.model.enums import MarketStatusAction
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Price


BETFAIR: Final[str] = "BETFAIR"
BETFAIR_VENUE: Final[Venue] = Venue(BETFAIR)
BETFAIR_CLIENT_ID: Final[ClientId] = ClientId(BETFAIR)

BETFAIR_PRICE_PRECISION: Final[int] = 2
BETFAIR_QUANTITY_PRECISION: Final[int] = 2
BETFAIR_BOOK_TYPE: Final[BookType] = BookType.L2_MBP

CLOSE_PRICE_WINNER: Final[Price] = Price(1.0, precision=BETFAIR_PRICE_PRECISION)
CLOSE_PRICE_LOSER: Final[Price] = Price(0.0, precision=BETFAIR_PRICE_PRECISION)

MARKET_STATUS_MAPPING: Final[dict[tuple[BetfairMarketStatus, bool], MarketStatusAction]] = {
    (BetfairMarketStatus.INACTIVE, False): MarketStatusAction.CLOSE,
    (BetfairMarketStatus.OPEN, False): MarketStatusAction.PRE_OPEN,
    (BetfairMarketStatus.OPEN, True): MarketStatusAction.TRADING,
    (BetfairMarketStatus.SUSPENDED, False): MarketStatusAction.PAUSE,
    (BetfairMarketStatus.SUSPENDED, True): MarketStatusAction.PAUSE,
    (BetfairMarketStatus.CLOSED, False): MarketStatusAction.CLOSE,
    (BetfairMarketStatus.CLOSED, True): MarketStatusAction.CLOSE,
}
```


---

## Overview

This file is located at `nautilus_trader/adapters/betfair/constants.py` within the repository.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `from typing import Final`
- `from betfair_parser.spec.betting import MarketStatus as BetfairMarketStatus`
- `from nautilus_trader.model.enums import BookType`
- `from nautilus_trader.model.enums import MarketStatusAction`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Price`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.betfair.constants
```


---

## Related Files

This file imports from the following modules:

- `from typing import Final`
- `from betfair_parser.spec.betting import MarketStatus as BetfairMarketStatus`
- `from nautilus_trader.model.enums import BookType`
- `from nautilus_trader.model.enums import MarketStatusAction`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Price`

**Directory:** `nautilus_trader/adapters/betfair`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


