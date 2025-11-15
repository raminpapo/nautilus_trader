# Documentation: `tests/performance_tests/test_perf_identifiers.py`
**Generated:** 2025-11-15T19:40:08.044681Z
**File Size:** 1304 bytes
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

- **Path:** `tests/performance_tests/test_perf_identifiers.py`
- **Size:** 1,304 bytes
- **Lines:** 35
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 4

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

from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import Venue


def test_symbol_equality(benchmark):
    symbol = Symbol("AUD/USD")

    def symbol_equality() -> bool:
        return symbol == symbol

    benchmark(symbol_equality)


def test_venue_equality(benchmark):
    venue = Venue("SIM")

    def venue_equality() -> bool:
        return venue == venue

    benchmark(venue_equality)
```


---

## Overview

This file is located at `tests/performance_tests/test_perf_identifiers.py` within the repository.

**Functions defined:** test_symbol_equality, symbol_equality, test_venue_equality, venue_equality

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `test_symbol_equality(benchmark)`


#### `symbol_equality()`


#### `test_venue_equality(benchmark)`


#### `venue_equality()`


### Imports

- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import Venue`


---

## Usage Examples

### Importing

```python
from tests.performance_tests.test_perf_identifiers import test_symbol_equality
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.model.identifiers import Symbol`
- `from nautilus_trader.model.identifiers import Venue`

**Directory:** `tests/performance_tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


