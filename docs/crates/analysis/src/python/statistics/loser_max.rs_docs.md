# Documentation: `crates/analysis/src/python/statistics/loser_max.rs`
**Generated:** 2025-11-15T19:40:01.532020Z
**File Size:** 1991 bytes
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

- **Path:** `crates/analysis/src/python/statistics/loser_max.rs`
- **Size:** 1,991 bytes
- **Lines:** 56
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
use pyo3::prelude::*;

use crate::{statistic::PortfolioStatistic, statistics::loser_max::MaxLoser};

#[pymethods]
impl MaxLoser {
    #[new]
    fn py_new() -> Self {
        Self {}
    }

    fn __repr__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[pyo3(name = "calculate_from_realized_pnls")]
    fn py_calculate_from_realized_pnls(&mut self, realized_pnls: Vec<f64>) -> Option<f64> {
        self.calculate_from_realized_pnls(&realized_pnls)
    }

    #[pyo3(name = "calculate_from_returns")]
    #[allow(unused_variables)] // Pattern preserved for consistency across statistics
    fn py_calculate_from_returns(&mut self, _returns: BTreeMap<u64, f64>) -> Option<f64> {
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

This file is located at `crates/analysis/src/python/statistics/loser_max.rs` within the repository.

**Classes defined:** MaxLoser

**Functions defined:** py_new, __repr__, py_name, py_calculate_from_realized_pnls, py_calculate_from_returns, py_calculate_from_positions


---

## Detailed Analysis

### Classes

#### `MaxLoser`

**Type:** impl


### Functions

#### `py_new()`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_calculate_from_realized_pnls(&mut self, realized_pnls: Vec<f64>)`


#### `py_calculate_from_returns(&mut self, _returns: BTreeMap<u64, f64>)`


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


