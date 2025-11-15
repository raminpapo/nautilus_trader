# Documentation: `crates/indicators/src/python/volatility/atr.rs`
**Generated:** 2025-11-15T19:40:02.259508Z
**File Size:** 3048 bytes
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

- **Path:** `crates/indicators/src/python/volatility/atr.rs`
- **Size:** 3,048 bytes
- **Lines:** 102
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

use nautilus_model::data::{Bar, QuoteTick, TradeTick};
use pyo3::prelude::*;

use crate::{average::MovingAverageType, indicator::Indicator, volatility::atr::AverageTrueRange};

#[pymethods]
impl AverageTrueRange {
    #[new]
    #[pyo3(signature = (period, ma_type=None, use_previous=None, value_floor=None))]
    #[must_use]
    pub fn py_new(
        period: usize,
        ma_type: Option<MovingAverageType>,
        use_previous: Option<bool>,
        value_floor: Option<f64>,
    ) -> Self {
        Self::new(period, ma_type, use_previous, value_floor)
    }

    fn __repr__(&self) -> String {
        format!(
            "AverageTrueRange({},{},{},{})",
            self.period, self.ma_type, self.use_previous, self.value_floor,
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
    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[getter]
    #[pyo3(name = "count")]
    const fn py_count(&self) -> usize {
        self.count
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
        self.update_raw((&bar.high).into(), (&bar.low).into(), (&bar.close).into());
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/volatility/atr.rs` within the repository.

**Classes defined:** AverageTrueRange

**Functions defined:** py_new, __repr__, py_name, py_period, py_has_inputs, py_count, py_value, py_initialized, py_update_raw, py_handle_quote_tick and 3 more


---

## Detailed Analysis

### Classes

#### `AverageTrueRange`

**Type:** impl


### Functions

#### `py_new(
        period: usize,
        ma_type: Option<MovingAverageType>,
        use_previous: Option<bool>,
        value_floor: Option<f64>,
    )`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_has_inputs(&self)`


#### `py_count(&self)`


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


