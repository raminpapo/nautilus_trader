# Documentation: mod.rs

## File Metadata

- **Path**: `crates/model/src/ffi/data/mod.rs`
- **Size**: 1,536 bytes
- **Lines**: 36
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`data_clone()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `data_clone`

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
*Generated on 2025-11-18T21:55:02.559522Z*
