# Documentation: any.rs

## File Metadata

- **Path**: `crates/model/src/accounts/any.rs`
- **Size**: 5,880 bytes
- **Lines**: 182
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

//! Enum wrapper providing a type-erased view over the various concrete [`Account`] implementations.
//!
//! The `AccountAny` enum is primarily used when heterogeneous account types need to be stored in a
//! single collection (e.g. `Vec<AccountAny>`).  Each variant simply embeds one of the concrete
//! account structs defined in this module.

use std::collections::HashMap;

use enum_dispatch::enum_dispatch;
use serde::{Deserialize, Serialize};

use crate::{
    accounts::{Account, CashAccount, MarginAccount},
    enums::{AccountType, LiquiditySide},
    events::{AccountState, OrderFilled},
    identifiers::AccountId,
    instruments::InstrumentAny,
    position::Position,
    types::{AccountBalance, Currency, Money, Price, Quantity},
};

#[derive(Debug, Clone, Serialize, Deserialize)]
#[enum_dispatch(Account)]
pub enum AccountAny {
    Margin(MarginAccount),
    Cash(CashAccount),
}

impl AccountAny {
    #[must_use]
    pub fn id(&self) -> AccountId {
        match self {
            Self::Margin(margin) => margin.id,
            Self::Cash(cash) => cash.id,
        }
    }

    pub fn last_event(&self) -> Option<AccountState> {
        match self {
            Self::Margin(margin) => margin.last_event(),
            Self::Cash(cash) => cash.last_event(),
        }
    }

    pub fn events(&self) -> Vec<AccountState> {
        match self {
            Self::Margin(margin) => margin.events(),
            Self::Cash(cash) => cash.events(),
        }
    }

    pub fn apply(&mut self, event: AccountState) {
        match self {
            Self::Margin(margin) => margin.apply(event),
            Self::Cash(cash) => cash.apply(event),
        }
    }

    pub fn balances(&self) -> HashMap<Currency, AccountBalance> {
        match self {
            Self::Margin(margin) => margin.balances(),
            Self::Cash(cash) => cash.balances(),
        }
    }

    pub fn balances_locked(&self) -> HashMap<Currency, Money> {
        match self {
            Self::Margin(margin) => margin.balances_locked(),
            Self::Cash(cash) => cash.balances_locked(),
        }
    }

    pub fn base_currency(&self) -> Option<Currency> {
        match self {
            Self::Margin(margin) => margin.base_currency(),
            Self::Cash(cash) => cash.base_currency(),
        }
    }

    /// # Errors
    ///
    /// Returns an error if `events` is empty.
    ///
    /// # Panics
    ///
    /// Panics if `events` is empty when unwrapping the first element.
    pub fn from_events(events: Vec<AccountState>) -> anyhow::Result<Self> {
        if events.is_empty() {
            anyhow::bail!("No order events provided to create `AccountAny`");
        }

        let init_event = events.first().unwrap();
        let mut account = Self::from(init_event.clone());
        for event in events.iter().skip(1) {
            account.apply(event.clone());
        }
        Ok(account)
    }

    /// # Errors
    ///
    /// Returns an error if calculating P&Ls fails for the underlying account.
    pub fn calculate_pnls(
        &self,
        instrument: InstrumentAny,
        fill: OrderFilled,
        position: Option<Position>,
    ) -> anyhow::Result<Vec<Money>> {
        match self {
            Self::Margin(margin) => margin.calculate_pnls(instrument, fill, position),
            Self::Cash(cash) => cash.calculate_pnls(instrument, fill, position),
        }
    }

    /// # Errors
    ///
    /// Returns an error if calculating commission fails for the underlying account.
    pub fn calculate_commission(
        &self,
        instrument: InstrumentAny,
        last_qty: Quantity,
        last_px: Price,
        liquidity_side: LiquiditySide,
        use_quote_for_inverse: Option<bool>,
    ) -> anyhow::Result<Money> {
        match self {
            Self::Margin(margin) => margin.calculate_commission(
                instrument,
                last_qty,
                last_px,
                liquidity_side,
                use_quote_for_inverse,
            ),
            Self::Cash(cash) => cash.calculate_commission(
                instrument,
                last_qty,
                last_px,
                liquidity_side,
                use_quote_for_inverse,
            ),
        }
    }

    pub fn balance(&self, currency: Option<Currency>) -> Option<&AccountBalance> {
        match self {
            Self::Margin(margin) => margin.balance(currency),
            Self::Cash(cash) => cash.balance(currency),
        }
    }
}

impl From<AccountState> for AccountAny {
    fn from(event: AccountState) -> Self {
        match event.account_type {
            AccountType::Margin => Self::Margin(MarginAccount::new(event, false)),
            AccountType::Cash => Self::Cash(CashAccount::new(event, false, false)),
            AccountType::Betting => panic!("Betting account not implemented"),
        }
    }
}

impl PartialEq for AccountAny {
    fn eq(&self, other: &Self) -> bool {
        self.id() == other.id()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 13 function(s).

## Detailed Walkthrough

### Functions
- **`id()`**: Function defined in this file
- **`last_event()`**: Function defined in this file
- **`events()`**: Function defined in this file
- **`apply()`**: Function defined in this file
- **`balances()`**: Function defined in this file
- **`balances_locked()`**: Function defined in this file
- **`base_currency()`**: Function defined in this file
- **`from_events()`**: Function defined in this file
- **`calculate_pnls()`**: Function defined in this file
- **`calculate_commission()`**: Function defined in this file
- **`balance()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`eq()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 17


**Enums**: `AccountAny`, `is`
**Functions**: `apply`, `balance`, `balances`, `balances_locked`, `base_currency`, `calculate_commission`, `calculate_pnls`, `eq`, `events`, `from`, `from_events`, `id`, `last_event`
**Impls**: `AccountAny`, `From`, `PartialEq`

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
*Generated on 2025-11-18T21:55:02.175926Z*
