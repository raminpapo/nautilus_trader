# Documentation: `crates/model/src/python/macros.rs`
**Generated:** 2025-11-15T19:40:03.083573Z
**File Size:** 3875 bytes
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

- **Path:** `crates/model/src/python/macros.rs`
- **Size:** 3,875 bytes
- **Lines:** 98
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 11

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

//! Provides macros.

#[macro_export]
macro_rules! identifier_for_python {
    ($ty:ty) => {
        #[pymethods]
        impl $ty {
            #[new]
            fn py_new(value: &str) -> PyResult<Self> {
                <$ty>::new_checked(value).map_err(to_pyvalue_err)
            }

            fn __setstate__(&mut self, state: &Bound<'_, PyAny>) -> PyResult<()> {
                let py_tuple: &Bound<'_, PyTuple> = state.cast::<PyTuple>()?;
                let bindings = py_tuple.get_item(0)?;
                let value = bindings.cast::<PyString>()?.extract::<&str>()?;
                self.set_inner(value);
                Ok(())
            }

            fn __getstate__(&self, py: Python) -> PyResult<Py<PyAny>> {
                use pyo3::IntoPyObjectExt;
                (self.to_string(),).into_py_any(py)
            }

            fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
                use pyo3::IntoPyObjectExt;
                let safe_constructor = py.get_type::<Self>().getattr("_safe_constructor")?;
                let state = self.__getstate__(py)?;
                (safe_constructor, PyTuple::empty(py), state).into_py_any(py)
            }

            #[staticmethod]
            fn _safe_constructor() -> PyResult<Self> {
                Ok(<$ty>::from("NULL")) // Safe default
            }

            // Note: Cannot use into_py_any_unwrap from IntoPyObjectNautilusExt
            // because type resolution for the trait happens after macros have
            // been run.
            fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
                use nautilus_core::python::IntoPyObjectNautilusExt;

                match op {
                    CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
                    CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
                    CompareOp::Ge => self.ge(other).into_py_any_unwrap(py),
                    CompareOp::Gt => self.gt(other).into_py_any_unwrap(py),
                    CompareOp::Le => self.le(other).into_py_any_unwrap(py),
                    CompareOp::Lt => self.lt(other).into_py_any_unwrap(py),
                }
            }

            fn __hash__(&self) -> isize {
                self.inner().precomputed_hash() as isize
            }

            fn __repr__(&self) -> String {
                format!(
                    "{}('{}')",
                    stringify!($ty).split("::").last().unwrap_or(""),
                    self.as_str()
                )
            }

            fn __str__(&self) -> &'static str {
                self.inner().as_str()
            }

            #[getter]
            #[pyo3(name = "value")]
            fn py_value(&self) -> String {
                self.to_string()
            }

            #[staticmethod]
            #[pyo3(name = "from_str")]
            fn py_from_str(value: &str) -> Self {
                Self::from(value)
            }
        }
    };
}
```


---

## Overview

This file is located at `crates/model/src/python/macros.rs` within the repository.

**Functions defined:** py_new, __setstate__, __getstate__, __reduce__, _safe_constructor, __richcmp__, __hash__, __repr__, __str__, py_value and 1 more


---

## Detailed Analysis

### Functions

#### `py_new(value: &str)`


#### `__setstate__(&mut self, state: &Bound<'_, PyAny>)`


#### `__getstate__(&self, py: Python)`


#### `__reduce__(&self, py: Python)`


#### `_safe_constructor()`


#### `__richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>)`


#### `__hash__(&self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_value(&self)`


#### `py_from_str(value: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


