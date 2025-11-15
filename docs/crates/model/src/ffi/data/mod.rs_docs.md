# Documentation: `crates/model/src/ffi/data/mod.rs`
**Generated:** 2025-11-15T19:40:02.699556Z
**File Size:** 1536 bytes
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

- **Path:** `crates/model/src/ffi/data/mod.rs`
- **Size:** 1,536 bytes
- **Lines:** 35
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

pub mod bar;
pub mod delta;
pub mod deltas;
pub mod depth;
pub mod order;
pub mod prices;
pub mod quote;
pub mod trade;

// TODO: https://blog.rust-lang.org/2024/03/30/i128-layout-update.html
// i128 and u128 is now FFI compatible. However, since the clippy lint
// hasn't been removed yet. We'll suppress with #[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]

/// Clones a data instance.
// FFI wrapper for cloning Data instances
#[unsafe(no_mangle)]
#[cfg_attr(feature = "high-precision", allow(improper_ctypes_definitions))]
pub extern "C" fn data_clone(data: &crate::data::Data) -> crate::data::Data {
    data.clone()
}
```


---

## Overview

This file is located at `crates/model/src/ffi/data/mod.rs` within the repository.

**Functions defined:** data_clone


---

## Detailed Analysis

### Functions

#### `data_clone(data: &crate::data::Data)`



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


