# Documentation: `crates/indicators/src/python/momentum/dm.rs`
**Generated:** 2025-11-15T19:40:02.234230Z
**File Size:** 2377 bytes
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

- **Path:** `crates/indicators/src/python/momentum/dm.rs`
- **Size:** 2,377 bytes
- **Lines:** 84
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

use nautilus_model::data::Bar;
use pyo3::prelude::*;

use crate::{average::MovingAverageType, indicator::Indicator, momentum::dm::DirectionalMovement};

#[pymethods]
impl DirectionalMovement {
    #[new]
    #[pyo3(signature = (period, ma_type=None))]
    #[must_use]
    pub fn py_new(period: usize, ma_type: Option<MovingAverageType>) -> Self {
        Self::new(period, ma_type)
    }

    fn __repr__(&self) -> String {
        format!("DirectionalMovement({},{})", self.period, self.ma_type)
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
    #[pyo3(name = "pos")]
    const fn py_pos(&self) -> f64 {
        self.pos
    }

    #[getter]
    #[pyo3(name = "neg")]
    const fn py_neg(&self) -> f64 {
        self.neg
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

This file is located at `crates/indicators/src/python/momentum/dm.rs` within the repository.

**Classes defined:** DirectionalMovement

**Functions defined:** py_new, __repr__, py_name, py_period, py_has_inputs, py_pos, py_neg, py_initialized, py_update_raw, py_handle_bar and 1 more


---

## Detailed Analysis

### Classes

#### `DirectionalMovement`

**Type:** impl


### Functions

#### `py_new(period: usize, ma_type: Option<MovingAverageType>)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_has_inputs(&self)`


#### `py_pos(&self)`


#### `py_neg(&self)`


#### `py_initialized(&self)`


#### `py_update_raw(&mut self, high: f64, low: f64)`


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


