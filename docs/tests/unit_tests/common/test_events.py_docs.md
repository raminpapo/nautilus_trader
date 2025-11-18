# Documentation: test_events.py

## File Metadata

- **Path**: `tests/unit_tests/common/test_events.py`
- **Size**: 1,786 bytes
- **Lines**: 69
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`test_time_event_equality()`**: Function defined in this file
- **`test_time_event_picking()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `test_time_event_equality`, `test_time_event_picking`
**Imports**: `nautilus_trader.common.events`, `nautilus_trader.core.uuid`, `pickle`

## Related Files

This file is located in `tests/unit_tests/common/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/common/test_events.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.269762Z*
