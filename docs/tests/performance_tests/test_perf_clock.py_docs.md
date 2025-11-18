# Documentation: test_perf_clock.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_clock.py`
- **Size**: 2,348 bytes
- **Lines**: 74
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

from datetime import timedelta

import pandas as pd
import pytest

from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import TestClock
from nautilus_trader.common.events import TimeEvent


_LIVE_CLOCK = LiveClock()
_TEST_CLOCK = TestClock()


def test_live_clock_utc_now(benchmark) -> None:
    benchmark(_LIVE_CLOCK.utc_now)


def test_live_clock_unix_timestamp(benchmark) -> None:
    benchmark(_LIVE_CLOCK.timestamp)


def test_live_clock_timestamp_ns(benchmark) -> None:
    benchmark(_LIVE_CLOCK.timestamp_ns)


def test_live_clock_timestamp_us(benchmark) -> None:
    benchmark(_LIVE_CLOCK.timestamp_us)


def test_live_clock_timestamp_ms(benchmark) -> None:
    benchmark(_LIVE_CLOCK.timestamp_ms)


@pytest.mark.skip
def test_live_clock_cancel(benchmark) -> None:
    def _start_and_cancel():
        _LIVE_CLOCK.set_timer("timer1", pd.Timedelta(microseconds=10), callback=print)
        _LIVE_CLOCK.cancel_timer("timer1")

    benchmark(_start_and_cancel)


def test_advance_time(benchmark) -> None:
    benchmark(_TEST_CLOCK.advance_time, 0)


def test_iteratively_advance_time(benchmark) -> None:
    store: list[TimeEvent] = []
    _TEST_CLOCK.set_timer("test", timedelta(seconds=1), callback=store.append)

    def _iteratively_advance_time():
        test_time = 0
        for _ in range(100_000):
            test_time += 1
        _TEST_CLOCK.advance_time(to_time_ns=test_time)

    benchmark(_iteratively_advance_time)

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`test_live_clock_utc_now()`**: Function defined in this file
- **`test_live_clock_unix_timestamp()`**: Function defined in this file
- **`test_live_clock_timestamp_ns()`**: Function defined in this file
- **`test_live_clock_timestamp_us()`**: Function defined in this file
- **`test_live_clock_timestamp_ms()`**: Function defined in this file
- **`test_live_clock_cancel()`**: Function defined in this file
- **`test_advance_time()`**: Function defined in this file
- **`test_iteratively_advance_time()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Functions**: `test_advance_time`, `test_iteratively_advance_time`, `test_live_clock_cancel`, `test_live_clock_timestamp_ms`, `test_live_clock_timestamp_ns`, `test_live_clock_timestamp_us`, `test_live_clock_unix_timestamp`, `test_live_clock_utc_now`
**Imports**: `datetime`, `nautilus_trader.common.component`, `nautilus_trader.common.events`, `pandas`, `pytest`

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
pytest tests/performance_tests/test_perf_clock.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.301909Z*
