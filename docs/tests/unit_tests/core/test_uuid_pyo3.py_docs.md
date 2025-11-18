# Documentation: test_uuid_pyo3.py

## File Metadata

- **Path**: `tests/unit_tests/core/test_uuid_pyo3.py`
- **Size**: 2,491 bytes
- **Lines**: 70
- **Language**: Python

## Original Source

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

from nautilus_trader.core.nautilus_pyo3 import UUID4


class TestUUID:
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
        uuid3 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c758")

        # Assert
        assert uuid1 == uuid1
        assert uuid1 == uuid2
        assert uuid2 != uuid3

    def test_hash(self):
        # Arrange
        uuid1 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c758")
        uuid2 = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c758")

        # Act, Assert
        assert isinstance((hash(uuid1)), int)
        assert hash(uuid1) == hash(uuid2)

    def test_str_and_repr(self):
        # Arrange
        uuid = UUID4.from_str("2d89666b-1a1e-4a75-b193-4eb3b454c758")

        # Act, Assert
        assert uuid.value == "2d89666b-1a1e-4a75-b193-4eb3b454c758"
        assert str(uuid) == "2d89666b-1a1e-4a75-b193-4eb3b454c758"
        assert repr(uuid) == "UUID4('2d89666b-1a1e-4a75-b193-4eb3b454c758')"

    def test_uuid4_produces_valid_uuid4(self):
        # Arrange, Act
        result = UUID4()

        # Assert
        assert isinstance(result, UUID4)
        assert len(str(result)) == 36
        assert len(str(result).replace("-", "")) == 32

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`TestUUID`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Classs**: `TestUUID`
**Imports**: `nautilus_trader.core.nautilus_pyo3`, `pickle`

## Related Files

This file is located in `tests/unit_tests/core/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/core/test_uuid_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.319737Z*
