# Documentation: instrument_id.rs

## File Metadata

- **Path**: `crates/model/src/python/identifiers/instrument_id.rs`
- **Size**: 4,053 bytes
- **Lines**: 130
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
    str::FromStr,
};

use nautilus_core::python::{IntoPyObjectNautilusExt, to_pyvalue_err};
use pyo3::{
    IntoPyObjectExt,
    prelude::*,
    pyclass::CompareOp,
    types::{PyString, PyTuple},
};

use crate::identifiers::{InstrumentId, Symbol, Venue};

#[pymethods]
impl InstrumentId {
    #[new]
    fn py_new(symbol: Symbol, venue: Venue) -> Self {
        Self::new(symbol, venue)
    }

    fn __setstate__(&mut self, state: &Bound<'_, PyAny>) -> PyResult<()> {
        let py_tuple: &Bound<'_, PyTuple> = state.cast::<PyTuple>()?;
        self.symbol = Symbol::new_checked(
            py_tuple
                .get_item(0)?
                .cast::<PyString>()?
                .extract::<&str>()?,
        )
        .map_err(to_pyvalue_err)?;
        self.venue = Venue::new_checked(
            py_tuple
                .get_item(1)?
                .cast::<PyString>()?
                .extract::<&str>()?,
        )
        .map_err(to_pyvalue_err)?;
        Ok(())
    }

    fn __getstate__(&self, py: Python) -> PyResult<Py<PyAny>> {
        (self.symbol.to_string(), self.venue.to_string()).into_py_any(py)
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let safe_constructor = py.get_type::<Self>().getattr("_safe_constructor")?;
        let state = self.__getstate__(py)?;
        (safe_constructor, PyTuple::empty(py), state).into_py_any(py)
    }

    #[staticmethod]
    fn _safe_constructor() -> PyResult<Self> {
        Ok(Self::from_str("NULL.NULL").unwrap()) // Safe default
    }

    fn __richcmp__(&self, other: Py<PyAny>, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        if let Ok(other) = other.extract::<Self>(py) {
            match op {
                CompareOp::Eq => self.eq(&other).into_py_any_unwrap(py),
                CompareOp::Ne => self.ne(&other).into_py_any_unwrap(py),
                CompareOp::Ge => self.ge(&other).into_py_any_unwrap(py),
                CompareOp::Gt => self.gt(&other).into_py_any_unwrap(py),
                CompareOp::Le => self.le(&other).into_py_any_unwrap(py),
                CompareOp::Lt => self.lt(&other).into_py_any_unwrap(py),
            }
        } else {
            py.NotImplemented()
        }
    }

    fn __hash__(&self) -> isize {
        let mut h = DefaultHasher::new();
        self.hash(&mut h);
        h.finish() as isize
    }

    fn __repr__(&self) -> String {
        format!("{}('{}')", stringify!(InstrumentId), self)
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "symbol")]
    fn py_symbol(&self) -> Symbol {
        self.symbol
    }

    #[getter]
    #[pyo3(name = "venue")]
    fn py_venue(&self) -> Venue {
        self.venue
    }

    #[getter]
    fn value(&self) -> String {
        self.to_string()
    }

    #[staticmethod]
    #[pyo3(name = "from_str")]
    fn py_from_str(value: &str) -> PyResult<Self> {
        Self::from_str(value).map_err(to_pyvalue_err)
    }

    #[pyo3(name = "is_synthetic")]
    fn py_is_synthetic(&self) -> bool {
        self.is_synthetic()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 14 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__setstate__()`**: Function defined in this file
- **`__getstate__()`**: Function defined in this file
- **`__reduce__()`**: Function defined in this file
- **`_safe_constructor()`**: Function defined in this file
- **`__richcmp__()`**: Function defined in this file
- **`__hash__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`py_symbol()`**: Function defined in this file
- **`py_venue()`**: Function defined in this file
- **`value()`**: Function defined in this file
- **`py_from_str()`**: Function defined in this file
- **`py_is_synthetic()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Functions**: `__getstate__`, `__hash__`, `__reduce__`, `__repr__`, `__richcmp__`, `__setstate__`, `__str__`, `_safe_constructor`, `py_from_str`, `py_is_synthetic`, `py_new`, `py_symbol`, `py_venue`, `value`
**Impls**: `InstrumentId`

## Related Files

This file is located in `crates/model/src/python/identifiers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.096182Z*
