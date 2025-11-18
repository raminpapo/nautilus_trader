# Documentation: test_perf_events.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_events.py`
- **Size**: 2,467 bytes
- **Lines**: 66
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`stub_order_denied()`**: Function defined in this file
- **`test_order_denied_to_dict()`**: Function defined in this file
- **`test_order_denied_to_dict_then_msgspec_to_json()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `stub_order_denied`, `test_order_denied_to_dict`, `test_order_denied_to_dict_then_msgspec_to_json`
**Imports**: `msgspec`, `nautilus_trader.core.uuid`, `nautilus_trader.model.events`, `nautilus_trader.model.identifiers`

## Related Files

This file is located in `tests/performance_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/performance_tests/test_perf_events.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.305942Z*
