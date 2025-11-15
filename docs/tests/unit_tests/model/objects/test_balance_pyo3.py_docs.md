# Documentation: `tests/unit_tests/model/objects/test_balance_pyo3.py`
**Generated:** 2025-11-15T19:40:09.285574Z
**File Size:** 3411 bytes
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

- **Path:** `tests/unit_tests/model/objects/test_balance_pyo3.py`
- **Size:** 3,411 bytes
- **Lines:** 85
- **Extension:** `.py`
- **Type:** text
- **Imports:** 3
- **Functions:** 6

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
from nautilus_trader.core.nautilus_pyo3 import AccountBalance
from nautilus_trader.core.nautilus_pyo3 import MarginBalance
from nautilus_trader.test_kit.rust.types_pyo3 import TestTypesProviderPyo3


################################################################################
# Account balance
################################################################################
def test_account_balance_equality():
    account_balance1 = TestTypesProviderPyo3.account_balance()
    account_balance2 = TestTypesProviderPyo3.account_balance()
    assert account_balance1 == account_balance2


def test_account_balance_display():
    account_balance = TestTypesProviderPyo3.account_balance()
    assert (
        str(account_balance)
        == "AccountBalance(total=1525000.00 USD, locked=25000.00 USD, free=1500000.00 USD)"
    )
    assert (
        repr(account_balance)
        == "AccountBalance(total=1525000.00 USD, locked=25000.00 USD, free=1500000.00 USD)"
    )


def test_account_balance_to_from_dict():
    account_balance = TestTypesProviderPyo3.account_balance()
    result_dict = account_balance.to_dict()
    assert account_balance == AccountBalance.from_dict(result_dict)
    assert result_dict == {
        "type": "AccountBalance",
        "free": "1500000.00",
        "locked": "25000.00",
        "total": "1525000.00",
        "currency": "USD",
    }


################################################################################
# Margin balance
################################################################################
def test_margin_balance_equality():
    margin_balance1 = TestTypesProviderPyo3.margin_balance()
    margin_balance2 = TestTypesProviderPyo3.margin_balance()
    assert margin_balance1 == margin_balance2


def test_margin_balance_display():
    margin_balance = TestTypesProviderPyo3.margin_balance()
    assert (
        str(margin_balance)
        == "MarginBalance(initial=1.00 USD, maintenance=1.00 USD, instrument_id=AUD/USD.SIM)"
    )
    assert (
        str(margin_balance)
        == "MarginBalance(initial=1.00 USD, maintenance=1.00 USD, instrument_id=AUD/USD.SIM)"
    )


def test_margin_balance_to_from_dict():
    margin_balance = TestTypesProviderPyo3.margin_balance()
    result_dict = margin_balance.to_dict()
    assert margin_balance == MarginBalance.from_dict(result_dict)
    assert result_dict == {
        "type": "MarginBalance",
        "initial": "1.00",
        "maintenance": "1.00",
        "instrument_id": "AUD/USD.SIM",
        "currency": "USD",
    }
```


---

## Overview

This file is located at `tests/unit_tests/model/objects/test_balance_pyo3.py` within the repository.

**Functions defined:** test_account_balance_equality, test_account_balance_display, test_account_balance_to_from_dict, test_margin_balance_equality, test_margin_balance_display, test_margin_balance_to_from_dict

**Import statements:** 3


---

## Detailed Analysis

### Functions

#### `test_account_balance_equality()`


#### `test_account_balance_display()`


#### `test_account_balance_to_from_dict()`


#### `test_margin_balance_equality()`


#### `test_margin_balance_display()`


#### `test_margin_balance_to_from_dict()`


### Imports

- `from nautilus_trader.core.nautilus_pyo3 import AccountBalance`
- `from nautilus_trader.core.nautilus_pyo3 import MarginBalance`
- `from nautilus_trader.test_kit.rust.types_pyo3 import TestTypesProviderPyo3`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.model.objects.test_balance_pyo3 import test_account_balance_equality
```


---

## Related Files

This file imports from the following modules:

- `from nautilus_trader.core.nautilus_pyo3 import AccountBalance`
- `from nautilus_trader.core.nautilus_pyo3 import MarginBalance`
- `from nautilus_trader.test_kit.rust.types_pyo3 import TestTypesProviderPyo3`

**Directory:** `tests/unit_tests/model/objects`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


