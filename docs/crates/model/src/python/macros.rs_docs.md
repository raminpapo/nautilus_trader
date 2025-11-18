# Documentation: macros.rs

## File Metadata

- **Path**: `crates/model/src/python/macros.rs`
- **Size**: 3,875 bytes
- **Lines**: 99
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s).

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
- **`py_value()`**: Function defined in this file
- **`py_from_str()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Functions**: `__getstate__`, `__hash__`, `__reduce__`, `__repr__`, `__richcmp__`, `__setstate__`, `__str__`, `_safe_constructor`, `py_from_str`, `py_new`, `py_value`
**Traits**: `happens`

## Related Files

This file is located in `crates/model/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.143955Z*
