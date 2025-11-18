# Documentation: kp.rs

## File Metadata

- **Path**: `crates/indicators/src/python/volatility/kp.rs`
- **Size**: 3,016 bytes
- **Lines**: 111
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

use crate::{average::MovingAverageType, indicator::Indicator, volatility::kp::KeltnerPosition};

#[pymethods]
impl KeltnerPosition {
    #[new]
    #[pyo3(signature = (period, k_multiplier, ma_type=None, ma_type_atr=None, use_previous=None, atr_floor=None))]
    #[must_use]
    pub fn py_new(
        period: usize,
        k_multiplier: f64,
        ma_type: Option<MovingAverageType>,
        ma_type_atr: Option<MovingAverageType>,
        use_previous: Option<bool>,
        atr_floor: Option<f64>,
    ) -> Self {
        Self::new(
            period,
            k_multiplier,
            ma_type,
            ma_type_atr,
            use_previous,
            atr_floor,
        )
    }

    fn __repr__(&self) -> String {
        format!("KeltnerPosition({})", self.period)
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
    #[pyo3(name = "k_multiplier")]
    const fn py_k_multiplier(&self) -> f64 {
        self.k_multiplier
    }

    #[getter]
    #[pyo3(name = "use_previous")]
    const fn py_use_previous(&self) -> bool {
        self.use_previous
    }

    #[getter]
    #[pyo3(name = "atr_floor")]
    const fn py_atr_floor(&self) -> f64 {
        self.atr_floor
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
    fn py_update_raw(&mut self, high: f64, low: f64, close: f64) {
        self.update_raw(high, low, close);
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

This file is part of the NautilusTrader repository. It defines 13 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_period()`**: Function defined in this file
- **`py_k_multiplier()`**: Function defined in this file
- **`py_use_previous()`**: Function defined in this file
- **`py_atr_floor()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_value()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_update_raw()`**: Function defined in this file
- **`py_handle_bar()`**: Function defined in this file
- **`py_reset()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `__repr__`, `py_atr_floor`, `py_handle_bar`, `py_has_inputs`, `py_initialized`, `py_k_multiplier`, `py_name`, `py_new`, `py_period`, `py_reset`, `py_update_raw`, `py_use_previous`, `py_value`
**Impls**: `KeltnerPosition`

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
*Generated on 2025-11-18T21:55:01.939883Z*
