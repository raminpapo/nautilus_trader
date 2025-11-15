# Documentation: `crates/adapters/coinbase_intx/src/python/fix.rs`
**Generated:** 2025-11-15T19:40:00.793643Z
**File Size:** 3211 bytes
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

- **Path:** `crates/adapters/coinbase_intx/src/python/fix.rs`
- **Size:** 3,211 bytes
- **Lines:** 104
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 10

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

//! Provides `PyO3` bindings for the Coinbase International FIX client.

use nautilus_core::python::{to_pyruntime_err, to_pyvalue_err};
use pyo3::prelude::*;

use crate::fix::client::CoinbaseIntxFixClient;

#[pymethods]
impl CoinbaseIntxFixClient {
    #[new]
    #[pyo3(signature = (endpoint=None, api_key=None, api_secret=None, api_passphrase=None, portfolio_id=None))]
    fn py_new(
        endpoint: Option<String>,
        api_key: Option<String>,
        api_secret: Option<String>,
        api_passphrase: Option<String>,
        portfolio_id: Option<String>,
    ) -> PyResult<Self> {
        Self::new(endpoint, api_key, api_secret, api_passphrase, portfolio_id)
            .map_err(to_pyvalue_err)
    }

    #[getter]
    #[pyo3(name = "endpoint")]
    #[must_use]
    pub const fn py_endpoint(&self) -> &str {
        self.endpoint()
    }

    #[getter]
    #[pyo3(name = "api_key")]
    #[must_use]
    pub const fn py_api_key(&self) -> &str {
        self.api_key()
    }

    #[getter]
    #[pyo3(name = "portfolio_id")]
    #[must_use]
    pub const fn py_portfolio_id(&self) -> &str {
        self.portfolio_id()
    }

    #[getter]
    #[pyo3(name = "sender_comp_id")]
    #[must_use]
    pub const fn py_sender_comp_id(&self) -> &str {
        self.sender_comp_id()
    }

    #[getter]
    #[pyo3(name = "target_comp_id")]
    #[must_use]
    pub const fn py_target_comp_id(&self) -> &str {
        self.target_comp_id()
    }

    #[pyo3(name = "is_connected")]
    fn py_is_connected(&self) -> bool {
        self.is_connected()
    }

    #[pyo3(name = "is_logged_on")]
    fn py_is_logged_on(&self) -> bool {
        self.is_logged_on()
    }

    #[pyo3(name = "connect")]
    fn py_connect<'py>(
        &mut self,
        py: Python<'py>,
        handler: Py<PyAny>,
    ) -> PyResult<Bound<'py, PyAny>> {
        let mut client = self.clone();

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            client.connect(handler).await.map_err(to_pyruntime_err)
        })
    }

    #[pyo3(name = "close")]
    fn py_close<'py>(&mut self, py: Python<'py>) -> PyResult<Bound<'py, PyAny>> {
        let mut client = self.clone();

        pyo3_async_runtimes::tokio::future_into_py(py, async move {
            client.close().await.map_err(to_pyruntime_err)
        })
    }
}
```


---

## Overview

This file is located at `crates/adapters/coinbase_intx/src/python/fix.rs` within the repository.

**Classes defined:** CoinbaseIntxFixClient

**Functions defined:** py_new, py_endpoint, py_api_key, py_portfolio_id, py_sender_comp_id, py_target_comp_id, py_is_connected, py_is_logged_on, py_connect, py_close


---

## Detailed Analysis

### Classes

#### `CoinbaseIntxFixClient`

**Type:** impl


### Functions

#### `py_new(
        endpoint: Option<String>,
        api_key: Option<String>,
        api_secret: Option<String>,
        api_passphrase: Option<String>,
        portfolio_id: Option<String>,
    )`


#### `py_endpoint(&self)`


#### `py_api_key(&self)`


#### `py_portfolio_id(&self)`


#### `py_sender_comp_id(&self)`


#### `py_target_comp_id(&self)`


#### `py_is_connected(&self)`


#### `py_is_logged_on(&self)`


#### `py_connect(
        &mut self,
        py: Python<'py>,
        handler: Py<PyAny>,
    )`


#### `py_close(&mut self, py: Python<'py>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/coinbase_intx/src/python`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key. Ensure proper handling of secrets.


