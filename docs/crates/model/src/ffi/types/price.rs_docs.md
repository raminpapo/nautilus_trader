# Documentation: price.rs

## File Metadata

- **Path**: `crates/model/src/ffi/types/price.rs`
- **Size**: 1,932 bytes
- **Lines**: 50
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`price_new()`**: Function defined in this file
- **`price_from_raw()`**: Function defined in this file
- **`price_as_f64()`**: Function defined in this file
- **`price_add_assign()`**: Function defined in this file
- **`price_sub_assign()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `price_add_assign`, `price_as_f64`, `price_from_raw`, `price_new`, `price_sub_assign`

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
*Generated on 2025-11-18T21:55:02.632197Z*
