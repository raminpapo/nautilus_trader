# Documentation: exec_algorithm_id.rs

## File Metadata

- **Path**: `crates/model/src/ffi/identifiers/exec_algorithm_id.rs`
- **Size**: 1,460 bytes
- **Lines**: 37
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

use std::ffi::c_char;

use nautilus_core::ffi::string::cstr_as_str;

use crate::identifiers::exec_algorithm_id::ExecAlgorithmId;

/// Returns a Nautilus identifier from a C string pointer.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn exec_algorithm_id_new(ptr: *const c_char) -> ExecAlgorithmId {
    let value = unsafe { cstr_as_str(ptr) };
    ExecAlgorithmId::from(value)
}

#[unsafe(no_mangle)]
pub extern "C" fn exec_algorithm_id_hash(id: &ExecAlgorithmId) -> u64 {
    id.inner().precomputed_hash()
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`exec_algorithm_id_new()`**: Function defined in this file
- **`exec_algorithm_id_hash()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `exec_algorithm_id_hash`, `exec_algorithm_id_new`

## Related Files

This file is located in `crates/model/src/ffi/identifiers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.590998Z*
