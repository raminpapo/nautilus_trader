# Documentation: fuzzy.rs

## File Metadata

- **Path**: `crates/indicators/src/python/volatility/fuzzy.rs`
- **Size**: 4,442 bytes
- **Lines**: 174
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

use crate::{
    indicator::Indicator,
    volatility::fuzzy::{
        CandleBodySize, CandleDirection, CandleSize, CandleWickSize, FuzzyCandle, FuzzyCandlesticks,
    },
};

#[pymethods]
impl FuzzyCandle {
    #[new]
    #[must_use]
    pub const fn py_new(
        direction: CandleDirection,
        size: CandleSize,
        body_size: CandleBodySize,
        upper_wick_size: CandleWickSize,
        lower_wick_size: CandleWickSize,
    ) -> Self {
        Self::new(direction, size, body_size, upper_wick_size, lower_wick_size)
    }

    fn __repr__(&self) -> String {
        format!(
            "FuzzyCandle({},{},{},{},{})",
            self.direction, self.size, self.body_size, self.upper_wick_size, self.lower_wick_size
        )
    }

    #[getter]
    #[pyo3(name = "direction")]
    const fn py_direction(&self) -> CandleDirection {
        self.direction
    }

    #[getter]
    #[pyo3(name = "size")]
    const fn py_size(&self) -> CandleSize {
        self.size
    }

    #[getter]
    #[pyo3(name = "body_size")]
    const fn py_body_size(&self) -> CandleBodySize {
        self.body_size
    }

    #[getter]
    #[pyo3(name = "upper_wick_size")]
    const fn py_upper_wick_size(&self) -> CandleWickSize {
        self.upper_wick_size
    }

    #[getter]
    #[pyo3(name = "lower_wick_size")]
    const fn py_lower_wick_size(&self) -> CandleWickSize {
        self.lower_wick_size
    }
}

#[pymethods]
impl FuzzyCandlesticks {
    #[new]
    #[must_use]
    pub fn py_new(
        period: usize,
        threshold1: f64,
        threshold2: f64,
        threshold3: f64,
        threshold4: f64,
    ) -> Self {
        Self::new(period, threshold1, threshold2, threshold3, threshold4)
    }

    fn __repr__(&self) -> String {
        format!(
            "FuzzyCandlesticks({},{},{},{},{})",
            self.period, self.threshold1, self.threshold2, self.threshold3, self.threshold4
        )
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
    #[pyo3(name = "threshold1")]
    const fn py_threshold1(&self) -> f64 {
        self.threshold1
    }

    #[getter]
    #[pyo3(name = "threshold2")]
    const fn py_threshold2(&self) -> f64 {
        self.threshold2
    }

    #[getter]
    #[pyo3(name = "threshold3")]
    const fn py_threshold3(&self) -> f64 {
        self.threshold3
    }

    #[getter]
    #[pyo3(name = "threshold4")]
    const fn py_threshold4(&self) -> f64 {
        self.threshold4
    }

    #[getter]
    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[getter]
    #[pyo3(name = "value")]
    const fn py_value(&self) -> FuzzyCandle {
        self.value
    }

    #[getter]
    #[pyo3(name = "vector")]
    fn py_vector(&self) -> PyResult<Vec<i32>> {
        Result::<_, PyErr>::Ok(self.vector.clone())
    }

    #[getter]
    #[pyo3(name = "initialized")]
    const fn py_initialized(&self) -> bool {
        self.initialized
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, open: f64, high: f64, low: f64, close: f64) {
        self.update_raw(open, high, low, close);
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

This file is part of the NautilusTrader repository. It defines 22 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_direction()`**: Function defined in this file
- **`py_size()`**: Function defined in this file
- **`py_body_size()`**: Function defined in this file
- **`py_upper_wick_size()`**: Function defined in this file
- **`py_lower_wick_size()`**: Function defined in this file
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_period()`**: Function defined in this file
- **`py_threshold1()`**: Function defined in this file
- **`py_threshold2()`**: Function defined in this file
- **`py_threshold3()`**: Function defined in this file
- **`py_threshold4()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_value()`**: Function defined in this file
- **`py_vector()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_update_raw()`**: Function defined in this file

*...and 2 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 22


**Functions**: `__repr__`, `py_body_size`, `py_direction`, `py_handle_bar`, `py_has_inputs`, `py_initialized`, `py_lower_wick_size`, `py_name`, `py_new`, `py_period`, `py_reset`, `py_size`, `py_threshold1`, `py_threshold2`, `py_threshold3`, `py_threshold4`, `py_update_raw`, `py_upper_wick_size`, `py_value`, `py_vector`
**Impls**: `FuzzyCandle`, `FuzzyCandlesticks`

## Related Files

This file is located in `crates/indicators/src/python/volatility/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.933962Z*
