# Documentation: tracemalloc_quote_ticks.py

## File Metadata

- **Path**: `tests/mem_leak_tests/tracemalloc_quote_ticks.py`
- **Size**: 1,458 bytes
- **Lines**: 38
- **Language**: Python

## Original Source

```python
#!/usr/bin/env python3
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

from nautilus_trader.model.data import QuoteTick
from nautilus_trader.test_kit.rust.data_pyo3 import TestDataProviderPyo3
from nautilus_trader.test_kit.stubs.data import TestDataStubs
from tests.mem_leak_tests.conftest import snapshot_memory


@snapshot_memory(4000)
def run_repr(*args, **kwargs):
    quote = TestDataStubs.quote_tick()
    repr(quote)


@snapshot_memory(4000)
def run_from_pyo3(*args, **kwargs):
    pyo3_quote = TestDataProviderPyo3.quote_tick()
    QuoteTick.from_pyo3(pyo3_quote)


if __name__ == "__main__":
    run_repr()
    run_from_pyo3()

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`run_repr()`**: Function defined in this file
- **`run_from_pyo3()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `run_from_pyo3`, `run_repr`
**Imports**: `nautilus_trader.model.data`, `nautilus_trader.test_kit.rust.data_pyo3`, `nautilus_trader.test_kit.stubs.data`, `tests.mem_leak_tests.conftest`

## Related Files

This file is located in `tests/mem_leak_tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/mem_leak_tests/tracemalloc_quote_ticks.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.280278Z*
