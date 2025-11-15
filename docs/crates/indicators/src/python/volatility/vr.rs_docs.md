# Documentation: `crates/indicators/src/python/volatility/vr.rs`
**Generated:** 2025-11-15T19:40:02.271192Z
**File Size:** 3274 bytes
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

- **Path:** `crates/indicators/src/python/volatility/vr.rs`
- **Size:** 3,274 bytes
- **Lines:** 112
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

use nautilus_model::data::{Bar, QuoteTick, TradeTick};
use pyo3::prelude::*;

use crate::{average::MovingAverageType, indicator::Indicator, volatility::vr::VolatilityRatio};

#[pymethods]
impl VolatilityRatio {
    #[new]
    #[pyo3(signature = (fast_period, slow_period, use_previous=None, value_floor=None, ma_type=None))]
    #[must_use]
    pub fn py_new(
        fast_period: usize,
        slow_period: usize,
        use_previous: Option<bool>,
        value_floor: Option<f64>,
        ma_type: Option<MovingAverageType>,
    ) -> Self {
        Self::new(fast_period, slow_period, ma_type, use_previous, value_floor)
    }

    fn __repr__(&self) -> String {
        format!("VolatilityRatio({},{})", self.fast_period, self.slow_period)
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
    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[getter]
    #[pyo3(name = "use_previous")]
    const fn py_use_previous(&self) -> bool {
        self.use_previous
    }

    #[getter]
    #[pyo3(name = "value_floor")]
    const fn py_value_floor(&self) -> f64 {
        self.value_floor
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

    #[pyo3(name = "handle_quote_tick")]
    const fn py_handle_quote_tick(&mut self, _quote: &QuoteTick) {
        // Function body intentionally left blank.
    }

    #[pyo3(name = "handle_trade_tick")]
    const fn py_handle_trade_tick(&mut self, _trade: &TradeTick) {
        // Function body intentionally left blank.
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

This file is located at `crates/indicators/src/python/volatility/vr.rs` within the repository.

**Classes defined:** VolatilityRatio

**Functions defined:** py_new, __repr__, py_name, py_fast_period, py_slow_period, py_has_inputs, py_use_previous, py_value_floor, py_value, py_initialized and 5 more


---

## Detailed Analysis

### Classes

#### `VolatilityRatio`

**Type:** impl


### Functions

#### `py_new(
        fast_period: usize,
        slow_period: usize,
        use_previous: Option<bool>,
        value_floor: Option<f64>,
        ma_type: Option<MovingAverageType>,
    )`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_fast_period(&self)`


#### `py_slow_period(&self)`


#### `py_has_inputs(&self)`


#### `py_use_previous(&self)`


#### `py_value_floor(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64, close: f64)`


#### `py_handle_quote_tick(&mut self, _quote: &QuoteTick)`


#### `py_handle_trade_tick(&mut self, _trade: &TradeTick)`


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


