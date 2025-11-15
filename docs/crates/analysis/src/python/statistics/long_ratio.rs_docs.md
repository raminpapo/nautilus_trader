# Documentation: `crates/analysis/src/python/statistics/long_ratio.rs`
**Generated:** 2025-11-15T19:40:01.529386Z
**File Size:** 2752 bytes
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

- **Path:** `crates/analysis/src/python/statistics/long_ratio.rs`
- **Size:** 2,752 bytes
- **Lines:** 79
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 6

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

use std::collections::BTreeMap;

#[allow(unused_imports)] // Used in template pattern for returns conversion
use nautilus_core::UnixNanos;
use nautilus_model::enums::OrderSide;
use pyo3::prelude::*;

use crate::{statistic::PortfolioStatistic, statistics::long_ratio::LongRatio};

#[pymethods]
impl LongRatio {
    #[new]
    #[pyo3(signature = (precision=None))]
    fn py_new(precision: Option<usize>) -> Self {
        Self::new(precision)
    }

    fn __repr__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[pyo3(name = "calculate_from_positions")]
    fn py_calculate_from_positions(
        &mut self,
        py: Python,
        positions: Vec<Py<PyAny>>,
    ) -> PyResult<Option<f64>> {
        if positions.is_empty() {
            return Ok(None);
        }

        // Extract entry side from each Cython Position object
        // OrderSide.Buy has value 1 in both Cython and Rust
        let mut longs = 0;
        for position in &positions {
            let entry = position.getattr(py, "entry")?;
            let entry_value: u8 = entry.extract(py)?;
            if entry_value == OrderSide::Buy as u8 {
                longs += 1;
            }
        }

        let value = f64::from(longs) / positions.len() as f64;
        let scale = 10f64.powi(self.precision as i32);
        Ok(Some((value * scale).round() / scale))
    }

    #[pyo3(name = "calculate_from_realized_pnls")]
    fn py_calculate_from_realized_pnls(&mut self, _realized_pnls: Vec<f64>) -> Option<f64> {
        None
    }

    #[pyo3(name = "calculate_from_returns")]
    #[allow(unused_variables)] // Pattern preserved for consistency across statistics
    fn py_calculate_from_returns(&mut self, _returns: BTreeMap<u64, f64>) -> Option<f64> {
        None
    }
}
```


---

## Overview

This file is located at `crates/analysis/src/python/statistics/long_ratio.rs` within the repository.

**Classes defined:** LongRatio

**Functions defined:** py_new, __repr__, py_name, py_calculate_from_positions, py_calculate_from_realized_pnls, py_calculate_from_returns


---

## Detailed Analysis

### Classes

#### `LongRatio`

**Type:** impl


### Functions

#### `py_new(precision: Option<usize>)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_calculate_from_positions(
        &mut self,
        py: Python,
        positions: Vec<Py<PyAny>>,
    )`


#### `py_calculate_from_realized_pnls(&mut self, _realized_pnls: Vec<f64>)`


#### `py_calculate_from_returns(&mut self, _returns: BTreeMap<u64, f64>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/analysis/src/python/statistics`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


