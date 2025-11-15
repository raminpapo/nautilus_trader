# Documentation: `crates/model/src/ffi/identifiers/client_order_id.rs`
**Generated:** 2025-11-15T19:40:02.716115Z
**File Size:** 1429 bytes
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

- **Path:** `crates/model/src/ffi/identifiers/client_order_id.rs`
- **Size:** 1,429 bytes
- **Lines:** 36
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

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

use nautilus_core::ffi::string::cstr_as_str;

use crate::identifiers::ClientOrderId;

/// Returns a Nautilus identifier from a C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn client_order_id_new(ptr: *const c_char) -> ClientOrderId {
    let value = unsafe { cstr_as_str(ptr) };
    ClientOrderId::from(value)
}

#[unsafe(no_mangle)]
pub extern "C" fn client_order_id_hash(id: &ClientOrderId) -> u64 {
    id.inner().precomputed_hash()
}
```


---

## Overview

This file is located at `crates/model/src/ffi/identifiers/client_order_id.rs` within the repository.

**Functions defined:** client_order_id_new, client_order_id_hash


---

## Detailed Analysis

### Functions

#### `client_order_id_new(ptr: *const c_char)`


#### `client_order_id_hash(id: &ClientOrderId)`



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


