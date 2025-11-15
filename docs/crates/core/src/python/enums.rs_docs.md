# Documentation: `crates/core/src/python/enums.rs`
**Generated:** 2025-11-15T19:40:01.924346Z
**File Size:** 1914 bytes
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

- **Path:** `crates/core/src/python/enums.rs`
- **Size:** 1,914 bytes
- **Lines:** 45
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

//! Macro-generated enum utilities for PyO3.

use ::pyo3::exceptions::PyValueError;
use ::strum::{IntoEnumIterator, ParseError};
use pyo3::PyResult;

/// Converts a raw string to the enum `E`, returning a nicely‑formatted
/// `PyValueError` if the string does not match any variant.
///
/// The helper is aimed at Python‑exposed functions that still accept plain
/// `&str` parameters internally: call `parse_enum` instead of writing repetitive
/// `str::parse()` + error‑formatting logic yourself.
///
/// # Errors
///
/// Returns an error if `input` does not match any known variant of `E`.
pub fn parse_enum<E>(input: &str, param: &str) -> PyResult<E>
where
    E: std::str::FromStr<Err = ParseError> + IntoEnumIterator + ToString,
{
    input.parse::<E>().map_err(|_| {
        let allowed = E::iter()
            .map(|v| v.to_string())
            .collect::<Vec<_>>()
            .join(", ");
        PyValueError::new_err(format!(
            "unknown {param} `{input}`; valid values: {allowed}"
        ))
    })
}
```


---

## Overview

This file is located at `crates/core/src/python/enums.rs` within the repository.

**Functions defined:** parse_enum


---

## Detailed Analysis

### Functions

#### `parse_enum(input: &str, param: &str)`



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


