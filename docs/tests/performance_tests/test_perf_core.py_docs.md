# Documentation: `tests/performance_tests/test_perf_core.py`
**Generated:** 2025-11-15T19:40:08.040522Z
**File Size:** 1545 bytes
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

- **Path:** `tests/performance_tests/test_perf_core.py`
- **Size:** 1,545 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
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

import pandas as pd

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.core.datetime import format_iso8601
from nautilus_trader.core.datetime import unix_nanos_to_iso8601


def test_nautilus_convert_to_snake_case(benchmark) -> None:
    benchmark(nautilus_pyo3.convert_to_snake_case, "PascalCase")


def test_unix_nanos_to_iso8601(benchmark) -> None:
    benchmark(lambda: unix_nanos_to_iso8601(0))


def test_format_iso8601(benchmark) -> None:
    dt = pd.Timestamp(0)

    benchmark(lambda: format_iso8601(dt))


def test_format_iso8601_millis(benchmark) -> None:
    dt = pd.Timestamp(0)

    benchmark(lambda: format_iso8601(dt, nanos_precision=False))
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_core.py` within the repository.

**Functions defined:** test_nautilus_convert_to_snake_case, test_unix_nanos_to_iso8601, test_format_iso8601, test_format_iso8601_millis

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `test_nautilus_convert_to_snake_case(benchmark)`


#### `test_unix_nanos_to_iso8601(benchmark)`


#### `test_format_iso8601(benchmark)`


#### `test_format_iso8601_millis(benchmark)`


### Imports

- `import pandas as pd`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.datetime import format_iso8601`
- `from nautilus_trader.core.datetime import unix_nanos_to_iso8601`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_core import test_nautilus_convert_to_snake_case
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.core.datetime import format_iso8601`
- `from nautilus_trader.core.datetime import unix_nanos_to_iso8601`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


