# Documentation: transformer.rs

## File Metadata

- **Path**: `crates/model/src/python/account/transformer.rs`
- **Size**: 3,018 bytes
- **Lines**: 85
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

use nautilus_core::python::to_pyvalue_err;
use pyo3::{prelude::*, types::PyDict};

use crate::{
    accounts::{Account, CashAccount, MarginAccount},
    events::AccountState,
};

/// Constructs a `CashAccount` from a list of Python dict events.
///
/// # Errors
///
/// Returns a `PyErr` if the input `events` list is empty.
///
/// # Panics
///
/// Panics if event conversion (`py_from_dict`) unwrap fails.
#[pyfunction]
#[pyo3(signature = (events, calculate_account_state, allow_borrowing = false))]
pub fn cash_account_from_account_events(
    events: Vec<Bound<'_, PyDict>>,
    calculate_account_state: bool,
    allow_borrowing: bool,
) -> PyResult<CashAccount> {
    let account_events = events
        .into_iter()
        .map(|obj| AccountState::py_from_dict(&obj))
        .collect::<PyResult<Vec<AccountState>>>()
        .unwrap();
    if account_events.is_empty() {
        return Err(to_pyvalue_err("No account events"));
    }
    let init_event = account_events[0].clone();
    let mut cash_account = CashAccount::new(init_event, calculate_account_state, allow_borrowing);
    for event in account_events.iter().skip(1) {
        cash_account.apply(event.clone());
    }
    Ok(cash_account)
}

/// Constructs a `MarginAccount` from a list of Python dict events.
///
/// # Errors
///
/// Returns a `PyErr` if the input `events` list is empty.
///
/// # Panics
///
/// Panics if event conversion (`py_from_dict`) unwrap fails.
#[pyfunction]
pub fn margin_account_from_account_events(
    events: Vec<Bound<'_, PyDict>>,
    calculate_account_state: bool,
) -> PyResult<MarginAccount> {
    let account_events = events
        .into_iter()
        .map(|obj| AccountState::py_from_dict(&obj))
        .collect::<PyResult<Vec<AccountState>>>()
        .unwrap();
    if account_events.is_empty() {
        return Err(to_pyvalue_err("No account events"));
    }
    let init_event = account_events[0].clone();
    let mut margin_account = MarginAccount::new(init_event, calculate_account_state);
    for event in account_events.iter().skip(1) {
        margin_account.apply(event.clone());
    }
    Ok(margin_account)
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`cash_account_from_account_events()`**: Function defined in this file
- **`margin_account_from_account_events()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `cash_account_from_account_events`, `margin_account_from_account_events`

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
*Generated on 2025-11-18T21:55:02.946263Z*
