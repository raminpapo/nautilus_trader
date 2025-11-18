# Documentation: casing.rs

## File Metadata

- **Path**: `crates/core/src/python/casing.rs`
- **Size**: 1,552 bytes
- **Lines**: 41
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

//! String-case conversion helpers (`CamelCase` ⇄ `snake_case`).

use heck::ToSnakeCase;
use pyo3::prelude::*;
use pyo3_stub_gen::derive::gen_stub_pyfunction;

/// Convert the given string from any common case (PascalCase, camelCase, kebab-case, etc.)
/// to *lower* `snake_case`.
///
/// This function uses the `heck` Rust crate under the hood.
///
/// Parameters
/// ----------
/// input : str
///     The input string to convert.
///
/// Returns
/// -------
/// str
#[must_use]
#[gen_stub_pyfunction(module = "nautilus_trader.core")]
#[pyfunction(name = "convert_to_snake_case")]
pub fn py_convert_to_snake_case(input: &str) -> String {
    input.to_snake_case()
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`py_convert_to_snake_case()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `py_convert_to_snake_case`

## Related Files

This file is located in `crates/core/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.417231Z*
