# Documentation: `crates/adapters/hyperliquid/src/python/urls.rs`
**Generated:** 2025-11-15T19:40:01.061880Z
**File Size:** 1549 bytes
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

- **Path:** `crates/adapters/hyperliquid/src/python/urls.rs`
- **Size:** 1,549 bytes
- **Lines:** 42
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

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

//! Python bindings for Hyperliquid URL helper functions.

use pyo3::prelude::*;

use crate::common::consts::{info_url, ws_url};

/// Get the HTTP base URL for Hyperliquid API (info endpoint).
///
/// # Returns
///
/// The HTTP base URL string.
#[pyfunction]
#[pyo3(name = "get_hyperliquid_http_base_url")]
pub fn get_hyperliquid_http_base_url(is_testnet: bool) -> String {
    info_url(is_testnet).to_string()
}

/// Get the WebSocket URL for Hyperliquid API.
///
/// # Returns
///
/// The WebSocket URL string.
#[pyfunction]
#[pyo3(name = "get_hyperliquid_ws_url")]
pub fn get_hyperliquid_ws_url(is_testnet: bool) -> String {
    ws_url(is_testnet).to_string()
}
```


---

## Overview

This file is located at `crates/adapters/hyperliquid/src/python/urls.rs` within the repository.

**Functions defined:** get_hyperliquid_http_base_url, get_hyperliquid_ws_url


---

## Detailed Analysis

### Functions

#### `get_hyperliquid_http_base_url(is_testnet: bool)`


#### `get_hyperliquid_ws_url(is_testnet: bool)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/hyperliquid/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


