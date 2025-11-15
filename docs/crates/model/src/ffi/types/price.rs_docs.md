# Documentation: `crates/model/src/ffi/types/price.rs`
**Generated:** 2025-11-15T19:40:02.748275Z
**File Size:** 1932 bytes
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

- **Path:** `crates/model/src/ffi/types/price.rs`
- **Size:** 1,932 bytes
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

use crate::types::price::{Price, PriceRaw};

// TODO: Document panic
#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn price_new(value: f64, precision: u8) -> Price {
    // SAFETY: Assumes `value` and `precision` are properly validated
    Price::new(value, precision)
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn price_from_raw(raw: PriceRaw, precision: u8) -> Price {
    Price::from_raw(raw, precision)
}

#[unsafe(no_mangle)]
pub extern "C" fn price_as_f64(price: &Price) -> f64 {
    price.as_f64()
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn price_add_assign(mut a: Price, b: Price) {
    a.add_assign(b);
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn price_sub_assign(mut a: Price, b: Price) {
    a.sub_assign(b);
}
```


---

## Overview

This file is located at `crates/model/src/ffi/types/price.rs` within the repository.

**Functions defined:** price_new, price_from_raw, price_as_f64, price_add_assign, price_sub_assign


---

## Detailed Analysis

### Functions

#### `price_new(value: f64, precision: u8)`


#### `price_from_raw(raw: PriceRaw, precision: u8)`


#### `price_as_f64(price: &Price)`


#### `price_add_assign(mut a: Price, b: Price)`


#### `price_sub_assign(mut a: Price, b: Price)`



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


