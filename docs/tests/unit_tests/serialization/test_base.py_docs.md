# Documentation: `tests/unit_tests/serialization/test_base.py`
**Generated:** 2025-11-15T19:40:09.480321Z
**File Size:** 1726 bytes
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

- **Path:** `tests/unit_tests/serialization/test_base.py`
- **Size:** 1,726 bytes
- **Lines:** 49
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Classes:** 2
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

from __future__ import annotations

from nautilus_trader.serialization.base import register_serializable_type


class TestObject:
    """
    Represents some generic user object which implements serialization value dicts.
    """

    __test__ = False  # Prevents pytest from collecting this as a test class

    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_dict(values: dict) -> TestObject:
        return TestObject(values["value"])

    @staticmethod
    def to_dict(obj):
        return {"value": obj.value}


class TestSerializationBase:
    def test_register_serializable_type(self):
        # Arrange, Act, Assert
        register_serializable_type(
            cls=TestObject,
            to_dict=TestObject.to_dict,
            from_dict=TestObject.from_dict,
        )

        # Does not raise exception
```


---

## Overview

This file is located at `tests/unit_tests/serialization/test_base.py` within the repository.

**Classes defined:** TestObject, TestSerializationBase

**Functions defined:** __init__, from_dict, to_dict, test_register_serializable_type

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `TestObject`


#### `TestSerializationBase`


### Functions

#### `__init__(self, value)`


#### `from_dict(values: dict)`


#### `to_dict(obj)`


#### `test_register_serializable_type(self)`


### Imports

- `from __future__ import annotations`
- `from nautilus_trader.serialization.base import register_serializable_type`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.serialization.test_base import TestObject
```


---

## Related Files

This file imports from the following modules:

- `from __future__ import annotations`
- `from nautilus_trader.serialization.base import register_serializable_type`

**Directory:** `tests/unit_tests/serialization`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


