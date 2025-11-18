# Documentation: order.rs

## File Metadata

- **Path**: `crates/model/src/ffi/data/order.rs`
- **Size**: 2,355 bytes
- **Lines**: 74
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

use std::{
    collections::hash_map::DefaultHasher,
    ffi::c_char,
    hash::{Hash, Hasher},
};

use nautilus_core::ffi::string::str_to_cstr;

use crate::{
    data::BookOrder,
    enums::OrderSide,
    types::{Price, Quantity},
};

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn book_order_new(
    order_side: OrderSide,
    price: Price,
    size: Quantity,
    order_id: u64,
) -> BookOrder {
    BookOrder::new(order_side, price, size, order_id)
}

#[unsafe(no_mangle)]
pub extern "C" fn book_order_eq(lhs: &BookOrder, rhs: &BookOrder) -> u8 {
    u8::from(lhs == rhs)
}

#[unsafe(no_mangle)]
pub extern "C" fn book_order_hash(order: &BookOrder) -> u64 {
    let mut hasher = DefaultHasher::new();
    order.hash(&mut hasher);
    hasher.finish()
}

#[unsafe(no_mangle)]
pub extern "C" fn book_order_exposure(order: &BookOrder) -> f64 {
    order.exposure()
}

#[unsafe(no_mangle)]
pub extern "C" fn book_order_signed_size(order: &BookOrder) -> f64 {
    order.signed_size()
}

/// Returns a [`BookOrder`] display string as a C string pointer.
#[unsafe(no_mangle)]
pub extern "C" fn book_order_display_to_cstr(order: &BookOrder) -> *const c_char {
    str_to_cstr(&format!("{order}"))
}

/// Returns a [`BookOrder`] debug string as a C string pointer.
#[unsafe(no_mangle)]
pub extern "C" fn book_order_debug_to_cstr(order: &BookOrder) -> *const c_char {
    str_to_cstr(&format!("{order:?}"))
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s).

## Detailed Walkthrough

### Functions
- **`book_order_new()`**: Function defined in this file
- **`book_order_eq()`**: Function defined in this file
- **`book_order_hash()`**: Function defined in this file
- **`book_order_exposure()`**: Function defined in this file
- **`book_order_signed_size()`**: Function defined in this file
- **`book_order_display_to_cstr()`**: Function defined in this file
- **`book_order_debug_to_cstr()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `book_order_debug_to_cstr`, `book_order_display_to_cstr`, `book_order_eq`, `book_order_exposure`, `book_order_hash`, `book_order_new`, `book_order_signed_size`

## Related Files

This file is located in `crates/model/src/ffi/data/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.561449Z*
