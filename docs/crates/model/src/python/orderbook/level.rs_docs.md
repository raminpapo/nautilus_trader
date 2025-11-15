# Documentation: `crates/model/src/python/orderbook/level.rs`
**Generated:** 2025-11-15T19:40:03.089645Z
**File Size:** 2161 bytes
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

- **Path:** `crates/model/src/python/orderbook/level.rs`
- **Size:** 2,161 bytes
- **Lines:** 80
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

use pyo3::prelude::*;

use crate::{
    data::order::BookOrder,
    orderbook::BookLevel,
    types::{price::Price, quantity::QuantityRaw},
};

#[pymethods]
impl BookLevel {
    fn __repr__(&self) -> String {
        format!("{self:?}")
    }

    fn __str__(&self) -> String {
        // TODO: Return debug string for now
        format!("{self:?}")
    }

    #[getter]
    #[pyo3(name = "price")]
    fn py_price(&self) -> Price {
        self.price.value
    }

    #[pyo3(name = "len")]
    fn py_len(&self) -> usize {
        self.len()
    }

    #[pyo3(name = "is_empty")]
    fn py_is_empty(&self) -> bool {
        self.is_empty()
    }

    #[pyo3(name = "size")]
    fn py_size(&self) -> f64 {
        self.size()
    }

    #[pyo3(name = "size_raw")]
    fn py_size_raw(&self) -> QuantityRaw {
        self.size_raw()
    }

    #[pyo3(name = "exposure")]
    fn py_exposure(&self) -> f64 {
        self.exposure()
    }

    #[pyo3(name = "exposure_raw")]
    fn py_exposure_raw(&self) -> QuantityRaw {
        self.exposure_raw()
    }

    #[pyo3(name = "first")]
    fn py_fist(&self) -> Option<BookOrder> {
        self.first().copied()
    }

    #[pyo3(name = "get_orders")]
    fn py_get_orders(&self) -> Vec<BookOrder> {
        self.get_orders()
    }
}
```


---

## Overview

This file is located at `crates/model/src/python/orderbook/level.rs` within the repository.

**Classes defined:** BookLevel

**Functions defined:** __repr__, __str__, py_price, py_len, py_is_empty, py_size, py_size_raw, py_exposure, py_exposure_raw, py_fist and 1 more


---

## Detailed Analysis

### Classes

#### `BookLevel`

**Type:** impl


### Functions

#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_price(&self)`


#### `py_len(&self)`


#### `py_is_empty(&self)`


#### `py_size(&self)`


#### `py_size_raw(&self)`


#### `py_exposure(&self)`


#### `py_exposure_raw(&self)`


#### `py_fist(&self)`


#### `py_get_orders(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/orderbook`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


