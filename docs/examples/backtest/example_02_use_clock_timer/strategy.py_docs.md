# Documentation: `examples/backtest/example_02_use_clock_timer/strategy.py`
**Generated:** 2025-11-15T19:40:03.820999Z
**File Size:** 3540 bytes
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

- **Path:** `examples/backtest/example_02_use_clock_timer/strategy.py`
- **Size:** 3,540 bytes
- **Lines:** 83
- **Extension:** `.py`
- **Type:** text
- **Imports:** 8
- **Classes:** 1
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


---

## Overview

This file is located at `examples/backtest/example_02_use_clock_timer/strategy.py` within the repository.

**Classes defined:** SimpleTimerStrategy

**Functions defined:** __init__, on_start, on_bar, on_timer, on_stop

**Import statements:** 8


---

## Detailed Analysis

### Classes

#### `SimpleTimerStrategy`

**Inherits from:** Strategy


### Functions

#### `__init__(self, primary_bar_type: BarType)`


#### `on_start(self)`


#### `on_bar(self, bar: Bar)`


#### `on_timer(self, event: TimeEvent)`


#### `on_stop(self)`


### Imports

- `import datetime as dt`
- `import pandas as pd`
- `from nautilus_trader.common.enums import LogColor`
- `from nautilus_trader.common.events import TimeEvent`
- `from nautilus_trader.core.datetime import unix_nanos_to_dt`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.trading.strategy import Strategy`


---

## Usage Examples

### Importing

```python
from examples.backtest.example_02_use_clock_timer.strategy import SimpleTimerStrategy
```


---

## Related Files

This file imports from the following modules:

- `import datetime as dt`
- `import pandas as pd`
- `from nautilus_trader.common.enums import LogColor`
- `from nautilus_trader.common.events import TimeEvent`
- `from nautilus_trader.core.datetime import unix_nanos_to_dt`
- `from nautilus_trader.model.data import Bar`
- `from nautilus_trader.model.data import BarType`
- `from nautilus_trader.trading.strategy import Strategy`

**Directory:** `examples/backtest/example_02_use_clock_timer`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


