# Documentation: `crates/adapters/databento/src/python/enums.rs`
**Generated:** 2025-11-15T19:40:00.875449Z
**File Size:** 5450 bytes
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

- **Path:** `crates/adapters/databento/src/python/enums.rs`
- **Size:** 5,450 bytes
- **Lines:** 211
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 31

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


---

## Overview

This file is located at `crates/adapters/databento/src/python/enums.rs` within the repository.

**Classes defined:** DatabentoStatisticType, DatabentoStatisticUpdateAction

**Functions defined:** py_new, __hash__, __repr__, __str__, name, value, variants, py_from_str, py_opening_price, py_indicative_opening_price and 21 more


---

## Detailed Analysis

### Classes

#### `DatabentoStatisticType`

**Type:** impl


#### `DatabentoStatisticUpdateAction`

**Type:** impl


### Functions

#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants(_: &PyType, py: Python<'_>)`


#### `py_from_str(_: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_opening_price()`


#### `py_indicative_opening_price()`


#### `py_settlement_price()`


#### `py_trading_session_low_price()`


#### `py_trading_session_high_price()`


#### `py_cleared_volume()`


#### `py_lowest_offer()`


#### `py_highest_bid()`


#### `py_open_interest()`


#### `py_fixing_price()`


#### `py_close_price()`


#### `py_net_change()`


#### `py_vwap()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants(_: &PyType, py: Python<'_>)`


#### `py_from_str(_: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_added()`


#### `py_deleted()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento/src/python`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token, session. Ensure proper handling of secrets.


