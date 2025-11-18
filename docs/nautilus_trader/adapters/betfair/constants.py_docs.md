# Documentation: constants.py

## File Metadata

- **Path**: `nautilus_trader/adapters/betfair/constants.py`
- **Size**: 2,240 bytes
- **Lines**: 47
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Imports**: `betfair_parser.spec.betting`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/betfair/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.461553Z*
