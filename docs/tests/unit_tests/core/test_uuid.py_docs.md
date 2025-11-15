# Documentation: `tests/unit_tests/core/test_uuid.py`
**Generated:** 2025-11-15T19:40:09.087434Z
**File Size:** 3088 bytes
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

- **Path:** `tests/unit_tests/core/test_uuid.py`
- **Size:** 3,088 bytes
- **Lines:** 87
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Classes:** 1
- **Functions:** 6

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

import pickle

import pytest

from nautilus_trader.core.uuid import UUID4


class TestUUID:

    @pytest.mark.parametrize(
        ("value"),
        [
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8"  # v1 (time-based)
            "000001f5-8fa9-21d1-9df3-00e098032b8c"  # v2 (DCE Security)
            "3d813cbb-47fb-32ba-91df-831e1593ac29"  # v3 (MD5 hash)
            "fb4f37c1-4ba3-5173-9812-2b90e76a06f7"  # v5 (SHA-1 hash)
            "550e8400-e29b-41d4-0000-446655440000",  # v4 but not RFC 4122
        ],
    )
    def test_invalid_uuid4_values(self, value: str):
        # Arrange, Act, Assert
        with pytest.raises(ValueError):
            UUID4.from_str(value)

    def test_pickling_round_trip(self):
        # Arrange
        uuid = UUID4()

        # Act
        pickled = pickle.dumps(uuid)
        unpickled = pickle.loads(pickled)  # noqa: S301 (pickle safe here)

        # Assert
        assert unpickled == uuid

    def test_equality(self):
        # Arrange, Act
        uuid1 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c757")
        uuid2 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c757")
        uuid3 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c753")

        # Assert
        assert uuid1 == uuid1
        assert uuid1 == uuid2
        assert uuid2 != uuid3

    def test_hash(self):
        # Arrange
        uuid1 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c757")
        uuid2 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c757")

        # Act, Assert
        assert isinstance((hash(uuid1)), int)
        assert hash(uuid1) == hash(uuid2)

    def test_str_and_repr(self):
        # Arrange
        uuid = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c757")

        # Act, Assert
        assert uuid.value == "2d89666b-1a1e-4a75-b193-4eb3b454c757"
        assert str(uuid) == "2d89666b-1a1e-4a75-b193-4eb3b454c757"
        assert repr(uuid) == "UUID4('2d89666b-1a1e-4a75-b193-4eb3b454c757')"

    def test_uuid4_produces_valid_uuid4(self):
        # Arrange, Act
        result = UUID4()

        # Assert
        assert isinstance(result, UUID4)
        assert len(str(result)) == 36
        assert len(str(result).replace("-", "")) == 32
```


---

## Overview

This file is located at `tests/unit_tests/core/test_uuid.py` within the repository.

**Classes defined:** TestUUID

**Functions defined:** test_invalid_uuid4_values, test_pickling_round_trip, test_equality, test_hash, test_str_and_repr, test_uuid4_produces_valid_uuid4

**Import statements:** 3


---

## Detailed Analysis

### Classes

#### `TestUUID`


### Functions

#### `test_invalid_uuid4_values(self, value: str)`


#### `test_pickling_round_trip(self)`


#### `test_equality(self)`


#### `test_hash(self)`


#### `test_str_and_repr(self)`


#### `test_uuid4_produces_valid_uuid4(self)`


### Imports

- `import pickle`
- `import pytest`
- `from nautilus_trader.core.uuid import UUID4`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.core.test_uuid import TestUUID
```


---

## Related Files

This file imports from the following modules:

- `import pickle`
- `import pytest`
- `from nautilus_trader.core.uuid import UUID4`

**Directory:** `tests/unit_tests/core`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


