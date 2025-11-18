# Documentation: currency.rs

## File Metadata

- **Path**: `crates/model/src/python/types/currency.rs`
- **Size**: 4,205 bytes
- **Lines**: 141
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

use std::str::FromStr;

use nautilus_core::python::{to_pyruntime_err, to_pyvalue_err};
use pyo3::{IntoPyObjectExt, prelude::*};

use crate::{enums::CurrencyType, types::Currency};

#[pymethods]
impl Currency {
    #[new]
    fn py_new(
        code: &str,
        precision: u8,
        iso4217: u16,
        name: &str,
        currency_type: CurrencyType,
    ) -> PyResult<Self> {
        Self::new_checked(code, precision, iso4217, name, currency_type).map_err(to_pyvalue_err)
    }

    fn __reduce__(&self, py: Python) -> PyResult<Py<PyAny>> {
        let unpickle = py.get_type::<Self>().getattr("_unpickle")?;
        let args = (
            self.code.to_string(),
            self.precision,
            self.iso4217,
            self.name.to_string(),
            self.currency_type.to_string(),
        )
            .into_py_any(py)?;
        (unpickle, args).into_py_any(py)
    }

    #[staticmethod]
    fn _unpickle(
        code: &str,
        precision: u8,
        iso4217: u16,
        name: &str,
        currency_type_str: &str,
    ) -> PyResult<Self> {
        let currency_type = CurrencyType::from_str(currency_type_str).map_err(to_pyvalue_err)?;
        Self::new_checked(code, precision, iso4217, name, currency_type).map_err(to_pyvalue_err)
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }

    fn __str__(&self) -> &'static str {
        self.code.as_str()
    }

    #[getter]
    #[pyo3(name = "code")]
    fn py_code(&self) -> &'static str {
        self.code.as_str()
    }

    #[getter]
    #[pyo3(name = "precision")]
    fn py_precision(&self) -> u8 {
        self.precision
    }

    #[getter]
    #[pyo3(name = "iso4217")]
    fn py_iso4217(&self) -> u16 {
        self.iso4217
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> &'static str {
        self.name.as_str()
    }

    #[getter]
    #[pyo3(name = "currency_type")]
    fn py_currency_type(&self) -> CurrencyType {
        self.currency_type
    }

    #[staticmethod]
    #[pyo3(name = "is_fiat")]
    fn py_is_fiat(code: &str) -> PyResult<bool> {
        Self::is_fiat(code).map_err(to_pyvalue_err)
    }

    #[staticmethod]
    #[pyo3(name = "is_crypto")]
    fn py_is_crypto(code: &str) -> PyResult<bool> {
        Self::is_crypto(code).map_err(to_pyvalue_err)
    }

    #[staticmethod]
    #[pyo3(name = "is_commodity_backed")]
    fn py_is_commodidity_backed(code: &str) -> PyResult<bool> {
        Self::is_commodity_backed(code).map_err(to_pyvalue_err)
    }

    #[staticmethod]
    #[pyo3(name = "from_str")]
    #[pyo3(signature = (value, strict = false))]
    fn py_from_str(value: &str, strict: bool) -> PyResult<Self> {
        match Self::from_str(value) {
            Ok(currency) => Ok(currency),
            Err(e) => {
                if strict {
                    Err(to_pyvalue_err(e))
                } else {
                    Self::new_checked(value, 8, 0, value, CurrencyType::Crypto)
                        .map_err(to_pyvalue_err)
                }
            }
        }
    }

    #[staticmethod]
    #[pyo3(name = "register")]
    #[pyo3(signature = (currency, overwrite = false))]
    fn py_register(currency: Self, overwrite: bool) -> PyResult<()> {
        Self::register(currency, overwrite).map_err(to_pyruntime_err)
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 15 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__reduce__()`**: Function defined in this file
- **`_unpickle()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`py_code()`**: Function defined in this file
- **`py_precision()`**: Function defined in this file
- **`py_iso4217()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_currency_type()`**: Function defined in this file
- **`py_is_fiat()`**: Function defined in this file
- **`py_is_crypto()`**: Function defined in this file
- **`py_is_commodidity_backed()`**: Function defined in this file
- **`py_from_str()`**: Function defined in this file
- **`py_register()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Functions**: `__reduce__`, `__repr__`, `__str__`, `_unpickle`, `py_code`, `py_currency_type`, `py_from_str`, `py_is_commodidity_backed`, `py_is_crypto`, `py_is_fiat`, `py_iso4217`, `py_name`, `py_new`, `py_precision`, `py_register`
**Impls**: `Currency`

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
*Generated on 2025-11-18T21:55:03.213815Z*
