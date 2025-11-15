# Documentation: `crates/indicators/src/python/ratio/spread_analyzer.rs`
**Generated:** 2025-11-15T19:40:02.257482Z
**File Size:** 2210 bytes
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

- **Path:** `crates/indicators/src/python/ratio/spread_analyzer.rs`
- **Size:** 2,210 bytes
- **Lines:** 76
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 10

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

use nautilus_model::{data::QuoteTick, identifiers::InstrumentId};
use pyo3::prelude::*;

use crate::{indicator::Indicator, ratio::spread_analyzer::SpreadAnalyzer};

#[pymethods]
impl SpreadAnalyzer {
    #[new]
    fn py_new(instrument_id: InstrumentId, capacity: usize) -> Self {
        Self::new(capacity, instrument_id)
    }

    fn __repr__(&self) -> String {
        format!("SpreadAnalyzer({})", self.capacity)
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[getter]
    #[pyo3(name = "capacity")]
    const fn py_capacity(&self) -> usize {
        self.capacity
    }

    #[getter]
    #[pyo3(name = "current")]
    const fn py_current(&self) -> f64 {
        self.current
    }

    #[getter]
    #[pyo3(name = "average")]
    const fn py_average(&self) -> f64 {
        self.average
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

    #[pyo3(name = "handle_quote_tick")]
    fn py_handle_quote_tick(&mut self, quote: &QuoteTick) {
        self.handle_quote(quote);
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }
}
```


---

## Overview

This file is located at `crates/indicators/src/python/ratio/spread_analyzer.rs` within the repository.

**Classes defined:** SpreadAnalyzer

**Functions defined:** py_new, __repr__, py_name, py_capacity, py_current, py_average, py_initialized, py_has_inputs, py_handle_quote_tick, py_reset


---

## Detailed Analysis

### Classes

#### `SpreadAnalyzer`

**Type:** impl


### Functions

#### `py_new(instrument_id: InstrumentId, capacity: usize)`


#### `__repr__(&self)`


#### `py_name(&self)`


#### `py_capacity(&self)`


#### `py_current(&self)`


#### `py_average(&self)`


#### `py_initialized(&self)`


#### `py_has_inputs(&self)`


#### `py_handle_quote_tick(&mut self, quote: &QuoteTick)`


#### `py_reset(&mut self)`



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


