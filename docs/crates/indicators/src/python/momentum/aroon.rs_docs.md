# Documentation: `crates/indicators/src/python/momentum/aroon.rs`
**Generated:** 2025-11-15T19:40:02.226758Z
**File Size:** 2871 bytes
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

- **Path:** `crates/indicators/src/python/momentum/aroon.rs`
- **Size:** 2,871 bytes
- **Lines:** 105
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

use crate::{indicator::Indicator, momentum::aroon::AroonOscillator};

#[pymethods]
impl AroonOscillator {
    #[new]
    #[must_use]
    pub fn py_new(period: usize) -> Self {
        Self::new(period)
    }

    fn __repr__(&self) -> String {
        format!("AroonOscillator({})", self.period)
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
    #[pyo3(name = "aroon_up")]
    const fn py_aroon_up(&self) -> f64 {
        self.aroon_up
    }

    #[getter]
    #[pyo3(name = "aroon_down")]
    const fn py_aroon_down(&self) -> f64 {
        self.aroon_down
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
    fn py_update_raw(&mut self, high: f64, low: f64) {
        self.update_raw(high, low);
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
        self.update_raw((&bar.close).into(), (&bar.close).into());
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/momentum/aroon.rs` within the repository.

**Classes defined:** AroonOscillator

**Functions defined:** py_new, __repr__, py_name, py_period, py_has_inputs, py_count, py_aroon_up, py_aroon_down, py_value, py_initialized and 5 more


---

## Detailed Analysis

### Classes

#### `AroonOscillator`

**Type:** impl


### Functions

#### `py_new(period: usize)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_has_inputs(&self)`


#### `py_count(&self)`


#### `py_aroon_up(&self)`


#### `py_aroon_down(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64)`


#### `py_handle_quote_tick(&mut self, _quote: &QuoteTick)`


#### `py_handle_trade_tick(&mut self, _trade: &TradeTick)`


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


