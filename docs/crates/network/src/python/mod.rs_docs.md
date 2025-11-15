# Documentation: `crates/network/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:03.223942Z
**File Size:** 4515 bytes
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

- **Path:** `crates/network/src/python/mod.rs`
- **Size:** 4,515 bytes
- **Lines:** 126
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

//! Python bindings from [PyO3](https://pyo3.rs).

// We need to allow `unexpected_cfgs` because the PyO3 macros internally check for
// the `gil-refs` feature. We don’t define or enable `gil-refs` ourselves (due to a
// memory leak), so the compiler raises an error about an unknown cfg feature.
// This attribute prevents those errors without actually enabling `gil-refs`.
#![allow(unexpected_cfgs)]

pub mod http;
pub mod socket;
pub mod websocket;

use std::num::NonZeroU32;

use pyo3::{exceptions::PyException, prelude::*};

use crate::{
    python::{
        http::{HttpClientBuildError, HttpError, HttpInvalidProxyError, HttpTimeoutError},
        websocket::WebSocketClientError,
    },
    ratelimiter::quota::Quota,
};

#[pymethods]
impl Quota {
    /// Construct a quota for a number of requests per second.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if the max burst capacity is 0
    #[staticmethod]
    pub fn rate_per_second(max_burst: u32) -> PyResult<Self> {
        match NonZeroU32::new(max_burst) {
            Some(max_burst) => Ok(Self::per_second(max_burst)),
            None => Err(PyErr::new::<PyException, _>(
                "Max burst capacity should be a non-zero integer",
            )),
        }
    }

    /// Construct a quota for a number of requests per minute.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if the max burst capacity is 0
    #[staticmethod]
    pub fn rate_per_minute(max_burst: u32) -> PyResult<Self> {
        match NonZeroU32::new(max_burst) {
            Some(max_burst) => Ok(Self::per_minute(max_burst)),
            None => Err(PyErr::new::<PyException, _>(
                "Max burst capacity should be a non-zero integer",
            )),
        }
    }

    /// Construct a quota for a number of requests per hour.
    ///
    /// # Errors
    ///
    /// Returns a `PyErr` if the max burst capacity is 0
    #[staticmethod]
    pub fn rate_per_hour(max_burst: u32) -> PyResult<Self> {
        match NonZeroU32::new(max_burst) {
            Some(max_burst) => Ok(Self::per_hour(max_burst)),
            None => Err(PyErr::new::<PyException, _>(
                "Max burst capacity should be a non-zero integer",
            )),
        }
    }
}

/// Loaded as `nautilus_pyo3.network`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn network(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<crate::http::HttpClient>()?;
    m.add_class::<crate::http::HttpMethod>()?;
    m.add_class::<crate::http::HttpResponse>()?;
    m.add_class::<crate::ratelimiter::quota::Quota>()?;
    m.add_class::<crate::websocket::WebSocketClient>()?;
    m.add_class::<crate::websocket::WebSocketConfig>()?;
    m.add_class::<crate::socket::SocketClient>()?;
    m.add_class::<crate::socket::SocketConfig>()?;

    m.add(
        "WebSocketClientError",
        m.py().get_type::<WebSocketClientError>(),
    )?;
    m.add("HttpError", m.py().get_type::<HttpError>())?;
    m.add("HttpTimeoutError", m.py().get_type::<HttpTimeoutError>())?;
    m.add(
        "HttpInvalidProxyError",
        m.py().get_type::<HttpInvalidProxyError>(),
    )?;
    m.add(
        "HttpClientBuildError",
        m.py().get_type::<HttpClientBuildError>(),
    )?;

    m.add_function(wrap_pyfunction!(http::http_get, m)?)?;
    m.add_function(wrap_pyfunction!(http::http_post, m)?)?;
    m.add_function(wrap_pyfunction!(http::http_patch, m)?)?;
    m.add_function(wrap_pyfunction!(http::http_delete, m)?)?;
    m.add_function(wrap_pyfunction!(http::http_download, m)?)?;

    Ok(())
}
```


---

## Overview

This file is located at `crates/network/src/python/mod.rs` within the repository.

**Classes defined:** Quota

**Functions defined:** rate_per_second, rate_per_minute, rate_per_hour, network


---

## Detailed Analysis

### Classes

#### `Quota`

**Type:** impl


### Functions

#### `rate_per_second(max_burst: u32)`


#### `rate_per_minute(max_burst: u32)`


#### `rate_per_hour(max_burst: u32)`


#### `network(_py: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/network/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


