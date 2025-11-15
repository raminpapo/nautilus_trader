# Documentation: `crates/indicators/src/python/momentum/kvo.rs`
**Generated:** 2025-11-15T19:40:02.235632Z
**File Size:** 2851 bytes
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

- **Path:** `crates/indicators/src/python/momentum/kvo.rs`
- **Size:** 2,851 bytes
- **Lines:** 100
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 12

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


---

## Overview

This file is located at `crates/indicators/src/python/momentum/kvo.rs` within the repository.

**Classes defined:** KlingerVolumeOscillator

**Functions defined:** py_new, __repr__, py_name, py_fast_period, py_slow_period, py_signal_period, py_has_inputs, py_value, py_initialized, py_update_raw and 2 more


---

## Detailed Analysis

### Classes

#### `KlingerVolumeOscillator`

**Type:** impl


### Functions

#### `py_new(
        fast_period: usize,
        slow_period: usize,
        signal_period: usize,
        ma_type: Option<MovingAverageType>,
    )`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_fast_period(&self)`


#### `py_slow_period(&self)`


#### `py_signal_period(&self)`


#### `py_has_inputs(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64, close: f64, volume: f64)`


#### `py_handle_bar(&mut self, bar: &Bar)`


#### `py_reset(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src/python/momentum`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


