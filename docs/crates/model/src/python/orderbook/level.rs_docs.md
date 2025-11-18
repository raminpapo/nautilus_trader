# Documentation: level.rs

## File Metadata

- **Path**: `crates/model/src/python/orderbook/level.rs`
- **Size**: 2,161 bytes
- **Lines**: 81
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s).

## Detailed Walkthrough

### Functions
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`py_price()`**: Function defined in this file
- **`py_len()`**: Function defined in this file
- **`py_is_empty()`**: Function defined in this file
- **`py_size()`**: Function defined in this file
- **`py_size_raw()`**: Function defined in this file
- **`py_exposure()`**: Function defined in this file
- **`py_exposure_raw()`**: Function defined in this file
- **`py_fist()`**: Function defined in this file
- **`py_get_orders()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Functions**: `__repr__`, `__str__`, `py_exposure`, `py_exposure_raw`, `py_fist`, `py_get_orders`, `py_is_empty`, `py_len`, `py_price`, `py_size`, `py_size_raw`
**Impls**: `BookLevel`

## Related Files

This file is located in `crates/model/src/python/orderbook/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.151972Z*
