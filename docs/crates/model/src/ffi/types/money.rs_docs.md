# Documentation: `crates/model/src/ffi/types/money.rs`
**Generated:** 2025-11-15T19:40:02.747048Z
**File Size:** 1936 bytes
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

- **Path:** `crates/model/src/ffi/types/money.rs`
- **Size:** 1,936 bytes
- **Lines:** 49
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 5

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

use std::ops::{AddAssign, SubAssign};

use crate::types::{Currency, Money, money::MoneyRaw};

// TODO: Document panic
#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn money_new(amount: f64, currency: Currency) -> Money {
    // SAFETY: Assumes `amount` is properly validated
    Money::new(amount, currency)
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn money_from_raw(raw: MoneyRaw, currency: Currency) -> Money {
    Money::from_raw(raw, currency)
}

#[unsafe(no_mangle)]
pub extern "C" fn money_as_f64(money: &Money) -> f64 {
    money.as_f64()
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn money_add_assign(mut a: Money, b: Money) {
    a.add_assign(b);
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn money_sub_assign(mut a: Money, b: Money) {
    a.sub_assign(b);
}
```


---

## Overview

This file is located at `crates/model/src/ffi/types/money.rs` within the repository.

**Functions defined:** money_new, money_from_raw, money_as_f64, money_add_assign, money_sub_assign


---

## Detailed Analysis

### Functions

#### `money_new(amount: f64, currency: Currency)`


#### `money_from_raw(raw: MoneyRaw, currency: Currency)`


#### `money_as_f64(money: &Money)`


#### `money_add_assign(mut a: Money, b: Money)`


#### `money_sub_assign(mut a: Money, b: Money)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/ffi/types`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


