# Documentation: `tests/mem_leak_tests/tracemalloc_orderbook_delta.py`
**Generated:** 2025-11-15T19:40:08.029266Z
**File Size:** 1549 bytes
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

- **Path:** `tests/mem_leak_tests/tracemalloc_orderbook_delta.py`
- **Size:** 1,549 bytes
- **Lines:** 37
- **Extension:** `.py`
- **Type:** text
- **Imports:** 4
- **Functions:** 2

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

from nautilus_trader.model.data import OrderBookDelta
from nautilus_trader.test_kit.rust.data_pyo3 import TestDataProviderPyo3
from nautilus_trader.test_kit.stubs.data import TestDataStubs
from tests.mem_leak_tests.conftest import snapshot_memory


@snapshot_memory(4000)
def run_repr(*args, **kwargs):
    delta = TestDataStubs.order_book_delta()
    repr(delta)  # Copies bids and asks book order data from Rust on every iteration


@snapshot_memory(4000)
def run_from_pyo3(*args, **kwargs):
    pyo3_delta = TestDataProviderPyo3.order_book_delta()
    OrderBookDelta.from_pyo3(pyo3_delta)


if __name__ == "__main__":
    run_repr()
    run_from_pyo3()
```


---

## Overview

This file is located at `tests/mem_leak_tests/tracemalloc_orderbook_delta.py` within the repository.

**Functions defined:** run_repr, run_from_pyo3

**Import statements:** 4


---

## Detailed Analysis

### Functions

#### `run_repr(*args, **kwargs)`


#### `run_from_pyo3(*args, **kwargs)`


### Imports

- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.test_kit.rust.data_pyo3 import TestDataProviderPyo3`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from tests.mem_leak_tests.conftest import snapshot_memory`


---

## Usage Examples

### Importing

```python
from tests.mem_leak_tests.tracemalloc_orderbook_delta import run_repr
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.data import OrderBookDelta`
- `from nautilus_trader.test_kit.rust.data_pyo3 import TestDataProviderPyo3`
- `from nautilus_trader.test_kit.stubs.data import TestDataStubs`
- `from tests.mem_leak_tests.conftest import snapshot_memory`

**Directory:** `tests/mem_leak_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


