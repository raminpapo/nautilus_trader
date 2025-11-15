# Documentation: `crates/adapters/databento/src/python/data.rs`
**Generated:** 2025-11-15T19:40:00.873789Z
**File Size:** 2543 bytes
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

- **Path:** `crates/adapters/databento/src/python/data.rs`
- **Size:** 2,543 bytes
- **Lines:** 72
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 4

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

//! Python bindings for the Databento data client.

use std::path::PathBuf;

use nautilus_core::time::get_atomic_clock_realtime;
use nautilus_data::client::DataClient;
use nautilus_model::identifiers::ClientId;
use pyo3::prelude::*;

use crate::data::{DatabentoDataClient, DatabentoDataClientConfig};

#[cfg(feature = "python")]
#[pymethods]
impl DatabentoDataClient {
    /// Creates a new [`DatabentoDataClient`] instance.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if client creation fails.
    #[new]
    #[pyo3(signature = (client_id, api_key, publishers_filepath, use_exchange_as_venue = true, bars_timestamp_on_close = true))]
    pub fn py_new(
        client_id: ClientId,
        api_key: String,
        publishers_filepath: PathBuf,
        use_exchange_as_venue: bool,
        bars_timestamp_on_close: bool,
    ) -> PyResult<Self> {
        let config = DatabentoDataClientConfig::new(
            api_key,
            publishers_filepath,
            use_exchange_as_venue,
            bars_timestamp_on_close,
        );

        Self::new(client_id, config, get_atomic_clock_realtime())
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("{e}")))
    }

    /// Returns the client ID.
    #[getter]
    pub fn client_id(&self) -> ClientId {
        DataClient::client_id(self)
    }

    /// Returns whether the client is connected.
    #[getter]
    pub fn is_connected(&self) -> bool {
        DataClient::is_connected(self)
    }

    /// Returns whether the client is disconnected.
    #[getter]
    pub fn is_disconnected(&self) -> bool {
        DataClient::is_disconnected(self)
    }
}
```


---

## Overview

This file is located at `crates/adapters/databento/src/python/data.rs` within the repository.

**Classes defined:** DatabentoDataClient

**Functions defined:** py_new, client_id, is_connected, is_disconnected


---

## Detailed Analysis

### Classes

#### `DatabentoDataClient`

**Type:** impl


### Functions

#### `py_new(
        client_id: ClientId,
        api_key: String,
        publishers_filepath: PathBuf,
        use_exchange_as_venue: bool,
        bars_timestamp_on_close: bool,
    )`


#### `client_id(&self)`


#### `is_connected(&self)`


#### `is_disconnected(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento/src/python`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key. Ensure proper handling of secrets.


