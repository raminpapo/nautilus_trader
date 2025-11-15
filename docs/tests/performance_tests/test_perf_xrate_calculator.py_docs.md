# Documentation: `tests/performance_tests/test_perf_xrate_calculator.py`
**Generated:** 2025-11-15T19:40:08.060317Z
**File Size:** 1447 bytes
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

- **Path:** `tests/performance_tests/test_perf_xrate_calculator.py`
- **Size:** 1,447 bytes
- **Lines:** 41
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 1

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

from nautilus_trader.core import nautilus_pyo3
from nautilus_trader.model.currencies import ETH
from nautilus_trader.model.currencies import USDT


def test_get_rate(benchmark):
    bid_quotes = {
        "BTC/USD": 11291.38,
        "ETH/USDT": 371.90,
        "XBT/USD": 11285.50,
    }

    ask_quotes = {
        "BTC/USD": 11292.58,
        "ETH/USDT": 372.11,
        "XBT/USD": 11286.0,
    }

    benchmark(
        nautilus_pyo3.get_exchange_rate,
        ETH.code,
        USDT.code,
        nautilus_pyo3.PriceType.MID,
        bid_quotes,
        ask_quotes,
    )
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_xrate_calculator.py` within the repository.

**Functions defined:** test_get_rate

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_get_rate(benchmark)`


### Imports

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.currencies import ETH`
- `from nautilus_trader.model.currencies import USDT`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_xrate_calculator import test_get_rate
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core import nautilus_pyo3`
- `from nautilus_trader.model.currencies import ETH`
- `from nautilus_trader.model.currencies import USDT`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


