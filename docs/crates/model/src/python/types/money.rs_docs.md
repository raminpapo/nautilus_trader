# Documentation: `crates/model/src/python/types/money.rs`
**Generated:** 2025-11-15T19:40:03.133631Z
**File Size:** 13422 bytes
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

- **Path:** `crates/model/src/python/types/money.rs`
- **Size:** 13,422 bytes
- **Lines:** 354
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 33

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

use std::{
    collections::hash_map::DefaultHasher,
    hash::{Hash, Hasher},
    ops::Neg,
    str::FromStr,
};

use nautilus_core::python::{get_pytype_name, to_pytype_err, to_pyvalue_err};
use pyo3::{IntoPyObjectExt, basic::CompareOp, prelude::*, types::PyFloat};
use rust_decimal::{Decimal, RoundingStrategy};

use crate::types::{Currency, Money, money::MoneyRaw};

#[pymethods]
impl Money {
    #[new]
    fn py_new(amount: f64, currency: Currency) -> PyResult<Self> {
        Self::new_checked(amount, currency).map_err(to_pyvalue_err)
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let from_raw = py.get_type::<Self>().getattr("from_raw")?;
        let args = (self.raw, self.currency).into_py_any(py)?;
        (from_raw, args).into_py_any(py)
    }

    fn __richcmp__(
        &self,
        other: &Bound<'_, PyAny>,
        op: CompareOp,
        py: Python<'_>,
    ) -> PyResult<Py<PyAny>> {
        if let Ok(other_money) = other.extract::<Self>() {
            if self.currency != other_money.currency {
                return Err(to_pyvalue_err(format!(
                    "Cannot compare Money with different currencies: {} vs {}",
                    self.currency.code, other_money.currency.code
                )));
            }
            let result = match op {
                CompareOp::Eq => self.eq(&other_money),
                CompareOp::Ne => self.ne(&other_money),
                CompareOp::Ge => self.ge(&other_money),
                CompareOp::Gt => self.gt(&other_money),
                CompareOp::Le => self.le(&other_money),
                CompareOp::Lt => self.lt(&other_money),
            };
            result.into_py_any(py)
        } else {
            Ok(py.NotImplemented())
        }
    }

    fn __hash__(&self) -> isize {
        let mut h = DefaultHasher::new();
        self.hash(&mut h);
        h.finish() as isize
    }

    fn __add__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract::<f64>()?;
            (self.as_f64() + other_float).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (self.as_decimal() + other_qty.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (self.as_decimal() + other_dec).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __add__, was `{pytype_name}`"
            )))
        }
    }

    fn __radd__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (other_float + self.as_f64()).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (other_qty.as_decimal() + self.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (other_dec + self.as_decimal()).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __radd__, was `{pytype_name}`"
            )))
        }
    }

    fn __sub__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (self.as_f64() - other_float).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (self.as_decimal() - other_qty.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (self.as_decimal() - other_dec).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __sub__, was `{pytype_name}`"
            )))
        }
    }

    fn __rsub__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (other_float - self.as_f64()).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (other_qty.as_decimal() - self.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (other_dec - self.as_decimal()).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __rsub__, was `{pytype_name}`"
            )))
        }
    }

    fn __mul__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (self.as_f64() * other_float).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (self.as_decimal() * other_qty.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (self.as_decimal() * other_dec).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __mul__, was `{pytype_name}`"
            )))
        }
    }

    fn __rmul__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (other_float * self.as_f64()).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (other_qty.as_decimal() * self.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (other_dec * self.as_decimal()).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __rmul__, was `{pytype_name}`"
            )))
        }
    }

    fn __truediv__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (self.as_f64() / other_float).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (self.as_decimal() / other_qty.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (self.as_decimal() / other_dec).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __truediv__, was `{pytype_name}`"
            )))
        }
    }

    fn __rtruediv__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (other_float / self.as_f64()).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (other_qty.as_decimal() / self.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (other_dec / self.as_decimal()).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __rtruediv__, was `{pytype_name}`"
            )))
        }
    }

    fn __floordiv__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (self.as_f64() / other_float).floor().into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (self.as_decimal() / other_qty.as_decimal())
                .floor()
                .into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (self.as_decimal() / other_dec).floor().into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __floordiv__, was `{pytype_name}`"
            )))
        }
    }

    fn __rfloordiv__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (other_float / self.as_f64()).floor().into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (other_qty.as_decimal() / self.as_decimal())
                .floor()
                .into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (other_dec / self.as_decimal()).floor().into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __rfloordiv__, was `{pytype_name}`"
            )))
        }
    }

    fn __mod__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (self.as_f64() % other_float).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (self.as_decimal() % other_qty.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (self.as_decimal() % other_dec).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __mod__, was `{pytype_name}`"
            )))
        }
    }

    fn __rmod__(&self, other: &Bound<'_, PyAny>, py: Python) -> PyResult<Py<PyAny>> {
        if other.is_instance_of::<PyFloat>() {
            let other_float: f64 = other.extract()?;
            (other_float % self.as_f64()).into_py_any(py)
        } else if let Ok(other_qty) = other.extract::<Self>() {
            (other_qty.as_decimal() % self.as_decimal()).into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            (other_dec % self.as_decimal()).into_py_any(py)
        } else {
            let pytype_name = get_pytype_name(other)?;
            Err(to_pytype_err(format!(
                "Unsupported type for __rmod__, was `{pytype_name}`"
            )))
        }
    }

    fn __neg__(&self) -> Decimal {
        self.as_decimal().neg()
    }

    fn __pos__(&self) -> Decimal {
        let mut value = self.as_decimal();
        value.set_sign_positive(true);
        value
    }

    fn __abs__(&self) -> Decimal {
        self.as_decimal().abs()
    }

    fn __int__(&self) -> u64 {
        self.as_f64() as u64
    }

    fn __float__(&self) -> f64 {
        self.as_f64()
    }

    #[pyo3(signature = (ndigits=None))]
    fn __round__(&self, ndigits: Option<u32>) -> Decimal {
        self.as_decimal()
            .round_dp_with_strategy(ndigits.unwrap_or(0), RoundingStrategy::MidpointNearestEven)
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    fn raw(&self) -> MoneyRaw {
        self.raw
    }

    #[getter]
    fn currency(&self) -> Currency {
        self.currency
    }

    #[staticmethod]
    #[pyo3(name = "zero")]
    fn py_zero(currency: Currency) -> Self {
        Self::new(0.0, currency)
    }

    #[staticmethod]
    #[pyo3(name = "from_raw")]
    fn py_from_raw(raw: MoneyRaw, currency: Currency) -> PyResult<Self> {
        Ok(Self::from_raw(raw, currency))
    }

    #[staticmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(value: &str) -> PyResult<Self> {
        Self::from_str(value).map_err(to_pyvalue_err)
    }

    #[pyo3(name = "is_zero")]
    fn py_is_zero(&self) -> bool {
        self.is_zero()
    }

    #[pyo3(name = "as_decimal")]
    fn py_as_decimal(&self) -> Decimal {
        self.as_decimal()
    }

    #[pyo3(name = "as_double")]
    fn py_as_double(&self) -> f64 {
        self.as_f64()
    }

    #[pyo3(name = "to_formatted_str")]
    fn py_to_formatted_str(&self) -> String {
        self.to_formatted_string()
    }
}
```


---

## Overview

This file is located at `crates/model/src/python/types/money.rs` within the repository.

**Classes defined:** Money

**Functions defined:** py_new, __reduce__, __richcmp__, __hash__, __add__, __radd__, __sub__, __rsub__, __mul__, __rmul__ and 23 more


---

## Detailed Analysis

### Classes

#### `Money`

**Type:** impl


### Functions

#### `py_new(amount: f64, currency: Currency)`


#### `__reduce__(&self, py: Python)`


#### `__richcmp__(
        &self,
        other: &Bound<'_, PyAny>,
        op: CompareOp,
        py: Python<'_>,
    )`


#### `__hash__(&self)`


#### `__add__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__radd__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__sub__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__rsub__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__mul__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__rmul__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__truediv__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__rtruediv__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__floordiv__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__rfloordiv__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__mod__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__rmod__(&self, other: &Bound<'_, PyAny>, py: Python)`


#### `__neg__(&self)`


#### `__pos__(&self)`


#### `__abs__(&self)`


#### `__int__(&self)`


#### `__float__(&self)`


#### `__round__(&self, ndigits: Option<u32>)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `raw(&self)`


#### `currency(&self)`


#### `py_zero(currency: Currency)`


#### `py_from_raw(raw: MoneyRaw, currency: Currency)`


#### `py_from_str(value: &str)`


#### `py_is_zero(&self)`


#### `py_as_decimal(&self)`


#### `py_as_double(&self)`


#### `py_to_formatted_str(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/types`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


