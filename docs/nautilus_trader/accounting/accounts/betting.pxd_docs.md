# Documentation: betting.pxd

## File Metadata

- **Path**: `nautilus_trader/accounting/accounts/betting.pxd`
- **Size**: 1,740 bytes
- **Lines**: 40
- **Language**: Unknown

## Original Source

```
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

from nautilus_trader.accounting.accounts.cash cimport CashAccount
from nautilus_trader.core.rust.model cimport OrderSide
from nautilus_trader.model.instruments.base cimport Instrument
from nautilus_trader.model.objects cimport Money
from nautilus_trader.model.objects cimport Price
from nautilus_trader.model.objects cimport Quantity


cdef class BettingAccount(CashAccount):
    cpdef Money calculate_balance_locked(
        self,
        Instrument instrument,
        OrderSide side,
        Quantity quantity,
        Price price,
        bint use_quote_for_inverse=*,
    )


cpdef stake(Quantity quantity, Price price)
cpdef liability(Quantity quantity, Price price, OrderSide side)
cpdef win_payoff(Quantity quantity, Price price, OrderSide side)
cpdef lose_payoff(Quantity quantity, OrderSide side)
cpdef exposure(Quantity quantity, Price price, OrderSide side)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 29


**Identifiers**: `ANY`, `All`, `BASIS`, `BettingAccount`, `CONDITIONS`, `CashAccount`, `Copyright`, `GNU`, `General`, `Instrument`, `KIND`, `Lesser`, `License`, `Licensed`, `Ltd`, `Money`, `Nautech`, `OrderSide`, `Price`, `Pty`, `Public`, `Quantity`, `See`, `Systems`, `Unless`, `Version`, `WARRANTIES`, `WITHOUT`, `You`

## Related Files

This file is located in `nautilus_trader/accounting/accounts/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.413114Z*
