# Documentation: tracemalloc_orderbook_deltas.py

## File Metadata

- **Path**: `tests/mem_leak_tests/tracemalloc_orderbook_deltas.py`
- **Size**: 1,807 bytes
- **Lines**: 49
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

from nautilus_trader.model.data import OrderBookDeltas
from nautilus_trader.model.data import capsule_to_data
from nautilus_trader.test_kit.stubs.data import TestDataStubs
from tests.mem_leak_tests.conftest import snapshot_memory


@snapshot_memory(4000)
def run_comprehensive(*args, **kwargs):
    # Create the stub Cython objects
    delta = TestDataStubs.order_book_delta()
    deltas = OrderBookDeltas(delta.instrument_id, deltas=[delta] * 1024)

    # Check printing Cython objects doesn't leak
    repr(deltas.deltas)
    repr(deltas)

    # Convert to pyo3 objects
    pyo3_deltas = deltas.to_pyo3()

    # Convert to capsule
    capsule = pyo3_deltas.as_pycapsule()

    # Convert from capsule back to Cython objects
    deltas = capsule_to_data(capsule)

    # Check printing Cython and pyo3 objects doesn't leak
    repr(pyo3_deltas)
    repr(deltas)


if __name__ == "__main__":
    run_comprehensive()

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`run_comprehensive()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `run_comprehensive`
**Imports**: `nautilus_trader.model.data`, `nautilus_trader.test_kit.stubs.data`, `tests.mem_leak_tests.conftest`

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
pytest tests/mem_leak_tests/tracemalloc_orderbook_deltas.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:07.277660Z*
