# Documentation: urls.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/python/urls.rs`
- **Size**: 1,793 bytes
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`py_get_http_base_url()`**: Function defined in this file
- **`py_get_ws_public_url()`**: Function defined in this file
- **`py_get_ws_private_url()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `py_get_http_base_url`, `py_get_ws_private_url`, `py_get_ws_public_url`

## Related Files

This file is located in `crates/adapters/kraken/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.199696Z*
