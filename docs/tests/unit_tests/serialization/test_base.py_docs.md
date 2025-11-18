# Documentation: test_base.py

## File Metadata

- **Path**: `tests/unit_tests/serialization/test_base.py`
- **Size**: 1,726 bytes
- **Lines**: 50
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

## High-Level Overview

This file is part of the NautilusTrader repository. 2 class(es).

## Detailed Walkthrough


### Classes
- **`TestObject`**: Class defined in this file
- **`TestSerializationBase`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Classs**: `TestObject`, `TestSerializationBase`
**Imports**: `__future__`, `nautilus_trader.serialization.base`

## Related Files

This file is located in `tests/unit_tests/serialization/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/serialization/test_base.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.765396Z*
