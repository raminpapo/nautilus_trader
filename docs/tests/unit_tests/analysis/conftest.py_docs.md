# Documentation: `tests/unit_tests/analysis/conftest.py`
**Generated:** 2025-11-15T19:40:08.904268Z
**File Size:** 1521 bytes
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

- **Path:** `tests/unit_tests/analysis/conftest.py`
- **Size:** 1,521 bytes
- **Lines:** 34
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
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

import pandas as pd


def convert_series_to_dict(series: pd.Series) -> dict[int, float]:
    """
    Convert pandas Series to dict with unix nanoseconds (or integer keys).
    """
    if series.empty:
        return {}
    result = {}
    for idx, val in series.items():
        # Check if index is datetime (has .value attribute for nanoseconds)
        if hasattr(idx, "value"):
            key = idx.value  # Direct nanosecond value, no float precision loss
        else:
            # Use integer index directly (convert to nanoseconds for consistency)
            key = int(idx) * 1_000_000_000
        result[key] = float(val)
    return result
```


---

## Overview

This file is located at `tests/unit_tests/analysis/conftest.py` within the repository.

**Functions defined:** convert_series_to_dict

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `convert_series_to_dict(series: pd.Series)`


### Imports

- `import pandas as pd`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.analysis.conftest import convert_series_to_dict
```


---

## Related Files

This file imports from the following modules:

- `import pandas as pd`

**Directory:** `tests/unit_tests/analysis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


