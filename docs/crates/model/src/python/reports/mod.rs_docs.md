# Documentation: mod.rs

## File Metadata

- **Path**: `crates/model/src/python/reports/mod.rs`
- **Size**: 1,527 bytes
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

//! Python bindings from [PyO3](https://pyo3.rs).

use pyo3::prelude::*;

use crate::reports;

pub mod fill;
pub mod mass_status;
pub mod order;
pub mod position;

/// Loaded as `nautilus_pyo3.execution`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
#[rustfmt::skip]
pub fn execution(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<reports::fill::FillReport>()?;
    m.add_class::<reports::order::OrderStatusReport>()?;
    m.add_class::<reports::position::PositionStatusReport>()?;
    m.add_class::<reports::mass_status::ExecutionMassStatus>()?;
    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`execution()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `execution`

## Related Files

This file is located in `crates/model/src/python/reports/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.201152Z*
