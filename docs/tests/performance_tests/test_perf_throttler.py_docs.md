# Documentation: `tests/performance_tests/test_perf_throttler.py`
**Generated:** 2025-11-15T19:40:08.057102Z
**File Size:** 1460 bytes
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

- **Path:** `tests/performance_tests/test_perf_throttler.py`
- **Size:** 1,460 bytes
- **Lines:** 38
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
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

import pandas as pd
import pytest

from nautilus_trader.common.component import LiveClock
from nautilus_trader.common.component import Throttler


def buffering_throttler(name: str, limit: int) -> Throttler:
    handler: list[str] = []
    return Throttler(
        name=name,
        limit=limit,
        interval=pd.Timedelta(seconds=1),
        output_send=handler.append,
        output_drop=None,
        clock=LiveClock(),
    )


@pytest.mark.skip()
def test_send_unlimited(benchmark):
    throttler = buffering_throttler("buffer-1", 10_000)
    benchmark(throttler.send, "MESSAGE")
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_throttler.py` within the repository.

**Functions defined:** buffering_throttler, test_send_unlimited

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `buffering_throttler(name: str, limit: int)`


#### `test_send_unlimited(benchmark)`


### Imports

- `import pandas as pd`
- `import pytest`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import Throttler`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_throttler import buffering_throttler
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`
- `import pytest`
- `from nautilus_trader.common.component import LiveClock`
- `from nautilus_trader.common.component import Throttler`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


