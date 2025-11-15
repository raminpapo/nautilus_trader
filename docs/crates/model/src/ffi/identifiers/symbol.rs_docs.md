# Documentation: `crates/model/src/ffi/identifiers/symbol.rs`
**Generated:** 2025-11-15T19:40:02.726374Z
**File Size:** 1742 bytes
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

- **Path:** `crates/model/src/ffi/identifiers/symbol.rs`
- **Size:** 1,742 bytes
- **Lines:** 51
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 5

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

use std::ffi::c_char;

use nautilus_core::ffi::string::{cstr_as_str, str_to_cstr};

use crate::identifiers::Symbol;

/// Returns a Nautilus identifier from a C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn symbol_new(ptr: *const c_char) -> Symbol {
    let value = unsafe { cstr_as_str(ptr) };
    Symbol::from(value)
}

#[unsafe(no_mangle)]
pub extern "C" fn symbol_hash(id: &Symbol) -> u64 {
    id.inner().precomputed_hash()
}

#[unsafe(no_mangle)]
pub extern "C" fn symbol_is_composite(id: &Symbol) -> u8 {
    u8::from(id.is_composite())
}

#[unsafe(no_mangle)]
pub extern "C" fn symbol_root(id: &Symbol) -> *const c_char {
    str_to_cstr(id.root())
}

#[unsafe(no_mangle)]
pub extern "C" fn symbol_topic(id: &Symbol) -> *const c_char {
    str_to_cstr(&id.topic())
}
```


---

## Overview

This file is located at `crates/model/src/ffi/identifiers/symbol.rs` within the repository.

**Functions defined:** symbol_new, symbol_hash, symbol_is_composite, symbol_root, symbol_topic


---

## Detailed Analysis

### Functions

#### `symbol_new(ptr: *const c_char)`


#### `symbol_hash(id: &Symbol)`


#### `symbol_is_composite(id: &Symbol)`


#### `symbol_root(id: &Symbol)`


#### `symbol_topic(id: &Symbol)`



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


