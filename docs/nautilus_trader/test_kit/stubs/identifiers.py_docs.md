# Documentation: `nautilus_trader/test_kit/stubs/identifiers.py`
**Generated:** 2025-11-15T19:40:05.387934Z
**File Size:** 4579 bytes
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

- **Path:** `nautilus_trader/test_kit/stubs/identifiers.py`
- **Size:** 4,579 bytes
- **Lines:** 135
- **Extension:** `.py`
- **Type:** text
- **Imports:** 13
- **Classes:** 1
- **Functions:** 25

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

from nautilus_trader.core.uuid import UUID4
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import OrderListId
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import TradeId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.identifiers import VenueOrderId


class TestIdStubs:
    @staticmethod
    def uuid() -> UUID4:
        return UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c757")

    @staticmethod
    def trader_id() -> TraderId:
        return TraderId("TESTER-000")

    @staticmethod
    def account_id() -> AccountId:
        return AccountId("SIM-000")

    @staticmethod
    def strategy_id() -> StrategyId:
        return StrategyId("S-001")

    @staticmethod
    def position_id() -> PositionId:
        return PositionId("001")

    @staticmethod
    def btcusdt_binance_id() -> InstrumentId:
        return InstrumentId(Symbol("BTCUSDT"), Venue("BINANCE"))

    @staticmethod
    def btcusdt_perp_binance_id() -> InstrumentId:
        return InstrumentId(Symbol("BTCUSDT-PERP"), Venue("BINANCE"))

    @staticmethod
    def ethusdt_binance_id() -> InstrumentId:
        return InstrumentId(Symbol("ETHUSDT"), Venue("BINANCE"))

    @staticmethod
    def ethusdt_perp_binance_id() -> InstrumentId:
        return InstrumentId(Symbol("ETHUSDT-PERP"), Venue("BINANCE"))

    @staticmethod
    def adabtc_binance_id() -> InstrumentId:
        return InstrumentId(Symbol("ADABTC"), Venue("BINANCE"))

    @staticmethod
    def audusd_id() -> InstrumentId:
        return InstrumentId(Symbol("AUD/USD"), Venue("SIM"))

    @staticmethod
    def gbpusd_id() -> InstrumentId:
        return InstrumentId(Symbol("GBP/USD"), Venue("SIM"))

    @staticmethod
    def usdjpy_id() -> InstrumentId:
        return InstrumentId(Symbol("USD/JPY"), Venue("SIM"))

    @staticmethod
    def audusd_idealpro_id() -> InstrumentId:
        return InstrumentId(Symbol("AUD/USD"), Venue("IDEALPRO"))

    @staticmethod
    def aapl_xnas_id() -> InstrumentId:
        return InstrumentId(Symbol("AAPL"), Venue("XNAS"))

    @staticmethod
    def msft_xnas_id() -> InstrumentId:
        return InstrumentId(Symbol("MSFT"), Venue("XNAS"))

    @staticmethod
    def betting_instrument_id():
        from nautilus_trader.adapters.betfair.parsing.common import betfair_instrument_id

        return betfair_instrument_id(
            market_id="1-179082386",
            selection_id=50214,
            selection_handicap=None,
        )

    @staticmethod
    def synthetic_id():
        return InstrumentId(Symbol("BTC-ETH"), Venue("SYNTH"))

    @staticmethod
    def client_order_id(counter: int = 1) -> ClientOrderId:
        return ClientOrderId(f"O-20210410-022422-001-001-{counter}")

    @staticmethod
    def order_list_id(counter: int = 1) -> OrderListId:
        return OrderListId(f"OL-20210410-022422-001-001-{counter}")

    @staticmethod
    def venue_order_id() -> VenueOrderId:
        return VenueOrderId("1")

    @staticmethod
    def trade_id() -> TradeId:
        return TradeId("1")

    @staticmethod
    def position_id_long() -> PositionId:
        return PositionId("001-LONG")

    @staticmethod
    def position_id_short() -> PositionId:
        return PositionId("001-SHORT")

    @staticmethod
    def position_id_both() -> PositionId:
        return PositionId("001-BOTH")
```


---

## Overview

This file is located at `nautilus_trader/test_kit/stubs/identifiers.py` within the repository.

**Classes defined:** TestIdStubs

**Functions defined:** uuid, trader_id, account_id, strategy_id, position_id, btcusdt_binance_id, btcusdt_perp_binance_id, ethusdt_binance_id, ethusdt_perp_binance_id, adabtc_binance_id and 15 more

**Import statements:** 13


---

## Detailed Analysis

### Classes

#### `TestIdStubs`


### Functions

#### `uuid()`


#### `trader_id()`


#### `account_id()`


#### `strategy_id()`


#### `position_id()`


#### `btcusdt_binance_id()`


#### `btcusdt_perp_binance_id()`


#### `ethusdt_binance_id()`


#### `ethusdt_perp_binance_id()`


#### `adabtc_binance_id()`


#### `audusd_id()`


#### `gbpusd_id()`


#### `usdjpy_id()`


#### `audusd_idealpro_id()`


#### `aapl_xnas_id()`


#### `msft_xnas_id()`


#### `betting_instrument_id()`


#### `synthetic_id()`


#### `client_order_id(counter: int = 1)`


#### `order_list_id(counter: int = 1)`


#### `venue_order_id()`


#### `trade_id()`


#### `position_id_long()`


#### `position_id_short()`


#### `position_id_both()`


### Imports

- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import OrderListId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import TradeId`
- `from nautilus_trader.model.identifiers import TraderId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.identifiers import VenueOrderId`
- `from nautilus_trader.adapters.betfair.parsing.common import betfair_instrument_id`


---

## Usage Examples

### Importing

```python
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.identifiers import AccountId`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import OrderListId`
- `from nautilus_trader.model.identifiers import PositionId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import TradeId`
- `from nautilus_trader.model.identifiers import TraderId`

*... and 3 more*

**Directory:** `nautilus_trader/test_kit/stubs`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


