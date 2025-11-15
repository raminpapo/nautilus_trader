# Documentation: `tests/performance_tests/test_perf_fill_model.py`
**Generated:** 2025-11-15T19:40:08.043640Z
**File Size:** 1191 bytes
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

- **Path:** `tests/performance_tests/test_perf_fill_model.py`
- **Size:** 1,191 bytes
- **Lines:** 31
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
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

from nautilus_trader.backtest.models import FillModel


_FILL_MODEL = FillModel(
    prob_fill_on_stop=0.95,
    prob_fill_on_limit=0.5,
    random_seed=42,
)


def test_is_limit_filled(benchmark):
    benchmark(_FILL_MODEL.is_limit_filled)


def test_is_stop_filled(benchmark):
    benchmark(_FILL_MODEL.is_stop_filled)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_fill_model.py` within the repository.

**Functions defined:** test_is_limit_filled, test_is_stop_filled

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `test_is_limit_filled(benchmark)`


#### `test_is_stop_filled(benchmark)`


### Imports

- `from nautilus_trader.backtest.models import FillModel`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_fill_model import test_is_limit_filled
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.backtest.models import FillModel`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


