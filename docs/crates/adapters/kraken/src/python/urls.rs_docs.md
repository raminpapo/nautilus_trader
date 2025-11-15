# Documentation: `crates/adapters/kraken/src/python/urls.rs`
**Generated:** 2025-11-15T19:40:01.154582Z
**File Size:** 1793 bytes
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

- **Path:** `crates/adapters/kraken/src/python/urls.rs`
- **Size:** 1,793 bytes
- **Lines:** 50
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 3

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

//! Python bindings for URL builder functions.

use pyo3::prelude::*;

use crate::common::{
    enums::{KrakenEnvironment, KrakenProductType},
    urls::{get_http_base_url, get_ws_private_url, get_ws_public_url},
};

#[pyfunction]
#[pyo3(name = "get_http_base_url")]
pub fn py_get_http_base_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
) -> String {
    get_http_base_url(product_type, environment).to_string()
}

#[pyfunction]
#[pyo3(name = "get_ws_public_url")]
pub fn py_get_ws_public_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
) -> String {
    get_ws_public_url(product_type, environment).to_string()
}

#[pyfunction]
#[pyo3(name = "get_ws_private_url")]
pub fn py_get_ws_private_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
) -> String {
    get_ws_private_url(product_type, environment).to_string()
}
```


---

## Overview

This file is located at `crates/adapters/kraken/src/python/urls.rs` within the repository.

**Functions defined:** py_get_http_base_url, py_get_ws_public_url, py_get_ws_private_url


---

## Detailed Analysis

### Functions

#### `py_get_http_base_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
)`


#### `py_get_ws_public_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
)`


#### `py_get_ws_private_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


