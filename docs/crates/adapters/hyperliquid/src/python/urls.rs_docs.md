# Documentation: urls.rs

## File Metadata

- **Path**: `crates/adapters/hyperliquid/src/python/urls.rs`
- **Size**: 1,555 bytes
- **Lines**: 43
- **Language**: Rust

## Original Source

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
pub fn py_get_hyperliquid_http_base_url(is_testnet: bool) -> String {
    info_url(is_testnet).to_string()
}

/// Get the WebSocket URL for Hyperliquid API.
///
/// # Returns
///
/// The WebSocket URL string.
#[pyfunction]
#[pyo3(name = "get_hyperliquid_ws_url")]
pub fn py_get_hyperliquid_ws_url(is_testnet: bool) -> String {
    ws_url(is_testnet).to_string()
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`py_get_hyperliquid_http_base_url()`**: Function defined in this file
- **`py_get_hyperliquid_ws_url()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `py_get_hyperliquid_http_base_url`, `py_get_hyperliquid_ws_url`

## Related Files

This file is located in `crates/adapters/hyperliquid/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.066134Z*
