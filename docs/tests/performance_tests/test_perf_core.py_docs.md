# Documentation: test_perf_core.py

## File Metadata

- **Path**: `tests/performance_tests/test_perf_core.py`
- **Size**: 1,545 bytes
- **Lines**: 41
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

import pandas as pd

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.core.datetime import format_iso8601
from nautilus_trader.core.datetime import unix_nanos_to_iso8601


def test_nautilus_convert_to_snake_case(benchmark) -> None:
    benchmark(nautilus_pyo3.convert_to_snake_case, "PascalCase")


def test_unix_nanos_to_iso8601(benchmark) -> None:
    benchmark(lambda: unix_nanos_to_iso8601(0))


def test_format_iso8601(benchmark) -> None:
    dt = pd.Timestamp(0)

    benchmark(lambda: format_iso8601(dt))


def test_format_iso8601_millis(benchmark) -> None:
    dt = pd.Timestamp(0)

    benchmark(lambda: format_iso8601(dt, nanos_precision=False))

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`test_nautilus_convert_to_snake_case()`**: Function defined in this file
- **`test_unix_nanos_to_iso8601()`**: Function defined in this file
- **`test_format_iso8601()`**: Function defined in this file
- **`test_format_iso8601_millis()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `test_format_iso8601`, `test_format_iso8601_millis`, `test_nautilus_convert_to_snake_case`, `test_unix_nanos_to_iso8601`
**Imports**: `nautilus_trader.core`, `nautilus_trader.core.datetime`, `pandas`

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
pytest tests/performance_tests/test_perf_core.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.303182Z*
