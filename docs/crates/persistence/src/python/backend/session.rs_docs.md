# Documentation: `crates/persistence/src/python/backend/session.rs`
**Generated:** 2025-11-15T19:40:03.346252Z
**File Size:** 5216 bytes
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

- **Path:** `crates/persistence/src/python/backend/session.rs`
- **Size:** 5,216 bytes
- **Lines:** 134
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 6

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

use nautilus_core::{
    ffi::cvec::CVec,
    python::{IntoPyObjectNautilusExt, to_pyruntime_err},
};
use nautilus_model::data::{
    Bar, MarkPriceUpdate, OrderBookDelta, OrderBookDepth10, QuoteTick, TradeTick,
};
use pyo3::{prelude::*, types::PyCapsule};

use crate::backend::session::{DataBackendSession, DataQueryResult};

#[repr(C)]
#[pyclass(eq, eq_int)]
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum NautilusDataType {
    // Custom = 0,  # First slot reserved for custom data
    OrderBookDelta = 1,
    OrderBookDepth10 = 2,
    QuoteTick = 3,
    TradeTick = 4,
    Bar = 5,
    MarkPriceUpdate = 6,
}

#[pymethods]
impl DataBackendSession {
    #[new]
    #[pyo3(signature=(chunk_size=10_000))]
    fn new_session(chunk_size: usize) -> Self {
        Self::new(chunk_size)
    }

    /// Query a file for its records. the caller must specify `T` to indicate
    /// the kind of data expected from this query.
    ///
    /// `table_name`: Logical `table_name` assigned to this file. Queries to this file should address the
    /// file by its table name.
    /// `file_path`: Path to file
    /// `sql_query`: A custom sql query to retrieve records from file. If no query is provided a default
    /// query "SELECT * FROM <`table_name`>" is run.
    ///
    /// # Safety
    ///
    /// The file data must be ordered by the `ts_init` in ascending order for this
    /// to work correctly.
    #[pyo3(name = "add_file")]
    #[pyo3(signature = (data_type, table_name, file_path, sql_query=None))]
    fn add_file_py(
        mut slf: PyRefMut<'_, Self>,
        data_type: NautilusDataType,
        table_name: &str,
        file_path: &str,
        sql_query: Option<&str>,
    ) -> PyResult<()> {
        let _guard = slf.runtime.enter();

        match data_type {
            NautilusDataType::OrderBookDelta => slf
                .add_file::<OrderBookDelta>(table_name, file_path, sql_query)
                .map_err(to_pyruntime_err),
            NautilusDataType::OrderBookDepth10 => slf
                .add_file::<OrderBookDepth10>(table_name, file_path, sql_query)
                .map_err(to_pyruntime_err),
            NautilusDataType::QuoteTick => slf
                .add_file::<QuoteTick>(table_name, file_path, sql_query)
                .map_err(to_pyruntime_err),
            NautilusDataType::TradeTick => slf
                .add_file::<TradeTick>(table_name, file_path, sql_query)
                .map_err(to_pyruntime_err),
            NautilusDataType::Bar => slf
                .add_file::<Bar>(table_name, file_path, sql_query)
                .map_err(to_pyruntime_err),
            NautilusDataType::MarkPriceUpdate => slf
                .add_file::<MarkPriceUpdate>(table_name, file_path, sql_query)
                .map_err(to_pyruntime_err),
        }
    }

    fn to_query_result(mut slf: PyRefMut<'_, Self>) -> DataQueryResult {
        let query_result = slf.get_query_result();
        DataQueryResult::new(query_result, slf.chunk_size)
    }

    /// Register an object store with the session context from a URI with optional storage options
    #[pyo3(name = "register_object_store_from_uri")]
    #[pyo3(signature = (uri, storage_options=None))]
    fn register_object_store_from_uri_py(
        mut slf: PyRefMut<'_, Self>,
        uri: &str,
        storage_options: Option<std::collections::HashMap<String, String>>,
    ) -> PyResult<()> {
        slf.register_object_store_from_uri(uri, storage_options)
            .map_err(to_pyruntime_err)
    }
}

#[pymethods]
impl DataQueryResult {
    /// The reader implements an iterator.
    const fn __iter__(slf: PyRef<'_, Self>) -> PyRef<'_, Self> {
        slf
    }

    /// Each iteration returns a chunk of values read from the parquet file.
    fn __next__(mut slf: PyRefMut<'_, Self>) -> PyResult<Option<Py<PyAny>>> {
        match slf.next() {
            Some(acc) if !acc.is_empty() => {
                let cvec = slf.set_chunk(acc);
                Python::attach(|py| {
                    match PyCapsule::new_with_destructor::<CVec, _>(py, cvec, None, |_, _| {}) {
                        Ok(capsule) => Ok(Some(capsule.into_py_any_unwrap(py))),
                        Err(e) => Err(to_pyruntime_err(e)),
                    }
                })
            }
            _ => Ok(None),
        }
    }
}
```


---

## Overview

This file is located at `crates/persistence/src/python/backend/session.rs` within the repository.

**Classes defined:** DataBackendSession, DataQueryResult

**Functions defined:** new_session, add_file_py, to_query_result, register_object_store_from_uri_py, __iter__, __next__


---

## Detailed Analysis

### Classes

#### `DataBackendSession`

**Type:** impl


#### `DataQueryResult`

**Type:** impl


### Functions

#### `new_session(chunk_size: usize)`


#### `add_file_py(
        mut slf: PyRefMut<'_, Self>,
        data_type: NautilusDataType,
        table_name: &str,
        file_path: &str,
        sql_query: Option<&str>,
    )`


#### `to_query_result(mut slf: PyRefMut<'_, Self>)`


#### `register_object_store_from_uri_py(
        mut slf: PyRefMut<'_, Self>,
        uri: &str,
        storage_options: Option<std::collections::HashMap<String, String>>,
    )`


#### `__iter__(slf: PyRef<'_, Self>)`


#### `__next__(mut slf: PyRefMut<'_, Self>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/persistence/src/python/backend`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: session. Ensure proper handling of secrets.


