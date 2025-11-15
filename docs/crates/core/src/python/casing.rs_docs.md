# Documentation: `crates/core/src/python/casing.rs`
**Generated:** 2025-11-15T19:40:01.919950Z
**File Size:** 1554 bytes
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

- **Path:** `crates/core/src/python/casing.rs`
- **Size:** 1,554 bytes
- **Lines:** 40
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


---

## Overview

This file is located at `crates/core/src/python/casing.rs` within the repository.

**Functions defined:** py_convert_to_snake_case


---

## Detailed Analysis

### Functions

#### `py_convert_to_snake_case(input: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


