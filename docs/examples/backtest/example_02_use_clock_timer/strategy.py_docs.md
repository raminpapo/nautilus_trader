# Documentation: strategy.py

## File Metadata

- **Path**: `examples/backtest/example_02_use_clock_timer/strategy.py`
- **Size**: 3,540 bytes
- **Lines**: 84
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

import pandas as pd

from nautilus_trader.common.enums import LogColor
from nautilus_trader.common.events import TimeEvent
from nautilus_trader.core.datetime import unix_nanos_to_dt
from nautilus_trader.model.data import Bar
from nautilus_trader.model.data import BarType
from nautilus_trader.trading.strategy import Strategy


class SimpleTimerStrategy(Strategy):
    TIMER_NAME = "every_3_minutes"
    TIMER_INTERVAL = pd.Timedelta(minutes=3)

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

        # ==================================================================
        # POINT OF FOCUS: Timer invokes action at regular time intervals
        # ------------------------------------------------------------------

        # Setup recurring timer
        self.clock.set_timer(
            name=self.TIMER_NAME,  # Custom timer name
            interval=self.TIMER_INTERVAL,  # Timer interval
            callback=self.on_timer,  # Custom callback function invoked on timer
        )

    def on_bar(self, bar: Bar):
        # You can implement any action here (like submit order), but for simplicity, we are just counting bars
        self.bars_processed += 1
        self.log.info(f"Processed bars: {self.bars_processed}")

    # ==================================================================
    # POINT OF FOCUS: Custom callback function invoked by Timer
    # ------------------------------------------------------------------

    def on_timer(self, event: TimeEvent):
        if event.name == self.TIMER_NAME:
            event_time_dt = unix_nanos_to_dt(event.ts_event)
            # You can implement any action here (like submit order), which should be executed in regular interval,
            # but for simplicity, we just create a log.
            self.log.info(
                f"TimeEvent received. | Name: {event.name} | Time: {event_time_dt}",
                color=LogColor.YELLOW,
            )

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
- **`SimpleTimerStrategy`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Classs**: `SimpleTimerStrategy`
**Imports**: `datetime`, `nautilus_trader.common.enums`, `nautilus_trader.common.events`, `nautilus_trader.core.datetime`, `nautilus_trader.model.data`, `nautilus_trader.trading.strategy`, `pandas`

## Related Files

This file is located in `examples/backtest/example_02_use_clock_timer/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest examples/backtest/example_02_use_clock_timer/strategy.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.222757Z*
