# Documentation: `tests/unit_tests/common/test_events.py`
**Generated:** 2025-11-15T19:40:09.050337Z
**File Size:** 1786 bytes
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

- **Path:** `tests/unit_tests/common/test_events.py`
- **Size:** 1,786 bytes
- **Lines:** 68
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 2

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

import pickle

from nautilus_trader.common.events import TimeEvent
from nautilus_trader.core.uuid import UUID4


def test_time_event_equality():
    # Arrange
    event_id = UUID4()

    event1 = TimeEvent(
        "TEST_EVENT",
        event_id,
        1,
        2,
    )

    event2 = TimeEvent(
        "TEST_EVENT",
        event_id,
        1,
        2,
    )

    event3 = TimeEvent(
        "TEST_EVENT",
        UUID4(),
        1,
        2,
    )

    # Act, Assert
    assert event1.name == event2.name == event3.name
    assert event1 == event2
    assert event3 != event1
    assert event3 != event2


def test_time_event_picking():
    # Arrange
    event = TimeEvent(
        "TEST_EVENT",
        UUID4(),
        1,
        2,
    )

    # Act
    pickled = pickle.dumps(event)
    unpickled = pickle.loads(pickled)  # noqa: S301 (pickle is safe here)

    # Assert
    assert event == unpickled
```


---

## Overview

This file is located at `tests/unit_tests/common/test_events.py` within the repository.

**Functions defined:** test_time_event_equality, test_time_event_picking

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_time_event_equality()`


#### `test_time_event_picking()`


### Imports

- `import pickle`
- `from nautilus_trader.common.events import TimeEvent`
- `from nautilus_trader.core.uuid import UUID4`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_events import test_time_event_equality
```


---

## Related Files

This file imports from the following modules:

- `import pickle`
- `from nautilus_trader.common.events import TimeEvent`
- `from nautilus_trader.core.uuid import UUID4`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


