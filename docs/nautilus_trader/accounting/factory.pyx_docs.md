# Documentation: factory.pyx

## File Metadata

- **Path**: `nautilus_trader/accounting/factory.pyx`
- **Size**: 4,776 bytes
- **Lines**: 142
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

from nautilus_trader.accounting.accounts.base cimport Account
from nautilus_trader.accounting.accounts.betting cimport BettingAccount
from nautilus_trader.accounting.accounts.cash cimport CashAccount
from nautilus_trader.accounting.accounts.margin cimport MarginAccount
from nautilus_trader.core.correctness cimport Condition
from nautilus_trader.core.rust.model cimport AccountType


cdef dict[str, type] _ISSUER_ACCOUNT_TYPE = {}
cdef dict[str, bint] _ISSUER_ACCOUNT_CALCULATED = {}
cdef dict[str, bint] _ISSUER_CASH_BORROWING = {}


cdef class AccountFactory:
    """
    Provides a factory for creating different account types.
    """

    @staticmethod
    def register_account_type(str issuer, type account_cls):
        """
        Register the given custom account type for the issuer.

        Parameters
        ----------
        issuer : str
            The issuer for the account.
        account_cls : type
            The custom account type.

        Raises
        ------
        KeyError
            If `issuer` has already registered a custom account type.

        """
        Condition.not_none(issuer, "issuer")
        Condition.not_none(account_cls, "account_cls")
        Condition.not_in(issuer, _ISSUER_ACCOUNT_TYPE, "issuer", "_ISSUER_ACCOUNT_TYPE")

        _ISSUER_ACCOUNT_TYPE[issuer] = account_cls

    @staticmethod
    def register_calculated_account(str issuer):
        """
        Register for account state of the given issuer to be calculated from
        order fills.

        Parameters
        ----------
        issuer : str
            The issuer for the account.

        Raises
        ------
        KeyError
            If an issuer has already been registered for the `issuer`.

        """
        Condition.not_none(issuer, "issuer")
        Condition.not_in(issuer, _ISSUER_ACCOUNT_TYPE, "issuer", "_ISSUER_ACCOUNT_TYPE")

        _ISSUER_ACCOUNT_CALCULATED[issuer] = True

    @staticmethod
    def register_cash_borrowing(str issuer):
        """
        Register for cash accounts of the given issuer to allow borrowing
        (negative balances).

        Parameters
        ----------
        issuer : str
            The issuer for the account.

        Raises
        ------
        KeyError
            If cash borrowing has already been registered for the `issuer`.

        """
        Condition.not_none(issuer, "issuer")
        Condition.not_in(issuer, _ISSUER_CASH_BORROWING, "issuer", "_ISSUER_CASH_BORROWING")

        _ISSUER_CASH_BORROWING[issuer] = True

    @staticmethod
    cdef Account create_c(AccountState event):
        Condition.not_none(event, "event")

        # Parse account issuer
        cdef str issuer = event.account_id.get_issuer()

        # Determine account settings
        cdef type account_cls = _ISSUER_ACCOUNT_TYPE.get(issuer)
        cdef bint calculated = _ISSUER_ACCOUNT_CALCULATED.get(issuer, False)
        cdef bint allow_borrowing = _ISSUER_CASH_BORROWING.get(issuer, False)

        # Create account
        if account_cls is not None:
            return account_cls(event, calculated)
        if event.account_type == AccountType.CASH:
            return CashAccount(event, calculated, allow_borrowing)
        elif event.account_type == AccountType.MARGIN:
            return MarginAccount(event, calculated)
        elif event.account_type == AccountType.BETTING:
            return BettingAccount(event, calculated)
        else:
            raise RuntimeError("invalid `AccountType`")  # pragma: no cover (design-time error)

    @staticmethod
    def create(AccountState event) -> Account:
        """
        Create an account based on the events account type.

        Parameters
        ----------
        event : AccountState
            The account state event for the creation.

        Returns
        -------
        Account

        """
        return AccountFactory.create_c(event)

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 47


**Identifiers**: `ANY`, `Account`, `AccountFactory`, `AccountState`, `AccountType`, `All`, `BASIS`, `BETTING`, `BettingAccount`, `CASH`, `CONDITIONS`, `CashAccount`, `Condition`, `Copyright`, `Create`, `Determine`, `False`, `GNU`, `General`, `KIND`, `KeyError`, `Lesser`, `License`, `Licensed`, `Ltd`, `MARGIN`, `MarginAccount`, `Nautech`, `None`, `Parameters` *(+17 more)*

## Related Files

This file is located in `nautilus_trader/accounting/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.431082Z*
