# Documentation: swings.rs

## File Metadata

- **Path**: `crates/indicators/src/python/momentum/swings.rs`
- **Size**: 3,635 bytes
- **Lines**: 142
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 21 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_period()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_direction()`**: Function defined in this file
- **`py_changed()`**: Function defined in this file
- **`py_high_datetime()`**: Function defined in this file
- **`py_low_datetime()`**: Function defined in this file
- **`py_high_price()`**: Function defined in this file
- **`py_low_price()`**: Function defined in this file
- **`py_length()`**: Function defined in this file
- **`py_duration()`**: Function defined in this file
- **`py_since_high()`**: Function defined in this file
- **`py_since_low()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_update_raw()`**: Function defined in this file
- **`py_handle_quote_tick()`**: Function defined in this file
- **`py_handle_trade_tick()`**: Function defined in this file
- **`py_handle_bar()`**: Function defined in this file

*...and 1 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 22


**Functions**: `__repr__`, `py_changed`, `py_direction`, `py_duration`, `py_handle_bar`, `py_handle_quote_tick`, `py_handle_trade_tick`, `py_has_inputs`, `py_high_datetime`, `py_high_price`, `py_initialized`, `py_length`, `py_low_datetime`, `py_low_price`, `py_name`, `py_new`, `py_period`, `py_reset`, `py_since_high`, `py_since_low`, `py_update_raw`
**Impls**: `Swings`

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
*Generated on 2025-11-18T21:55:01.919821Z*
