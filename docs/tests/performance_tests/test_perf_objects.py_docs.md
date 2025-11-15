# Documentation: `tests/performance_tests/test_perf_objects.py`
**Generated:** 2025-11-15T19:40:08.049697Z
**File Size:** 3954 bytes
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

- **Path:** `tests/performance_tests/test_perf_objects.py`
- **Size:** 3,954 bytes
- **Lines:** 128
- **Extension:** `.py`
- **Type:** text
- **Imports:** 13
- **Functions:** 12

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

from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.model.enums import AggressorSide
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import TradeId
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.data import TestDataStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


def test_create_symbol(benchmark):
    benchmark(Symbol, "AUD/USD")


def test_create_instrument_id(benchmark):
    benchmark(InstrumentId, Symbol("AUD/USD"), Venue("IDEALPRO"))


def test_instrument_id_to_str(benchmark):
    benchmark(str, TestIdStubs.audusd_id())


def test_create_bar(benchmark):
    benchmark(
        Bar,
        TestDataStubs.bartype_audusd_1min_bid(),
        Price.from_str("1.00001"),
        Price.from_str("1.00004"),
        Price.from_str("1.00000"),
        Price.from_str("1.00003"),
        Quantity.from_str("100000"),
        0,
        0,
    )


def test_create_quote_tick(benchmark):
    audusd_sim = TestInstrumentProvider.default_fx_ccy("AUD/USD")

    def create_quote_tick():
        QuoteTick(
            instrument_id=audusd_sim.id,
            bid_price=Price.from_str("1.00000"),
            ask_price=Price.from_str("1.00001"),
            bid_size=Quantity.from_int(1),
            ask_size=Quantity.from_int(1),
            ts_event=0,
            ts_init=0,
        )

    benchmark(create_quote_tick)


def test_create_quote_tick_raw(benchmark):
    audusd_sim = TestInstrumentProvider.default_fx_ccy("AUD/USD")

    def create_quote_tick():
        QuoteTick.from_raw(
            audusd_sim.id,
            1000000000,
            1000010000,
            5,
            5,
            1000000000,
            1000000000,
            0,
            0,
            0,
            0,
        )

    benchmark(create_quote_tick)


def test_create_trade_tick(benchmark):
    audusd_sim = TestInstrumentProvider.default_fx_ccy("AUD/USD")

    def create_trade_tick():
        TradeTick(
            instrument_id=audusd_sim.id,
            price=Price.from_str("1.00000"),
            size=Quantity.from_int(1),
            aggressor_side=AggressorSide.BUYER,
            trade_id=TradeId("123458"),
            ts_event=0,
            ts_init=0,
        )

    benchmark(create_trade_tick)


def test_create_trade_tick_from_raw(benchmark):
    audusd_sim = TestInstrumentProvider.default_fx_ccy("AUD/USD")

    def create_trade_tick():
        TradeTick.from_raw(
            audusd_sim.id,
            10000000000000000,
            5,
            10000000000000000,
            0,
            AggressorSide.BUYER,
            TradeId("123458"),
            0,
            0,
        )

    benchmark(create_trade_tick)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_objects.py` within the repository.

**Functions defined:** test_create_symbol, test_create_instrument_id, test_instrument_id_to_str, test_create_bar, test_create_quote_tick, create_quote_tick, test_create_quote_tick_raw, create_quote_tick, test_create_trade_tick, create_trade_tick and 2 more

**Import statements:** 13


---

## Detailed Analysis

### Functions

#### `test_create_symbol(benchmark)`


#### `test_create_instrument_id(benchmark)`


#### `test_instrument_id_to_str(benchmark)`


#### `test_create_bar(benchmark)`


#### `test_create_quote_tick(benchmark)`


#### `create_quote_tick()`


#### `test_create_quote_tick_raw(benchmark)`


#### `create_quote_tick()`


#### `test_create_trade_tick(benchmark)`


#### `create_trade_tick()`


#### `test_create_trade_tick_from_raw(benchmark)`


#### `create_trade_tick()`


### Imports

- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.enums import AggressorSide`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import TradeId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_objects import test_create_symbol
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import QuoteTick`
- `from nautilus_trader.model.data import TradeTick`
- `from nautilus_trader.model.enums import AggressorSide`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import TradeId`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.model.objects import Price`
- `from nautilus_trader.model.objects import Quantity`

*... and 3 more*

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


