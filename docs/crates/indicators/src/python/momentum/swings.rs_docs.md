# Documentation: `crates/indicators/src/python/momentum/swings.rs`
**Generated:** 2025-11-15T19:40:02.250442Z
**File Size:** 3635 bytes
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

- **Path:** `crates/indicators/src/python/momentum/swings.rs`
- **Size:** 3,635 bytes
- **Lines:** 141
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 21

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

use crate::{indicator::Indicator, momentum::swings::Swings};

#[pymethods]
impl Swings {
    #[new]
    #[must_use]
    pub fn py_new(period: usize) -> Self {
        Self::new(period)
    }

    fn __repr__(&self) -> String {
        format!("Swings({})", self.period)
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
    #[pyo3(name = "direction")]
    const fn py_direction(&self) -> i64 {
        self.direction
    }

    #[getter]
    #[pyo3(name = "changed")]
    const fn py_changed(&self) -> bool {
        self.changed
    }

    #[getter]
    #[pyo3(name = "high_datetime")]
    const fn py_high_datetime(&self) -> f64 {
        self.high_datetime
    }

    #[getter]
    #[pyo3(name = "low_datetime")]
    const fn py_low_datetime(&self) -> f64 {
        self.low_datetime
    }

    #[getter]
    #[pyo3(name = "high_price")]
    const fn py_high_price(&self) -> f64 {
        self.high_price
    }

    #[getter]
    #[pyo3(name = "low_price")]
    const fn py_low_price(&self) -> f64 {
        self.low_price
    }

    #[getter]
    #[pyo3(name = "length")]
    const fn py_length(&self) -> usize {
        self.length
    }

    #[getter]
    #[pyo3(name = "duration")]
    const fn py_duration(&self) -> usize {
        self.duration
    }

    #[getter]
    #[pyo3(name = "since_high")]
    const fn py_since_high(&self) -> usize {
        self.since_high
    }

    #[getter]
    #[pyo3(name = "since_low")]
    const fn py_since_low(&self) -> usize {
        self.since_low
    }

    #[getter]
    #[pyo3(name = "initialized")]
    fn py_initialized(&self) -> bool {
        self.initialized()
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, high: f64, low: f64, timestamp: f64) {
        self.update_raw(high, low, timestamp);
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
        self.update_raw((&bar.high).into(), (&bar.low).into(), bar.ts_init.as_f64());
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/momentum/swings.rs` within the repository.

**Classes defined:** Swings

**Functions defined:** py_new, __repr__, py_name, py_period, py_has_inputs, py_direction, py_changed, py_high_datetime, py_low_datetime, py_high_price and 11 more


---

## Detailed Analysis

### Classes

#### `Swings`

**Type:** impl


### Functions

#### `py_new(period: usize)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_has_inputs(&self)`


#### `py_direction(&self)`


#### `py_changed(&self)`


#### `py_high_datetime(&self)`


#### `py_low_datetime(&self)`


#### `py_high_price(&self)`


#### `py_low_price(&self)`


#### `py_length(&self)`


#### `py_duration(&self)`


#### `py_since_high(&self)`


#### `py_since_low(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64, timestamp: f64)`


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


