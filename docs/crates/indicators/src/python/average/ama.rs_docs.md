# Documentation: `crates/indicators/src/python/average/ama.rs`
**Generated:** 2025-11-15T19:40:02.204380Z
**File Size:** 2949 bytes
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

- **Path:** `crates/indicators/src/python/average/ama.rs`
- **Size:** 2,949 bytes
- **Lines:** 104
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 11

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

use nautilus_model::{
    data::{Bar, QuoteTick, TradeTick},
    enums::PriceType,
};
use pyo3::prelude::*;

use crate::{
    average::ama::AdaptiveMovingAverage,
    indicator::{Indicator, MovingAverage},
};

#[pymethods]
impl AdaptiveMovingAverage {
    #[new]
    #[pyo3(signature = (period_efficiency_ratio, period_fast, period_slow, price_type=None))]
    #[must_use]
    pub fn py_new(
        period_efficiency_ratio: usize,
        period_fast: usize,
        period_slow: usize,
        price_type: Option<PriceType>,
    ) -> Self {
        Self::new(
            period_efficiency_ratio,
            period_fast,
            period_slow,
            price_type,
        )
    }

    fn __repr__(&self) -> String {
        format!(
            "WeightedMovingAverage({}({},{},{})",
            self.name(),
            self.period_efficiency_ratio,
            self.period_fast,
            self.period_slow
        )
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[getter]
    #[pyo3(name = "count")]
    const fn py_count(&self) -> usize {
        self.count
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
    const fn py_reset(&mut self) {
        self.reset();
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, value: f64) {
        self.update_raw(value);
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/average/ama.rs` within the repository.

**Classes defined:** AdaptiveMovingAverage

**Functions defined:** py_new, __repr__, py_name, py_count, py_has_inputs, py_initialized, py_handle_quote_tick, py_handle_trade_tick, py_handle_bar, py_reset and 1 more


---

## Detailed Analysis

### Classes

#### `AdaptiveMovingAverage`

**Type:** impl


### Functions

#### `py_new(
        period_efficiency_ratio: usize,
        period_fast: usize,
        period_slow: usize,
        price_type: Option<PriceType>,
    )`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_count(&self)`


#### `py_has_inputs(&self)`


#### `py_initialized(&self)`


#### `py_handle_quote_tick(&mut self, quote: &QuoteTick)`


#### `py_handle_trade_tick(&mut self, trade: &TradeTick)`


#### `py_handle_bar(&mut self, bar: &Bar)`


#### `py_reset(&mut self)`


#### `py_update_raw(&mut self, value: f64)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src/python/average`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


