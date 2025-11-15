# Documentation: `nautilus_trader/adapters/polymarket/schemas/trade.py`
**Generated:** 2025-11-15T19:40:04.478585Z
**File Size:** 6493 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/schemas/trade.py`
- **Size:** 6,493 bytes
- **Lines:** 164
- **Extension:** `.py`
- **Type:** text
- **Imports:** 20
- **Classes:** 1
- **Functions:** 10

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
from typing import Any

import msgspec

from nautilus_trader.adapters.polymarket.common.enums import PolymarketLiquiditySide
from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide
from nautilus_trader.adapters.polymarket.common.parsing import parse_order_side
from nautilus_trader.adapters.polymarket.schemas.user import PolymarketMakerOrder
from nautilus_trader.core.datetime import millis_to_nanos
from nautilus_trader.core.stats import basis_points_as_percentage
from nautilus_trader.core.uuid import UUID4
from nautilus_trader.execution.reports import FillReport
from nautilus_trader.model.currencies import USDC_POS
from nautilus_trader.model.enums import LiquiditySide
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import TradeId
from nautilus_trader.model.identifiers import VenueOrderId
from nautilus_trader.model.instruments import BinaryOption
from nautilus_trader.model.objects import Money


class PolymarketTradeReport(msgspec.Struct, frozen=True):
    """
    Represents a Polymarket trade report.

    References
    ----------
    https://docs.polymarket.com/#get-trades

    """

    id: str  # trade ID
    taker_order_id: str
    market: str
    asset_id: str
    side: PolymarketOrderSide
    size: str
    fee_rate_bps: str
    price: str
    status: str
    match_time: str
    last_update: str
    outcome: str
    bucket_index: int
    owner: str
    maker_address: str
    transaction_hash: str
    maker_orders: list[PolymarketMakerOrder]
    trader_side: PolymarketLiquiditySide

    def to_dict(self) -> dict[str, Any]:
        return msgspec.json.decode(msgspec.json.encode(self))

    def get_filled_user_order_ids(self, maker_address: str, api_key: str) -> list[str]:
        if self.trader_side == PolymarketLiquiditySide.TAKER:
            user_order_ids = [self.taker_order_id]
        else:
            user_order_ids = [
                order.order_id
                for order in self.maker_orders
                if order.maker_address == maker_address or order.owner == api_key
            ]
        return user_order_ids

    def get_maker_order(self, filled_user_order_id: str) -> PolymarketMakerOrder:
        for order in self.maker_orders:
            if order.order_id == filled_user_order_id:
                return order

        raise ValueError(f"Invalid maker order ID {filled_user_order_id}")

    def liquidity_side(self) -> LiquiditySide:
        if self.trader_side == PolymarketLiquiditySide.TAKER:
            return LiquiditySide.TAKER
        else:
            return LiquiditySide.MAKER

    def order_side(self) -> OrderSide:
        order_side = parse_order_side(self.side)
        if self.trader_side == PolymarketLiquiditySide.TAKER:
            return order_side
        else:
            return OrderSide.BUY if order_side == OrderSide.SELL else OrderSide.SELL

    def venue_order_id(self, filled_user_order_id: str) -> VenueOrderId:
        if self.trader_side == PolymarketLiquiditySide.TAKER:
            return VenueOrderId(self.taker_order_id)
        else:
            try:
                order = self.get_maker_order(filled_user_order_id)
                return VenueOrderId(order.order_id)
            except ValueError:
                # Fallback for signature-type 2 trades
                if self.maker_orders:
                    return VenueOrderId(self.maker_orders[0].order_id)
                return VenueOrderId(self.taker_order_id)

    def last_px(self, filled_user_order_id: str) -> Decimal:
        if self.liquidity_side() == LiquiditySide.TAKER:
            return Decimal(self.price)
        else:
            order = self.get_maker_order(filled_user_order_id)
            return Decimal(order.price)

    def last_qty(self, filled_user_order_id: str) -> Decimal:
        if self.liquidity_side() == LiquiditySide.TAKER:
            return Decimal(self.size)
        else:
            order = self.get_maker_order(filled_user_order_id)
            return Decimal(order.matched_amount)

    def get_fee_rate_bps(self, filled_user_order_id: str) -> Decimal:
        if self.liquidity_side() == LiquiditySide.TAKER:
            return Decimal(self.fee_rate_bps)
        else:
            order = self.get_maker_order(filled_user_order_id)
            return Decimal(order.fee_rate_bps)

    def parse_to_fill_report(
        self,
        account_id: AccountId,
        instrument: BinaryOption,
        client_order_id: ClientOrderId | None,
        ts_init: int,
        filled_user_order_id: str,
    ) -> FillReport:
        last_qty = instrument.make_qty(self.last_qty(filled_user_order_id))
        last_px = instrument.make_price(self.last_px(filled_user_order_id))
        fee_rate_bps = self.get_fee_rate_bps(filled_user_order_id)
        commission = float(last_qty * last_px) * basis_points_as_percentage(fee_rate_bps)

        return FillReport(
            account_id=account_id,
            instrument_id=instrument.id,
            client_order_id=client_order_id,
            venue_order_id=self.venue_order_id(filled_user_order_id),
            trade_id=TradeId(self.id),
            order_side=self.order_side(),
            last_qty=last_qty,
            last_px=last_px,
            commission=Money(commission, USDC_POS),
            liquidity_side=self.liquidity_side(),
            report_id=UUID4(),
            ts_event=millis_to_nanos(int(self.match_time)),
            ts_init=ts_init,
        )
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/schemas/trade.py` within the repository.

**Classes defined:** PolymarketTradeReport

**Functions defined:** to_dict, get_filled_user_order_ids, get_maker_order, liquidity_side, order_side, venue_order_id, last_px, last_qty, get_fee_rate_bps, parse_to_fill_report

**Import statements:** 20


---

## Detailed Analysis

### Classes

#### `PolymarketTradeReport`

**Inherits from:** msgspec.Struct, frozen=True


### Functions

#### `to_dict(self)`


#### `get_filled_user_order_ids(self, maker_address: str, api_key: str)`


#### `get_maker_order(self, filled_user_order_id: str)`


#### `liquidity_side(self)`


#### `order_side(self)`


#### `venue_order_id(self, filled_user_order_id: str)`


#### `last_px(self, filled_user_order_id: str)`


#### `last_qty(self, filled_user_order_id: str)`


#### `get_fee_rate_bps(self, filled_user_order_id: str)`


#### `parse_to_fill_report(
        self,
        account_id: AccountId,
        instrument: BinaryOption,
        client_order_id: ClientOrderId | None,
        ts_init: int,
        filled_user_order_id: str,
    )`


### Imports

- `from decimal import Decimal`
- `from typing import Any`
- `import msgspec`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketLiquiditySide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide`
- `from nautilus_trader.adapters.polymarket.common.parsing import parse_order_side`
- `from nautilus_trader.adapters.polymarket.schemas.user import PolymarketMakerOrder`
- `from nautilus_trader.core.datetime import millis_to_nanos`
- `from nautilus_trader.core.stats import basis_points_as_percentage`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.execution.reports import FillReport`
- `from nautilus_trader.model.currencies import USDC_POS`
- `from nautilus_trader.model.enums import LiquiditySide`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import TradeId`
- `from nautilus_trader.model.identifiers import VenueOrderId`
- `from nautilus_trader.model.instruments import BinaryOption`
- `from nautilus_trader.model.objects import Money`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.schemas.trade import PolymarketTradeReport
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from typing import Any`
- `import msgspec`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketLiquiditySide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide`
- `from nautilus_trader.adapters.polymarket.common.parsing import parse_order_side`
- `from nautilus_trader.adapters.polymarket.schemas.user import PolymarketMakerOrder`
- `from nautilus_trader.core.datetime import millis_to_nanos`
- `from nautilus_trader.core.stats import basis_points_as_percentage`
- `from nautilus_trader.core.uuid import UUID4`

*... and 10 more*

**Directory:** `nautilus_trader/adapters/polymarket/schemas`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key. Ensure proper handling of secrets.


