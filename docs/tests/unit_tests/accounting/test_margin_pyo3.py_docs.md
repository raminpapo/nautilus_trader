# Documentation: `tests/unit_tests/accounting/test_margin_pyo3.py`
**Generated:** 2025-11-15T19:40:08.902042Z
**File Size:** 6108 bytes
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

- **Path:** `tests/unit_tests/accounting/test_margin_pyo3.py`
- **Size:** 6,108 bytes
- **Lines:** 177
- **Extension:** `.py`
- **Type:** text
- **Imports:** 11
- **Functions:** 13

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

import pytest

from nautilus_trader.accounting.accounts.margin import MarginAccount
from nautilus_trader.core.nautilus_pyo3 import AccountId
from nautilus_trader.core.nautilus_pyo3 import Currency
from nautilus_trader.core.nautilus_pyo3 import Money
from nautilus_trader.core.nautilus_pyo3 import Price
from nautilus_trader.core.nautilus_pyo3 import Quantity
from nautilus_trader.core.nautilus_pyo3 import margin_account_from_account_events
from nautilus_trader.test_kit.rust.accounting_pyo3 import TestAccountingProviderPyo3
from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3
from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3


AUDUSD_SIM = TestIdProviderPyo3.audusd_id()
USD = Currency.from_str("USD")
BTC = Currency.from_str("BTC")


def test_instantiated_account_basic_properties():
    account = TestAccountingProviderPyo3.margin_account()

    assert account.id == AccountId("SIM-000")
    assert str(account) == "MarginAccount(id=SIM-000, type=MARGIN, base=USD)"
    assert repr(account) == "MarginAccount(id=SIM-000, type=MARGIN, base=USD)"
    assert account == account
    assert account.default_leverage == 1.0


def test_set_default_leverage():
    account = TestAccountingProviderPyo3.margin_account()

    account.set_default_leverage(100.0)

    assert account.default_leverage == 100.0
    assert account.leverages() == {}


def test_set_leverage():
    account = TestAccountingProviderPyo3.margin_account()

    account.set_leverage(AUDUSD_SIM, 100.0)

    assert account.leverage(AUDUSD_SIM) == 100.0
    assert account.leverages() == {AUDUSD_SIM: 100.0}


def test_is_unleveraged_with_leverage_returns_false():
    account = TestAccountingProviderPyo3.margin_account()

    account.set_leverage(AUDUSD_SIM, 100.0)

    assert not account.is_unleveraged(AUDUSD_SIM)


def test_is_unleveraged_with_no_leverage_returns_true():
    account = TestAccountingProviderPyo3.margin_account()

    account.set_leverage(AUDUSD_SIM, 1.0)

    assert account.is_unleveraged(AUDUSD_SIM)


def test_is_unleveraged_with_default_leverage_of_1_returns_true():
    account = TestAccountingProviderPyo3.margin_account()

    assert account.is_unleveraged(AUDUSD_SIM)


def test_update_initial_margin():
    account = TestAccountingProviderPyo3.margin_account()
    margin = Money(1_000.00, USD)

    account.update_initial_margin(AUDUSD_SIM, margin)

    assert account.initial_margin(AUDUSD_SIM) == margin
    assert account.initial_margins() == {AUDUSD_SIM: margin}


def test_update_maintenance_margin():
    account = TestAccountingProviderPyo3.margin_account()
    margin = Money(1_000.00, USD)

    account.update_maintenance_margin(AUDUSD_SIM, margin)

    assert account.maintenance_margin(AUDUSD_SIM) == margin
    assert account.maintenance_margins() == {AUDUSD_SIM: margin}


def test_calculate_initial_margin_with_leverage():
    account = TestAccountingProviderPyo3.margin_account()
    instrument = TestInstrumentProviderPyo3.default_fx_ccy("AUD/USD")
    account.set_leverage(instrument.id, 50.0)

    result = account.calculate_initial_margin(
        instrument=instrument,
        quantity=Quantity.from_int(100_000),
        price=Price.from_str("0.80000"),
    )

    assert result == Money(48.00, USD)


def test_calculate_initial_margin_with_default_leverage():
    account = TestAccountingProviderPyo3.margin_account()
    instrument = TestInstrumentProviderPyo3.default_fx_ccy("AUD/USD")
    account.set_default_leverage(10.0)

    result = account.calculate_initial_margin(
        instrument=instrument,
        quantity=Quantity.from_int(100_000),
        price=Price.from_str("0.80000"),
    )

    assert result == Money(240.00, USD)


@pytest.mark.parametrize(
    ("use_quote_for_inverse", "expected"),
    [
        [False, Money(0.08700494, BTC)],
        [True, Money(1000.00, USD)],
    ],
)
def test_calculate_initial_margin_with_no_leverage_for_inverse(
    use_quote_for_inverse,
    expected,
):
    account = TestAccountingProviderPyo3.margin_account()
    instrument = TestInstrumentProviderPyo3.xbtusd_bitmex()

    result = account.calculate_initial_margin(
        instrument=instrument,
        quantity=Quantity.from_int(100_000),
        price=Price.from_str("11493.60"),
        use_quote_for_inverse=use_quote_for_inverse,
    )
    assert result == expected


def test_calculate_maintenance_margin_with_no_leverage():
    account = TestAccountingProviderPyo3.margin_account()
    instrument = TestInstrumentProviderPyo3.xbtusd_bitmex()

    result = account.calculate_maintenance_margin(
        instrument=instrument,
        quantity=Quantity.from_int(100_000),
        price=Price.from_str("11493.60"),
    )

    assert result == Money(0.03045173, BTC)


def test_pyo3_cython_conversion():
    account_pyo3 = TestAccountingProviderPyo3.margin_account()
    account_cython = MarginAccount.from_dict(account_pyo3.to_dict())
    account_cython_dict = MarginAccount.to_dict(account_cython)
    account_pyo3_back = margin_account_from_account_events(
        events=account_cython_dict["events"],
        calculate_account_state=account_cython_dict["calculate_account_state"],
    )
    assert account_pyo3 == account_pyo3_back
```


---

## Overview

This file is located at `tests/unit_tests/accounting/test_margin_pyo3.py` within the repository.

**Functions defined:** test_instantiated_account_basic_properties, test_set_default_leverage, test_set_leverage, test_is_unleveraged_with_leverage_returns_false, test_is_unleveraged_with_no_leverage_returns_true, test_is_unleveraged_with_default_leverage_of_1_returns_true, test_update_initial_margin, test_update_maintenance_margin, test_calculate_initial_margin_with_leverage, test_calculate_initial_margin_with_default_leverage and 3 more

**Import statements:** 11


---

## Detailed Analysis

### Functions

#### `test_instantiated_account_basic_properties()`


#### `test_set_default_leverage()`


#### `test_set_leverage()`


#### `test_is_unleveraged_with_leverage_returns_false()`


#### `test_is_unleveraged_with_no_leverage_returns_true()`


#### `test_is_unleveraged_with_default_leverage_of_1_returns_true()`


#### `test_update_initial_margin()`


#### `test_update_maintenance_margin()`


#### `test_calculate_initial_margin_with_leverage()`


#### `test_calculate_initial_margin_with_default_leverage()`


#### `test_calculate_initial_margin_with_no_leverage_for_inverse(
    use_quote_for_inverse,
    expected,
)`


#### `test_calculate_maintenance_margin_with_no_leverage()`


#### `test_pyo3_cython_conversion()`


### Imports

- `import pytest`
- `from nautilus_trader.accounting.accounts.margin import MarginAccount`
- `from nautilus_trader.core.nautilus_pyo3 import AccountId`
- `from nautilus_trader.core.nautilus_pyo3 import Currency`
- `from nautilus_trader.core.nautilus_pyo3 import Money`
- `from nautilus_trader.core.nautilus_pyo3 import Price`
- `from nautilus_trader.core.nautilus_pyo3 import Quantity`
- `from nautilus_trader.core.nautilus_pyo3 import margin_account_from_account_events`
- `from nautilus_trader.test_kit.rust.accounting_pyo3 import TestAccountingProviderPyo3`
- `from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3`
- `from nautilus_trader.test_kit.rust.instruments_pyo3 import TestInstrumentProviderPyo3`


---

## Usage Examples

### Importing

```python
from tests.unit_tests.accounting.test_margin_pyo3 import test_instantiated_account_basic_properties
```


---

## Related Files

This file imports from the following modules:

- `import pytest`
- `from nautilus_trader.accounting.accounts.margin import MarginAccount`
- `from nautilus_trader.core.nautilus_pyo3 import AccountId`
- `from nautilus_trader.core.nautilus_pyo3 import Currency`
- `from nautilus_trader.core.nautilus_pyo3 import Money`
- `from nautilus_trader.core.nautilus_pyo3 import Price`
- `from nautilus_trader.core.nautilus_pyo3 import Quantity`
- `from nautilus_trader.core.nautilus_pyo3 import margin_account_from_account_events`
- `from nautilus_trader.test_kit.rust.accounting_pyo3 import TestAccountingProviderPyo3`
- `from nautilus_trader.test_kit.rust.identifiers_pyo3 import TestIdProviderPyo3`

*... and 1 more*

**Directory:** `tests/unit_tests/accounting`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


