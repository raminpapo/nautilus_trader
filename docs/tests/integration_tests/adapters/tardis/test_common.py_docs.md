# Documentation: `tests/integration_tests/adapters/tardis/test_common.py`
**Generated:** 2025-11-15T19:40:07.978156Z
**File Size:** 1216 bytes
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

- **Path:** `tests/integration_tests/adapters/tardis/test_common.py`
- **Size:** 1,216 bytes
- **Lines:** 29
- **Extension:** `.py`
- **Type:** text
- **Imports:** 1
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


def test_normalize_symbol_str() -> None:
    # Arrange, Act
    result = nautilus_pyo3.tardis_normalize_symbol_str(
        symbol="BTCUSDT",
        exchange="binance-futures",
        instrument_type="perpetual",
        is_inverse=False,
    )

    # Assert
    assert result == "BTCUSDT-PERP"
```


---

## Overview

This file is located at `tests/integration_tests/adapters/tardis/test_common.py` within the repository.

**Functions defined:** test_normalize_symbol_str

**Import statements:** 1


---

## Detailed Analysis

### Functions

#### `test_normalize_symbol_str()`


### Imports

- `from nautilus_trader.core import nautilus_pyo3`


---

## Usage Examples

### Importing

```python
from tests.integration_tests.adapters.tardis.test_common import test_normalize_symbol_str
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core import nautilus_pyo3`

**Directory:** `tests/integration_tests/adapters/tardis`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


