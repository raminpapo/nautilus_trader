# Documentation: `crates/model/src/ffi/types/quantity.rs`
**Generated:** 2025-11-15T19:40:02.749556Z
**File Size:** 2568 bytes
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

- **Path:** `crates/model/src/ffi/types/quantity.rs`
- **Size:** 2,568 bytes
- **Lines:** 67
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 8

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

use crate::types::quantity::{Quantity, QuantityRaw};

// TODO: Document panic
#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_new(value: f64, precision: u8) -> Quantity {
    // SAFETY: Assumes `value` and `precision` are properly validated
    Quantity::new(value, precision)
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_from_raw(raw: QuantityRaw, precision: u8) -> Quantity {
    Quantity::from_raw(raw, precision)
}

#[unsafe(no_mangle)]
pub extern "C" fn quantity_as_f64(qty: &Quantity) -> f64 {
    qty.as_f64()
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_add_assign(mut a: Quantity, b: Quantity) {
    a.add_assign(b);
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_add_assign_u64(mut a: Quantity, b: u64) {
    a.add_assign(b);
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_sub_assign(mut a: Quantity, b: Quantity) {
    a.sub_assign(b);
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_sub_assign_u64(mut a: Quantity, b: u64) {
    a.sub_assign(b);
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn quantity_saturating_sub(a: Quantity, b: Quantity) -> Quantity {
    a.saturating_sub(b)
}
```


---

## Overview

This file is located at `crates/model/src/ffi/types/quantity.rs` within the repository.

**Functions defined:** quantity_new, quantity_from_raw, quantity_as_f64, quantity_add_assign, quantity_add_assign_u64, quantity_sub_assign, quantity_sub_assign_u64, quantity_saturating_sub


---

## Detailed Analysis

### Functions

#### `quantity_new(value: f64, precision: u8)`


#### `quantity_from_raw(raw: QuantityRaw, precision: u8)`


#### `quantity_as_f64(qty: &Quantity)`


#### `quantity_add_assign(mut a: Quantity, b: Quantity)`


#### `quantity_add_assign_u64(mut a: Quantity, b: u64)`


#### `quantity_sub_assign(mut a: Quantity, b: Quantity)`


#### `quantity_sub_assign_u64(mut a: Quantity, b: u64)`


#### `quantity_saturating_sub(a: Quantity, b: Quantity)`



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


