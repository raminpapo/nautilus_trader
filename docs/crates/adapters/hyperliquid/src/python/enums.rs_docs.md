# Documentation: `crates/adapters/hyperliquid/src/python/enums.rs`
**Generated:** 2025-11-15T19:40:01.056148Z
**File Size:** 8827 bytes
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

- **Path:** `crates/adapters/hyperliquid/src/python/enums.rs`
- **Size:** 8,827 bytes
- **Lines:** 382
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 5
- **Functions:** 57

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


---

## Overview

This file is located at `crates/adapters/hyperliquid/src/python/enums.rs` within the repository.

**Classes defined:** HyperliquidTriggerPriceType, HyperliquidTpSl, HyperliquidConditionalOrderType, HyperliquidTrailingOffsetType, HyperliquidProductType

**Functions defined:** py_new, __hash__, __repr__, __str__, name, value, variants, py_from_str, py_last, py_mark and 47 more


---

## Detailed Analysis

### Classes

#### `HyperliquidTriggerPriceType`

**Type:** impl


#### `HyperliquidTpSl`

**Type:** impl


#### `HyperliquidConditionalOrderType`

**Type:** impl


#### `HyperliquidTrailingOffsetType`

**Type:** impl


#### `HyperliquidProductType`

**Type:** impl


### Functions

#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_last()`


#### `py_mark()`


#### `py_oracle()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_tp()`


#### `py_sl()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_stop_market()`


#### `py_stop_limit()`


#### `py_take_profit_market()`


#### `py_take_profit_limit()`


#### `py_trailing_stop_market()`


#### `py_trailing_stop_limit()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_price()`


#### `py_percentage()`


#### `py_basis_points()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__eq__(&self, other: &Self)`


#### `__repr__(&self)`


*... and 7 more functions*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/hyperliquid/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


