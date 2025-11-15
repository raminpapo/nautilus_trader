# Documentation: `crates/common/src/python/custom.rs`
**Generated:** 2025-11-15T19:40:01.819061Z
**File Size:** 1807 bytes
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

- **Path:** `crates/common/src/python/custom.rs`
- **Size:** 1,807 bytes
- **Lines:** 58
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 5

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

use bytes::Bytes;
use nautilus_core::UnixNanos;
use nautilus_model::data::DataType;
use pyo3::prelude::*;

use crate::custom::CustomData;

#[pymethods]
impl CustomData {
    #[new]
    fn py_new(data_type: DataType, value: Vec<u8>, ts_event: u64, ts_init: u64) -> Self {
        Self::new(
            data_type,
            Bytes::from(value),
            UnixNanos::from(ts_event),
            UnixNanos::from(ts_init),
        )
    }

    #[getter]
    #[pyo3(name = "data_type")]
    fn py_data_type(&self) -> DataType {
        self.data_type.clone()
    }

    #[getter]
    #[pyo3(name = "value")]
    fn py_value(&self) -> Vec<u8> {
        self.value.to_vec()
    }

    #[getter]
    #[pyo3(name = "ts_event")]
    const fn py_ts_event(&self) -> u64 {
        self.ts_event.as_u64()
    }

    #[getter]
    #[pyo3(name = "ts_init")]
    const fn py_ts_init(&self) -> u64 {
        self.ts_init.as_u64()
    }
}
```


---

## Overview

This file is located at `crates/common/src/python/custom.rs` within the repository.

**Classes defined:** CustomData

**Functions defined:** py_new, py_data_type, py_value, py_ts_event, py_ts_init


---

## Detailed Analysis

### Classes

#### `CustomData`

**Type:** impl


### Functions

#### `py_new(data_type: DataType, value: Vec<u8>, ts_event: u64, ts_init: u64)`


#### `py_data_type(&self)`


#### `py_value(&self)`


#### `py_ts_event(&self)`


#### `py_ts_init(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


