# Documentation: `tests/performance_tests/test_perf_stats.py`
**Generated:** 2025-11-15T19:40:08.055935Z
**File Size:** 1386 bytes
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

- **Path:** `tests/performance_tests/test_perf_stats.py`
- **Size:** 1,386 bytes
- **Lines:** 38
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
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

import numpy as np

from nautilus_trader.core.stats import fast_mean
from nautilus_trader.core.stats import fast_std


def test_np_mean(benchmark):
    benchmark(
        np.mean,
        np.random.default_rng(10).random(100),
    )


def test_np_std(benchmark):
    benchmark(np.std, np.random.default_rng(10).random(100))


def test_fast_mean(benchmark):
    benchmark(fast_mean, np.random.default_rng(10).random(100))


def test_fast_std(benchmark):
    benchmark(fast_std, np.random.default_rng(10).random(100))
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_stats.py` within the repository.

**Functions defined:** test_np_mean, test_np_std, test_fast_mean, test_fast_std

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_np_mean(benchmark)`


#### `test_np_std(benchmark)`


#### `test_fast_mean(benchmark)`


#### `test_fast_std(benchmark)`


### Imports

- `import numpy as np`
- `from nautilus_trader.core.stats import fast_mean`
- `from nautilus_trader.core.stats import fast_std`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_stats import test_np_mean
```


---

## Related Files

This file imports from the following modules:

- `import numpy as np`
- `from nautilus_trader.core.stats import fast_mean`
- `from nautilus_trader.core.stats import fast_std`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


