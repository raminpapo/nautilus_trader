# Documentation: `crates/indicators/src/python/average/vwap.rs`
**Generated:** 2025-11-15T19:40:02.218237Z
**File Size:** 2160 bytes
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

- **Path:** `crates/indicators/src/python/average/vwap.rs`
- **Size:** 2,160 bytes
- **Lines:** 75
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 9

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

use crate::{average::vwap::VolumeWeightedAveragePrice, indicator::Indicator};

#[pymethods]
impl VolumeWeightedAveragePrice {
    #[new]
    #[must_use]
    pub const fn py_new() -> Self {
        Self::new()
    }

    fn __repr__(&self) -> String {
        "VolumeWeightedAveragePrice".to_string()
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
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

    #[pyo3(name = "handle_bar")]
    fn py_handle_bar(&mut self, bar: &Bar) {
        self.py_update_raw(
            (&bar.close).into(),
            (&bar.volume).into(),
            bar.ts_init.as_f64(),
        );
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, value: f64, volume: f64, ts: f64) {
        self.update_raw(value, volume, ts);
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/average/vwap.rs` within the repository.

**Classes defined:** VolumeWeightedAveragePrice

**Functions defined:** py_new, __repr__, py_name, py_has_inputs, py_value, py_initialized, py_handle_bar, py_reset, py_update_raw


---

## Detailed Analysis

### Classes

#### `VolumeWeightedAveragePrice`

**Type:** impl


### Functions

#### `py_new()`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_has_inputs(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_handle_bar(&mut self, bar: &Bar)`


#### `py_reset(&mut self)`


#### `py_update_raw(&mut self, value: f64, volume: f64, ts: f64)`



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


