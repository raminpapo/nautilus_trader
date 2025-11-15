# Documentation: `crates/model/src/ffi/identifiers/venue.rs`
**Generated:** 2025-11-15T19:40:02.731123Z
**File Size:** 2415 bytes
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

- **Path:** `crates/model/src/ffi/identifiers/venue.rs`
- **Size:** 2,415 bytes
- **Lines:** 71
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

use nautilus_core::{MUTEX_POISONED, ffi::string::cstr_as_str};

use crate::{identifiers::Venue, venues::VENUE_MAP};

/// Returns a Nautilus identifier from a C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn venue_new(ptr: *const c_char) -> Venue {
    let value = unsafe { cstr_as_str(ptr) };
    Venue::from(value)
}

#[unsafe(no_mangle)]
pub extern "C" fn venue_hash(id: &Venue) -> u64 {
    id.inner().precomputed_hash()
}

#[unsafe(no_mangle)]
pub extern "C" fn venue_is_synthetic(venue: &Venue) -> u8 {
    u8::from(venue.is_synthetic())
}

/// Checks if a venue code exists in the internal map.
///
/// # Safety
///
/// Assumes `code_ptr` is a valid NUL-terminated UTF-8 C string pointer.
///
/// # Panics
///
/// Panics if the internal mutex `VENUE_MAP` is poisoned.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn venue_code_exists(code_ptr: *const c_char) -> u8 {
    let code = unsafe { cstr_as_str(code_ptr) };
    u8::from(VENUE_MAP.lock().expect(MUTEX_POISONED).contains_key(code))
}

/// Converts a UTF-8 C string pointer to a `Venue`.
///
/// # Safety
///
/// Assumes `code_ptr` is a valid NUL-terminated UTF-8 C string pointer.
///
/// # Panics
///
/// Panics if the code is not found or invalid (unwrap on `from_code`).
#[unsafe(no_mangle)]
pub unsafe extern "C" fn venue_from_cstr_code(code_ptr: *const c_char) -> Venue {
    let code = unsafe { cstr_as_str(code_ptr) };
    Venue::from_code(code).unwrap()
}
```


---

## Overview

This file is located at `crates/model/src/ffi/identifiers/venue.rs` within the repository.

**Functions defined:** venue_new, venue_hash, venue_is_synthetic, venue_code_exists, venue_from_cstr_code


---

## Detailed Analysis

### Functions

#### `venue_new(ptr: *const c_char)`


#### `venue_hash(id: &Venue)`


#### `venue_is_synthetic(venue: &Venue)`


#### `venue_code_exists(code_ptr: *const c_char)`


#### `venue_from_cstr_code(code_ptr: *const c_char)`



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


