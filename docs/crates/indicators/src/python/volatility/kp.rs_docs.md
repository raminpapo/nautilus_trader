# Documentation: `crates/indicators/src/python/volatility/kp.rs`
**Generated:** 2025-11-15T19:40:02.267033Z
**File Size:** 3016 bytes
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

- **Path:** `crates/indicators/src/python/volatility/kp.rs`
- **Size:** 3,016 bytes
- **Lines:** 110
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 13

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


---

## Overview

This file is located at `crates/indicators/src/python/volatility/kp.rs` within the repository.

**Classes defined:** KeltnerPosition

**Functions defined:** py_new, __repr__, py_name, py_period, py_k_multiplier, py_use_previous, py_atr_floor, py_has_inputs, py_value, py_initialized and 3 more


---

## Detailed Analysis

### Classes

#### `KeltnerPosition`

**Type:** impl


### Functions

#### `py_new(
        period: usize,
        k_multiplier: f64,
        ma_type: Option<MovingAverageType>,
        ma_type_atr: Option<MovingAverageType>,
        use_previous: Option<bool>,
        atr_floor: Option<f64>,
    )`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_k_multiplier(&self)`


#### `py_use_previous(&self)`


#### `py_atr_floor(&self)`


#### `py_has_inputs(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64, close: f64)`


#### `py_handle_bar(&mut self, bar: &Bar)`


#### `py_reset(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src/python/volatility`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


