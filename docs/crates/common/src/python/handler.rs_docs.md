# Documentation: `crates/common/src/python/handler.rs`
**Generated:** 2025-11-15T19:40:01.822050Z
**File Size:** 2191 bytes
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

- **Path:** `crates/common/src/python/handler.rs`
- **Size:** 2,191 bytes
- **Lines:** 73
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 5

---

## Source Code

```rust
// -------------------------------------------------------------------------------------------------
//  Copyright (C) 2015-2025 2Nautech Systems Pty Ltd. All rights reserved.
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

use std::any::Any;

use nautilus_core::python::clone_py_object;
use pyo3::prelude::*;
use ustr::Ustr;

use crate::msgbus::handler::MessageHandler;

#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.common")
)]
#[derive(Debug)]
pub struct PythonMessageHandler {
    id: Ustr,
    handler: Py<PyAny>,
}

impl Clone for PythonMessageHandler {
    fn clone(&self) -> Self {
        Self {
            id: self.id,
            handler: clone_py_object(&self.handler),
        }
    }
}

#[pymethods]
impl PythonMessageHandler {
    /// Creates a new [`PythonMessageHandler`] instance.
    #[new]
    #[must_use]
    pub fn new(id: &str, handler: Py<PyAny>) -> Self {
        let id = Ustr::from(id);
        Self { id, handler }
    }
}

impl MessageHandler for PythonMessageHandler {
    #[allow(unused_variables)]
    fn handle(&self, message: &dyn Any) {
        // TODO: convert message to Py<PyAny>
        let py_event = ();
        let result =
            pyo3::Python::attach(|py| self.handler.call_method1(py, "handle", (py_event,)));
        if let Err(e) = result {
            eprintln!("Error calling handle method: {e:?}");
        }
    }

    fn id(&self) -> Ustr {
        self.id
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}
```


---

## Overview

This file is located at `crates/common/src/python/handler.rs` within the repository.

**Classes defined:** PythonMessageHandler, Clone, PythonMessageHandler, MessageHandler

**Functions defined:** clone, new, handle, id, as_any


---

## Detailed Analysis

### Classes

#### `PythonMessageHandler`

**Type:** struct


#### `Clone`

**Type:** impl


#### `PythonMessageHandler`

**Type:** impl


#### `MessageHandler`

**Type:** impl


### Functions

#### `clone(&self)`


#### `new(id: &str, handler: Py<PyAny>)`


#### `handle(&self, message: &dyn Any)`


#### `id(&self)`


#### `as_any(&self)`



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


