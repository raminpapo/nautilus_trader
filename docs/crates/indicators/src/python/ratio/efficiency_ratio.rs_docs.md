# Documentation: `crates/indicators/src/python/ratio/efficiency_ratio.rs`
**Generated:** 2025-11-15T19:40:02.254100Z
**File Size:** 1997 bytes
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

- **Path:** `crates/indicators/src/python/ratio/efficiency_ratio.rs`
- **Size:** 1,997 bytes
- **Lines:** 66
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 8

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

use nautilus_model::enums::PriceType;
use pyo3::prelude::*;

use crate::{indicator::Indicator, ratio::efficiency_ratio::EfficiencyRatio};

#[pymethods]
impl EfficiencyRatio {
    #[new]
    #[pyo3(signature = (period, price_type=None))]
    fn py_new(period: usize, price_type: Option<PriceType>) -> Self {
        Self::new(period, price_type)
    }

    fn __repr__(&self) -> String {
        format!("EfficiencyRatio({})", self.period)
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
    #[pyo3(name = "value")]
    const fn py_value(&self) -> f64 {
        self.value
    }

    #[getter]
    #[pyo3(name = "initialized")]
    const fn py_initialized(&self) -> bool {
        self.initialized
    }

    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[pyo3(name = "update_raw")]
    fn py_update_raw(&mut self, value: f64) {
        self.update_raw(value);
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/ratio/efficiency_ratio.rs` within the repository.

**Classes defined:** EfficiencyRatio

**Functions defined:** py_new, __repr__, py_name, py_period, py_value, py_initialized, py_has_inputs, py_update_raw


---

## Detailed Analysis

### Classes

#### `EfficiencyRatio`

**Type:** impl


### Functions

#### `py_new(period: usize, price_type: Option<PriceType>)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_period(&self)`


#### `py_value(&self)`


#### `py_initialized(&self)`


#### `py_has_inputs(&self)`


#### `py_update_raw(&mut self, value: f64)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src/python/ratio`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


