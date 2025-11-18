# Documentation: mod.rs

## File Metadata

- **Path**: `crates/model/src/accounts/mod.rs`
- **Size**: 3,841 bytes
- **Lines**: 108
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

//! Account types such as `CashAccount` and `MarginAccount`.

pub mod any;
pub mod base;
pub mod cash;
pub mod margin;

#[cfg(any(test, feature = "stubs"))]
pub mod stubs;

use std::collections::HashMap;

use enum_dispatch::enum_dispatch;
use nautilus_core::UnixNanos;

// Re-exports
pub use crate::accounts::{
    any::AccountAny, base::BaseAccount, cash::CashAccount, margin::MarginAccount,
};
use crate::{
    enums::{AccountType, LiquiditySide, OrderSide},
    events::{AccountState, OrderFilled},
    identifiers::AccountId,
    instruments::InstrumentAny,
    position::Position,
    types::{AccountBalance, Currency, Money, Price, Quantity},
};

#[enum_dispatch]
pub trait Account: 'static + Send {
    fn id(&self) -> AccountId;
    fn account_type(&self) -> AccountType;
    fn base_currency(&self) -> Option<Currency>;
    fn is_cash_account(&self) -> bool;
    fn is_margin_account(&self) -> bool;
    fn calculated_account_state(&self) -> bool;
    fn balance_total(&self, currency: Option<Currency>) -> Option<Money>;
    fn balances_total(&self) -> HashMap<Currency, Money>;
    fn balance_free(&self, currency: Option<Currency>) -> Option<Money>;
    fn balances_free(&self) -> HashMap<Currency, Money>;
    fn balance_locked(&self, currency: Option<Currency>) -> Option<Money>;
    fn balances_locked(&self) -> HashMap<Currency, Money>;
    fn balance(&self, currency: Option<Currency>) -> Option<&AccountBalance>;
    fn last_event(&self) -> Option<AccountState>;
    fn events(&self) -> Vec<AccountState>;
    fn event_count(&self) -> usize;
    fn currencies(&self) -> Vec<Currency>;
    fn starting_balances(&self) -> HashMap<Currency, Money>;
    fn balances(&self) -> HashMap<Currency, AccountBalance>;
    fn apply(&mut self, event: AccountState);
    fn purge_account_events(&mut self, ts_now: UnixNanos, lookback_secs: u64);

    /// Calculates locked balance for the order parameters.
    ///
    /// # Errors
    ///
    /// Returns an error if calculating locked balance fails.
    fn calculate_balance_locked(
        &mut self,
        instrument: InstrumentAny,
        side: OrderSide,
        quantity: Quantity,
        price: Price,
        use_quote_for_inverse: Option<bool>,
    ) -> anyhow::Result<Money>;

    /// Calculates PnLs for the fill and position.
    ///
    /// # Errors
    ///
    /// Returns an error if calculating PnLs fails.
    fn calculate_pnls(
        &self,
        instrument: InstrumentAny,
        fill: OrderFilled,
        position: Option<Position>,
    ) -> anyhow::Result<Vec<Money>>;

    /// Calculates commission for the order fill parameters.
    ///
    /// # Errors
    ///
    /// Returns an error if calculating commission fails.
    fn calculate_commission(
        &self,
        instrument: InstrumentAny,
        last_qty: Quantity,
        last_px: Price,
        liquidity_side: LiquiditySide,
        use_quote_for_inverse: Option<bool>,
    ) -> anyhow::Result<Money>;
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 24 function(s).

## Detailed Walkthrough

### Functions
- **`id()`**: Function defined in this file
- **`account_type()`**: Function defined in this file
- **`base_currency()`**: Function defined in this file
- **`is_cash_account()`**: Function defined in this file
- **`is_margin_account()`**: Function defined in this file
- **`calculated_account_state()`**: Function defined in this file
- **`balance_total()`**: Function defined in this file
- **`balances_total()`**: Function defined in this file
- **`balance_free()`**: Function defined in this file
- **`balances_free()`**: Function defined in this file
- **`balance_locked()`**: Function defined in this file
- **`balances_locked()`**: Function defined in this file
- **`balance()`**: Function defined in this file
- **`last_event()`**: Function defined in this file
- **`events()`**: Function defined in this file
- **`event_count()`**: Function defined in this file
- **`currencies()`**: Function defined in this file
- **`starting_balances()`**: Function defined in this file
- **`balances()`**: Function defined in this file
- **`apply()`**: Function defined in this file

*...and 4 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 25


**Functions**: `account_type`, `apply`, `balance`, `balance_free`, `balance_locked`, `balance_total`, `balances`, `balances_free`, `balances_locked`, `balances_total`, `base_currency`, `calculate_balance_locked`, `calculate_commission`, `calculate_pnls`, `calculated_account_state`, `currencies`, `event_count`, `events`, `id`, `is_cash_account`, `is_margin_account`, `last_event`, `purge_account_events`, `starting_balances`
**Traits**: `Account`

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
*Generated on 2025-11-18T21:55:02.200584Z*
