# Documentation: urls.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/common/urls.rs`
- **Size**: 2,520 bytes
- **Lines**: 59
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`get_http_base_url()`**: Function defined in this file
- **`get_ws_public_url()`**: Function defined in this file
- **`get_ws_private_url()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `get_http_base_url`, `get_ws_private_url`, `get_ws_public_url`

## Related Files

This file is located in `crates/adapters/kraken/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.168027Z*
