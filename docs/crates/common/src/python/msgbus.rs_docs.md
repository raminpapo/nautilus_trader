# Documentation: `crates/common/src/python/msgbus.rs`
**Generated:** 2025-11-15T19:40:01.828991Z
**File Size:** 5292 bytes
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

- **Path:** `crates/common/src/python/msgbus.rs`
- **Size:** 5,292 bytes
- **Lines:** 154
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 12

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

use std::rc::Rc;

use nautilus_core::python::to_pyvalue_err;
use pyo3::{Py, PyAny, PyResult, pyfunction, pymethods};

use super::handler::PythonMessageHandler;
use crate::msgbus::{
    BusMessage, MStr, Topic, core::Endpoint, deregister, get_message_bus,
    handler::ShareableMessageHandler, publish, register, send_any, subscribe, unsubscribe,
};

#[pymethods]
impl BusMessage {
    #[getter]
    #[pyo3(name = "topic")]
    fn py_topic(&mut self) -> String {
        self.topic.to_string()
    }

    #[getter]
    #[pyo3(name = "payload")]
    fn py_payload(&mut self) -> &[u8] {
        self.payload.as_ref()
    }

    fn __repr__(&self) -> String {
        format!("{}('{}')", stringify!(BusMessage), self)
    }

    fn __str__(&self) -> String {
        self.to_string()
    }
}

/// Sends the `message` to the `endpoint`.
///
/// # Errors
///
/// Returns an error if `endpoint` is invalid.
#[pyfunction]
#[pyo3(name = "msgbus_send")]
pub fn py_msgbus_send(endpoint: &str, message: Py<PyAny>) -> PyResult<()> {
    let endpoint = MStr::<Endpoint>::endpoint(endpoint).map_err(to_pyvalue_err)?;
    send_any(endpoint, &message);
    Ok(())
}

/// Returns whether there are subscribers for the given `pattern`.
#[pyfunction]
#[pyo3(name = "msgbus_is_subscribed")]
pub fn py_msgbus_is_subscribed(topic: &str, handler: PythonMessageHandler) -> bool {
    let handler = ShareableMessageHandler(Rc::new(handler));
    get_message_bus().borrow().is_subscribed(topic, handler)
}

/// Returns whether there are subscribers for the given `pattern`.
#[pyfunction]
#[pyo3(name = "msgbus_is_registered")]
pub fn py_msgbus_is_registered(endpoint: &str) -> bool {
    get_message_bus().borrow().is_registered(endpoint)
}

/// Publishes the `message` to the `topic`.
///
/// # Errors
///
/// Returns an error if `topic` is invalid.
#[pyfunction]
#[pyo3(name = "msgbus_publish")]
pub fn py_msgbus_publish(topic: &str, message: Py<PyAny>) -> PyResult<()> {
    let topic = MStr::<Topic>::topic(topic).map_err(to_pyvalue_err)?;
    publish(topic, &message);
    Ok(())
}

/// Registers the given `handler` for the `endpoint` address.
///
/// Updates endpoint handler if already exists.
///
/// # Errors
///
/// Returns an error if `endpoint` is invalid.
#[pyfunction]
#[pyo3(name = "msgbus_register")]
pub fn py_msgbus_register(endpoint: &str, handler: PythonMessageHandler) -> PyResult<()> {
    let endpoint = MStr::<Endpoint>::endpoint(endpoint).map_err(to_pyvalue_err)?;
    let handler = ShareableMessageHandler(Rc::new(handler));
    register(endpoint, handler);
    Ok(())
}

/// Subscribes the given `handler` to the `topic`.
///
/// The priority for the subscription determines the ordering of
/// handlers receiving messages being processed, higher priority
/// handlers will receive messages before lower priority handlers.
///
/// Safety: Priority should be between 0 and 255
///
/// Updates topic handler if already exists.
///
/// # Warnings
///
/// Assigning priority handling is an advanced feature which *shouldn't
/// normally be needed by most users*. **Only assign a higher priority to the
/// subscription if you are certain of what you're doing**. If an inappropriate
/// priority is assigned then the handler may receive messages before core
/// system components have been able to process necessary calculations and
/// produce potential side effects for logically sound behavior.
#[pyfunction]
#[pyo3(name = "msgbus_subscribe")]
#[pyo3(signature = (topic, handler, priority=None))]
pub fn py_msgbus_subscribe(topic: &str, handler: PythonMessageHandler, priority: Option<u8>) {
    let pattern = topic.into();
    let handler = ShareableMessageHandler(Rc::new(handler));
    subscribe(pattern, handler, priority);
}

/// Unsubscribes the given `handler` from the `topic`.
#[pyfunction]
#[pyo3(name = "msgbus_unsubscribe")]
pub fn py_msgbus_unsubscribe(topic: &str, handler: PythonMessageHandler) {
    let pattern = topic.into();
    let handler = ShareableMessageHandler(Rc::new(handler));
    unsubscribe(pattern, handler);
}

/// Deregisters the given `handler` for the `endpoint` address.
///
/// # Errors
///
/// Returns an error if `endpoint` is invalid.
#[pyfunction]
#[pyo3(name = "msgbus_deregister")]
pub fn py_msgbus_deregister(endpoint: &str) -> PyResult<()> {
    let endpoint = MStr::<Endpoint>::endpoint(endpoint).map_err(to_pyvalue_err)?;
    deregister(endpoint);
    Ok(())
}
```


---

## Overview

This file is located at `crates/common/src/python/msgbus.rs` within the repository.

**Classes defined:** BusMessage

**Functions defined:** py_topic, py_payload, __repr__, __str__, py_msgbus_send, py_msgbus_is_subscribed, py_msgbus_is_registered, py_msgbus_publish, py_msgbus_register, py_msgbus_subscribe and 2 more


---

## Detailed Analysis

### Classes

#### `BusMessage`

**Type:** impl


### Functions

#### `py_topic(&mut self)`


#### `py_payload(&mut self)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_msgbus_send(endpoint: &str, message: Py<PyAny>)`


#### `py_msgbus_is_subscribed(topic: &str, handler: PythonMessageHandler)`


#### `py_msgbus_is_registered(endpoint: &str)`


#### `py_msgbus_publish(topic: &str, message: Py<PyAny>)`


#### `py_msgbus_register(endpoint: &str, handler: PythonMessageHandler)`


#### `py_msgbus_subscribe(topic: &str, handler: PythonMessageHandler, priority: Option<u8>)`


#### `py_msgbus_unsubscribe(topic: &str, handler: PythonMessageHandler)`


#### `py_msgbus_deregister(endpoint: &str)`



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


