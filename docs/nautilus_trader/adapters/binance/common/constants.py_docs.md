# Documentation: `nautilus_trader/adapters/binance/common/constants.py`
**Generated:** 2025-11-15T19:40:04.053058Z
**File Size:** 2628 bytes
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

- **Path:** `nautilus_trader/adapters/binance/common/constants.py`
- **Size:** 2,628 bytes
- **Lines:** 70
- **Extension:** `.py`
- **Type:** text
- **Imports:** 6

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


---

## Overview

This file is located at `nautilus_trader/adapters/binance/common/constants.py` within the repository.

**Import statements:** 6


---

## Detailed Analysis

### Imports

- `from decimal import Decimal`
- `from typing import Final`
- `from nautilus_trader.adapters.binance.common.enums import BinanceErrorCode`
- `from nautilus_trader.model.enums import OrderType`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
import nautilus_trader.adapters.binance.common.constants
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from typing import Final`
- `from nautilus_trader.adapters.binance.common.enums import BinanceErrorCode`
- `from nautilus_trader.model.enums import OrderType`
- `from nautilus_trader.model.identifiers import ClientId`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `nautilus_trader/adapters/binance/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


