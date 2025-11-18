# Documentation: constants.py

## File Metadata

- **Path**: `nautilus_trader/adapters/binance/common/constants.py`
- **Size**: 2,628 bytes
- **Lines**: 71
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

from decimal import Decimal
from typing import Final

from nautilus_trader.adapters.binance.common.enums import BinanceErrorCode
from nautilus_trader.model.enums import OrderType
from nautilus_trader.model.identifiers import ClientId
from nautilus_trader.model.identifiers import Venue


BINANCE: Final[str] = "BINANCE"
BINANCE_VENUE: Final[Venue] = Venue(BINANCE)
BINANCE_CLIENT_ID: Final[ClientId] = ClientId(BINANCE)

BINANCE_MIN_CALLBACK_RATE: Final[Decimal] = Decimal("0.1")
BINANCE_MAX_CALLBACK_RATE: Final[Decimal] = Decimal("10.0")

# Set of Binance error codes for which Nautilus will attempt retries,
# potentially temporary conditions where a retry might make sense.
BINANCE_RETRY_ERRORS: set[BinanceErrorCode] = {
    BinanceErrorCode.DISCONNECTED,
    BinanceErrorCode.TOO_MANY_REQUESTS,  # Short retry delays may result in bans
    BinanceErrorCode.TIMEOUT,
    BinanceErrorCode.SERVER_BUSY,
    BinanceErrorCode.INVALID_TIMESTAMP,
    BinanceErrorCode.CANCEL_REJECTED,
    BinanceErrorCode.ME_RECVWINDOW_REJECT,
}

# Set of Binance error codes for which Nautilus will log a warning on failure, rather than an error
BINANCE_RETRY_WARNINGS: set[BinanceErrorCode] = {
    BinanceErrorCode.FOK_ORDER_REJECT,
    BinanceErrorCode.GTX_ORDER_REJECT,
}

# Valid `priceMatch` argument values for Binance Futures order placement.
BINANCE_PRICE_MATCH_VALUES: Final[frozenset[str]] = frozenset(
    {
        "OPPONENT",
        "OPPONENT_5",
        "OPPONENT_10",
        "OPPONENT_20",
        "QUEUE",
        "QUEUE_5",
        "QUEUE_10",
        "QUEUE_20",
    },
)

BINANCE_PRICE_MATCH_ORDER_TYPES: Final[frozenset[OrderType]] = frozenset(
    {
        OrderType.LIMIT,
        OrderType.STOP_LIMIT,
        OrderType.LIMIT_IF_TOUCHED,
    },
)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Imports**: `decimal`, `nautilus_trader.adapters.binance.common.enums`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `typing`

## Related Files

This file is located in `nautilus_trader/adapters/binance/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.496821Z*
