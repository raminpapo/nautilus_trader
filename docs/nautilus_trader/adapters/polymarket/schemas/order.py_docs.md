# Documentation: `nautilus_trader/adapters/polymarket/schemas/order.py`
**Generated:** 2025-11-15T19:40:04.477112Z
**File Size:** 2339 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/schemas/order.py`
- **Size:** 2,339 bytes
- **Lines:** 64
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 2

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

import msgspec

from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide
from nautilus_trader.adapters.polymarket.common.enums import PolymarketSignatureType


class PolymarketOrder(msgspec.Struct, frozen=True):
    """
    Represents a Polymarket limit order.

    References
    ----------
    https://docs.polymarket.com/#create-and-place-an-order

    """

    salt: int  # random salt used to create unique order
    maker: str  # maker address (funder)
    signer: str  # signed address
    taker: str  # taker address (operator)
    tokenId: str  # ERC1155 token ID of conditional token being traded
    makerAmount: str  # maximum amount maker is willing to spend
    takerAmount: str  # maximum amount taker is willing to spend
    expiration: str  # UNIX expiration timestamp (seconds?)  # TBD
    nonce: str  # makers Exchange nonce the order is associated with
    feeRateBps: str  # fee rate in basis points as required by the operator
    side: PolymarketOrderSide
    signatureType: PolymarketSignatureType  # signature
    signature: str  # hex encoded string


class PolymarketMakerOrder(msgspec.Struct, frozen=True):
    """
    Represents a Polymarket maker order (included for trades).

    References
    ----------
    https://docs.polymarket.com/#user-channel

    """

    asset_id: str
    fee_rate_bps: str
    maker_address: str
    matched_amount: str
    order_id: str
    outcome: str
    owner: str
    price: str
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/schemas/order.py` within the repository.

**Classes defined:** PolymarketOrder, PolymarketMakerOrder

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `PolymarketOrder`

**Inherits from:** msgspec.Struct, frozen=True


#### `PolymarketMakerOrder`

**Inherits from:** msgspec.Struct, frozen=True


### Imports

- `import msgspec`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketSignatureType`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.schemas.order import PolymarketOrder
```


---

## Related Files

This file imports from the following modules:

- `import msgspec`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketSignatureType`

**Directory:** `nautilus_trader/adapters/polymarket/schemas`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.


