# Documentation: `crates/model/src/ffi/data/trade.rs`
**Generated:** 2025-11-15T19:40:02.705916Z
**File Size:** 2138 bytes
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

- **Path:** `crates/model/src/ffi/data/trade.rs`
- **Size:** 2,138 bytes
- **Lines:** 69
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 4

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

use std::{
    collections::hash_map::DefaultHasher,
    ffi::c_char,
    hash::{Hash, Hasher},
};

use nautilus_core::ffi::string::str_to_cstr;

use crate::{
    data::TradeTick,
    enums::AggressorSide,
    identifiers::{InstrumentId, TradeId},
    types::{Price, Quantity},
};

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn trade_tick_new(
    instrument_id: InstrumentId,
    price: Price,
    size: Quantity,
    aggressor_side: AggressorSide,
    trade_id: TradeId,
    ts_event: u64,
    ts_init: u64,
) -> TradeTick {
    TradeTick::new(
        instrument_id,
        price,
        size,
        aggressor_side,
        trade_id,
        ts_event.into(),
        ts_init.into(),
    )
}

#[unsafe(no_mangle)]
pub extern "C" fn trade_tick_eq(lhs: &TradeTick, rhs: &TradeTick) -> u8 {
    u8::from(lhs == rhs)
}

#[unsafe(no_mangle)]
pub extern "C" fn trade_tick_hash(delta: &TradeTick) -> u64 {
    let mut hasher = DefaultHasher::new();
    delta.hash(&mut hasher);
    hasher.finish()
}

/// Returns a [`TradeTick`] as a C string pointer.
#[unsafe(no_mangle)]
pub extern "C" fn trade_tick_to_cstr(trade: &TradeTick) -> *const c_char {
    str_to_cstr(&trade.to_string())
}
```


---

## Overview

This file is located at `crates/model/src/ffi/data/trade.rs` within the repository.

**Functions defined:** trade_tick_new, trade_tick_eq, trade_tick_hash, trade_tick_to_cstr


---

## Detailed Analysis

### Functions

#### `trade_tick_new(
    instrument_id: InstrumentId,
    price: Price,
    size: Quantity,
    aggressor_side: AggressorSide,
    trade_id: TradeId,
    ts_event: u64,
    ts_init: u64,
)`


#### `trade_tick_eq(lhs: &TradeTick, rhs: &TradeTick)`


#### `trade_tick_hash(delta: &TradeTick)`


#### `trade_tick_to_cstr(trade: &TradeTick)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/ffi/data`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


