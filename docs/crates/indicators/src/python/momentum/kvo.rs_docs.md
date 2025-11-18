# Documentation: kvo.rs

## File Metadata

- **Path**: `crates/indicators/src/python/momentum/kvo.rs`
- **Size**: 2,851 bytes
- **Lines**: 101
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
    average::MovingAverageType, indicator::Indicator, momentum::kvo::KlingerVolumeOscillator,
};

#[pymethods]
impl KlingerVolumeOscillator {
    #[new]
    #[pyo3(signature = (fast_period, slow_period, signal_period, ma_type=None))]
    #[must_use]
    pub fn py_new(
        fast_period: usize,
        slow_period: usize,
        signal_period: usize,
        ma_type: Option<MovingAverageType>,
    ) -> Self {
        Self::new(fast_period, slow_period, signal_period, ma_type)
    }

    fn __repr__(&self) -> String {
        format!(
            "KlingerVolumeOscillator({},{},{},{})",
            self.fast_period, self.slow_period, self.signal_period, self.ma_type
        )
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[getter]
    #[pyo3(name = "fast_period")]
    const fn py_fast_period(&self) -> usize {
        self.fast_period
    }

    #[getter]
    #[pyo3(name = "slow_period")]
    const fn py_slow_period(&self) -> usize {
        self.slow_period
    }

    #[getter]
    #[pyo3(name = "signal_period")]
    const fn py_signal_period(&self) -> usize {
        self.signal_period
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
    fn py_update_raw(&mut self, high: f64, low: f64, close: f64, volume: f64) {
        self.update_raw(high, low, close, volume);
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

This file is part of the NautilusTrader repository. It defines 12 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_fast_period()`**: Function defined in this file
- **`py_slow_period()`**: Function defined in this file
- **`py_signal_period()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_value()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_update_raw()`**: Function defined in this file
- **`py_handle_bar()`**: Function defined in this file
- **`py_reset()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Functions**: `__repr__`, `py_fast_period`, `py_handle_bar`, `py_has_inputs`, `py_initialized`, `py_name`, `py_new`, `py_reset`, `py_signal_period`, `py_slow_period`, `py_update_raw`, `py_value`
**Impls**: `KlingerVolumeOscillator`

## Related Files

This file is located in `crates/indicators/src/python/momentum/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.901790Z*
