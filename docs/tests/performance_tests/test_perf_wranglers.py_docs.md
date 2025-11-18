# Documentation: test_perf_wranglers.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_wranglers.py`
- **Size**: 1,981 bytes
- **Lines**: 48
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

from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler
from nautilus_trader.persistence.wranglers import TradeTickDataWrangler
from nautilus_trader.test_kit.providers import TestDataProvider
from nautilus_trader.test_kit.providers import TestInstrumentProvider


def test_quote_tick_data_wrangler_process_tick_data(benchmark):
    usdjpy = TestInstrumentProvider.default_fx_ccy("USD/JPY")

    wrangler = QuoteTickDataWrangler(instrument=usdjpy)
    provider = TestDataProvider()

    def wrangler_process():
        # 1000 ticks in data
        wrangler.process(
            data=provider.read_csv_ticks("truefx/usdjpy-ticks.csv"),
            default_volume=1_000_000,
        )

    benchmark(wrangler_process)


def test_trade_tick_data_wrangler_process(benchmark):
    ethusdt = TestInstrumentProvider.ethusdt_binance()
    wrangler = TradeTickDataWrangler(instrument=ethusdt)
    provider = TestDataProvider()

    def wrangler_process():
        # 69_806 ticks in data
        wrangler.process(data=provider.read_csv_ticks("binance/ethusdt-trades.csv"))

    benchmark(wrangler_process)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`test_quote_tick_data_wrangler_process_tick_data()`**: Function defined in this file
- **`test_trade_tick_data_wrangler_process()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `test_quote_tick_data_wrangler_process_tick_data`, `test_trade_tick_data_wrangler_process`
**Imports**: `nautilus_trader.persistence.wranglers`, `nautilus_trader.test_kit.providers`

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
pytest tests/performance_tests/test_perf_wranglers.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.323700Z*
