# Documentation: `crates/model/src/events/account/stubs.rs`
**Generated:** 2025-11-15T19:40:02.620239Z
**File Size:** 3981 bytes
**Extension:** .rs
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

- **Path:** `crates/model/src/events/account/stubs.rs`
- **Size:** 3,981 bytes
- **Lines:** 149
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 6

---

## Source Code

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

use nautilus_core::UUID4;
use rstest::fixture;

use crate::{
    enums::AccountType,
    events::AccountState,
    identifiers::stubs::{account_id, uuid4},
    types::{
        AccountBalance, Currency, Money,
        stubs::{stub_account_balance, stub_margin_balance},
    },
};

#[fixture]
pub fn cash_account_state() -> AccountState {
    AccountState::new(
        account_id(),
        AccountType::Cash,
        vec![stub_account_balance()],
        vec![],
        true,
        uuid4(),
        0.into(),
        0.into(),
        Some(Currency::USD()),
    )
}

#[fixture]
pub fn cash_account_state_million_usd(
    #[default("1000000 USD")] total: &str,
    #[default("0 USD")] locked: &str,
    #[default("1000000 USD")] free: &str,
) -> AccountState {
    AccountState::new(
        account_id(),
        AccountType::Cash,
        vec![AccountBalance::new(
            Money::from(total),
            Money::from(locked),
            Money::from(free),
        )],
        vec![],
        true,
        UUID4::new(),
        0.into(),
        0.into(),
        Some(Currency::USD()),
    )
}

#[fixture]
pub fn cash_account_state_million_usdt() -> AccountState {
    AccountState::new(
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
    )
}

#[fixture]
pub fn cash_account_state_multi() -> AccountState {
    let btc_account_balance = AccountBalance::new(
        Money::from("10 BTC"),
        Money::from("0 BTC"),
        Money::from("10 BTC"),
    );
    let eth_account_balance = AccountBalance::new(
        Money::from("20 ETH"),
        Money::from("0 ETH"),
        Money::from("20 ETH"),
    );
    AccountState::new(
        account_id(),
        AccountType::Cash,
        vec![btc_account_balance, eth_account_balance],
        vec![],
        true,
        uuid4(),
        0.into(),
        0.into(),
        None, // multi cash account
    )
}

#[fixture]
pub fn cash_account_state_multi_changed_btc() -> AccountState {
    let btc_account_balance = AccountBalance::new(
        Money::from("9 BTC"),
        Money::from("0.5 BTC"),
        Money::from("8.5 BTC"),
    );
    let eth_account_balance = AccountBalance::new(
        Money::from("20 ETH"),
        Money::from("0 ETH"),
        Money::from("20 ETH"),
    );
    AccountState::new(
        account_id(),
        AccountType::Cash,
        vec![btc_account_balance, eth_account_balance],
        vec![],
        true,
        uuid4(),
        0.into(),
        0.into(),
        None, // multi cash account
    )
}

#[fixture]
pub fn margin_account_state() -> AccountState {
    AccountState::new(
        account_id(),
        AccountType::Margin,
        vec![stub_account_balance()],
        vec![stub_margin_balance()],
        true,
        uuid4(),
        0.into(),
        0.into(),
        Some(Currency::USD()),
    )
}
```


---

## Overview

This file is located at `crates/model/src/events/account/stubs.rs` within the repository.

**Functions defined:** cash_account_state, cash_account_state_million_usd, cash_account_state_million_usdt, cash_account_state_multi, cash_account_state_multi_changed_btc, margin_account_state


---

## Detailed Analysis

### Functions

#### `cash_account_state()`


#### `cash_account_state_million_usd(
    #[default("1000000 USD")`


#### `cash_account_state_million_usdt()`


#### `cash_account_state_multi()`


#### `cash_account_state_multi_changed_btc()`


#### `margin_account_state()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/events/account`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


