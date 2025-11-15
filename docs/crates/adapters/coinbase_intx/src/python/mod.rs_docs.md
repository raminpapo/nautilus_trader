# Documentation: `crates/adapters/coinbase_intx/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:00.797764Z
**File Size:** 1397 bytes
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

- **Path:** `crates/adapters/coinbase_intx/src/python/mod.rs`
- **Size:** 1,397 bytes
- **Lines:** 34
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

pub mod fix;
pub mod http;
pub mod websocket;

use pyo3::prelude::*;

/// Loaded as `nautilus_pyo3.coinbase`.
#[pymodule]
/// # Errors
///
/// Returns a Python exception if module initialization fails.
pub fn coinbase_intx(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<super::http::CoinbaseIntxHttpClient>()?;
    m.add_class::<super::websocket::CoinbaseIntxWebSocketClient>()?;
    m.add_class::<super::fix::CoinbaseIntxFixClient>()?;
    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/coinbase_intx/src/python/mod.rs` within the repository.

**Functions defined:** coinbase_intx


---

## Detailed Analysis

### Functions

#### `coinbase_intx(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/coinbase_intx/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


