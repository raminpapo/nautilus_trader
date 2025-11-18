# Documentation: deltas.rs

## File Metadata

- **Path**: `crates/model/src/ffi/data/deltas.rs`
- **Size**: 3,588 bytes
- **Lines**: 97
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

use nautilus_core::{UnixNanos, ffi::cvec::CVec};

use crate::{
    data::{OrderBookDelta, OrderBookDeltas, OrderBookDeltas_API},
    enums::BookAction,
    identifiers::InstrumentId,
};

/// Creates a new [`OrderBookDeltas_API`] instance from a `CVec` of `OrderBookDelta`.
///
/// # Safety
///
/// - The `deltas` must be a valid pointer to a `CVec` containing `OrderBookDelta` objects.
/// - This function clones the data pointed to by `deltas` into Rust-managed memory, then forgets the original `Vec` to prevent Rust from auto-deallocating it.
/// - The caller is responsible for managing the memory of `deltas` (including its deallocation) to avoid memory leaks.
#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_new(
    instrument_id: InstrumentId,
    deltas: &CVec,
) -> OrderBookDeltas_API {
    let CVec { ptr, len, cap } = *deltas;
    let deltas: Vec<OrderBookDelta> =
        unsafe { Vec::from_raw_parts(ptr.cast::<OrderBookDelta>(), len, cap) };
    let cloned_deltas = deltas.clone();
    std::mem::forget(deltas); // Prevents Rust from dropping `deltas`
    OrderBookDeltas_API::new(OrderBookDeltas::new(instrument_id, cloned_deltas))
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_drop(deltas: OrderBookDeltas_API) {
    drop(deltas); // Memory freed here
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_clone(deltas: &OrderBookDeltas_API) -> OrderBookDeltas_API {
    deltas.clone()
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_instrument_id(deltas: &OrderBookDeltas_API) -> InstrumentId {
    deltas.instrument_id
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_vec_deltas(deltas: &OrderBookDeltas_API) -> CVec {
    deltas.deltas.clone().into()
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_is_snapshot(deltas: &OrderBookDeltas_API) -> u8 {
    u8::from(deltas.deltas[0].action == BookAction::Clear)
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_flags(deltas: &OrderBookDeltas_API) -> u8 {
    deltas.flags
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_sequence(deltas: &OrderBookDeltas_API) -> u64 {
    deltas.sequence
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_ts_event(deltas: &OrderBookDeltas_API) -> UnixNanos {
    deltas.ts_event
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_ts_init(deltas: &OrderBookDeltas_API) -> UnixNanos {
    deltas.ts_init
}

#[allow(clippy::drop_non_drop)]
#[unsafe(no_mangle)]
pub extern "C" fn orderbook_deltas_vec_drop(v: CVec) {
    let CVec { ptr, len, cap } = v;
    let deltas: Vec<OrderBookDelta> =
        unsafe { Vec::from_raw_parts(ptr.cast::<OrderBookDelta>(), len, cap) };
    drop(deltas); // Memory freed here
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s).

## Detailed Walkthrough

### Functions
- **`orderbook_deltas_new()`**: Function defined in this file
- **`orderbook_deltas_drop()`**: Function defined in this file
- **`orderbook_deltas_clone()`**: Function defined in this file
- **`orderbook_deltas_instrument_id()`**: Function defined in this file
- **`orderbook_deltas_vec_deltas()`**: Function defined in this file
- **`orderbook_deltas_is_snapshot()`**: Function defined in this file
- **`orderbook_deltas_flags()`**: Function defined in this file
- **`orderbook_deltas_sequence()`**: Function defined in this file
- **`orderbook_deltas_ts_event()`**: Function defined in this file
- **`orderbook_deltas_ts_init()`**: Function defined in this file
- **`orderbook_deltas_vec_drop()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `orderbook_deltas_clone`, `orderbook_deltas_drop`, `orderbook_deltas_flags`, `orderbook_deltas_instrument_id`, `orderbook_deltas_is_snapshot`, `orderbook_deltas_new`, `orderbook_deltas_sequence`, `orderbook_deltas_ts_event`, `orderbook_deltas_ts_init`, `orderbook_deltas_vec_deltas`, `orderbook_deltas_vec_drop`

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
*Generated on 2025-11-18T21:55:02.554611Z*
