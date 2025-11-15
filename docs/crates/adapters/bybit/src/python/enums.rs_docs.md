# Documentation: `crates/adapters/bybit/src/python/enums.rs`
**Generated:** 2025-11-15T19:40:00.661306Z
**File Size:** 8923 bytes
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

- **Path:** `crates/adapters/bybit/src/python/enums.rs`
- **Size:** 8,923 bytes
- **Lines:** 375
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 5
- **Functions:** 53

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

//! Bybit enumerations Python bindings.

use std::str::FromStr;

use nautilus_core::python::to_pyvalue_err;
use pyo3::{PyTypeInfo, prelude::*, types::PyType};
use strum::IntoEnumIterator;

use crate::common::enums::{
    BybitAccountType, BybitEnvironment, BybitMarginMode, BybitPositionMode, BybitProductType,
};

#[pymethods]
impl BybitProductType {
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
            stringify!(BybitProductType),
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
    #[pyo3(name = "SPOT")]
    fn py_spot() -> Self {
        Self::Spot
    }

    #[classattr]
    #[pyo3(name = "LINEAR")]
    fn py_linear() -> Self {
        Self::Linear
    }

    #[classattr]
    #[pyo3(name = "INVERSE")]
    fn py_inverse() -> Self {
        Self::Inverse
    }

    #[classattr]
    #[pyo3(name = "OPTION")]
    fn py_option() -> Self {
        Self::Option
    }
}

#[pymethods]
impl BybitEnvironment {
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
            "<{}.{}: {}>",
            stringify!(BybitEnvironment),
            self.name(),
            *self as u8,
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
    #[pyo3(name = "MAINNET")]
    fn py_mainnet() -> Self {
        Self::Mainnet
    }

    #[classattr]
    #[pyo3(name = "DEMO")]
    fn py_demo() -> Self {
        Self::Demo
    }

    #[classattr]
    #[pyo3(name = "TESTNET")]
    fn py_testnet() -> Self {
        Self::Testnet
    }
}

#[pymethods]
impl BybitAccountType {
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
            "<{}.{}: {}>",
            stringify!(BybitAccountType),
            self.name(),
            *self as u8,
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
        self.to_string().to_uppercase()
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
    #[pyo3(name = "UNIFIED")]
    fn py_unified() -> Self {
        Self::Unified
    }
}

#[pymethods]
impl BybitMarginMode {
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
            stringify!(BybitMarginMode),
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
        match self {
            Self::IsolatedMargin => "ISOLATED_MARGIN".to_string(),
            Self::RegularMargin => "REGULAR_MARGIN".to_string(),
            Self::PortfolioMargin => "PORTFOLIO_MARGIN".to_string(),
        }
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
    #[pyo3(name = "ISOLATED_MARGIN")]
    fn py_isolated_margin() -> Self {
        Self::IsolatedMargin
    }

    #[classattr]
    #[pyo3(name = "REGULAR_MARGIN")]
    fn py_regular_margin() -> Self {
        Self::RegularMargin
    }

    #[classattr]
    #[pyo3(name = "PORTFOLIO_MARGIN")]
    fn py_portfolio_margin() -> Self {
        Self::PortfolioMargin
    }
}

#[pymethods]
impl BybitPositionMode {
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
            "<{}.{}: {}>",
            stringify!(BybitPositionMode),
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
    pub fn value(&self) -> i32 {
        *self as i32
    }

    #[staticmethod]
    #[must_use]
    fn variants() -> Vec<String> {
        Self::iter().map(|x| x.to_string()).collect()
    }

    #[classmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>) -> PyResult<Self> {
        // Try to extract as integer first (for API payloads that send 0 or 3)
        if let Ok(int_val) = data.extract::<i32>() {
            return match int_val {
                0 => Ok(Self::MergedSingle),
                3 => Ok(Self::BothSides),
                _ => Err(to_pyvalue_err(anyhow::anyhow!(
                    "Invalid BybitPositionMode value: {int_val}"
                ))),
            };
        }

        // Fall back to string parsing for variant names
        let data_str: String = data.str()?.extract()?;
        Self::from_str(&data_str).map_err(to_pyvalue_err)
    }

    #[classattr]
    #[pyo3(name = "MERGED_SINGLE")]
    fn py_merged_single() -> Self {
        Self::MergedSingle
    }

    #[classattr]
    #[pyo3(name = "BOTH_SIDES")]
    fn py_both_sides() -> Self {
        Self::BothSides
    }
}
```


---

## Overview

This file is located at `crates/adapters/bybit/src/python/enums.rs` within the repository.

**Classes defined:** BybitProductType, BybitEnvironment, BybitAccountType, BybitMarginMode, BybitPositionMode

**Functions defined:** py_new, __hash__, __repr__, __str__, name, value, variants, py_from_str, py_spot, py_linear and 43 more


---

## Detailed Analysis

### Classes

#### `BybitProductType`

**Type:** impl


#### `BybitEnvironment`

**Type:** impl


#### `BybitAccountType`

**Type:** impl


#### `BybitMarginMode`

**Type:** impl


#### `BybitPositionMode`

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


#### `py_spot()`


#### `py_linear()`


#### `py_inverse()`


#### `py_option()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_mainnet()`


#### `py_demo()`


#### `py_testnet()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_unified()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


#### `py_from_str(_cls: &Bound<'_, PyType>, data: &Bound<'_, PyAny>)`


#### `py_isolated_margin()`


#### `py_regular_margin()`


#### `py_portfolio_margin()`


#### `py_new(py: Python<'_>, value: &Bound<'_, PyAny>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `name(&self)`


#### `value(&self)`


#### `variants()`


*... and 3 more functions*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


