# Documentation: test_perf_pyo3_conversion.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_pyo3_conversion.py`
- **Size**: 2,428 bytes
- **Lines**: 61
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

from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.model.data import QuoteTick
from nautilus_trader.model.data import TradeTick
from nautilus_trader.test_kit.rust.data_pyo3 import TestDataProviderPyo3


def test_pyo3_delta_to_legacy_cython(benchmark):
    pyo3_delta = TestDataProviderPyo3.order_book_delta()
    benchmark(OrderBookDelta.from_pyo3, pyo3_delta)


def test_pyo3_deltas_to_legacy_cython_list(benchmark):
    pyo3_deltas = [TestDataProviderPyo3.order_book_delta()] * 10_000
    benchmark(OrderBookDelta.from_pyo3_list, pyo3_deltas)


def test_pyo3_quote_to_legacy_cython(benchmark):
    pyo3_quote = TestDataProviderPyo3.quote_tick()
    benchmark(QuoteTick.from_pyo3, pyo3_quote)


def test_pyo3_quotes_to_legacy_cython_list(benchmark):
    pyo3_quotes = [TestDataProviderPyo3.quote_tick()] * 10_000
    benchmark(QuoteTick.from_pyo3_list, pyo3_quotes)


def test_pyo3_trade_to_legacy_cython(benchmark):
    pyo3_trade = TestDataProviderPyo3.trade_tick()
    benchmark(TradeTick.from_pyo3, pyo3_trade)


def test_pyo3_trades_to_legacy_cython_list(benchmark):
    pyo3_trades = [TestDataProviderPyo3.trade_tick()] * 10_000
    benchmark(TradeTick.from_pyo3_list, pyo3_trades)


def test_pyo3_bar_to_legacy_cython(benchmark):
    pyo3_bar = TestDataProviderPyo3.bar_5decimal()
    benchmark(Bar.from_pyo3, pyo3_bar)


def test_pyo3_bars_to_legacy_cython_list(benchmark):
    pyo3_bars = [TestDataProviderPyo3.bar_5decimal()] * 10_000
    benchmark(Bar.from_pyo3_list, pyo3_bars)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`test_pyo3_delta_to_legacy_cython()`**: Function defined in this file
- **`test_pyo3_deltas_to_legacy_cython_list()`**: Function defined in this file
- **`test_pyo3_quote_to_legacy_cython()`**: Function defined in this file
- **`test_pyo3_quotes_to_legacy_cython_list()`**: Function defined in this file
- **`test_pyo3_trade_to_legacy_cython()`**: Function defined in this file
- **`test_pyo3_trades_to_legacy_cython_list()`**: Function defined in this file
- **`test_pyo3_bar_to_legacy_cython()`**: Function defined in this file
- **`test_pyo3_bars_to_legacy_cython_list()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Functions**: `test_pyo3_bar_to_legacy_cython`, `test_pyo3_bars_to_legacy_cython_list`, `test_pyo3_delta_to_legacy_cython`, `test_pyo3_deltas_to_legacy_cython_list`, `test_pyo3_quote_to_legacy_cython`, `test_pyo3_quotes_to_legacy_cython_list`, `test_pyo3_trade_to_legacy_cython`, `test_pyo3_trades_to_legacy_cython_list`
**Imports**: `nautilus_trader.model.data`, `nautilus_trader.test_kit.rust.data_pyo3`

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
pytest tests/performance_tests/test_perf_pyo3_conversion.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.318298Z*
