# Documentation: `crates/adapters/tardis/src/python/config.rs`
**Generated:** 2025-11-15T19:40:01.483848Z
**File Size:** 2569 bytes
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

- **Path:** `crates/adapters/tardis/src/python/config.rs`
- **Size:** 2,569 bytes
- **Lines:** 82
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 7

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

use nautilus_model::{data::BarSpecification, identifiers::InstrumentId};
use pyo3::prelude::*;
use ustr::Ustr;

use crate::{
    enums::TardisExchange, machine::types::TardisInstrumentMiniInfo,
    parse::bar_spec_to_tardis_trade_bar_string,
};

#[pymethods]
impl TardisInstrumentMiniInfo {
    #[new]
    fn py_new(
        instrument_id: InstrumentId,
        raw_symbol: String,
        exchange: String,
        price_precision: u8,
        size_precision: u8,
    ) -> PyResult<Self> {
        let exchange: TardisExchange = exchange
            .parse()
            .expect("`exchange` should be Tardis convention");
        Ok(Self::new(
            instrument_id,
            Some(Ustr::from(&raw_symbol)),
            exchange,
            price_precision,
            size_precision,
        ))
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    const fn py_instrument_id(&self) -> InstrumentId {
        self.instrument_id
    }

    #[getter]
    #[pyo3(name = "raw_symbol")]
    fn py_raw_symbol(&self) -> String {
        self.raw_symbol.to_string()
    }

    #[getter]
    #[pyo3(name = "exchange")]
    fn py_exchange(&self) -> String {
        self.exchange.to_string()
    }

    #[getter]
    #[pyo3(name = "price_precision")]
    const fn py_price_precision(&self) -> u8 {
        self.price_precision
    }

    #[getter]
    #[pyo3(name = "size_precision")]
    const fn py_size_precision(&self) -> u8 {
        self.size_precision
    }
}

#[must_use]
#[pyfunction(name = "bar_spec_to_tardis_trade_bar_string")]
pub fn py_bar_spec_to_tardis_trade_bar_string(bar_spec: &BarSpecification) -> String {
    bar_spec_to_tardis_trade_bar_string(bar_spec)
}
```


---

## Overview

This file is located at `crates/adapters/tardis/src/python/config.rs` within the repository.

**Classes defined:** TardisInstrumentMiniInfo

**Functions defined:** py_new, py_instrument_id, py_raw_symbol, py_exchange, py_price_precision, py_size_precision, py_bar_spec_to_tardis_trade_bar_string


---

## Detailed Analysis

### Classes

#### `TardisInstrumentMiniInfo`

**Type:** impl


### Functions

#### `py_new(
        instrument_id: InstrumentId,
        raw_symbol: String,
        exchange: String,
        price_precision: u8,
        size_precision: u8,
    )`


#### `py_instrument_id(&self)`


#### `py_raw_symbol(&self)`


#### `py_exchange(&self)`


#### `py_price_precision(&self)`


#### `py_size_precision(&self)`


#### `py_bar_spec_to_tardis_trade_bar_string(bar_spec: &BarSpecification)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


