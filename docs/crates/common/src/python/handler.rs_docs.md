# Documentation: handler.rs

## File Metadata

- **Path**: `crates/common/src/python/handler.rs`
- **Size**: 2,191 bytes
- **Lines**: 74
- **Language**: Rust

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`clone()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`as_any()`**: Function defined in this file

### Classes
- **`PythonMessageHandler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Functions**: `as_any`, `clone`, `handle`, `id`, `new`
**Impls**: `Clone`, `MessageHandler`, `PythonMessageHandler`
**Structs**: `PythonMessageHandler`

## Related Files

This file is located in `crates/common/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.272787Z*
