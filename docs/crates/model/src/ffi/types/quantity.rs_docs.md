# Documentation: quantity.rs

## File Metadata

- **Path**: `crates/model/src/ffi/types/quantity.rs`
- **Size**: 2,568 bytes
- **Lines**: 68
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`quantity_new()`**: Function defined in this file
- **`quantity_from_raw()`**: Function defined in this file
- **`quantity_as_f64()`**: Function defined in this file
- **`quantity_add_assign()`**: Function defined in this file
- **`quantity_add_assign_u64()`**: Function defined in this file
- **`quantity_sub_assign()`**: Function defined in this file
- **`quantity_sub_assign_u64()`**: Function defined in this file
- **`quantity_saturating_sub()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `quantity_add_assign`, `quantity_add_assign_u64`, `quantity_as_f64`, `quantity_from_raw`, `quantity_new`, `quantity_saturating_sub`, `quantity_sub_assign`, `quantity_sub_assign_u64`

## Related Files

This file is located in `crates/model/src/ffi/types/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.634007Z*
