# Documentation: enums.rs

## File Metadata

- **Path**: `crates/core/src/python/enums.rs`
- **Size**: 1,908 bytes
- **Lines**: 46
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`parse_enum()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Enums**: `utilities`
**Functions**: `parse_enum`

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
*Generated on 2025-11-18T21:55:01.422090Z*
