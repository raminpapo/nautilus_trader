# Documentation: `tests/__init__.py`
**Generated:** 2025-11-15T19:40:05.534064Z
**File Size:** 1104 bytes
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

- **Path:** `tests/__init__.py`
- **Size:** 1,104 bytes
- **Lines:** 24
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1

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
"""
The test suite for NautilusTrader including unit, integration, acceptance and
performance tests.
"""

from pathlib import Path


TESTS_PACKAGE_ROOT = Path(__file__).parent.resolve()
TEST_DATA_DIR = TESTS_PACKAGE_ROOT / "test_data"
```


---

## Overview

This file is located at `tests/__init__.py` within the repository.

This is a Python package initialization file that may expose package contents or execute initialization code.

**Import statements:** 1


---

## Detailed Analysis

### Imports

- `from pathlib import Path`


---

## Usage Examples

### Importing

```python
import tests.__init__
```


---

## Related Files

This file imports from the following modules:

- `from pathlib import Path`

**Directory:** `tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


