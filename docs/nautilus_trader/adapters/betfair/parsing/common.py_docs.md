# Documentation: common.py

## File Metadata

- **Path**: `nautilus_trader/adapters/betfair/parsing/common.py`
- **Size**: 4,082 bytes
- **Lines**: 119
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

import hashlib
from functools import lru_cache

import msgspec
from betfair_parser.spec.common import Handicap
from betfair_parser.spec.common import MarketId
from betfair_parser.spec.common import OrderSide as BetSide
from betfair_parser.spec.common import SelectionId
from betfair_parser.spec.common import Size

from nautilus_trader.adapters.betfair.constants import BETFAIR_VENUE
from nautilus_trader.core.correctness import PyCondition
from nautilus_trader.core.nautilus_pyo3 import OrderSide
from nautilus_trader.model.enums import TimeInForce
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.instruments import BettingInstrument
from nautilus_trader.model.instruments.betting import make_symbol
from nautilus_trader.model.instruments.betting import null_handicap


@lru_cache
def betfair_instrument_id(
    market_id: MarketId,
    selection_id: SelectionId,
    selection_handicap: Handicap | None,
) -> InstrumentId:
    """
    Create an instrument ID from betfair fields.

    >>> betfair_instrument_id(market_id="1.201070830", selection_id=123456, selection_handicap=None)
    InstrumentId('1-201070830-123456-None.BETFAIR')

    """
    PyCondition.not_empty(market_id, "market_id")
    symbol = make_symbol(market_id, selection_id, selection_handicap or null_handicap())
    return InstrumentId(symbol=symbol, venue=BETFAIR_VENUE)


def instrument_id_betfair_ids(
    instrument_id: InstrumentId,
) -> tuple[MarketId, SelectionId, Handicap | None]:
    parts = instrument_id.symbol.value.rsplit("-", maxsplit=2)
    return (
        MarketId(parts[0]),
        SelectionId(parts[1]),
        Handicap(parts[2]) if parts[2] != "None" else None,
    )


def merge_instrument_fields(
    old: BettingInstrument,
    new: BettingInstrument,
    logger,
) -> BettingInstrument:
    old_dict = old.to_dict(old)
    new_dict = new.to_dict(new)
    for key, value in new_dict.items():
        if key in ("type", "id", "info"):
            continue
        if value != old_dict[key] and value:
            old_value = old_dict[key]
            logger.debug(f"Got updated field for {old.id}: {key=} {value=} {old_value=}")
            old_dict[key] = value

    return BettingInstrument.from_dict(old_dict)


def chunk(list_like, n):
    """
    Yield successive n-sized chunks from l.
    """
    for i in range(0, len(list_like), n):
        yield list_like[i : i + n]


def order_side_to_bet_side(side: OrderSide) -> BetSide:
    if side == OrderSide.BUY:
        return BetSide.LAY
    elif side == OrderSide.SELL:
        return BetSide.BACK
    else:
        raise RuntimeError(f"Unknown side: {side}")


def bet_side_to_order_side(side: BetSide) -> OrderSide:
    if side == BetSide.LAY:
        return OrderSide.BUY
    elif side == BetSide.BACK:
        return OrderSide.SELL
    else:
        raise RuntimeError(f"Unknown side: {side}")


def min_fill_size(time_in_force) -> Size | None:
    if time_in_force == TimeInForce.IOC:
        return 0
    else:
        return None


def hash_market_trade(timestamp: int, price: float, volume: float) -> str:
    data = (timestamp, price, volume)
    return hashlib.shake_256(msgspec.json.encode(data)).hexdigest(18)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`betfair_instrument_id()`**: Function defined in this file
- **`instrument_id_betfair_ids()`**: Function defined in this file
- **`merge_instrument_fields()`**: Function defined in this file
- **`chunk()`**: Function defined in this file
- **`order_side_to_bet_side()`**: Function defined in this file
- **`bet_side_to_order_side()`**: Function defined in this file
- **`min_fill_size()`**: Function defined in this file
- **`hash_market_trade()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 19


**Functions**: `bet_side_to_order_side`, `betfair_instrument_id`, `chunk`, `hash_market_trade`, `instrument_id_betfair_ids`, `merge_instrument_fields`, `min_fill_size`, `order_side_to_bet_side`
**Imports**: `betfair_parser.spec.common`, `functools`, `hashlib`, `msgspec`, `nautilus_trader.adapters.betfair.constants`, `nautilus_trader.core.correctness`, `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.instruments`, `nautilus_trader.model.instruments.betting`

## Related Files

This file is located in `nautilus_trader/adapters/betfair/parsing/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.479850Z*
