# Documentation: common.rs

## File Metadata

- **Path**: `crates/model/src/python/common.rs`
- **Size**: 8,595 bytes
- **Lines**: 280
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

use indexmap::IndexMap;
use nautilus_core::python::IntoPyObjectNautilusExt;
use pyo3::{
    conversion::IntoPyObjectExt,
    exceptions::PyValueError,
    prelude::*,
    types::{PyDict, PyList, PyNone},
};
use serde_json::Value;
use strum::IntoEnumIterator;

use crate::types::{Currency, Money};

pub const PY_MODULE_MODEL: &str = "nautilus_trader.core.nautilus_pyo3.model";

/// Python iterator over the variants of an enum.
#[allow(missing_debug_implementations)]
#[pyclass]
pub struct EnumIterator {
    // Type erasure for code reuse, generic types can't be exposed to Python
    iter: Box<dyn Iterator<Item = Py<PyAny>> + Send + Sync>,
}

#[pymethods]
impl EnumIterator {
    fn __iter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    fn __next__(mut slf: PyRefMut<'_, Self>) -> Option<Py<PyAny>> {
        slf.iter.next()
    }
}

impl EnumIterator {
    /// Creates a new Python iterator over the variants of an enum.
    ///
    /// # Panics
    ///
    /// Panics if conversion of enum variants into Python objects fails.
    #[must_use]
    pub fn new<'py, E>(py: Python<'py>) -> Self
    where
        E: strum::IntoEnumIterator + IntoPyObjectExt<'py>,
        <E as IntoEnumIterator>::Iterator: Send,
    {
        Self {
            iter: Box::new(
                E::iter()
                    .map(|var| var.into_py_any_unwrap(py))
                    // Force eager evaluation because `py` isn't `Send`
                    .collect::<Vec<_>>()
                    .into_iter(),
            ),
        }
    }
}

/// Converts a JSON `Value::Object` into a Python `dict`.
///
/// # Panics
///
/// Panics if creating a Python list fails due to an invalid iterator.
///
/// # Errors
///
/// Returns a `PyErr` if:
/// - the input `val` is not a JSON object.
/// - conversion of any nested JSON value into a Python object fails.
pub fn value_to_pydict(py: Python<'_>, val: &Value) -> PyResult<Py<PyAny>> {
    let dict = PyDict::new(py);

    match val {
        Value::Object(map) => {
            for (key, value) in map {
                let py_value = value_to_pyobject(py, value)?;
                dict.set_item(key, py_value)?;
            }
        }
        // This shouldn't be reached in this function, but we include it for completeness
        _ => return Err(PyValueError::new_err("Expected JSON object")),
    }

    dict.into_py_any(py)
}

/// Converts a JSON `Value` into a corresponding Python object.
///
/// # Panics
///
/// Panics if parsing numbers (`as_i64`, `as_f64`) or creating the Python list (`PyList::new().expect`) fails.
///
/// # Errors
///
/// Returns a `PyErr` if:
/// - encountering an unsupported JSON number type.
/// - conversion of nested arrays or objects fails.
pub fn value_to_pyobject(py: Python<'_>, val: &Value) -> PyResult<Py<PyAny>> {
    match val {
        Value::Null => Ok(py.None()),
        Value::Bool(b) => b.into_py_any(py),
        Value::String(s) => s.into_py_any(py),
        Value::Number(n) => {
            if n.is_i64() {
                n.as_i64().unwrap().into_py_any(py)
            } else if n.is_f64() {
                n.as_f64().unwrap().into_py_any(py)
            } else {
                Err(PyValueError::new_err("Unsupported JSON number type"))
            }
        }
        Value::Array(arr) => {
            let py_list =
                PyList::new(py, &[] as &[Py<PyAny>]).expect("Invalid `ExactSizeIterator`");
            for item in arr {
                let py_item = value_to_pyobject(py, item)?;
                py_list.append(py_item)?;
            }
            py_list.into_py_any(py)
        }
        Value::Object(_) => value_to_pydict(py, val),
    }
}

/// Converts a list of `Money` values into a Python list of strings, or `None` if empty.
///
/// # Panics
///
/// Panics if creating the Python list fails or during the conversion unwrap.
///
/// # Errors
///
/// Returns a `PyErr` if Python list creation or conversion fails.
pub fn commissions_from_vec(py: Python<'_>, commissions: Vec<Money>) -> PyResult<Bound<'_, PyAny>> {
    let mut values = Vec::new();

    for value in commissions {
        values.push(value.to_string());
    }

    if values.is_empty() {
        Ok(PyNone::get(py).to_owned().into_any())
    } else {
        values.sort();
        // SAFETY: Reasonable to expect `ExactSizeIterator` should be correctly implemented
        Ok(PyList::new(py, &values).unwrap().into_any())
    }
}

/// Converts an `IndexMap<Currency, Money>` into a Python list of strings, or `None` if empty.
///
/// # Errors
///
/// Returns a `PyErr` if Python list creation or conversion fails.
pub fn commissions_from_indexmap(
    py: Python<'_>,
    commissions: IndexMap<Currency, Money>,
) -> PyResult<Bound<'_, PyAny>> {
    commissions_from_vec(py, commissions.values().copied().collect())
}

#[cfg(test)]
mod tests {
    use pyo3::{
        prelude::*,
        types::{PyBool, PyInt, PyString},
    };
    use rstest::rstest;
    use serde_json::Value;

    use super::*;

    #[rstest]
    fn test_value_to_pydict() {
        Python::initialize();
        Python::attach(|py| {
            let json_str = r#"
        {
            "type": "OrderAccepted",
            "ts_event": 42,
            "is_reconciliation": false
        }
        "#;

            let val: Value = serde_json::from_str(json_str).unwrap();
            let py_dict_ref = value_to_pydict(py, &val).unwrap();
            let py_dict = py_dict_ref.bind(py);

            assert_eq!(
                py_dict
                    .get_item("type")
                    .unwrap()
                    .cast::<PyString>()
                    .unwrap()
                    .to_str()
                    .unwrap(),
                "OrderAccepted"
            );
            assert_eq!(
                py_dict
                    .get_item("ts_event")
                    .unwrap()
                    .cast::<PyInt>()
                    .unwrap()
                    .extract::<i64>()
                    .unwrap(),
                42
            );
            assert!(
                !py_dict
                    .get_item("is_reconciliation")
                    .unwrap()
                    .cast::<PyBool>()
                    .unwrap()
                    .is_true()
            );
        });
    }

    #[rstest]
    fn test_value_to_pyobject_string() {
        Python::initialize();
        Python::attach(|py| {
            let val = Value::String("Hello, world!".to_string());
            let py_obj = value_to_pyobject(py, &val).unwrap();

            assert_eq!(py_obj.extract::<&str>(py).unwrap(), "Hello, world!");
        });
    }

    #[rstest]
    fn test_value_to_pyobject_bool() {
        Python::initialize();
        Python::attach(|py| {
            let val = Value::Bool(true);
            let py_obj = value_to_pyobject(py, &val).unwrap();

            assert!(py_obj.extract::<bool>(py).unwrap());
        });
    }

    #[rstest]
    fn test_value_to_pyobject_array() {
        Python::initialize();
        Python::attach(|py| {
            let val = Value::Array(vec![
                Value::String("item1".to_string()),
                Value::String("item2".to_string()),
            ]);
            let binding = value_to_pyobject(py, &val).unwrap();
            let py_list: &Bound<'_, PyList> = binding.bind(py).cast::<PyList>().unwrap();

            assert_eq!(py_list.len(), 2);
            assert_eq!(
                py_list.get_item(0).unwrap().extract::<&str>().unwrap(),
                "item1"
            );
            assert_eq!(
                py_list.get_item(1).unwrap().extract::<&str>().unwrap(),
                "item2"
            );
        });
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`__iter__()`**: Function defined in this file
- **`__next__()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`value_to_pydict()`**: Function defined in this file
- **`value_to_pyobject()`**: Function defined in this file
- **`commissions_from_vec()`**: Function defined in this file
- **`commissions_from_indexmap()`**: Function defined in this file
- **`test_value_to_pydict()`**: Function defined in this file
- **`test_value_to_pyobject_string()`**: Function defined in this file
- **`test_value_to_pyobject_bool()`**: Function defined in this file
- **`test_value_to_pyobject_array()`**: Function defined in this file

### Classes
- **`EnumIterator`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Enums**: `variants`
**Functions**: `__iter__`, `__next__`, `commissions_from_indexmap`, `commissions_from_vec`, `new`, `test_value_to_pydict`, `test_value_to_pyobject_array`, `test_value_to_pyobject_bool`, `test_value_to_pyobject_string`, `value_to_pydict`, `value_to_pyobject`
**Impls**: `EnumIterator`
**Structs**: `EnumIterator`

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
*Generated on 2025-11-18T21:55:02.949407Z*
