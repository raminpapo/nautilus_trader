# Documentation: `tests/unit_tests/core/test_data.py`
**Generated:** 2025-11-15T19:40:09.076953Z
**File Size:** 1137 bytes
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

- **Path:** `tests/unit_tests/core/test_data.py`
- **Size:** 1,137 bytes
- **Lines:** 25
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
- **Classes:** 1
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

from nautilus_trader.core.data import Data


class TestCoreData:
    def test_fully_qualified_name_returns_expected(self):
        # Arrange, Act
        result = Data.fully_qualified_name()

        # Assert
        assert result == "nautilus_trader.core.data:Data"
```


---

## Overview

This file is located at `tests/unit_tests/core/test_data.py` within the repository.

**Classes defined:** TestCoreData

**Functions defined:** test_fully_qualified_name_returns_expected

**Import statements:** 1


---

## Detailed Analysis

### Classes

#### `TestCoreData`


### Functions

#### `test_fully_qualified_name_returns_expected(self)`


### Imports

- `from nautilus_trader.core.data import Data`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.core.test_data import TestCoreData
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.data import Data`

**Directory:** `tests/unit_tests/core`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


