# Documentation: `crates/model/src/python/identifiers/instrument_id.rs`
**Generated:** 2025-11-15T19:40:03.048664Z
**File Size:** 4053 bytes
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

- **Path:** `crates/model/src/python/identifiers/instrument_id.rs`
- **Size:** 4,053 bytes
- **Lines:** 129
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 14

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


---

## Overview

This file is located at `crates/model/src/python/identifiers/instrument_id.rs` within the repository.

**Classes defined:** InstrumentId

**Functions defined:** py_new, __setstate__, __getstate__, __reduce__, _safe_constructor, __richcmp__, __hash__, __repr__, __str__, py_symbol and 4 more


---

## Detailed Analysis

### Classes

#### `InstrumentId`

**Type:** impl


### Functions

#### `py_new(symbol: Symbol, venue: Venue)`


#### `__setstate__(&mut self, state: &Bound<'_, PyAny>)`


#### `__getstate__(&self, py: Python)`


#### `__reduce__(&self, py: Python)`


#### `_safe_constructor()`


#### `__richcmp__(&self, other: Py<PyAny>, op: CompareOp, py: Python<'_>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_symbol(&self)`


#### `py_venue(&self)`


#### `value(&self)`


#### `py_from_str(value: &str)`


#### `py_is_synthetic(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/identifiers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


