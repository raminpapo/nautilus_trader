# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/bitmex/src/python/mod.rs`
- **Size**: 1,964 bytes
- **Lines**: 47
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

//! Python bindings from `pyo3`.

pub mod canceller;
pub mod enums;
pub mod http;
pub mod submitter;
pub mod urls;
pub mod websocket;

use pyo3::prelude::*;

/// Loaded as `nautilus_pyo3.bitmex`.
///
/// # Errors
///
/// Returns an error if the module registration fails or if adding functions/classes fails.
#[pymodule]
pub fn bitmex(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("BITMEX_HTTP_URL", crate::common::consts::BITMEX_HTTP_URL)?;
    m.add("BITMEX_WS_URL", crate::common::consts::BITMEX_WS_URL)?;
    m.add_class::<crate::common::enums::BitmexSymbolStatus>()?;
    m.add_class::<crate::common::enums::BitmexPositionSide>()?;
    m.add_class::<crate::http::client::BitmexHttpClient>()?;
    m.add_class::<crate::websocket::BitmexWebSocketClient>()?;
    m.add_class::<crate::execution::canceller::CancelBroadcaster>()?;
    m.add_class::<crate::execution::submitter::SubmitBroadcaster>()?;
    m.add_function(wrap_pyfunction!(urls::get_bitmex_http_base_url, m)?)?;
    m.add_function(wrap_pyfunction!(urls::get_bitmex_ws_url, m)?)?;

    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`bitmex()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `bitmex`

## Related Files

This file is located in `crates/adapters/bitmex/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.045715Z*
