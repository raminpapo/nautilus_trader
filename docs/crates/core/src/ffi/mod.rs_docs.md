# Documentation: `crates/core/src/ffi/mod.rs`
**Generated:** 2025-11-15T19:40:01.889056Z
**File Size:** 2149 bytes
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

- **Path:** `crates/core/src/ffi/mod.rs`
- **Size:** 2,149 bytes
- **Lines:** 53
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

//! C foreign function interface (FFI) from [cbindgen](https://github.com/mozilla/cbindgen).
//!
//! All exported functions route through `abort_on_panic` so that any panic inside the
//! Rust implementation aborts immediately instead of unwinding across the foreign boundary.
//! Unwinding into C/Python is undefined behaviour, so this keeps the existing fail-fast
//! semantics while avoiding subtle stack corruption during debugging.

#![allow(unsafe_code)]
#![allow(unsafe_attr_outside_unsafe)]

pub mod cvec;
pub mod datetime;
pub mod parsing;
pub mod string;
pub mod uuid;

use std::{
    panic::{self, AssertUnwindSafe},
    process,
};

/// Executes `f`, aborting the process if it panics.
///
/// FFI exports always call this helper so a panic never unwinds across the
/// `extern "C"` boundary. Unwinding into C/Python is undefined behaviour and
/// can silently corrupt the foreign stack; aborting instead preserves the
/// fail-fast guarantee with effectively no debugging downside (the panic
/// message is still logged before the abort).
#[inline]
pub(crate) fn abort_on_panic<F, R>(f: F) -> R
where
    F: FnOnce() -> R,
{
    match panic::catch_unwind(AssertUnwindSafe(f)) {
        Ok(result) => result,
        Err(_) => process::abort(),
    }
}
```


---

## Overview

This file is located at `crates/core/src/ffi/mod.rs` within the repository.

**Functions defined:** abort_on_panic


---

## Detailed Analysis

### Functions

#### `abort_on_panic(f: F)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/src/ffi`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


