# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/databento/src/python/enums.rs`
- **Size**: 5,450 bytes
- **Lines**: 212
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

use std::str::FromStr;

use nautilus_core::python::to_pyvalue_err;
use pyo3::{PyTypeInfo, prelude::*, types::PyType};

use crate::enums::{DatabentoStatisticType, DatabentoStatisticUpdateAction};

#[pymethods]
impl DatabentoStatisticType {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value).map_err(to_pyvalue_err)
    }

    const fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(DatabentoStatisticType),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub const fn value(&self) -> u8 {
        *self as u8
    }

    // #[classmethod]
    // fn variants(_: &PyType, py: Python<'_>) -> EnumIterator {
    //     EnumIterator::new::<Self>(py)
    // }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: &str = data.extract()?;
        let tokenized = data_str.to_uppercase();
        Self::from_str(&tokenized).map_err(to_pyvalue_err)
    }
    #[classattr]
    #[pyo3(name = "OPENING_PRICE")]
    const fn py_opening_price() -> Self {
        Self::OpeningPrice
    }

    #[classattr]
    #[pyo3(name = "INDICATIVE_OPENING_PRICE")]
    const fn py_indicative_opening_price() -> Self {
        Self::IndicativeOpeningPrice
    }

    #[classattr]
    #[pyo3(name = "SETTLEMENT_PRICE")]
    const fn py_settlement_price() -> Self {
        Self::SettlementPrice
    }

    #[classattr]
    #[pyo3(name = "TRADING_SESSION_LOW_PRICE")]
    const fn py_trading_session_low_price() -> Self {
        Self::TradingSessionLowPrice
    }

    #[classattr]
    #[pyo3(name = "TRADING_SESSION_HIGH_PRICE")]
    const fn py_trading_session_high_price() -> Self {
        Self::TradingSessionHighPrice
    }

    #[classattr]
    #[pyo3(name = "CLEARED_VOLUME")]
    const fn py_cleared_volume() -> Self {
        Self::ClearedVolume
    }

    #[classattr]
    #[pyo3(name = "LOWEST_OFFER")]
    const fn py_lowest_offer() -> Self {
        Self::LowestOffer
    }

    #[classattr]
    #[pyo3(name = "HIGHEST_BID")]
    const fn py_highest_bid() -> Self {
        Self::HighestBid
    }

    #[classattr]
    #[pyo3(name = "OPEN_INTEREST")]
    const fn py_open_interest() -> Self {
        Self::OpenInterest
    }

    #[classattr]
    #[pyo3(name = "FIXING_PRICE")]
    const fn py_fixing_price() -> Self {
        Self::FixingPrice
    }

    #[classattr]
    #[pyo3(name = "CLOSE_PRICE")]
    const fn py_close_price() -> Self {
        Self::ClosePrice
    }

    #[classattr]
    #[pyo3(name = "NET_CHANGE")]
    const fn py_net_change() -> Self {
        Self::NetChange
    }

    #[classattr]
    #[pyo3(name = "VWAP")]
    const fn py_vwap() -> Self {
        Self::Vwap
    }
}

#[pymethods]
impl DatabentoStatisticUpdateAction {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value).map_err(to_pyvalue_err)
    }

    const fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(DatabentoStatisticUpdateAction),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub const fn value(&self) -> u8 {
        *self as u8
    }

    // #[classmethod]
    // fn variants(_: &PyType, py: Python<'_>) -> EnumIterator {
    //     EnumIterator::new::<Self>(py)
    // }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: &str = data.extract()?;
        let tokenized = data_str.to_uppercase();
        Self::from_str(&tokenized).map_err(to_pyvalue_err)
    }
    #[classattr]
    #[pyo3(name = "ADDED")]
    const fn py_added() -> Self {
        Self::Added
    }

    #[classattr]
    #[pyo3(name = "DELETED")]
    const fn py_deleted() -> Self {
        Self::Deleted
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 31 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__hash__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`value()`**: Function defined in this file
- **`variants()`**: Function defined in this file
- **`py_from_str()`**: Function defined in this file
- **`py_opening_price()`**: Function defined in this file
- **`py_indicative_opening_price()`**: Function defined in this file
- **`py_settlement_price()`**: Function defined in this file
- **`py_trading_session_low_price()`**: Function defined in this file
- **`py_trading_session_high_price()`**: Function defined in this file
- **`py_cleared_volume()`**: Function defined in this file
- **`py_lowest_offer()`**: Function defined in this file
- **`py_highest_bid()`**: Function defined in this file
- **`py_open_interest()`**: Function defined in this file
- **`py_fixing_price()`**: Function defined in this file
- **`py_close_price()`**: Function defined in this file
- **`py_net_change()`**: Function defined in this file

*...and 11 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 25


**Functions**: `__hash__`, `__repr__`, `__str__`, `name`, `py_added`, `py_cleared_volume`, `py_close_price`, `py_deleted`, `py_fixing_price`, `py_from_str`, `py_highest_bid`, `py_indicative_opening_price`, `py_lowest_offer`, `py_net_change`, `py_new`, `py_open_interest`, `py_opening_price`, `py_settlement_price`, `py_trading_session_high_price`, `py_trading_session_low_price`, `py_vwap`, `value`, `variants`
**Impls**: `DatabentoStatisticType`, `DatabentoStatisticUpdateAction`

## Related Files

This file is located in `crates/adapters/databento/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.722595Z*
