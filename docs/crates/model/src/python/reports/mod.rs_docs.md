# Documentation: `crates/model/src/python/reports/mod.rs`
**Generated:** 2025-11-15T19:40:03.122130Z
**File Size:** 1527 bytes
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

- **Path:** `crates/model/src/python/reports/mod.rs`
- **Size:** 1,527 bytes
- **Lines:** 40
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

//! Python bindings from [PyO3](https://pyo3.rs).

use pyo3::prelude::*;

use crate::reports;

pub mod fill;
pub mod mass_status;
pub mod order;
pub mod position;

/// Loaded as `nautilus_pyo3.execution`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
#[rustfmt::skip]
pub fn execution(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<reports::fill::FillReport>()?;
    m.add_class::<reports::order::OrderStatusReport>()?;
    m.add_class::<reports::position::PositionStatusReport>()?;
    m.add_class::<reports::mass_status::ExecutionMassStatus>()?;
    Ok(())
}
```


---

## Overview

This file is located at `crates/model/src/python/reports/mod.rs` within the repository.

**Functions defined:** execution


---

## Detailed Analysis

### Functions

#### `execution(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/reports`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


