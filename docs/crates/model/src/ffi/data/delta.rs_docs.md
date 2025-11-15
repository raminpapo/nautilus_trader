# Documentation: `crates/model/src/ffi/data/delta.rs`
**Generated:** 2025-11-15T19:40:02.695316Z
**File Size:** 1909 bytes
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

- **Path:** `crates/model/src/ffi/data/delta.rs`
- **Size:** 1,909 bytes
- **Lines:** 61
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 3

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
    hash::{Hash, Hasher},
};

use nautilus_core::UnixNanos;

use crate::{
    data::{BookOrder, OrderBookDelta},
    enums::BookAction,
    identifiers::InstrumentId,
};

#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn orderbook_delta_new(
    instrument_id: InstrumentId,
    action: BookAction,
    order: BookOrder,
    flags: u8,
    sequence: u64,
    ts_event: UnixNanos,
    ts_init: UnixNanos,
) -> OrderBookDelta {
    OrderBookDelta::new(
        instrument_id,
        action,
        order,
        flags,
        sequence,
        ts_event,
        ts_init,
    )
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_delta_eq(lhs: &OrderBookDelta, rhs: &OrderBookDelta) -> u8 {
    u8::from(lhs == rhs)
}

#[unsafe(no_mangle)]
pub extern "C" fn orderbook_delta_hash(delta: &OrderBookDelta) -> u64 {
    let mut hasher = DefaultHasher::new();
    delta.hash(&mut hasher);
    hasher.finish()
}
```


---

## Overview

This file is located at `crates/model/src/ffi/data/delta.rs` within the repository.

**Functions defined:** orderbook_delta_new, orderbook_delta_eq, orderbook_delta_hash


---

## Detailed Analysis

### Functions

#### `orderbook_delta_new(
    instrument_id: InstrumentId,
    action: BookAction,
    order: BookOrder,
    flags: u8,
    sequence: u64,
    ts_event: UnixNanos,
    ts_init: UnixNanos,
)`


#### `orderbook_delta_eq(lhs: &OrderBookDelta, rhs: &OrderBookDelta)`


#### `orderbook_delta_hash(delta: &OrderBookDelta)`



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


