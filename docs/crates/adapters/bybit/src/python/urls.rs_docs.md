# Documentation: `crates/adapters/bybit/src/python/urls.rs`
**Generated:** 2025-11-15T19:40:00.669466Z
**File Size:** 2122 bytes
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

- **Path:** `crates/adapters/bybit/src/python/urls.rs`
- **Size:** 2,122 bytes
- **Lines:** 54
- **Extension:** `.rs`
- **Type:** text
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

//! Python wrapper functions for Bybit URL helpers.

use pyo3::prelude::*;

use crate::common::{
    enums::{BybitEnvironment, BybitProductType},
    urls,
};

/// Gets the Bybit HTTP base URL for the given environment.
#[pyfunction]
#[pyo3(name = "get_bybit_http_base_url")]
pub fn py_get_bybit_http_base_url(environment: BybitEnvironment) -> &'static str {
    urls::bybit_http_base_url(environment)
}

/// Gets the Bybit WebSocket URL for public data (market data).
#[pyfunction]
#[pyo3(name = "get_bybit_ws_url_public")]
pub fn py_get_bybit_ws_url_public(
    product_type: BybitProductType,
    environment: BybitEnvironment,
) -> String {
    urls::bybit_ws_public_url(product_type, environment)
}

/// Gets the Bybit WebSocket URL for private data (account/order management).
#[pyfunction]
#[pyo3(name = "get_bybit_ws_url_private")]
pub fn py_get_bybit_ws_url_private(environment: BybitEnvironment) -> &'static str {
    urls::bybit_ws_private_url(environment)
}

/// Gets the Bybit WebSocket URL for trade operations (order placement/modification).
#[pyfunction]
#[pyo3(name = "get_bybit_ws_url_trade")]
pub fn py_get_bybit_ws_url_trade(environment: BybitEnvironment) -> &'static str {
    urls::bybit_ws_trade_url(environment)
}
```


---

## Overview

This file is located at `crates/adapters/bybit/src/python/urls.rs` within the repository.

**Functions defined:** py_get_bybit_http_base_url, py_get_bybit_ws_url_public, py_get_bybit_ws_url_private, py_get_bybit_ws_url_trade


---

## Detailed Analysis

### Functions

#### `py_get_bybit_http_base_url(environment: BybitEnvironment)`


#### `py_get_bybit_ws_url_public(
    product_type: BybitProductType,
    environment: BybitEnvironment,
)`


#### `py_get_bybit_ws_url_private(environment: BybitEnvironment)`


#### `py_get_bybit_ws_url_trade(environment: BybitEnvironment)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


