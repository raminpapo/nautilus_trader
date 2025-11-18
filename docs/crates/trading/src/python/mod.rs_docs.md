# Documentation: mod.rs

## File Metadata

- **Path**: `crates/trading/src/python/mod.rs`
- **Size**: 1,621 bytes
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

//! Python bindings from [PyO3](https://pyo3.rs).

pub mod sessions;

use pyo3::{prelude::*, pymodule};

/// Loaded as `nautilus_pyo3.trading`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn trading(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<crate::sessions::ForexSession>()?;
    m.add_function(wrap_pyfunction!(sessions::py_fx_local_from_utc, m)?)?;
    m.add_function(wrap_pyfunction!(sessions::py_fx_next_start, m)?)?;
    m.add_function(wrap_pyfunction!(sessions::py_fx_prev_start, m)?)?;
    m.add_function(wrap_pyfunction!(sessions::py_fx_next_end, m)?)?;
    m.add_function(wrap_pyfunction!(sessions::py_fx_prev_end, m)?)?;
    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`trading()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `trading`

## Related Files

This file is located in `crates/trading/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.193818Z*
