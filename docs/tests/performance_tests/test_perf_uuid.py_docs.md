# Documentation: test_perf_uuid.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_uuid.py`
- **Size**: 1,290 bytes
- **Lines**: 40
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

import uuid

from nautilus_trader.core.uuid import UUID4


def test_make_builtin_uuid(benchmark):
    benchmark(uuid.uuid4)


def test_make_nautilus_uuid(benchmark):
    benchmark(UUID4)


def test_nautilus_uuid_value(benchmark):
    uuid = UUID4()

    benchmark(lambda: uuid.value)


def test_nautilus_uuid_from_value(benchmark):
    uuid = UUID4()
    value = uuid.value

    benchmark(lambda: UUID4.from_str(value))

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`test_make_builtin_uuid()`**: Function defined in this file
- **`test_make_nautilus_uuid()`**: Function defined in this file
- **`test_nautilus_uuid_value()`**: Function defined in this file
- **`test_nautilus_uuid_from_value()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `test_make_builtin_uuid`, `test_make_nautilus_uuid`, `test_nautilus_uuid_from_value`, `test_nautilus_uuid_value`
**Imports**: `nautilus_trader.core.uuid`, `uuid`

## Related Files

This file is located in `tests/performance_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/performance_tests/test_perf_uuid.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.322631Z*
