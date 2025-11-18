# Documentation: stubs.rs

## File Metadata

- **Path**: `crates/model/src/accounts/stubs.rs`
- **Size**: 3,423 bytes
- **Lines**: 102
- **Language**: Rust

## Original Source

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 Nautech Systems Pty Ltd. All rights reserved.
//  https://nautechsystems.io
//
//  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
//  You may not use this file except in compliance with the License.
//  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
// -------------------------------------------------------------------------------------------------

//! Lightweight stub implementations useful in unit tests where a full account object is
//! unnecessary.

use rstest::fixture;

use crate::{
    accounts::{Account, AccountAny, CashAccount, MarginAccount},
    enums::{AccountType, LiquiditySide},
    events::account::{state::AccountState, stubs::*},
    identifiers::stubs::{account_id, uuid4},
    instruments::InstrumentAny,
    types::{AccountBalance, Currency, Money, Price, Quantity},
};

impl Default for CashAccount {
    /// Creates a new default [`CashAccount`] instance.
    fn default() -> Self {
        // million dollar account
        let init_event = AccountState::new(
            account_id(),
            AccountType::Cash,
            vec![AccountBalance::new(
                Money::from("1000000 USD"),
                Money::from("0 USD"),
                Money::from("1000000 USD"),
            )],
            vec![],
            true,
            uuid4(),
            0.into(),
            0.into(),
            Some(Currency::USD()),
        );
        Self::new(init_event, false, false)
    }
}

impl Default for AccountAny {
    /// Creates a new default [`AccountAny`] instance.
    fn default() -> Self {
        Self::Cash(CashAccount::default())
    }
}

#[fixture]
pub fn margin_account(margin_account_state: AccountState) -> MarginAccount {
    MarginAccount::new(margin_account_state, true)
}

#[fixture]
pub fn cash_account(cash_account_state: AccountState) -> CashAccount {
    CashAccount::new(cash_account_state, true, false)
}

#[fixture]
pub fn cash_account_million_usd(cash_account_state_million_usd: AccountState) -> CashAccount {
    CashAccount::new(cash_account_state_million_usd, true, false)
}

#[fixture]
pub fn cash_account_multi(cash_account_state_multi: AccountState) -> CashAccount {
    CashAccount::new(cash_account_state_multi, true, false)
}

/// Helper to calculate commission in test fixtures.
///
/// # Panics
///
/// Panics if the underlying `calculate_commission` returns an error.
#[must_use]
pub fn calculate_commission(
    instrument: InstrumentAny,
    quantity: Quantity,
    price: Price,
    currency: Option<Currency>,
) -> Money {
    let account_state = if Some(Currency::USDT()) == currency {
        cash_account_state_million_usdt()
    } else {
        cash_account_state_million_usd("1000000 USD", "0 USD", "1000000 USD")
    };
    let account = cash_account_million_usd(account_state);
    account
        .calculate_commission(instrument, quantity, price, LiquiditySide::Taker, None)
        .unwrap()
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s).

## Detailed Walkthrough

### Functions
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`margin_account()`**: Function defined in this file
- **`cash_account()`**: Function defined in this file
- **`cash_account_million_usd()`**: Function defined in this file
- **`cash_account_multi()`**: Function defined in this file
- **`calculate_commission()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `calculate_commission`, `cash_account`, `cash_account_million_usd`, `cash_account_multi`, `default`, `margin_account`
**Impls**: `Default`

## Related Files

This file is located in `crates/model/src/accounts/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.202765Z*
