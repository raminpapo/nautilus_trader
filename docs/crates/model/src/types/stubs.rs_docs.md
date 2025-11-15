# Documentation: `crates/model/src/types/stubs.rs`
**Generated:** 2025-11-15T19:40:03.185744Z
**File Size:** 1416 bytes
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

- **Path:** `crates/model/src/types/stubs.rs`
- **Size:** 1,416 bytes
- **Lines:** 36
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

---

## Source Code

```rust
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

use rstest::fixture;

use crate::{
    identifiers::stubs::instrument_id_btc_usdt,
    types::{AccountBalance, MarginBalance, Money},
};

#[fixture]
pub fn stub_account_balance() -> AccountBalance {
    let total = Money::from("1525000 USD");
    let locked = Money::from("25000 USD");
    let free = Money::from("1500000 USD");
    AccountBalance::new(total, locked, free)
}

#[fixture]
pub fn stub_margin_balance() -> MarginBalance {
    let initial = Money::from("5000 USD");
    let maintenance = Money::from("20000 USD");
    let instrument = instrument_id_btc_usdt();
    MarginBalance::new(initial, maintenance, instrument)
}
```


---

## Overview

This file is located at `crates/model/src/types/stubs.rs` within the repository.

**Functions defined:** stub_account_balance, stub_margin_balance


---

## Detailed Analysis

### Functions

#### `stub_account_balance()`


#### `stub_margin_balance()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/types`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


