# Documentation: `crates/adapters/kraken/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:01.153182Z
**File Size:** 2339 bytes
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

- **Path:** `crates/adapters/kraken/src/python/mod.rs`
- **Size:** 2,339 bytes
- **Lines:** 62
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

use pyo3::prelude::*;

use crate::{
    common::enums::{
        KrakenAssetClass, KrakenEnvironment, KrakenOrderSide, KrakenOrderStatus, KrakenOrderType,
        KrakenPairStatus, KrakenPositionSide, KrakenProductType, KrakenSystemStatus,
        KrakenTimeInForce,
    },
    http::client::KrakenHttpClient,
    websocket::{
        client::KrakenWebSocketClient,
        enums::{KrakenWsChannel, KrakenWsMessageType, KrakenWsMethod},
    },
};

pub mod enums;
pub mod http;
pub mod urls;
pub mod websocket;

#[pymodule]
pub fn kraken(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<KrakenEnvironment>()?;
    m.add_class::<KrakenProductType>()?;
    m.add_class::<KrakenOrderType>()?;
    m.add_class::<KrakenOrderSide>()?;
    m.add_class::<KrakenTimeInForce>()?;
    m.add_class::<KrakenOrderStatus>()?;
    m.add_class::<KrakenPositionSide>()?;
    m.add_class::<KrakenPairStatus>()?;
    m.add_class::<KrakenSystemStatus>()?;
    m.add_class::<KrakenAssetClass>()?;
    m.add_class::<KrakenWsMethod>()?;
    m.add_class::<KrakenWsChannel>()?;
    m.add_class::<KrakenWsMessageType>()?;

    m.add_class::<KrakenHttpClient>()?;
    m.add_class::<KrakenWebSocketClient>()?;

    m.add_function(wrap_pyfunction!(urls::py_get_http_base_url, m)?)?;
    m.add_function(wrap_pyfunction!(urls::py_get_ws_public_url, m)?)?;
    m.add_function(wrap_pyfunction!(urls::py_get_ws_private_url, m)?)?;

    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/kraken/src/python/mod.rs` within the repository.

**Functions defined:** kraken


---

## Detailed Analysis

### Functions

#### `kraken(m: &Bound<'_, PyModule>)`



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


