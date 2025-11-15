# Documentation: `nautilus_trader/adapters/binance/spot/schemas/account.py`
**Generated:** 2025-11-15T19:40:04.152806Z
**File Size:** 3260 bytes
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

- **Path:** `nautilus_trader/adapters/binance/spot/schemas/account.py`
- **Size:** 3,260 bytes
- **Lines:** 92
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Classes:** 3
- **Functions:** 2

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

import msgspec

from nautilus_trader.adapters.binance.common.enums import BinanceAccountType
from nautilus_trader.adapters.binance.common.schemas.account import BinanceOrder
from nautilus_trader.model.objects import AccountBalance
from nautilus_trader.model.objects import Currency
from nautilus_trader.model.objects import Money


################################################################################
# HTTP responses
################################################################################


class BinanceSpotBalanceInfo(msgspec.Struct, frozen=True):
    """
    HTTP response 'inner struct' from Binance Spot/Margin GET /api/v3/account (HMAC
    SHA256).
    """

    asset: str
    free: str
    locked: str

    def parse_to_account_balance(self) -> AccountBalance:
        currency = Currency.from_str(self.asset)
        free = Decimal(self.free)
        locked = Decimal(self.locked)
        total: Decimal = free + locked
        return AccountBalance(
            total=Money(total, currency),
            locked=Money(locked, currency),
            free=Money(free, currency),
        )


class BinanceSpotAccountInfo(msgspec.Struct, frozen=True):
    """
    HTTP response from Binance Spot/Margin GET /api/v3/account (HMAC SHA256).
    """

    makerCommission: int
    takerCommission: int
    buyerCommission: int
    sellerCommission: int
    canTrade: bool
    canWithdraw: bool
    canDeposit: bool
    updateTime: int
    accountType: BinanceAccountType
    balances: list[BinanceSpotBalanceInfo]
    permissions: list[str]

    def parse_to_account_balances(self) -> list[AccountBalance]:
        return [balance.parse_to_account_balance() for balance in self.balances]


class BinanceSpotOrderOco(msgspec.Struct, frozen=True):
    """
    HTTP response from Binance Spot/Margin GET /api/v3/orderList (HMAC SHA256).

    HTTP response from Binance Spot/Margin POST /api/v3/order/oco (HMAC SHA256). HTTP
    response from Binance Spot/Margin DELETE /api/v3/orderList (HMAC SHA256).

    """

    orderListId: int
    contingencyType: str
    listStatusType: str
    listOrderStatus: str
    listClientOrderId: str
    transactionTime: int
    symbol: str
    orders: list[BinanceOrder] | None = None  # Included for ACK response type
    orderReports: list[BinanceOrder] | None = None  # Included for FULL & RESPONSE types
```


---

## Overview

This file is located at `nautilus_trader/adapters/binance/spot/schemas/account.py` within the repository.

**Classes defined:** BinanceSpotBalanceInfo, BinanceSpotAccountInfo, BinanceSpotOrderOco

**Functions defined:** parse_to_account_balance, parse_to_account_balances

**Import statements:** 7


---

## Detailed Analysis

### Classes

#### `BinanceSpotBalanceInfo`

**Inherits from:** msgspec.Struct, frozen=True


#### `BinanceSpotAccountInfo`

**Inherits from:** msgspec.Struct, frozen=True


#### `BinanceSpotOrderOco`

**Inherits from:** msgspec.Struct, frozen=True


### Functions

#### `parse_to_account_balance(self)`


#### `parse_to_account_balances(self)`


### Imports

- `from decimal import Decimal`
- `import msgspec`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.common.schemas.account import BinanceOrder`
- `from nautilus_trader.model.objects import AccountBalance`
- `from nautilus_trader.model.objects import Currency`
- `from nautilus_trader.model.objects import Money`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.binance.spot.schemas.account import BinanceSpotBalanceInfo
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `import msgspec`
- `from nautilus_trader.adapters.binance.common.enums import BinanceAccountType`
- `from nautilus_trader.adapters.binance.common.schemas.account import BinanceOrder`
- `from nautilus_trader.model.objects import AccountBalance`
- `from nautilus_trader.model.objects import Currency`
- `from nautilus_trader.model.objects import Money`

**Directory:** `nautilus_trader/adapters/binance/spot/schemas`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


