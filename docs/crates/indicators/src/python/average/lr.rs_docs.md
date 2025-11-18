# Documentation: lr.rs

## File Metadata

- **Path**: `crates/indicators/src/python/average/lr.rs`
- **Size**: 2,652 bytes
- **Lines**: 108
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

use nautilus_model::data::Bar;
use pyo3::prelude::*;

use crate::{average::lr::LinearRegression, indicator::Indicator};

#[pymethods]
impl LinearRegression {
    #[new]
    #[must_use]
    pub fn py_new(period: usize) -> Self {
        Self::new(period)
    }

    fn __repr__(&self) -> String {
        format!("LinearRegression({})", self.period)
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[getter]
    #[pyo3(name = "period")]
    const fn py_period(&self) -> usize {
        self.period
    }

    #[getter]
    #[pyo3(name = "slope")]
    const fn py_slope(&self) -> f64 {
        self.slope
    }

    #[getter]
    #[pyo3(name = "intercept")]
    const fn py_intercept(&self) -> f64 {
        self.intercept
    }

    #[getter]
    #[pyo3(name = "degree")]
    const fn py_degree(&self) -> f64 {
        self.degree
    }

    #[getter]
    #[pyo3(name = "cfo")]
    const fn py_cfo(&self) -> f64 {
        self.cfo
    }

    #[getter]
    #[pyo3(name = "r2")]
    const fn py_r2(&self) -> f64 {
        self.r2
    }

    #[getter]
    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[getter]
    #[pyo3(name = "value")]
    const fn py_value(&self) -> f64 {
        self.value
    }

    #[getter]
    #[pyo3(name = "initialized")]
    const fn py_initialized(&self) -> bool {
        self.initialized
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, close: f64) {
        self.update_raw(close);
    }

    #[pyo3(name = "handle_bar")]
    fn py_handle_bar(&mut self, bar: &Bar) {
        self.handle_bar(bar);
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 15 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_period()`**: Function defined in this file
- **`py_slope()`**: Function defined in this file
- **`py_intercept()`**: Function defined in this file
- **`py_degree()`**: Function defined in this file
- **`py_cfo()`**: Function defined in this file
- **`py_r2()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_value()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_update_raw()`**: Function defined in this file
- **`py_handle_bar()`**: Function defined in this file
- **`py_reset()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Functions**: `__repr__`, `py_cfo`, `py_degree`, `py_handle_bar`, `py_has_inputs`, `py_initialized`, `py_intercept`, `py_name`, `py_new`, `py_period`, `py_r2`, `py_reset`, `py_slope`, `py_update_raw`, `py_value`
**Impls**: `LinearRegression`

## Related Files

This file is located in `crates/indicators/src/python/average/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.863618Z*
