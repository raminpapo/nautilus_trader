# Documentation: `crates/model/src/python/events/order/snapshot.rs`
**Generated:** 2025-11-15T19:40:03.036596Z
**File Size:** 1633 bytes
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

- **Path:** `crates/model/src/python/events/order/snapshot.rs`
- **Size:** 1,633 bytes
- **Lines:** 40
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 3

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

use nautilus_core::python::{IntoPyObjectNautilusExt, serialization::from_dict_pyo3};
use pyo3::{basic::CompareOp, prelude::*, types::PyDict};

use crate::events::OrderSnapshot;

#[pymethods]
impl OrderSnapshot {
    fn __richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>) -> Py<PyAny> {
        match op {
            CompareOp::Eq => self.eq(other).into_py_any_unwrap(py),
            CompareOp::Ne => self.ne(other).into_py_any_unwrap(py),
            _ => py.NotImplemented(),
        }
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }

    #[staticmethod]
    #[pyo3(name = "from_dict")]
    fn py_from_dict(py: Python<'_>, values: Py<PyDict>) -> PyResult<Self> {
        from_dict_pyo3(py, values)
    }
}
```


---

## Overview

This file is located at `crates/model/src/python/events/order/snapshot.rs` within the repository.

**Classes defined:** OrderSnapshot

**Functions defined:** __richcmp__, __repr__, py_from_dict


---

## Detailed Analysis

### Classes

#### `OrderSnapshot`

**Type:** impl


### Functions

#### `__richcmp__(&self, other: &Self, op: CompareOp, py: Python<'_>)`


#### `__repr__(&self)`


#### `py_from_dict(py: Python<'_>, values: Py<PyDict>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/events/order`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


