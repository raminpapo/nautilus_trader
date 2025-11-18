# Documentation: memray_data.py

## File Metadata

- **Path**: `tests/mem_leak_tests/memray_data.py`
- **Size**: 2,721 bytes
- **Lines**: 63
- **Language**: Python

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Imports**: `nautilus_trader.model.data`, `nautilus_trader.model.identifiers`, `nautilus_trader.persistence.wranglers`, `nautilus_trader.test_kit.providers`

## Related Files

This file is located in `tests/mem_leak_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/mem_leak_tests/memray_data.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.268258Z*
