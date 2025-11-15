# Documentation: `crates/indicators/src/python/momentum/bb.rs`
**Generated:** 2025-11-15T19:40:02.228316Z
**File Size:** 2899 bytes
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

- **Path:** `crates/indicators/src/python/momentum/bb.rs`
- **Size:** 2,899 bytes
- **Lines:** 106
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

use crate::{average::MovingAverageType, indicator::Indicator, momentum::bb::BollingerBands};

#[pymethods]
impl BollingerBands {
    #[new]
    #[pyo3(signature = (period, k, ma_type=None))]
    #[must_use]
    pub fn py_new(period: usize, k: f64, ma_type: Option<MovingAverageType>) -> Self {
        Self::new(period, k, ma_type)
    }

    fn __repr__(&self) -> String {
        format!("BollingerBands({})", self.period)
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
    #[pyo3(name = "k")]
    const fn py_k(&self) -> f64 {
        self.k
    }

    #[getter]
    #[pyo3(name = "upper")]
    const fn py_upper(&self) -> f64 {
        self.upper
    }

    #[getter]
    #[pyo3(name = "middle")]
    const fn py_middle(&self) -> f64 {
        self.middle
    }

    #[getter]
    #[pyo3(name = "lower")]
    const fn py_lower(&self) -> f64 {
        self.lower
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
    fn py_handle_quote_tick(&mut self, quote: &QuoteTick) {
        self.handle_quote(quote);
    }

    #[pyo3(name = "handle_trade_tick")]
    fn py_handle_trade_tick(&mut self, trade: &TradeTick) {
        self.handle_trade(trade);
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

This file is located at `crates/indicators/src/python/momentum/bb.rs` within the repository.

**Classes defined:** BollingerBands

**Functions defined:** py_new, __repr__, py_name, py_period, py_has_inputs, py_k, py_upper, py_middle, py_lower, py_initialized and 5 more


---

## Detailed Analysis

### Classes

#### `BollingerBands`

**Type:** impl


### Functions

#### `py_new(period: usize, k: f64, ma_type: Option<MovingAverageType>)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_has_inputs(&self)`


#### `py_k(&self)`


#### `py_upper(&self)`


#### `py_middle(&self)`


#### `py_lower(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64, close: f64)`


#### `py_handle_quote_tick(&mut self, quote: &QuoteTick)`


#### `py_handle_trade_tick(&mut self, trade: &TradeTick)`


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


