# Documentation: config.rs

## File Metadata

- **Path**: `crates/adapters/tardis/src/python/config.rs`
- **Size**: 2,569 bytes
- **Lines**: 83
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`py_instrument_id()`**: Function defined in this file
- **`py_raw_symbol()`**: Function defined in this file
- **`py_exchange()`**: Function defined in this file
- **`py_price_precision()`**: Function defined in this file
- **`py_size_precision()`**: Function defined in this file
- **`py_bar_spec_to_tardis_trade_bar_string()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `py_bar_spec_to_tardis_trade_bar_string`, `py_exchange`, `py_instrument_id`, `py_new`, `py_price_precision`, `py_raw_symbol`, `py_size_precision`
**Impls**: `TardisInstrumentMiniInfo`

## Related Files

This file is located in `crates/adapters/tardis/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.724166Z*
