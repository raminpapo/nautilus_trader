# Documentation: mod.rs

## File Metadata

- **Path**: `crates/model/src/python/account/mod.rs`
- **Size**: 2,402 bytes
- **Lines**: 62
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

pub mod cash;
pub mod margin;
pub mod transformer;

use nautilus_core::python::to_pyvalue_err;
use pyo3::{Py, PyAny, PyResult, Python, conversion::IntoPyObjectExt};

use crate::{
    accounts::{AccountAny, CashAccount, MarginAccount},
    enums::AccountType,
};

/// Converts a Python account object into a Rust `AccountAny` enum.
///
/// # Errors
///
/// Returns a `PyErr` if:
/// - retrieving the `account_type` attribute fails.
/// - extracting the object into `CashAccount` or `MarginAccount` fails.
/// - the `account_type` is unsupported.
pub fn pyobject_to_account_any(py: Python, account: Py<PyAny>) -> PyResult<AccountAny> {
    let account_type = account
        .getattr(py, "account_type")?
        .extract::<AccountType>(py)?;
    if account_type == AccountType::Cash {
        let cash = account.extract::<CashAccount>(py)?;
        Ok(AccountAny::Cash(cash))
    } else if account_type == AccountType::Margin {
        let margin = account.extract::<MarginAccount>(py)?;
        Ok(AccountAny::Margin(margin))
    } else {
        Err(to_pyvalue_err("Unsupported account type"))
    }
}

/// Converts a Rust `AccountAny` into a Python account object.
///
/// # Errors
///
/// Returns a `PyErr` if converting the underlying account into a Python object fails.
pub fn account_any_to_pyobject(py: Python, account: AccountAny) -> PyResult<Py<PyAny>> {
    match account {
        AccountAny::Cash(account) => account.into_py_any(py),
        AccountAny::Margin(account) => account.into_py_any(py),
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`pyobject_to_account_any()`**: Function defined in this file
- **`account_any_to_pyobject()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `account_any_to_pyobject`, `pyobject_to_account_any`

## Related Files

This file is located in `crates/model/src/python/account/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.943815Z*
