# Documentation: `tests/performance_tests/test_perf_events.py`
**Generated:** 2025-11-15T19:40:08.042546Z
**File Size:** 2467 bytes
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

- **Path:** `tests/performance_tests/test_perf_events.py`
- **Size:** 2,467 bytes
- **Lines:** 65
- **Extension:** `.py`
- **Type:** text
- **Imports:** 9
- **Functions:** 5

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

from nautilus_trader.core.uuid import UUID4
from nautilus_trader.model.events import OrderDenied
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import InstrumentId
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.identifiers import Venue


_STUB_ORDER_DENIED = OrderDenied(
    trader_id=TraderId("TRADER-001"),
    strategy_id=StrategyId("SCALPER-001"),
    instrument_id=InstrumentId(Symbol("BTCUSDT"), Venue("BINANCE")),
    client_order_id=ClientOrderId("O-2020872378423"),
    reason="Exceeded MAX_ORDER_SUBMIT_RATE",
    event_id=UUID4(),
    ts_init=0,
)


def stub_order_denied() -> OrderDenied:
    uuid = UUID4()
    reason = "Exceeded MAX_ORDER_SUBMIT_RATE"
    return OrderDenied(
        trader_id=TraderId("TRADER-001"),
        strategy_id=StrategyId("SCALPER-001"),
        instrument_id=InstrumentId(Symbol("BTCUSDT"), Venue("BINANCE")),
        client_order_id=ClientOrderId("O-2020872378423"),
        reason=reason,
        event_id=uuid,
        ts_init=0,
    )


def test_order_denied_to_dict(benchmark):
    def call_to_dict() -> None:
        OrderDenied.to_dict(_STUB_ORDER_DENIED)

    benchmark(call_to_dict)


def test_order_denied_to_dict_then_msgspec_to_json(benchmark):
    def call_to_dict_then_json() -> None:
        denied_dict = OrderDenied.to_dict(_STUB_ORDER_DENIED)
        msgspec.json.encode(denied_dict)

    benchmark(call_to_dict_then_json)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_events.py` within the repository.

**Functions defined:** stub_order_denied, test_order_denied_to_dict, call_to_dict, test_order_denied_to_dict_then_msgspec_to_json, call_to_dict_then_json

**Import statements:** 9


---

## Detailed Analysis

### Functions

#### `stub_order_denied()`


#### `test_order_denied_to_dict(benchmark)`


#### `call_to_dict()`


#### `test_order_denied_to_dict_then_msgspec_to_json(benchmark)`


#### `call_to_dict_then_json()`


### Imports

- `import msgspec`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.events import OrderDenied`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import TraderId`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_events import stub_order_denied
```


---

## Related Files

This file imports from the following modules:

- `import msgspec`
- `from nautilus_trader.core.uuid import UUID4`
- `from nautilus_trader.model.events import OrderDenied`
- `from nautilus_trader.model.identifiers import ClientOrderId`
- `from nautilus_trader.model.identifiers import InstrumentId`
- `from nautilus_trader.model.identifiers import StrategyId`
- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import TraderId`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


