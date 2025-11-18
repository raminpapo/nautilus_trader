# Documentation: urls.rs

## File Metadata

- **Path**: `crates/adapters/okx/src/python/urls.rs`
- **Size**: 1,865 bytes
- **Lines**: 51
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

//! Python wrapper functions for OKX URL helpers.

use pyo3::prelude::*;

use crate::common::urls;

/// Gets the OKX HTTP base URL.
#[pyfunction]
pub fn get_okx_http_base_url() -> String {
    urls::get_http_base_url()
}

/// Gets the OKX WebSocket URL for public data (market data).
#[pyfunction]
pub fn get_okx_ws_url_public(is_demo: bool) -> String {
    urls::get_ws_base_url_public(is_demo)
}

/// Gets the OKX WebSocket URL for private data (account/order management).
#[pyfunction]
pub fn get_okx_ws_url_private(is_demo: bool) -> String {
    urls::get_ws_base_url_private(is_demo)
}

/// Gets the OKX WebSocket URL for business data (bars/candlesticks).
#[pyfunction]
pub fn get_okx_ws_url_business(is_demo: bool) -> String {
    urls::get_ws_base_url_business(is_demo)
}

/// Checks if OKX endpoint requires authentication.
#[pyfunction]
pub fn okx_requires_authentication(endpoint_type: urls::OKXEndpointType) -> bool {
    urls::requires_authentication(endpoint_type)
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s).

## Detailed Walkthrough

### Functions
- **`get_okx_http_base_url()`**: Function defined in this file
- **`get_okx_ws_url_public()`**: Function defined in this file
- **`get_okx_ws_url_private()`**: Function defined in this file
- **`get_okx_ws_url_business()`**: Function defined in this file
- **`okx_requires_authentication()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `get_okx_http_base_url`, `get_okx_ws_url_business`, `get_okx_ws_url_private`, `get_okx_ws_url_public`, `okx_requires_authentication`

## Related Files

This file is located in `crates/adapters/okx/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.437830Z*
