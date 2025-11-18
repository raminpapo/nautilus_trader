# Documentation: level.rs

## File Metadata

- **Path**: `crates/model/src/ffi/orderbook/level.rs`
- **Size**: 4,526 bytes
- **Lines**: 144
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

use std::ops::{Deref, DerefMut};

use nautilus_core::ffi::cvec::CVec;

use crate::{
    data::order::BookOrder,
    enums::OrderSide,
    orderbook::{BookLevel, BookPrice},
    types::Price,
};

/// C compatible Foreign Function Interface (FFI) for an underlying order book[`BookLevel`].
///
/// This struct wraps `Level` in a way that makes it compatible with C function
/// calls, enabling interaction with `Level` in a C environment.
///
/// It implements the `Deref` trait, allowing instances of `Level_API` to be
/// dereferenced to `Level`, providing access to `Level`'s methods without
/// having to manually acce wss the underlying `Level` instance.
#[repr(C)]
#[derive(Clone, Debug)]
#[allow(non_camel_case_types)]
pub struct BookLevel_API(Box<BookLevel>);

impl BookLevel_API {
    /// Creates a new [`BookLevel_API`] instance.
    #[must_use]
    pub fn new(level: BookLevel) -> Self {
        Self(Box::new(level))
    }
}

impl Deref for BookLevel_API {
    type Target = BookLevel;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

impl DerefMut for BookLevel_API {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.0
    }
}

impl Drop for BookLevel_API {
    fn drop(&mut self) {
        // The Box<BookLevel> inside self.0 will be automatically dropped here.
        // This is critical for preventing memory leaks when BookLevel_API instances
        // are stored in CVecs, as each BookLevel may contain many BookOrder objects
        // in its IndexMap which need to be properly deallocated.
    }
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn level_new(order_side: OrderSide, price: Price, orders: CVec) -> BookLevel_API {
    let CVec { ptr, len, cap } = orders;
    let orders: Vec<BookOrder> = unsafe { Vec::from_raw_parts(ptr.cast::<BookOrder>(), len, cap) };
    let price = BookPrice {
        value: price,
        side: order_side.as_specified(),
    };
    let mut level = BookLevel::new(price);
    level.add_bulk(orders);
    BookLevel_API::new(level)
}

#[unsafe(no_mangle)]
pub extern "C" fn level_drop(level: BookLevel_API) {
    drop(level); // Memory freed here
}

#[unsafe(no_mangle)]
pub extern "C" fn level_clone(level: &BookLevel_API) -> BookLevel_API {
    level.clone()
}

#[unsafe(no_mangle)]
pub extern "C" fn level_side(level: &BookLevel_API) -> OrderSide {
    level.price.side.as_order_side()
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn level_price(level: &BookLevel_API) -> Price {
    level.price.value
}

#[unsafe(no_mangle)]
pub extern "C" fn level_orders(level: &BookLevel_API) -> CVec {
    let orders_vec: Vec<BookOrder> = level.orders.values().copied().collect();
    orders_vec.into()
}

#[unsafe(no_mangle)]
pub extern "C" fn level_size(level: &BookLevel_API) -> f64 {
    level.size()
}

#[unsafe(no_mangle)]
pub extern "C" fn level_exposure(level: &BookLevel_API) -> f64 {
    level.exposure()
}

#[unsafe(no_mangle)]
pub extern "C" fn vec_drop_book_levels(v: CVec) {
    if v.ptr.is_null() {
        return;
    }

    let CVec { ptr, len, cap } = v;
    let data: Vec<BookLevel_API> =
        unsafe { Vec::from_raw_parts(ptr.cast::<BookLevel_API>(), len, cap) };
    drop(data); // Memory freed here
}

#[unsafe(no_mangle)]
pub extern "C" fn vec_drop_book_orders(v: CVec) {
    if v.ptr.is_null() {
        return;
    }

    let CVec { ptr, len, cap } = v;
    let orders: Vec<BookOrder> = unsafe { Vec::from_raw_parts(ptr.cast::<BookOrder>(), len, cap) };
    drop(orders); // Memory freed here
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 14 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`deref()`**: Function defined in this file
- **`deref_mut()`**: Function defined in this file
- **`drop()`**: Function defined in this file
- **`level_new()`**: Function defined in this file
- **`level_drop()`**: Function defined in this file
- **`level_clone()`**: Function defined in this file
- **`level_side()`**: Function defined in this file
- **`level_price()`**: Function defined in this file
- **`level_orders()`**: Function defined in this file
- **`level_size()`**: Function defined in this file
- **`level_exposure()`**: Function defined in this file
- **`vec_drop_book_levels()`**: Function defined in this file
- **`vec_drop_book_orders()`**: Function defined in this file

### Classes
- **`wraps`**: Class defined in this file
- **`BookLevel_API`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 19


**Functions**: `deref`, `deref_mut`, `drop`, `level_clone`, `level_drop`, `level_exposure`, `level_new`, `level_orders`, `level_price`, `level_side`, `level_size`, `new`, `vec_drop_book_levels`, `vec_drop_book_orders`
**Impls**: `BookLevel_API`, `Deref`, `DerefMut`, `Drop`
**Structs**: `BookLevel_API`, `wraps`

## Related Files

This file is located in `crates/model/src/ffi/orderbook/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.622390Z*
