# Documentation: `tests/performance_tests/test_perf_uuid.py`
**Generated:** 2025-11-15T19:40:08.058217Z
**File Size:** 1290 bytes
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

- **Path:** `tests/performance_tests/test_perf_uuid.py`
- **Size:** 1,290 bytes
- **Lines:** 39
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 4

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

import uuid

from nautilus_trader.core.uuid import UUID4


def test_make_builtin_uuid(benchmark):
    benchmark(uuid.uuid4)


def test_make_nautilus_uuid(benchmark):
    benchmark(UUID4)


def test_nautilus_uuid_value(benchmark):
    uuid = UUID4()

    benchmark(lambda: uuid.value)


def test_nautilus_uuid_from_value(benchmark):
    uuid = UUID4()
    value = uuid.value

    benchmark(lambda: UUID4.from_str(value))
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_uuid.py` within the repository.

**Functions defined:** test_make_builtin_uuid, test_make_nautilus_uuid, test_nautilus_uuid_value, test_nautilus_uuid_from_value

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `test_make_builtin_uuid(benchmark)`


#### `test_make_nautilus_uuid(benchmark)`


#### `test_nautilus_uuid_value(benchmark)`


#### `test_nautilus_uuid_from_value(benchmark)`


### Imports

- `import uuid`
- `from nautilus_trader.core.uuid import UUID4`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_uuid import test_make_builtin_uuid
```


---

## Related Files

This file imports from the following modules:

- `import uuid`
- `from nautilus_trader.core.uuid import UUID4`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


