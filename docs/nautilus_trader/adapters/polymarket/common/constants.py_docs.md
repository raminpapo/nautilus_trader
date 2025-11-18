# Documentation: constants.py

## File Metadata

- **Path**: `nautilus_trader/adapters/polymarket/common/constants.py`
- **Size**: 1,846 bytes
- **Lines**: 46
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

from nautilus_trader.adapters.polymarket.common.enums import PolymarketTradeStatus
from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue


POLYMARKET: Final[str] = "POLYMARKET"
POLYMARKET_VENUE: Final[Venue] = Venue(POLYMARKET)
POLYMARKET_CLIENT_ID: Final[ClientId] = ClientId(POLYMARKET)

POLYMARKET_MAX_PRICE: Final[float] = 0.999
POLYMARKET_MIN_PRICE: Final[float] = 0.001
POLYMARKET_MAX_PRECISION_TAKER: Final[int] = 2
POLYMARKET_MAX_PRECISION_MAKER: Final[int] = 5

VALID_POLYMARKET_TIME_IN_FORCE: Final[set[TimeInForce]] = {
    TimeInForce.GTC,
    TimeInForce.GTD,
    TimeInForce.FOK,
    TimeInForce.IOC,
}

POLYMARKET_INVALID_API_KEY: Final[str] = "Unauthorized/Invalid api key"

POLYMARKET_FINALIZED_TRADE_STATUSES: Final[tuple[PolymarketTradeStatus, ...]] = (
    PolymarketTradeStatus.MINED,
    PolymarketTradeStatus.CONFIRMED,
)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Imports**: `nautilus_trader.adapters.polymarket.common.enums`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/polymarket/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.927629Z*
