# Documentation: `tests/unit_tests/model/objects/test_state_pyo3.py`
**Generated:** 2025-11-15T19:40:09.303079Z
**File Size:** 3053 bytes
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

- **Path:** `tests/unit_tests/model/objects/test_state_pyo3.py`
- **Size:** 3,053 bytes
- **Lines:** 84
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Functions:** 2

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

from nautilus_trader.core.nautilus_pyo3 import AccountState
from nautilus_trader.test_kit.rust.events_pyo3 import TestEventsProviderPyo3


################################################################################
# Account state
################################################################################


def test_cash_account_state():
    cash_account_state = TestEventsProviderPyo3.cash_account_state()
    result_dict = cash_account_state.to_dict()
    assert cash_account_state == AccountState.from_dict(result_dict)
    assert result_dict == {
        "type": "AccountState",
        "account_id": "SIM-000",
        "account_type": "CASH",
        "base_currency": "USD",
        "balances": [
            {
                "type": "AccountBalance",
                "free": "1500000.00",
                "locked": "25000.00",
                "total": "1525000.00",
                "currency": "USD",
            },
        ],
        "event_id": "91762096-b188-49ea-8562-8d8a4cc22ff2",
        "margins": [],
        "reported": True,
        "info": {},
        "ts_init": 0,
        "ts_event": 0,
    }


def test_margin_account_state():
    margin_account_state = TestEventsProviderPyo3.margin_account_state()
    result_dict = margin_account_state.to_dict()
    assert margin_account_state == AccountState.from_dict(result_dict)
    assert result_dict == {
        "type": "AccountState",
        "account_id": "SIM-000",
        "account_type": "MARGIN",
        "base_currency": "USD",
        "balances": [
            {
                "type": "AccountBalance",
                "free": "1500000.00",
                "locked": "25000.00",
                "total": "1525000.00",
                "currency": "USD",
            },
        ],
        "margins": [
            {
                "type": "MarginBalance",
                "instrument_id": "AUD/USD.SIM",
                "initial": "1.00",
                "maintenance": "1.00",
                "currency": "USD",
            },
        ],
        "event_id": "91762096-b188-49ea-8562-8d8a4cc22ff2",
        "reported": True,
        "info": {},
        "ts_init": 0,
        "ts_event": 0,
    }
```


---

## Overview

This file is located at `tests/unit_tests/model/objects/test_state_pyo3.py` within the repository.

**Functions defined:** test_cash_account_state, test_margin_account_state

**Import statements:** 2


---

## Detailed Analysis

### Functions

#### `test_cash_account_state()`


#### `test_margin_account_state()`


### Imports

- `from nautilus_trader.core.nautilus_pyo3 import AccountState`
- `from nautilus_trader.test_kit.rust.events_pyo3 import TestEventsProviderPyo3`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.objects.test_state_pyo3 import test_cash_account_state
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.nautilus_pyo3 import AccountState`
- `from nautilus_trader.test_kit.rust.events_pyo3 import TestEventsProviderPyo3`

**Directory:** `tests/unit_tests/model/objects`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


