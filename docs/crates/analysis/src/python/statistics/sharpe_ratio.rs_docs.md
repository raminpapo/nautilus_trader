# Documentation: `crates/analysis/src/python/statistics/sharpe_ratio.rs`
**Generated:** 2025-11-15T19:40:01.543795Z
**File Size:** 1923 bytes
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

- **Path:** `crates/analysis/src/python/statistics/sharpe_ratio.rs`
- **Size:** 1,923 bytes
- **Lines:** 55
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

use pyo3::prelude::*;

use super::transform_returns;
use crate::{statistic::PortfolioStatistic, statistics::sharpe_ratio::SharpeRatio};

#[pymethods]
impl SharpeRatio {
    #[new]
    #[pyo3(signature = (period=None))]
    fn py_new(period: Option<usize>) -> Self {
        Self::new(period)
    }

    fn __repr__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[pyo3(name = "calculate_from_returns")]
    fn py_calculate_from_returns(&mut self, raw_returns: BTreeMap<u64, f64>) -> Option<f64> {
        self.calculate_from_returns(&transform_returns(raw_returns))
    }

    #[pyo3(name = "calculate_from_realized_pnls")]
    fn py_calculate_from_realized_pnls(&mut self, _realized_pnls: Vec<f64>) -> Option<f64> {
        None
    }

    #[pyo3(name = "calculate_from_positions")]
    fn py_calculate_from_positions(&mut self, _positions: Vec<Py<PyAny>>) -> Option<f64> {
        None
    }
}
```


---

## Overview

This file is located at `crates/analysis/src/python/statistics/sharpe_ratio.rs` within the repository.

**Classes defined:** SharpeRatio

**Functions defined:** py_new, __repr__, py_name, py_calculate_from_returns, py_calculate_from_realized_pnls, py_calculate_from_positions


---

## Detailed Analysis

### Classes

#### `SharpeRatio`

**Type:** impl


### Functions

#### `py_new(period: Option<usize>)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_calculate_from_returns(&mut self, raw_returns: BTreeMap<u64, f64>)`


#### `py_calculate_from_realized_pnls(&mut self, _realized_pnls: Vec<f64>)`


#### `py_calculate_from_positions(&mut self, _positions: Vec<Py<PyAny>>)`



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


