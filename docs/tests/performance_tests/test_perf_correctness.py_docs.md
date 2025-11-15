# Documentation: `tests/performance_tests/test_perf_correctness.py`
**Generated:** 2025-11-15T19:40:08.041479Z
**File Size:** 1335 bytes
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

- **Path:** `tests/performance_tests/test_perf_correctness.py`
- **Size:** 1,335 bytes
- **Lines:** 32
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
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

from nautilus_trader.core.correctness import PyCondition


def test_condition_none(benchmark):
    benchmark(PyCondition.none, None, "param")


def test_condition_true(benchmark):
    benchmark(PyCondition.is_true, True, "this should be true")


def test_condition_valid_string(benchmark):
    benchmark(PyCondition.valid_string, "abc123", "string_param")


def test_condition_type_or_none(benchmark):
    benchmark(PyCondition.type_or_none, "hello", str, "world")
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_correctness.py` within the repository.

**Functions defined:** test_condition_none, test_condition_true, test_condition_valid_string, test_condition_type_or_none

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `test_condition_none(benchmark)`


#### `test_condition_true(benchmark)`


#### `test_condition_valid_string(benchmark)`


#### `test_condition_type_or_none(benchmark)`


### Imports

- `from nautilus_trader.core.correctness import PyCondition`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_correctness import test_condition_none
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.correctness import PyCondition`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


