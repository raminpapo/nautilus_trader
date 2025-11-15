# Documentation: `crates/adapters/bitmex/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:00.365454Z
**File Size:** 1964 bytes
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

- **Path:** `crates/adapters/bitmex/src/python/mod.rs`
- **Size:** 1,964 bytes
- **Lines:** 46
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


---

## Overview

This file is located at `crates/adapters/bitmex/src/python/mod.rs` within the repository.

**Functions defined:** bitmex


---

## Detailed Analysis

### Functions

#### `bitmex(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


