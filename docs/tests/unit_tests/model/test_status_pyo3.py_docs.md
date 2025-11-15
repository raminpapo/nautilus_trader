# Documentation: `tests/unit_tests/model/test_status_pyo3.py`
**Generated:** 2025-11-15T19:40:09.394759Z
**File Size:** 1624 bytes
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

- **Path:** `tests/unit_tests/model/test_status_pyo3.py`
- **Size:** 1,624 bytes
- **Lines:** 37
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

from nautilus_trader.core.nautilus_pyo3 import InstrumentId
from nautilus_trader.core.nautilus_pyo3 import InstrumentStatus
from nautilus_trader.core.nautilus_pyo3 import MarketStatusAction


def test_instrument_status():
    # Arrange
    update = InstrumentStatus(
        instrument_id=InstrumentId.from_str("MSFT.XNAS"),
        action=MarketStatusAction.TRADING,
        ts_event=0,
        ts_init=0,
        reason=None,
        trading_event=None,
        is_trading=True,
        is_quoting=True,
        is_short_sell_restricted=False,
    )

    # Act, Assert
    assert InstrumentStatus.from_dict(InstrumentStatus.to_dict(update)) == update
    assert repr(update) == "InstrumentStatus(MSFT.XNAS,TRADING,0,0)"  # TODO: Improve repr from Rust
```


---

## Overview

This file is located at `tests/unit_tests/model/test_status_pyo3.py` within the repository.

**Functions defined:** test_instrument_status

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_instrument_status()`


### Imports

- `from nautilus_trader.core.nautilus_pyo3 import InstrumentId`
- `from nautilus_trader.core.nautilus_pyo3 import InstrumentStatus`
- `from nautilus_trader.core.nautilus_pyo3 import MarketStatusAction`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.test_status_pyo3 import test_instrument_status
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.nautilus_pyo3 import InstrumentId`
- `from nautilus_trader.core.nautilus_pyo3 import InstrumentStatus`
- `from nautilus_trader.core.nautilus_pyo3 import MarketStatusAction`

**Directory:** `tests/unit_tests/model`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


