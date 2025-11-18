# Documentation: test_perf_orderbook.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_orderbook.py`
- **Size**: 3,557 bytes
- **Lines**: 91
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

import pytest

from nautilus_trader import TEST_DATA_DIR
from nautilus_trader.adapters.databento.loaders import DatabentoDataLoader
from nautilus_trader.common.component import TestClock
from nautilus_trader.common.factories import OrderFactory
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.enums import BookType
from nautilus_trader.model.enums import OrderSide
from nautilus_trader.model.identifiers import StrategyId
from nautilus_trader.model.identifiers import TraderId
from nautilus_trader.model.objects import Price
from nautilus_trader.model.objects import Quantity
from nautilus_trader.test_kit.providers import TestInstrumentProvider
from nautilus_trader.test_kit.stubs.component import TestComponentStubs
from nautilus_trader.test_kit.stubs.data import TestDataStubs
from nautilus_trader.test_kit.stubs.events import TestEventStubs
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


@pytest.mark.skip(reason="development_only")
def test_orderbook_spy_xnas_itch_mbo_l3(benchmark) -> None:
    loader = DatabentoDataLoader()
    path = TEST_DATA_DIR / "databento" / "temp" / "spy-xnas-itch-20231127.mbo.dbn.zst"
    instrument = TestInstrumentProvider.equity(symbol="SPY", venue="XNAS")
    data = loader.from_dbn_file(
        path,
        instrument_id=instrument.id,
        as_legacy_cython=True,
    )

    book = TestDataStubs.make_book(
        instrument=instrument,
        book_type=BookType.L3_MBO,
    )

    def _apply_deltas():
        for delta in data:
            if not isinstance(delta, OrderBookDelta):
                continue
            book.apply_delta(delta)

    benchmark(_apply_deltas)

    # Assert
    assert book.ts_last == 1701129555644234540
    assert book.sequence == 429411899
    assert book.update_count == 6197580
    assert len(book.bids()) == 52
    assert len(book.asks()) == 38
    assert book.best_bid_price() == Price.from_str("454.84")
    assert book.best_ask_price() == Price.from_str("454.90")


def test_own_book_audit(benchmark) -> None:
    order_factory = OrderFactory(
        trader_id=TraderId("TESTER-000"),
        strategy_id=StrategyId("S-001"),
        clock=TestClock(),
    )
    cache = TestComponentStubs.cache()

    for i in range(1000):
        order = order_factory.limit(
            TestIdStubs.audusd_id(),
            OrderSide.BUY,
            Quantity.from_int(100_000),
            Price.from_str(f"1.0000{i}"),
        )
        order.apply(TestEventStubs.order_submitted(order))
        order.apply(TestEventStubs.order_accepted(order))
        cache.add_order(order)
        cache.update_order(order)

    benchmark(cache.audit_own_order_books)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`test_orderbook_spy_xnas_itch_mbo_l3()`**: Function defined in this file
- **`test_own_book_audit()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Functions**: `test_orderbook_spy_xnas_itch_mbo_l3`, `test_own_book_audit`
**Imports**: `nautilus_trader`, `nautilus_trader.adapters.databento.loaders`, `nautilus_trader.common.component`, `nautilus_trader.common.factories`, `nautilus_trader.model.data`, `nautilus_trader.model.enums`, `nautilus_trader.model.identifiers`, `nautilus_trader.model.objects`, `nautilus_trader.test_kit.providers`, `nautilus_trader.test_kit.stubs.component`, `nautilus_trader.test_kit.stubs.data`, `nautilus_trader.test_kit.stubs.events`, `nautilus_trader.test_kit.stubs.identifiers`, `pytest`

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
pytest tests/performance_tests/test_perf_orderbook.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.316802Z*
