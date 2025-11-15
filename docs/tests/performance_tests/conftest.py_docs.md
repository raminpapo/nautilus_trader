# Documentation: `tests/performance_tests/conftest.py`
**Generated:** 2025-11-15T19:40:08.035662Z
**File Size:** 1016 bytes
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

- **Path:** `tests/performance_tests/conftest.py`
- **Size:** 1,016 bytes
- **Lines:** 23
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 1

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

import pytest

from nautilus_trader.common.component import LiveClock


@pytest.fixture(name="clock")
def fixture_clock():
    return LiveClock()
```


---

## Overview

This file is located at `tests/performance_tests/conftest.py` within the repository.

**Functions defined:** fixture_clock

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `fixture_clock()`


### Imports

- `import pytest`
- `from nautilus_trader.common.component import LiveClock`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.conftest import fixture_clock
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.common.component import LiveClock`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


