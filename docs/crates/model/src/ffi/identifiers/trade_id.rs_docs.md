# Documentation: `crates/model/src/ffi/identifiers/trade_id.rs`
**Generated:** 2025-11-15T19:40:02.727679Z
**File Size:** 1795 bytes
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

- **Path:** `crates/model/src/ffi/identifiers/trade_id.rs`
- **Size:** 1,795 bytes
- **Lines:** 51
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
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
    ffi::{CStr, CString, c_char},
    hash::{Hash, Hasher},
};

use crate::identifiers::trade_id::TradeId;

/// Returns a Nautilus identifier from a C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn trade_id_new(ptr: *const c_char) -> TradeId {
    let value = unsafe { CStr::from_ptr(ptr).to_owned() };
    TradeId::from(value)
}

#[unsafe(no_mangle)]
pub extern "C" fn trade_id_hash(id: &TradeId) -> u64 {
    let mut hasher = DefaultHasher::new();
    id.value.hash(&mut hasher);
    hasher.finish()
}

#[unsafe(no_mangle)]
pub extern "C" fn trade_id_to_cstr(trade_id: &TradeId) -> *const c_char {
    trade_id.as_cstr().as_ptr()
}

impl From<CString> for TradeId {
    fn from(value: CString) -> Self {
        Self::from_bytes(value.as_bytes_with_nul()).unwrap()
    }
}
```


---

## Overview

This file is located at `crates/model/src/ffi/identifiers/trade_id.rs` within the repository.

**Classes defined:** From

**Functions defined:** trade_id_new, trade_id_hash, trade_id_to_cstr, from


---

## Detailed Analysis

### Classes

#### `From`

**Type:** impl


### Functions

#### `trade_id_new(ptr: *const c_char)`


#### `trade_id_hash(id: &TradeId)`


#### `trade_id_to_cstr(trade_id: &TradeId)`


#### `from(value: CString)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/ffi/identifiers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


