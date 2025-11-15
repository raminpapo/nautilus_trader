# Documentation: `crates/common/src/python/signal.rs`
**Generated:** 2025-11-15T19:40:01.830510Z
**File Size:** 1724 bytes
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

- **Path:** `crates/common/src/python/signal.rs`
- **Size:** 1,724 bytes
- **Lines:** 57
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

use nautilus_core::UnixNanos;
use pyo3::prelude::*;
use ustr::Ustr;

use crate::signal::Signal;

#[pymethods]
impl Signal {
    #[new]
    fn py_new(name: &str, value: String, ts_event: u64, ts_init: u64) -> Self {
        Self::new(
            Ustr::from(name),
            value,
            UnixNanos::from(ts_event),
            UnixNanos::from(ts_init),
        )
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> &str {
        self.name.as_str()
    }

    #[getter]
    #[pyo3(name = "value")]
    fn py_value(&self) -> &str {
        self.value.as_str()
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

This file is located at `crates/common/src/python/signal.rs` within the repository.

**Classes defined:** Signal

**Functions defined:** py_new, py_name, py_value, py_ts_event, py_ts_init


---

## Detailed Analysis

### Classes

#### `Signal`

**Type:** impl


### Functions

#### `py_new(name: &str, value: String, ts_event: u64, ts_init: u64)`


#### `py_name(&self)`


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


