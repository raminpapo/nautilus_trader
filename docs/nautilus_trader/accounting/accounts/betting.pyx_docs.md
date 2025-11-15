# Documentation: `nautilus_trader/accounting/accounts/betting.pyx`
**Generated:** 2025-11-15T19:40:03.985361Z
**File Size:** 4117 bytes
**Extension:** .pyx
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

- **Path:** `nautilus_trader/accounting/accounts/betting.pyx`
- **Size:** 4,117 bytes
- **Lines:** 117
- **Extension:** `.pyx`
- **Type:** text
- **Imports:** 1

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

from decimal import Decimal

from nautilus_trader.accounting.accounts.cash cimport CashAccount
from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.core.rust.model cimport AccountType
from nautilus_trader.core.rust.model cimport OrderSide
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cdef class BettingAccount(CashAccount):
    """
    Provides a betting account.
    """
    ACCOUNT_TYPE = AccountType.BETTING

# -- CALCULATIONS ---------------------------------------------------------------------------------

    cpdef Money calculate_balance_locked(
        self,
        Instrument instrument,
        OrderSide side,
        Quantity quantity,
        Price price,
        bint use_quote_for_inverse=False,
    ):
        """
        Calculate the locked balance.

        Parameters
        ----------
        instrument : Instrument
            The instrument for the calculation.
        side : OrderSide {``BUY``, ``SELL``}
            The order side.
        quantity : Quantity
            The order quantity.
        price : Price
            The order price.
        use_quote_for_inverse : bool
            Not applicable for betting accounts.

        Returns
        -------
        Money

        """
        Condition.not_none(instrument, "instrument")
        Condition.not_none(quantity, "quantity")
        Condition.not_none(price, "price")
        Condition.not_equal(use_quote_for_inverse, True, "use_quote_for_inverse", "True")

        locked: Decimal = liability(quantity, price, side)
        return Money(locked, instrument.quote_currency)

    cpdef Money balance_impact(
        self,
        Instrument instrument,
        Quantity quantity,
        Price price,
        OrderSide order_side,
    ):
        cdef Money notional
        if order_side == OrderSide.SELL:
            notional = instrument.notional_value(quantity, price)
            return Money(-notional.as_f64_c(), notional.currency)
        elif order_side == OrderSide.BUY:
            notional = instrument.notional_value(quantity, price)
            return Money(-notional.as_f64_c() * (price.as_f64_c() - 1.0), notional.currency)
        else:
            raise RuntimeError(f"invalid `OrderSide`, was {order_side}")  # pragma: no cover (design-time error)


cpdef stake(Quantity quantity, Price price):
    return quantity * (price - 1)


cpdef liability(Quantity quantity, Price price, OrderSide side):
    if side == OrderSide.SELL:
        return quantity
    elif side == OrderSide.BUY:
        return stake(quantity, price)


cpdef win_payoff(Quantity quantity, Price price, OrderSide side):
    if side == OrderSide.BUY:
        return stake(quantity, price)
    elif side == OrderSide.SELL:
        return -stake(quantity, price)


cpdef lose_payoff(Quantity quantity, OrderSide side):
    if side == OrderSide.BUY:
        return -quantity
    elif side == OrderSide.SELL:
        return quantity


cpdef exposure(Quantity quantity, Price price, OrderSide side):
    return win_payoff(quantity, price, side) - lose_payoff(quantity, side)
```


---

## Overview

This file is located at `nautilus_trader/accounting/accounts/betting.pyx` within the repository.

**Import statements:** 1


---

## Detailed Analysis

### Imports

- `from decimal import Decimal`


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`

**Directory:** `nautilus_trader/accounting/accounts`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


