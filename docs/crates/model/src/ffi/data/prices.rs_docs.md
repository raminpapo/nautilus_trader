# Documentation: `crates/model/src/ffi/data/prices.rs`
**Generated:** 2025-11-15T19:40:02.702647Z
**File Size:** 2778 bytes
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

- **Path:** `crates/model/src/ffi/data/prices.rs`
- **Size:** 2,778 bytes
- **Lines:** 84
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

use std::{
    collections::hash_map::DefaultHasher,
    ffi::c_char,
    hash::{Hash, Hasher},
};

use nautilus_core::ffi::string::str_to_cstr;

use crate::{
    data::{IndexPriceUpdate, MarkPriceUpdate},
    identifiers::InstrumentId,
    types::Price,
};

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn mark_price_update_new(
    instrument_id: InstrumentId,
    value: Price,
    ts_event: u64,
    ts_init: u64,
) -> MarkPriceUpdate {
    MarkPriceUpdate::new(instrument_id, value, ts_event.into(), ts_init.into())
}

#[unsafe(no_mangle)]
pub extern "C" fn mark_price_update_eq(lhs: &MarkPriceUpdate, rhs: &MarkPriceUpdate) -> u8 {
    u8::from(lhs == rhs)
}

#[unsafe(no_mangle)]
pub extern "C" fn mark_price_update_hash(value: &MarkPriceUpdate) -> u64 {
    let mut hasher = DefaultHasher::new();
    value.hash(&mut hasher);
    hasher.finish()
}

#[unsafe(no_mangle)]
pub extern "C" fn mark_price_update_to_cstr(value: &MarkPriceUpdate) -> *const c_char {
    str_to_cstr(&value.to_string())
}

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn index_price_update_new(
    instrument_id: InstrumentId,
    value: Price,
    ts_event: u64,
    ts_init: u64,
) -> IndexPriceUpdate {
    IndexPriceUpdate::new(instrument_id, value, ts_event.into(), ts_init.into())
}

#[unsafe(no_mangle)]
pub extern "C" fn index_price_update_eq(lhs: &IndexPriceUpdate, rhs: &IndexPriceUpdate) -> u8 {
    u8::from(lhs == rhs)
}

#[unsafe(no_mangle)]
pub extern "C" fn index_price_update_hash(value: &IndexPriceUpdate) -> u64 {
    let mut hasher = DefaultHasher::new();
    value.hash(&mut hasher);
    hasher.finish()
}

#[unsafe(no_mangle)]
pub extern "C" fn index_price_update_to_cstr(value: &IndexPriceUpdate) -> *const c_char {
    str_to_cstr(&value.to_string())
}
```


---

## Overview

This file is located at `crates/model/src/ffi/data/prices.rs` within the repository.

**Functions defined:** mark_price_update_new, mark_price_update_eq, mark_price_update_hash, mark_price_update_to_cstr, index_price_update_new, index_price_update_eq, index_price_update_hash, index_price_update_to_cstr


---

## Detailed Analysis

### Functions

#### `mark_price_update_new(
    instrument_id: InstrumentId,
    value: Price,
    ts_event: u64,
    ts_init: u64,
)`


#### `mark_price_update_eq(lhs: &MarkPriceUpdate, rhs: &MarkPriceUpdate)`


#### `mark_price_update_hash(value: &MarkPriceUpdate)`


#### `mark_price_update_to_cstr(value: &MarkPriceUpdate)`


#### `index_price_update_new(
    instrument_id: InstrumentId,
    value: Price,
    ts_event: u64,
    ts_init: u64,
)`


#### `index_price_update_eq(lhs: &IndexPriceUpdate, rhs: &IndexPriceUpdate)`


#### `index_price_update_hash(value: &IndexPriceUpdate)`


#### `index_price_update_to_cstr(value: &IndexPriceUpdate)`



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


