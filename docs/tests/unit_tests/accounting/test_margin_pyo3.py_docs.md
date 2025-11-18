# Documentation: test_margin_pyo3.py

## File Metadata

- **Path**: `tests/unit_tests/accounting/test_margin_pyo3.py`
- **Size**: 6,108 bytes
- **Lines**: 178
- **Language**: Python

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 13 function(s).

## Detailed Walkthrough

### Functions
- **`test_instantiated_account_basic_properties()`**: Function defined in this file
- **`test_set_default_leverage()`**: Function defined in this file
- **`test_set_leverage()`**: Function defined in this file
- **`test_is_unleveraged_with_leverage_returns_false()`**: Function defined in this file
- **`test_is_unleveraged_with_no_leverage_returns_true()`**: Function defined in this file
- **`test_is_unleveraged_with_default_leverage_of_1_returns_true()`**: Function defined in this file
- **`test_update_initial_margin()`**: Function defined in this file
- **`test_update_maintenance_margin()`**: Function defined in this file
- **`test_calculate_initial_margin_with_leverage()`**: Function defined in this file
- **`test_calculate_initial_margin_with_default_leverage()`**: Function defined in this file
- **`test_calculate_initial_margin_with_no_leverage_for_inverse()`**: Function defined in this file
- **`test_calculate_maintenance_margin_with_no_leverage()`**: Function defined in this file
- **`test_pyo3_cython_conversion()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 19


**Functions**: `test_calculate_initial_margin_with_default_leverage`, `test_calculate_initial_margin_with_leverage`, `test_calculate_initial_margin_with_no_leverage_for_inverse`, `test_calculate_maintenance_margin_with_no_leverage`, `test_instantiated_account_basic_properties`, `test_is_unleveraged_with_default_leverage_of_1_returns_true`, `test_is_unleveraged_with_leverage_returns_false`, `test_is_unleveraged_with_no_leverage_returns_true`, `test_pyo3_cython_conversion`, `test_set_default_leverage`, `test_set_leverage`, `test_update_initial_margin`, `test_update_maintenance_margin`
**Imports**: `nautilus_trader.accounting.accounts.margin`, `nautilus_trader.core.nautilus_pyo3`, `nautilus_trader.test_kit.rust.accounting_pyo3`, `nautilus_trader.test_kit.rust.identifiers_pyo3`, `nautilus_trader.test_kit.rust.instruments_pyo3`, `pytest`

## Related Files

This file is located in `tests/unit_tests/accounting/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/unit_tests/accounting/test_margin_pyo3.py

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:11.114118Z*
