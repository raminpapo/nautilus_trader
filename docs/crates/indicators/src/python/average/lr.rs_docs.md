# Documentation: `crates/indicators/src/python/average/lr.rs`
**Generated:** 2025-11-15T19:40:02.210731Z
**File Size:** 2652 bytes
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

- **Path:** `crates/indicators/src/python/average/lr.rs`
- **Size:** 2,652 bytes
- **Lines:** 107
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 15

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


---

## Overview

This file is located at `crates/indicators/src/python/average/lr.rs` within the repository.

**Classes defined:** LinearRegression

**Functions defined:** py_new, __repr__, py_name, py_period, py_slope, py_intercept, py_degree, py_cfo, py_r2, py_has_inputs and 5 more


---

## Detailed Analysis

### Classes

#### `LinearRegression`

**Type:** impl


### Functions

#### `py_new(period: usize)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_slope(&self)`


#### `py_intercept(&self)`


#### `py_degree(&self)`


#### `py_cfo(&self)`


#### `py_r2(&self)`


#### `py_has_inputs(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, close: f64)`


#### `py_handle_bar(&mut self, bar: &Bar)`


#### `py_reset(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src/python/average`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


