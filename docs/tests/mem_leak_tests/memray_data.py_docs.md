# Documentation: `tests/mem_leak_tests/memray_data.py`
**Generated:** 2025-11-15T19:40:08.021401Z
**File Size:** 2721 bytes
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

- **Path:** `tests/mem_leak_tests/memray_data.py`
- **Size:** 2,721 bytes
- **Lines:** 62
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7

---

## Source Code

```python
#!/usr/bin/env python3
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

from nautilus_trader.model.data import BarType
from nautilus_trader.model.identifiers import Venue
from nautilus_trader.persistence.wranglers import BarDataWrangler
from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler
from nautilus_trader.persistence.wranglers import TradeTickDataWrangler
from nautilus_trader.test_kit.providers import TestDataProvider
from nautilus_trader.test_kit.providers import TestInstrumentProvider


if __name__ == "__main__":
    SIM = Venue("SIM")
    AUDUSD_SIM = TestInstrumentProvider.default_fx_ccy("AUD/USD", SIM)
    GBPUSD_SIM = TestInstrumentProvider.default_fx_ccy("GBP/USD", SIM)
    ETHUSDT_BINANCE = TestInstrumentProvider.ethusdt_binance()

    provider = TestDataProvider()

    # Set up wranglers
    trade_tick_wrangler = TradeTickDataWrangler(instrument=ETHUSDT_BINANCE)
    quote_tick_wrangler = QuoteTickDataWrangler(instrument=AUDUSD_SIM)
    bid_wrangler = BarDataWrangler(
        bar_type=BarType.from_str("GBP/USD.SIM-1-MINUTE-BID-EXTERNAL"),
        instrument=GBPUSD_SIM,
    )
    ask_wrangler = BarDataWrangler(
        bar_type=BarType.from_str("GBP/USD.SIM-1-MINUTE-ASK-EXTERNAL"),
        instrument=GBPUSD_SIM,
    )

    count = 0
    total_runs = 128
    while count < total_runs:
        count += 1
        print(f"Run: {count}/{total_runs}")

        # Process data
        ticks = quote_tick_wrangler.process(provider.read_csv_ticks("truefx/audusd-ticks.csv"))
        ticks = trade_tick_wrangler.process(provider.read_csv_ticks("binance/ethusdt-trades.csv"))

        # Add data
        bid_bars = bid_wrangler.process(
            data=provider.read_csv_bars("fxcm/gbpusd-m1-bid-2012.csv")[:10_000],
        )
        ask_bars = ask_wrangler.process(
            data=provider.read_csv_bars("fxcm/gbpusd-m1-ask-2012.csv")[:10_000],
        )
```


---

## Overview

This file is located at `tests/mem_leak_tests/memray_data.py` within the repository.

**Import statements:** 7


---

## Detailed Analysis

### Imports

- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.persistence.wranglers import BarDataWrangler`
- `from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler`
- `from nautilus_trader.persistence.wranglers import TradeTickDataWrangler`
- `from nautilus_trader.test_kit.providers import TestDataProvider`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`


---

## Usage Examples

### Importing

```python
import tests.mem_leak_tests.memray_data
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.model.identifiers import Venue`
- `from nautilus_trader.persistence.wranglers import BarDataWrangler`
- `from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler`
- `from nautilus_trader.persistence.wranglers import TradeTickDataWrangler`
- `from nautilus_trader.test_kit.providers import TestDataProvider`
- `from nautilus_trader.test_kit.providers import TestInstrumentProvider`

**Directory:** `tests/mem_leak_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


