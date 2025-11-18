# Documentation: mod.rs

## File Metadata

- **Path**: `crates/serialization/src/python/mod.rs`
- **Size**: 2,485 bytes
- **Lines**: 72
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

pub mod arrow;

use pyo3::prelude::*;

/// Loaded as `nautilus_pyo3.serialization`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn serialization(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::get_arrow_schema_map,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::pyobjects_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_book_deltas_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_book_depth10_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_quotes_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_trades_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_bars_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_mark_prices_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_index_prices_to_arrow_record_batch_bytes,
        m
    )?)?;
    m.add_function(wrap_pyfunction!(
        crate::python::arrow::py_instrument_closes_to_arrow_record_batch_bytes,
        m
    )?)?;

    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`serialization()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `serialization`

## Related Files

This file is located in `crates/serialization/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:04.135305Z*
