# Documentation: `crates/model/src/python/account/transformer.rs`
**Generated:** 2025-11-15T19:40:02.942679Z
**File Size:** 3018 bytes
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

- **Path:** `crates/model/src/python/account/transformer.rs`
- **Size:** 3,018 bytes
- **Lines:** 84
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

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


---

## Overview

This file is located at `crates/model/src/python/account/transformer.rs` within the repository.

**Functions defined:** cash_account_from_account_events, margin_account_from_account_events


---

## Detailed Analysis

### Functions

#### `cash_account_from_account_events(
    events: Vec<Bound<'_, PyDict>>,
    calculate_account_state: bool,
    allow_borrowing: bool,
)`


#### `margin_account_from_account_events(
    events: Vec<Bound<'_, PyDict>>,
    calculate_account_state: bool,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/account`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


