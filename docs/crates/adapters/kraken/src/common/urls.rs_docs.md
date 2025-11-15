# Documentation: `crates/adapters/kraken/src/common/urls.rs`
**Generated:** 2025-11-15T19:40:01.132942Z
**File Size:** 2520 bytes
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

- **Path:** `crates/adapters/kraken/src/common/urls.rs`
- **Size:** 2,520 bytes
- **Lines:** 58
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

//! URL builders for Kraken HTTP and WebSocket endpoints.

use super::{
    consts::{
        KRAKEN_FUTURES_HTTP_URL, KRAKEN_FUTURES_TESTNET_HTTP_URL, KRAKEN_FUTURES_TESTNET_WS_URL,
        KRAKEN_FUTURES_WS_URL, KRAKEN_SPOT_HTTP_URL, KRAKEN_SPOT_WS_PRIVATE_URL,
        KRAKEN_SPOT_WS_PUBLIC_URL,
    },
    enums::{KrakenEnvironment, KrakenProductType},
};

pub fn get_http_base_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
) -> &'static str {
    match (product_type, environment) {
        (KrakenProductType::Spot, _) => KRAKEN_SPOT_HTTP_URL,
        (KrakenProductType::Futures, KrakenEnvironment::Mainnet) => KRAKEN_FUTURES_HTTP_URL,
        (KrakenProductType::Futures, KrakenEnvironment::Testnet) => KRAKEN_FUTURES_TESTNET_HTTP_URL,
    }
}

pub fn get_ws_public_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
) -> &'static str {
    match (product_type, environment) {
        (KrakenProductType::Spot, _) => KRAKEN_SPOT_WS_PUBLIC_URL,
        (KrakenProductType::Futures, KrakenEnvironment::Mainnet) => KRAKEN_FUTURES_WS_URL,
        (KrakenProductType::Futures, KrakenEnvironment::Testnet) => KRAKEN_FUTURES_TESTNET_WS_URL,
    }
}

pub fn get_ws_private_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
) -> &'static str {
    match (product_type, environment) {
        (KrakenProductType::Spot, _) => KRAKEN_SPOT_WS_PRIVATE_URL,
        (KrakenProductType::Futures, KrakenEnvironment::Mainnet) => KRAKEN_FUTURES_WS_URL,
        (KrakenProductType::Futures, KrakenEnvironment::Testnet) => KRAKEN_FUTURES_TESTNET_WS_URL,
    }
}
```


---

## Overview

This file is located at `crates/adapters/kraken/src/common/urls.rs` within the repository.

**Functions defined:** get_http_base_url, get_ws_public_url, get_ws_private_url


---

## Detailed Analysis

### Functions

#### `get_http_base_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
)`


#### `get_ws_public_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
)`


#### `get_ws_private_url(
    product_type: KrakenProductType,
    environment: KrakenEnvironment,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


