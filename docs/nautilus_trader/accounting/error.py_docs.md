# Documentation: `nautilus_trader/accounting/error.py`
**Generated:** 2025-11-15T19:40:03.997674Z
**File Size:** 2111 bytes
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

- **Path:** `nautilus_trader/accounting/error.py`
- **Size:** 2,111 bytes
- **Lines:** 64
- **Extension:** `.py`
- **Type:** text
- **Imports:** 2
- **Classes:** 3
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

from decimal import Decimal

from nautilus_trader.model.objects import Currency


class AccountError(Exception):
    """
    The base class for all account type errors.
    """


class AccountBalanceNegative(AccountError):
    """
    Raised when the account balance for a currency becomes negative.
    """

    def __init__(self, balance: Decimal, currency: Currency):
        super().__init__()

        self.balance = balance
        self.currency = currency

    def __str__(self) -> str:
        return f"{type(self).__name__}(balance={self.balance}, currency={self.currency})"


class AccountMarginExceeded(AccountError):
    """
    Raised when the account margin for a currency is exceeded.

    In this scenario some form of liquidation event will occur.

    """

    def __init__(self, balance: Decimal, margin: Decimal, currency: Currency):
        super().__init__()

        self.balance = balance
        self.margin = margin
        self.currency = currency

    def __str__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"balance={self.balance}, "
            f"margin={self.margin}, "
            f"free={self.balance - self.margin}, "
            f"currency={self.currency})"
        )
```


---

## Overview

This file is located at `nautilus_trader/accounting/error.py` within the repository.

**Classes defined:** AccountError, AccountBalanceNegative, AccountMarginExceeded

**Functions defined:** __init__, __str__, __init__, __str__

**Import statements:** 2


---

## Detailed Analysis

### Classes

#### `AccountError`

**Inherits from:** Exception


#### `AccountBalanceNegative`

**Inherits from:** AccountError


#### `AccountMarginExceeded`

**Inherits from:** AccountError


### Functions

#### `__init__(self, balance: Decimal, currency: Currency)`


#### `__str__(self)`


#### `__init__(self, balance: Decimal, margin: Decimal, currency: Currency)`


#### `__str__(self)`


### Imports

- `from decimal import Decimal`
- `from nautilus_trader.model.objects import Currency`


---

## Usage Examples

### Importing

```python
from nautilus_trader.accounting.error import AccountError
```


---

## Related Files

This file imports from the following modules:

- `from decimal import Decimal`
- `from nautilus_trader.model.objects import Currency`

**Directory:** `nautilus_trader/accounting`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


