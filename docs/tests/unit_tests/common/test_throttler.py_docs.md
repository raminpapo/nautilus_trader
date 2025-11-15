# Documentation: `tests/unit_tests/common/test_throttler.py`
**Generated:** 2025-11-15T19:40:09.067695Z
**File Size:** 10003 bytes
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

- **Path:** `tests/unit_tests/common/test_throttler.py`
- **Size:** 10,003 bytes
- **Lines:** 307
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 2
- **Functions:** 15

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

from datetime import timedelta

from nautilus_trader.common.component import TestClock
from nautilus_trader.common.component import Throttler


class TestBufferingThrottler:
    def setup(self):
        # Fixture Setup
        self.clock = TestClock()

        self.handler = []
        self.throttler = Throttler(
            name="Buffer",
            limit=5,
            interval=timedelta(seconds=1),
            output_send=self.handler.append,
            output_drop=None,  # <-- no dropping handler so will buffer
            clock=self.clock,
        )

    def test_throttler_instantiation(self):
        # Arrange, Act, Assert
        assert self.throttler.name == "Buffer"
        assert not self.throttler.is_limiting
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 0
        assert self.throttler.recv_count == 0
        assert self.throttler.sent_count == 0

    def test_send_sends_message_to_handler(self):
        # Arrange
        item = "MESSAGE"

        # Act
        self.throttler.send(item)

        # Assert
        assert not self.throttler.is_limiting
        assert self.handler == ["MESSAGE"]
        assert self.throttler.recv_count == 1
        assert self.throttler.sent_count == 1

    def test_send_to_limit_becomes_throttled(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Assert: Only 5 items are sent
        assert self.clock.timer_names == ["Buffer|DEQUE"]
        assert self.clock.timer_count == 1
        assert self.throttler.is_limiting
        assert self.handler == ["MESSAGE"] * 5
        assert self.throttler.qsize == 1
        assert self.throttler.used() == 1
        assert self.throttler.recv_count == 6
        assert self.throttler.sent_count == 5

    def test_used_when_sent_to_limit_returns_one(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Act
        used = self.throttler.used()

        # Assert: Remaining items sent
        assert used == 1
        assert self.throttler.recv_count == 5
        assert self.throttler.sent_count == 5

    def test_used_when_half_interval_from_limit_returns_half(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.clock.advance_time(500_000_000)

        # Act
        used = self.throttler.used()

        # Assert: Remaining items sent
        assert used == 0.5
        assert self.throttler.recv_count == 5
        assert self.throttler.sent_count == 5

    def test_used_before_limit_when_halfway_returns_half(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Act
        used = self.throttler.used()

        # Assert
        assert used == 0.6

    def test_refresh_when_at_limit_sends_remaining_items(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Act: Trigger refresh token time alert
        events = self.clock.advance_time(1_000_000_000)
        events[0].handle()

        # Assert: Remaining items sent
        assert self.clock.timer_count == 0  # No longer timing to process
        assert self.throttler.is_limiting is False
        assert self.handler == ["MESSAGE"] * 6
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 0
        assert self.throttler.recv_count == 6
        assert self.throttler.sent_count == 6

    def test_send_message_after_dropping_message(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Act: Trigger refresh token time alert
        events = self.clock.advance_time(1_000_000_000)
        events[0].handle()

        assert self.throttler.is_limiting is False

        # Act: send a message after a previous message is throttled
        self.throttler.send(item)

        # Assert: Remaining items sent
        assert self.clock.timer_count == 0  # No longer timing to process
        assert self.throttler.is_limiting is False
        assert self.handler == ["MESSAGE"] * 7
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 0
        assert self.throttler.recv_count == 7
        assert self.throttler.sent_count == 7


class TestDroppingThrottler:
    def setup(self):
        # Fixture Setup
        self.clock = TestClock()

        self.handler = []
        self.dropped = []
        self.throttler = Throttler(
            name="Dropper",
            limit=5,
            interval=timedelta(seconds=1),
            output_send=self.handler.append,
            output_drop=self.dropped.append,  # <-- handler for dropping messages
            clock=self.clock,
        )

    def test_throttler_instantiation(self):
        # Arrange, Act, Assert
        assert self.throttler.name == "Dropper"
        assert not self.throttler.is_limiting
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 0
        assert self.throttler.recv_count == 0
        assert self.throttler.sent_count == 0

    def test_send_sends_message_to_handler(self):
        # Arrange
        item = "MESSAGE"

        # Act
        self.throttler.send(item)

        # Assert
        assert not self.throttler.is_limiting
        assert self.handler == ["MESSAGE"]
        assert self.throttler.recv_count == 1
        assert self.throttler.sent_count == 1

    def test_send_to_limit_drops_message(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Assert: Only 5 items are sent
        assert self.clock.timer_names == ["Dropper|DEQUE"]
        assert self.clock.timer_count == 1
        assert self.throttler.is_limiting
        assert self.handler == ["MESSAGE"] * 5
        assert self.dropped == ["MESSAGE"]
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 1
        assert self.throttler.recv_count == 6
        assert self.throttler.sent_count == 5

    def test_advance_time_when_at_limit_dropped_message(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Act: Trigger refresh token time alert
        events = self.clock.advance_time(1_000_000_000)
        events[0].handle()

        # Assert: Remaining items sent
        assert self.clock.timer_count == 0  # No longer timing to process
        assert self.throttler.is_limiting is False
        assert self.handler == ["MESSAGE"] * 5
        assert self.dropped == ["MESSAGE"]
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 0
        assert self.throttler.recv_count == 6
        assert self.throttler.sent_count == 5

    def test_send_message_after_dropping_message(self):
        # Arrange
        item = "MESSAGE"

        # Act: Send 6 items
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)
        self.throttler.send(item)

        # Act: Trigger refresh token time alert
        events = self.clock.advance_time(1_000_000_000)
        events[0].handle()

        assert self.throttler.is_limiting is False

        # Act: send a message after a previous message is throttled
        self.throttler.send(item)

        # Assert: Remaining items sent
        assert self.clock.timer_count == 0  # No longer timing to process
        assert self.throttler.is_limiting is False
        assert self.handler == ["MESSAGE"] * 6
        assert self.dropped == ["MESSAGE"]
        assert self.throttler.qsize == 0
        assert self.throttler.used() == 0
        assert self.throttler.recv_count == 7
        assert self.throttler.sent_count == 6
```


---

## Overview

This file is located at `tests/unit_tests/common/test_throttler.py` within the repository.

**Classes defined:** TestBufferingThrottler, TestDroppingThrottler

**Functions defined:** setup, test_throttler_instantiation, test_send_sends_message_to_handler, test_send_to_limit_becomes_throttled, test_used_when_sent_to_limit_returns_one, test_used_when_half_interval_from_limit_returns_half, test_used_before_limit_when_halfway_returns_half, test_refresh_when_at_limit_sends_remaining_items, test_send_message_after_dropping_message, setup and 5 more

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `TestBufferingThrottler`


#### `TestDroppingThrottler`


### Functions

#### `setup(self)`


#### `test_throttler_instantiation(self)`


#### `test_send_sends_message_to_handler(self)`


#### `test_send_to_limit_becomes_throttled(self)`


#### `test_used_when_sent_to_limit_returns_one(self)`


#### `test_used_when_half_interval_from_limit_returns_half(self)`


#### `test_used_before_limit_when_halfway_returns_half(self)`


#### `test_refresh_when_at_limit_sends_remaining_items(self)`


#### `test_send_message_after_dropping_message(self)`


#### `setup(self)`


#### `test_throttler_instantiation(self)`


#### `test_send_sends_message_to_handler(self)`


#### `test_send_to_limit_drops_message(self)`


#### `test_advance_time_when_at_limit_dropped_message(self)`


#### `test_send_message_after_dropping_message(self)`


### Imports

- `from datetime import timedelta`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.common.component import Throttler`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_throttler import TestBufferingThrottler
```


---

## Related Files

This file imports from the following modules:

- `from datetime import timedelta`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.common.component import Throttler`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


