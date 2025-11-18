# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/hyperliquid/src/python/enums.rs`
- **Size**: 8,827 bytes
- **Lines**: 383
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

//! Hyperliquid enumerations Python bindings.

use std::str::FromStr;

use nautilus_core::python::to_pyvalue_err;
use pyo3::{PyTypeInfo, prelude::*, types::PyType};
use strum::IntoEnumIterator;

use crate::common::enums::{
    HyperliquidConditionalOrderType, HyperliquidProductType, HyperliquidTpSl,
    HyperliquidTrailingOffsetType, HyperliquidTriggerPriceType,
};

#[pymethods]
impl HyperliquidTriggerPriceType {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value)
    }

    fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(HyperliquidTriggerPriceType),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> &str {
        self.as_ref()
    }

    #[getter]
    #[must_use]
    pub fn value(&self) -> String {
        self.to_string().to_lowercase()
    }

    #[staticmethod]
    #[must_use]
    fn variants() -> Vec<String> {
        Self::iter().map(|x| x.to_string()).collect()
    }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: String = data.str()?.extract()?;
        Self::from_str(&data_str).map_err(to_pyvalue_err)
    }

    #[classattr]
    #[pyo3(name = "LAST")]
    fn py_last() -> Self {
        Self::Last
    }

    #[classattr]
    #[pyo3(name = "MARK")]
    fn py_mark() -> Self {
        Self::Mark
    }

    #[classattr]
    #[pyo3(name = "ORACLE")]
    fn py_oracle() -> Self {
        Self::Oracle
    }
}

#[pymethods]
impl HyperliquidTpSl {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value)
    }

    fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(HyperliquidTpSl),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> &str {
        self.as_ref()
    }

    #[getter]
    #[must_use]
    pub fn value(&self) -> String {
        self.to_string().to_lowercase()
    }

    #[staticmethod]
    #[must_use]
    fn variants() -> Vec<String> {
        Self::iter().map(|x| x.to_string()).collect()
    }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: String = data.str()?.extract()?;
        Self::from_str(&data_str).map_err(to_pyvalue_err)
    }

    #[classattr]
    #[pyo3(name = "TP")]
    fn py_tp() -> Self {
        Self::Tp
    }

    #[classattr]
    #[pyo3(name = "SL")]
    fn py_sl() -> Self {
        Self::Sl
    }
}

#[pymethods]
impl HyperliquidConditionalOrderType {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value)
    }

    fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(HyperliquidConditionalOrderType),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> &str {
        self.as_ref()
    }

    #[getter]
    #[must_use]
    pub fn value(&self) -> String {
        self.to_string().to_lowercase()
    }

    #[staticmethod]
    #[must_use]
    fn variants() -> Vec<String> {
        Self::iter().map(|x| x.to_string()).collect()
    }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: String = data.str()?.extract()?;
        Self::from_str(&data_str).map_err(to_pyvalue_err)
    }

    #[classattr]
    #[pyo3(name = "STOP_MARKET")]
    fn py_stop_market() -> Self {
        Self::StopMarket
    }

    #[classattr]
    #[pyo3(name = "STOP_LIMIT")]
    fn py_stop_limit() -> Self {
        Self::StopLimit
    }

    #[classattr]
    #[pyo3(name = "TAKE_PROFIT_MARKET")]
    fn py_take_profit_market() -> Self {
        Self::TakeProfitMarket
    }

    #[classattr]
    #[pyo3(name = "TAKE_PROFIT_LIMIT")]
    fn py_take_profit_limit() -> Self {
        Self::TakeProfitLimit
    }

    #[classattr]
    #[pyo3(name = "TRAILING_STOP_MARKET")]
    fn py_trailing_stop_market() -> Self {
        Self::TrailingStopMarket
    }

    #[classattr]
    #[pyo3(name = "TRAILING_STOP_LIMIT")]
    fn py_trailing_stop_limit() -> Self {
        Self::TrailingStopLimit
    }
}

#[pymethods]
impl HyperliquidTrailingOffsetType {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value)
    }

    fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(HyperliquidTrailingOffsetType),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> &str {
        self.as_ref()
    }

    #[getter]
    #[must_use]
    pub fn value(&self) -> String {
        self.to_string().to_lowercase()
    }

    #[staticmethod]
    #[must_use]
    fn variants() -> Vec<String> {
        Self::iter().map(|x| x.to_string()).collect()
    }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: String = data.str()?.extract()?;
        Self::from_str(&data_str).map_err(to_pyvalue_err)
    }

    #[classattr]
    #[pyo3(name = "PRICE")]
    fn py_price() -> Self {
        Self::Price
    }

    #[classattr]
    #[pyo3(name = "PERCENTAGE")]
    fn py_percentage() -> Self {
        Self::Percentage
    }

    #[classattr]
    #[pyo3(name = "BASIS_POINTS")]
    fn py_basis_points() -> Self {
        Self::BasisPoints
    }
}

#[pymethods]
impl HyperliquidProductType {
    #[new]
    fn py_new(py: Python<'_>, value: &Bound<'_, PyAny>) -> PyResult<Self> {
        let t = Self::type_object(py);
        Self::py_from_str(&t, value)
    }

    fn __hash__(&self) -> isize {
        *self as isize
    }

    fn __eq__(&self, other: &Self) -> bool {
        self == other
    }

    fn __repr__(&self) -> String {
        format!(
            "<{}.{}: '{}'>",
            stringify!(HyperliquidProductType),
            self.name(),
            self.value(),
        )
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[must_use]
    pub fn name(&self) -> &str {
        self.as_ref()
    }

    #[getter]
    #[must_use]
    pub fn value(&self) -> String {
        self.to_string()
    }

    #[staticmethod]
    #[must_use]
    fn variants() -> Vec<String> {
        Self::iter().map(|x| x.to_string()).collect()
    }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        let data_str: String = data.str()?.extract()?;
        Self::from_str(&data_str).map_err(to_pyvalue_err)
    }

    #[classattr]
    #[pyo3(name = "PERP")]
    fn py_perp() -> Self {
        Self::Perp
    }

    #[classattr]
    #[pyo3(name = "SPOT")]
    fn py_spot() -> Self {
        Self::Spot
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 57 function(s).

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
- **`py_last()`**: Function defined in this file
- **`py_mark()`**: Function defined in this file
- **`py_oracle()`**: Function defined in this file
- **`py_new()`**: Function defined in this file
- **`__hash__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`value()`**: Function defined in this file
- **`variants()`**: Function defined in this file
- **`py_from_str()`**: Function defined in this file
- **`py_tp()`**: Function defined in this file

*...and 37 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 30


**Functions**: `__eq__`, `__hash__`, `__repr__`, `__str__`, `name`, `py_basis_points`, `py_from_str`, `py_last`, `py_mark`, `py_new`, `py_oracle`, `py_percentage`, `py_perp`, `py_price`, `py_sl`, `py_spot`, `py_stop_limit`, `py_stop_market`, `py_take_profit_limit`, `py_take_profit_market`, `py_tp`, `py_trailing_stop_limit`, `py_trailing_stop_market`, `value`, `variants`
**Impls**: `HyperliquidConditionalOrderType`, `HyperliquidProductType`, `HyperliquidTpSl`, `HyperliquidTrailingOffsetType`, `HyperliquidTriggerPriceType`

## Related Files

This file is located in `crates/adapters/hyperliquid/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.057498Z*
