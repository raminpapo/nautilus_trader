# Documentation: `crates/adapters/okx/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:01.306443Z
**File Size:** 2336 bytes
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

- **Path:** `crates/adapters/okx/src/python/mod.rs`
- **Size:** 2,336 bytes
- **Lines:** 51
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

//! Python bindings from `pyo3`.

pub mod enums;
pub mod http;
pub mod models;
pub mod urls;
pub mod websocket;

use pyo3::prelude::*;

/// Loaded as `nautilus_pyo3.okx`.
///
/// # Errors
///
/// Returns an error if any bindings fail to register with the Python module.
#[pymodule]
pub fn okx(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<super::websocket::OKXWebSocketClient>()?;
    m.add_class::<super::websocket::messages::OKXWebSocketError>()?;
    m.add_class::<super::http::OKXHttpClient>()?;
    m.add_class::<crate::http::models::OKXBalanceDetail>()?;
    m.add_class::<crate::common::enums::OKXInstrumentType>()?;
    m.add_class::<crate::common::enums::OKXContractType>()?;
    m.add_class::<crate::common::enums::OKXMarginMode>()?;
    m.add_class::<crate::common::enums::OKXTradeMode>()?;
    m.add_class::<crate::common::enums::OKXOrderStatus>()?;
    m.add_class::<crate::common::enums::OKXPositionMode>()?;
    m.add_class::<crate::common::enums::OKXVipLevel>()?;
    m.add_class::<crate::common::urls::OKXEndpointType>()?;
    m.add_function(wrap_pyfunction!(urls::get_okx_http_base_url, m)?)?;
    m.add_function(wrap_pyfunction!(urls::get_okx_ws_url_public, m)?)?;
    m.add_function(wrap_pyfunction!(urls::get_okx_ws_url_private, m)?)?;
    m.add_function(wrap_pyfunction!(urls::get_okx_ws_url_business, m)?)?;
    m.add_function(wrap_pyfunction!(urls::okx_requires_authentication, m)?)?;
    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/okx/src/python/mod.rs` within the repository.

**Functions defined:** okx


---

## Detailed Analysis

### Functions

#### `okx(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/src/python`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


