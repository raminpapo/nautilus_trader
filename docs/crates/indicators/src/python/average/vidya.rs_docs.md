# Documentation: vidya.rs

## File Metadata

- **Path**: `crates/indicators/src/python/average/vidya.rs`
- **Size**: 3,187 bytes
- **Lines**: 120
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

use nautilus_model::{
    data::{Bar, QuoteTick, TradeTick},
    enums::PriceType,
};
use pyo3::prelude::*;

use crate::{
    average::{MovingAverageType, vidya::VariableIndexDynamicAverage},
    indicator::{Indicator, MovingAverage},
};

#[pymethods]
impl VariableIndexDynamicAverage {
    #[new]
    #[pyo3(signature = (period, price_type=None, cmo_ma_type=None))]
    #[must_use]
    pub fn py_new(
        period: usize,
        price_type: Option<PriceType>,
        cmo_ma_type: Option<MovingAverageType>,
    ) -> Self {
        Self::new(period, price_type, cmo_ma_type)
    }

    fn __repr__(&self) -> String {
        format!(
            "VariableIndexDynamicAverage({},{:?})",
            self.period, self.price_type
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
    #[pyo3(name = "count")]
    fn py_count(&self) -> usize {
        self.count()
    }

    #[getter]
    #[pyo3(name = "alpha")]
    const fn py_alpha(&self) -> f64 {
        self.alpha
    }

    #[getter]
    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[getter]
    #[pyo3(name = "initialized")]
    const fn py_initialized(&self) -> bool {
        self.initialized
    }

    #[getter]
    #[pyo3(name = "cmo_pct")]
    const fn py_cmo_pct(&self) -> f64 {
        self.cmo_pct
    }

    #[getter]
    #[pyo3(name = "value")]
    const fn py_value(&self) -> f64 {
        self.value
    }

    #[pyo3(name = "handle_quote_tick")]
    fn py_handle_quote_tick(&mut self, quote: &QuoteTick) {
        self.py_update_raw(quote.extract_price(self.price_type).into());
    }

    #[pyo3(name = "handle_trade_tick")]
    fn py_handle_trade_tick(&mut self, trade: &TradeTick) {
        self.update_raw((&trade.price).into());
    }

    #[pyo3(name = "handle_bar")]
    fn py_handle_bar(&mut self, bar: &Bar) {
        self.update_raw((&bar.close).into());
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, value: f64) {
        self.update_raw(value);
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 15 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_period()`**: Function defined in this file
- **`py_count()`**: Function defined in this file
- **`py_alpha()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_cmo_pct()`**: Function defined in this file
- **`py_value()`**: Function defined in this file
- **`py_handle_quote_tick()`**: Function defined in this file
- **`py_handle_trade_tick()`**: Function defined in this file
- **`py_handle_bar()`**: Function defined in this file
- **`py_reset()`**: Function defined in this file
- **`py_update_raw()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Functions**: `__repr__`, `py_alpha`, `py_cmo_pct`, `py_count`, `py_handle_bar`, `py_handle_quote_tick`, `py_handle_trade_tick`, `py_has_inputs`, `py_initialized`, `py_name`, `py_new`, `py_period`, `py_reset`, `py_update_raw`, `py_value`
**Impls**: `VariableIndexDynamicAverage`

## Related Files

This file is located in `crates/indicators/src/python/average/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.871142Z*
