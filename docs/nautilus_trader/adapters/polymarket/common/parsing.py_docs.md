# Documentation: `nautilus_trader/adapters/polymarket/common/parsing.py`
**Generated:** 2025-11-15T19:40:04.447432Z
**File Size:** 7434 bytes
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

- **Path:** `nautilus_trader/adapters/polymarket/common/parsing.py`
- **Size:** 7,434 bytes
- **Lines:** 182
- **Extension:** `.py`
- **Type:** text
- **Imports:** 21
- **Functions:** 7

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

import time
from decimal import Decimal
from typing import Any

import pandas as pd

from nautilus_trader.adapters.polymarket.common.enums import PolymarketLiquiditySide
from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide
from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderStatus
from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderType
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id
from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_token_id
from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTickSizeChange
from nautilus_trader.model.currencies import USDC_POS
from nautilus_trader.model.enums import AssetClass
from nautilus_trader.model.enums import LiquiditySide
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.enums import OrderStatus
from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.instruments import BinaryOption
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity


def validate_ethereum_address(address: str) -> None:
    if not address.startswith("0x") or len(address) != 42:
        raise ValueError(
            f"Invalid Ethereum address format: {address!r}. "
            f"Expected 0x prefix with 40 hexadecimal characters",
        )
    try:
        int(address[2:], 16)
    except ValueError as e:
        raise ValueError(
            f"Invalid Ethereum address format: {address!r}. "
            f"Address contains non-hexadecimal characters",
        ) from e


def parse_order_side(order_side: PolymarketOrderSide) -> OrderSide:
    match order_side:
        case PolymarketOrderSide.BUY:
            return OrderSide.BUY
        case PolymarketOrderSide.SELL:
            return OrderSide.SELL
        case _:
            # Theoretically unreachable but retained to keep the match exhaustive
            raise ValueError(f"invalid order side, was {order_side}")


def parse_liquidity_side(liquidity_side: PolymarketLiquiditySide) -> LiquiditySide:
    match liquidity_side:
        case PolymarketLiquiditySide.MAKER:
            return LiquiditySide.MAKER
        case PolymarketLiquiditySide.TAKER:
            return LiquiditySide.TAKER
        case _:
            # Theoretically unreachable but retained to keep the match exhaustive
            raise ValueError(f"invalid liquidity side, was {liquidity_side}")


def parse_time_in_force(order_type: PolymarketOrderType) -> TimeInForce:
    match order_type:
        case PolymarketOrderType.GTC:
            return TimeInForce.GTC
        case PolymarketOrderType.GTD:
            return TimeInForce.GTD
        case PolymarketOrderType.FOK:
            return TimeInForce.FOK
        case PolymarketOrderType.FAK:
            return TimeInForce.IOC
        case _:
            # Theoretically unreachable but retained to keep the match exhaustive
            raise ValueError(f"invalid order type, was {order_type}")


def parse_order_status(order_status: PolymarketOrderStatus) -> OrderStatus:
    match order_status:
        case PolymarketOrderStatus.INVALID | PolymarketOrderStatus.UNMATCHED:
            return OrderStatus.REJECTED
        case PolymarketOrderStatus.LIVE | PolymarketOrderStatus.DELAYED:
            return OrderStatus.ACCEPTED
        case PolymarketOrderStatus.CANCELED | PolymarketOrderStatus.CANCELED_MARKET_RESOLVED:
            return OrderStatus.CANCELED
        case PolymarketOrderStatus.MATCHED:
            return OrderStatus.FILLED


def parse_polymarket_instrument(
    market_info: dict[str, Any],
    token_id: str,
    outcome: str,
    ts_init: int | None = None,
) -> BinaryOption:
    instrument_id = get_polymarket_instrument_id(str(market_info["condition_id"]), token_id)
    raw_symbol = Symbol(get_polymarket_token_id(instrument_id))
    description = market_info["question"]
    price_increment = Price.from_str(str(market_info["minimum_tick_size"]))
    min_quantity = Quantity.from_int(int(market_info["minimum_order_size"]))
    # size_increment can be 0.01 or 0.001 (precision 2 or 3). Need to determine a reliable solution
    # trades are reported with USDC.e increments though - so we use that here
    size_increment = Quantity.from_str("0.000001")
    end_date_iso = market_info["end_date_iso"]

    if end_date_iso:
        expiration_ns = pd.Timestamp(end_date_iso).value
    else:
        # end_date_iso can be missing in some conditions that are part of an event that has it
        expiration_ns = (pd.Timestamp.now(tz="UTC") + pd.DateOffset(years=10)).value

    maker_fee = Decimal(str(market_info["maker_base_fee"]))
    taker_fee = Decimal(str(market_info["taker_base_fee"]))

    ts_init = ts_init if ts_init is not None else time.time_ns()

    return BinaryOption(
        instrument_id=instrument_id,
        raw_symbol=raw_symbol,
        outcome=outcome,
        description=description,
        asset_class=AssetClass.ALTERNATIVE,
        currency=USDC_POS,
        price_increment=price_increment,
        price_precision=price_increment.precision,
        size_increment=size_increment,
        size_precision=size_increment.precision,
        activation_ns=0,  # TBD?
        expiration_ns=expiration_ns,
        max_quantity=None,
        min_quantity=min_quantity,
        maker_fee=maker_fee,
        taker_fee=taker_fee,
        ts_event=ts_init,
        ts_init=ts_init,
        info=market_info,
    )


def update_instrument(
    instrument: BinaryOption,
    change: PolymarketTickSizeChange,
    ts_init: int,
) -> BinaryOption:
    price_increment = Price.from_str(change.new_tick_size)

    return BinaryOption(
        instrument_id=instrument.id,
        raw_symbol=instrument.raw_symbol,
        outcome=instrument.outcome,
        description=instrument.description,
        asset_class=AssetClass.ALTERNATIVE,
        currency=USDC_POS,
        price_increment=price_increment,
        price_precision=price_increment.precision,
        size_increment=instrument.size_increment,
        size_precision=instrument.size_precision,
        activation_ns=instrument.activation_ns,
        expiration_ns=instrument.expiration_ns,
        max_quantity=None,
        min_quantity=instrument.min_quantity,
        maker_fee=instrument.maker_fee,
        taker_fee=instrument.taker_fee,
        ts_event=ts_init,
        ts_init=ts_init,
        info=instrument.info,
    )
```


---

## Overview

This file is located at `nautilus_trader/adapters/polymarket/common/parsing.py` within the repository.

**Functions defined:** validate_ethereum_address, parse_order_side, parse_liquidity_side, parse_time_in_force, parse_order_status, parse_polymarket_instrument, update_instrument

**Import statements:** 21


---

## Detailed Analysis

### Functions

#### `validate_ethereum_address(address: str)`


#### `parse_order_side(order_side: PolymarketOrderSide)`


#### `parse_liquidity_side(liquidity_side: PolymarketLiquiditySide)`


#### `parse_time_in_force(order_type: PolymarketOrderType)`


#### `parse_order_status(order_status: PolymarketOrderStatus)`


#### `parse_polymarket_instrument(
    market_info: dict[str, Any],
    token_id: str,
    outcome: str,
    ts_init: int | None = None,
)`


#### `update_instrument(
    instrument: BinaryOption,
    change: PolymarketTickSizeChange,
    ts_init: int,
)`


### Imports

- `import time`
- `from decimal import Decimal`
- `from typing import Any`
- `import pandas as pd`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketLiquiditySide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderStatus`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderType`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_token_id`
- `from nautilus_trader.adapters.polymarket.schemas.book import PolymarketTickSizeChange`
- `from nautilus_trader.model.currencies import USDC_POS`
- `from nautilus_trader.model.enums import AssetClass`
- `from nautilus_trader.model.enums import LiquiditySide`
- `from nautilus_trader.model.enums import OrderSide`
- `from nautilus_trader.model.enums import OrderStatus`
- `from nautilus_trader.model.enums import TimeInForce`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.instruments import BinaryOption`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`


---

## Usage Examples

### Importing

```python
from nautilus_trader.adapters.polymarket.common.parsing import validate_ethereum_address
```


---

## Related Files

This file imports from the following modules:

- `import time`
- `from decimal import Decimal`
- `from typing import Any`
- `import pandas as pd`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketLiquiditySide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderSide`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderStatus`
- `from nautilus_trader.adapters.polymarket.common.enums import PolymarketOrderType`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_instrument_id`
- `from nautilus_trader.adapters.polymarket.common.symbol import get_polymarket_token_id`

*... and 11 more*

**Directory:** `nautilus_trader/adapters/polymarket/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.


