# Documentation: `tests/performance_tests/test_perf_wranglers.py`
**Generated:** 2025-11-15T19:40:08.059308Z
**File Size:** 1981 bytes
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

- **Path:** `tests/performance_tests/test_perf_wranglers.py`
- **Size:** 1,981 bytes
- **Lines:** 47
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Functions:** 4

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


---

## Overview

This file is located at `tests/performance_tests/test_perf_wranglers.py` within the repository.

**Functions defined:** test_quote_tick_data_wrangler_process_tick_data, wrangler_process, test_trade_tick_data_wrangler_process, wrangler_process

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `test_quote_tick_data_wrangler_process_tick_data(benchmark)`


#### `wrangler_process()`


#### `test_trade_tick_data_wrangler_process(benchmark)`


#### `wrangler_process()`


### Imports

- `from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler`
- `from nautilus_trader.persistence.wranglers import TradeTickDataWrangler`
- `from nautilus_trader.test_kit.providers import TestDataProvider`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_wranglers import test_quote_tick_data_wrangler_process_tick_data
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler`
- `from nautilus_trader.persistence.wranglers import TradeTickDataWrangler`
- `from nautilus_trader.test_kit.providers import TestDataProvider`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


