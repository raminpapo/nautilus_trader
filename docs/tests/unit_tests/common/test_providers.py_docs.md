# Documentation: `tests/unit_tests/common/test_providers.py`
**Generated:** 2025-11-15T19:40:09.061860Z
**File Size:** 1510 bytes
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

- **Path:** `tests/unit_tests/common/test_providers.py`
- **Size:** 1,510 bytes
- **Lines:** 40
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Classes:** 1
- **Functions:** 3

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

from nautilus_trader.common.providers import InstrumentProvider
from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs


AUDUSD = TestIdStubs.audusd_id()


class TestInstrumentProvider:
    def setup(self):
        # Fixture Setup
        self.provider = InstrumentProvider()

    def test_get_all_when_no_instruments_returns_empty_dict(self):
        # Arrange, Act
        result = self.provider.get_all()

        # Assert
        assert result == {}

    def test_find_when_no_instruments_returns_none(self):
        # Arrange, Act
        result = self.provider.find(AUDUSD)

        # Assert
        assert result is None
```


---

## Overview

This file is located at `tests/unit_tests/common/test_providers.py` within the repository.

**Classes defined:** TestInstrumentProvider

**Functions defined:** setup, test_get_all_when_no_instruments_returns_empty_dict, test_find_when_no_instruments_returns_none

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `TestInstrumentProvider`


### Functions

#### `setup(self)`


#### `test_get_all_when_no_instruments_returns_empty_dict(self)`


#### `test_find_when_no_instruments_returns_none(self)`


### Imports

- `from nautilus_trader.common.providers import InstrumentProvider`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.common.test_providers import TestInstrumentProvider
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.common.providers import InstrumentProvider`
- `from nautilus_trader.test_kit.stubs.identifiers import TestIdStubs`

**Directory:** `tests/unit_tests/common`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


