# Documentation: `tests/mem_leak_tests/tracemalloc_orderbook_deltas.py`
**Generated:** 2025-11-15T19:40:08.030392Z
**File Size:** 1807 bytes
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

- **Path:** `tests/mem_leak_tests/tracemalloc_orderbook_deltas.py`
- **Size:** 1,807 bytes
- **Lines:** 48
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Functions:** 1

---

## Source Code

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


---

## Overview

This file is located at `tests/mem_leak_tests/tracemalloc_orderbook_deltas.py` within the repository.

**Functions defined:** run_comprehensive

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `run_comprehensive(*args, **kwargs)`


### Imports

- `from nautilus_trader.model.data import OrderBookDeltas`
- `from nautilus_trader.model.data import capsule_to_data`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from tests.mem_leak_tests.conftest import snapshot_memory`


---

## Usage Examples

### Importing

```python
from tests.mem_leak_tests.tracemalloc_orderbook_deltas import run_comprehensive
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.data import OrderBookDeltas`
- `from nautilus_trader.model.data import capsule_to_data`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from tests.mem_leak_tests.conftest import snapshot_memory`

**Directory:** `tests/mem_leak_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


