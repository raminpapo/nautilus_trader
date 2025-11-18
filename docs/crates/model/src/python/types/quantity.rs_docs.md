# Documentation: quantity.rs

## File Metadata

- **Path**: `crates/model/src/python/types/quantity.rs`
- **Size**: 13,954 bytes
- **Lines**: 370
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

use std::{
    collections::hash_map::DefaultHasher,
    hash::{Hash, Hasher},
    ops::Neg,
};

use nautilus_core::python::{get_pytype_name, to_pytype_err, to_pyvalue_err};
use pyo3::{basic::CompareOp, conversion::IntoPyObjectExt, prelude::*, types::PyFloat};
use rust_decimal::{Decimal, RoundingStrategy};

use crate::types::{Quantity, quantity::QuantityRaw};

#[pymethods]
impl Quantity {
    #[new]
    fn py_new(value: f64, precision: u8) -> PyResult<Self> {
        Self::new_checked(value, precision).map_err(to_pyvalue_err)
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let from_raw = py.get_type::<Self>().getattr("from_raw")?;
        let args = (self.raw, self.precision).into_py_any(py)?;
        (from_raw, args).into_py_any(py)
    }

    fn __richcmp__(
        &self,
        other: &Bound<'_, PyAny>,
        op: CompareOp,
        py: Python<'_>,
    ) -> PyResult<Py<PyAny>> {
        if let Ok(other_qty) = other.extract::<Self>() {
            let result = match op {
                CompareOp::Eq => self.eq(&other_qty),
                CompareOp::Ne => self.ne(&other_qty),
                CompareOp::Ge => self.ge(&other_qty),
                CompareOp::Gt => self.gt(&other_qty),
                CompareOp::Le => self.le(&other_qty),
                CompareOp::Lt => self.lt(&other_qty),
            };
            result.into_py_any(py)
        } else if let Ok(other_dec) = other.extract::<Decimal>() {
            let result = match op {
                CompareOp::Eq => self.as_decimal() == other_dec,
                CompareOp::Ne => self.as_decimal() != other_dec,
                CompareOp::Ge => self.as_decimal() >= other_dec,
                CompareOp::Gt => self.as_decimal() > other_dec,
                CompareOp::Le => self.as_decimal() <= other_dec,
                CompareOp::Lt => self.as_decimal() < other_dec,
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
            let other_float: f64 = other.extract()?;
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
    fn raw(&self) -> QuantityRaw {
        self.raw
    }

    #[getter]
    fn precision(&self) -> u8 {
        self.precision
    }

    #[staticmethod]
    #[pyo3(name = "from_raw")]
    fn py_from_raw(raw: QuantityRaw, precision: u8) -> Self {
        Self::from_raw(raw, precision)
    }

    #[staticmethod]
    #[pyo3(name = "zero")]
    #[pyo3(signature = (precision = 0))]
    fn py_zero(precision: u8) -> PyResult<Self> {
        Self::new_checked(0.0, precision).map_err(to_pyvalue_err)
    }

    #[staticmethod]
    #[pyo3(name = "from_int")]
    fn py_from_int(value: u64) -> PyResult<Self> {
        Self::new_checked(value as f64, 0).map_err(to_pyvalue_err)
    }

    #[staticmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(value: &str) -> Self {
        Self::from(value)
    }

    #[pyo3(name = "is_zero")]
    fn py_is_zero(&self) -> bool {
        self.is_zero()
    }

    #[pyo3(name = "is_positive")]
    fn py_is_positive(&self) -> bool {
        self.is_positive()
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 35 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__reduce__()`**: Function defined in this file
- **`__richcmp__()`**: Function defined in this file
- **`__hash__()`**: Function defined in this file
- **`__add__()`**: Function defined in this file
- **`__radd__()`**: Function defined in this file
- **`__sub__()`**: Function defined in this file
- **`__rsub__()`**: Function defined in this file
- **`__mul__()`**: Function defined in this file
- **`__rmul__()`**: Function defined in this file
- **`__truediv__()`**: Function defined in this file
- **`__rtruediv__()`**: Function defined in this file
- **`__floordiv__()`**: Function defined in this file
- **`__rfloordiv__()`**: Function defined in this file
- **`__mod__()`**: Function defined in this file
- **`__rmod__()`**: Function defined in this file
- **`__neg__()`**: Function defined in this file
- **`__pos__()`**: Function defined in this file
- **`__abs__()`**: Function defined in this file
- **`__int__()`**: Function defined in this file

*...and 15 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 36


**Functions**: `__abs__`, `__add__`, `__float__`, `__floordiv__`, `__hash__`, `__int__`, `__mod__`, `__mul__`, `__neg__`, `__pos__`, `__radd__`, `__reduce__`, `__repr__`, `__rfloordiv__`, `__richcmp__`, `__rmod__`, `__rmul__`, `__round__`, `__rsub__`, `__rtruediv__`, `__str__`, `__sub__`, `__truediv__`, `precision`, `py_as_decimal`, `py_as_double`, `py_from_int`, `py_from_raw`, `py_from_str`, `py_is_positive` *(+5 more)*
**Impls**: `Quantity`

## Related Files

This file is located in `crates/model/src/python/types/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.228842Z*
