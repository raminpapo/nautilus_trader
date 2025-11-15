# Documentation: `tests/unit_tests/live/test_enqueue.py`
**Generated:** 2025-11-15T19:40:09.231875Z
**File Size:** 3048 bytes
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

- **Path:** `tests/unit_tests/live/test_enqueue.py`
- **Size:** 3,048 bytes
- **Lines:** 104
- **Extension:** `.py`
- **Type:** text
- **Imports:** 7
- **Functions:** 3

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

import asyncio
from unittest.mock import MagicMock

import pytest

from nautilus_trader.common.component import Logger
from nautilus_trader.common.component import TestClock
from nautilus_trader.live.enqueue import ThrottledEnqueuer
from nautilus_trader.test_kit.functions import eventually


@pytest.fixture
def clock():
    return TestClock()


@pytest.fixture
def logger():
    return MagicMock(Logger)


def test_properties(event_loop, clock, logger):
    # Arrange
    queue = asyncio.Queue(maxsize=5)

    # Act
    enqueuer = ThrottledEnqueuer(
        qname="test_queue",
        queue=queue,
        loop=event_loop,
        clock=clock,
        logger=logger,
    )

    # Assert
    assert enqueuer.qname == "test_queue"
    assert enqueuer.size == 0
    assert enqueuer.capacity == 5

    # Put some items in
    event_loop.run_until_complete(queue.put("item1"))
    event_loop.run_until_complete(queue.put("item2"))
    assert enqueuer.size == 2
    assert enqueuer.capacity == 5


@pytest.mark.asyncio
async def test_enqueue_when_queue_has_capacity(event_loop, clock, logger):
    # Arrange
    queue = asyncio.Queue(maxsize=10)
    enqueuer = ThrottledEnqueuer(
        qname="test_queue",
        queue=queue,
        loop=event_loop,
        clock=clock,
        logger=logger,
    )

    # Act
    # We expect a call_soon_threadsafe to enqueue_nowait_safely
    # But that callback won't run until we let the loop step
    enqueuer.enqueue("message1")
    await eventually(lambda: not queue.empty())

    # Assert: check the queue now has our item
    assert not queue.empty()
    assert queue.get_nowait() == "message1"


@pytest.mark.asyncio
async def test_enqueue_when_queue_is_full(event_loop, clock, logger):
    # Arrange
    queue = asyncio.Queue(maxsize=1)
    await queue.put("message1")

    enqueuer = ThrottledEnqueuer(
        qname="test_queue",
        queue=queue,
        loop=event_loop,
        clock=clock,
        logger=logger,
    )

    # Act: enqueue the new item (queue is full)
    enqueuer.enqueue("message2")
    await eventually(lambda: queue.qsize() == 1)

    # Assert: check queue is still size=1
    assert queue.qsize() == 1
```


---

## Overview

This file is located at `tests/unit_tests/live/test_enqueue.py` within the repository.

**Functions defined:** clock, logger, test_properties

**Import statements:** 7


---

## Detailed Analysis

### Functions

#### `clock()`


#### `logger()`


#### `test_properties(event_loop, clock, logger)`


### Imports

- `import asyncio`
- `from unittest.mock import MagicMock`
- `import pytest`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.live.enqueue import ThrottledEnqueuer`
- `from nautilus_trader.test_kit.functions import eventually`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.live.test_enqueue import clock
```


---

## Related Files

This file imports from the following modules:

- `import asyncio`
- `from unittest.mock import MagicMock`
- `import pytest`
- `from nautilus_trader.common.component import Logger`
- `from nautilus_trader.common.component import TestClock`
- `from nautilus_trader.live.enqueue import ThrottledEnqueuer`
- `from nautilus_trader.test_kit.functions import eventually`

**Directory:** `tests/unit_tests/live`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


