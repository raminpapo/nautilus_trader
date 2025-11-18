# Documentation: strategy.py

## File Metadata

- **Path**: `examples/backtest/example_01_load_bars_from_custom_csv/strategy.py`
- **Size**: 2,124 bytes
- **Lines**: 52
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

import datetime as dt

from nautilus_trader.common.enums import LogColor
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarType
from nautilus_trader.trading.strategy import Strategy


# This is a trivial demo strategy that simply counts all processed 1-minute bars.
class DemoStrategy(Strategy):
    def __init__(self, primary_bar_type: BarType):
        super().__init__()
        self.primary_bar_type = primary_bar_type
        self.bars_processed = 0
        self.start_time = None
        self.end_time = None

    def on_start(self):
        # Remember and log start time of strategy
        self.start_time = dt.datetime.now()
        self.log.info(f"Strategy started at: {self.start_time}")

        # Subscribe to bars
        self.subscribe_bars(self.primary_bar_type)

    def on_bar(self, bar: Bar):
        self.bars_processed += 1
        self.log.info(f"Processed bars: {self.bars_processed}", color=LogColor.YELLOW)

    def on_stop(self):
        # Remember and log end time of strategy
        self.end_time = dt.datetime.now()
        self.log.info(f"Strategy finished at: {self.end_time}")

        # Log count of processed bars
        self.log.info(f"Total bars processed: {self.bars_processed}")

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DemoStrategy`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Classs**: `DemoStrategy`
**Imports**: `datetime`, `nautilus_trader.common.enums`, `nautilus_trader.model.data`, `nautilus_trader.trading.strategy`

## Related Files

This file is located in `examples/backtest/example_01_load_bars_from_custom_csv/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_01_load_bars_from_custom_csv/strategy.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.218653Z*
