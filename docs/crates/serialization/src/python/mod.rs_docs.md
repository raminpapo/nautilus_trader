# Documentation: `crates/serialization/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:03.743648Z
**File Size:** 2485 bytes
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

- **Path:** `crates/serialization/src/python/mod.rs`
- **Size:** 2,485 bytes
- **Lines:** 71
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


---

## Overview

This file is located at `crates/serialization/src/python/mod.rs` within the repository.

**Functions defined:** serialization


---

## Detailed Analysis

### Functions

#### `serialization(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/serialization/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


