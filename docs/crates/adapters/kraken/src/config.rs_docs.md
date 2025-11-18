# Documentation: config.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/config.rs`
- **Size**: 3,633 bytes
- **Lines**: 107
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

//! Configuration types for Kraken data and execution clients.

use crate::common::{
    enums::{KrakenEnvironment, KrakenProductType},
    urls::{get_http_base_url, get_ws_private_url, get_ws_public_url},
};

#[derive(Debug, Clone)]
pub struct KrakenDataClientConfig {
    pub api_key: Option<String>,
    pub api_secret: Option<String>,
    pub product_type: KrakenProductType,
    pub environment: KrakenEnvironment,
    pub base_url: Option<String>,
    pub ws_public_url: Option<String>,
    pub ws_private_url: Option<String>,
    pub http_proxy: Option<String>,
    pub ws_proxy: Option<String>,
    pub timeout_secs: Option<u64>,
    pub heartbeat_interval_secs: Option<u64>,
}

impl Default for KrakenDataClientConfig {
    fn default() -> Self {
        Self {
            api_key: None,
            api_secret: None,
            product_type: KrakenProductType::Spot,
            environment: KrakenEnvironment::Mainnet,
            base_url: None,
            ws_public_url: None,
            ws_private_url: None,
            http_proxy: None,
            ws_proxy: None,
            timeout_secs: Some(30),
            heartbeat_interval_secs: Some(30),
        }
    }
}

impl KrakenDataClientConfig {
    pub fn has_api_credentials(&self) -> bool {
        self.api_key.is_some() && self.api_secret.is_some()
    }

    pub fn http_base_url(&self) -> String {
        self.base_url
            .clone()
            .unwrap_or_else(|| get_http_base_url(self.product_type, self.environment).to_string())
    }

    pub fn ws_public_url(&self) -> String {
        self.ws_public_url
            .clone()
            .unwrap_or_else(|| get_ws_public_url(self.product_type, self.environment).to_string())
    }

    pub fn ws_private_url(&self) -> String {
        self.ws_private_url
            .clone()
            .unwrap_or_else(|| get_ws_private_url(self.product_type, self.environment).to_string())
    }
}

#[derive(Debug, Clone)]
pub struct KrakenExecClientConfig {
    pub api_key: String,
    pub api_secret: String,
    pub product_type: KrakenProductType,
    pub environment: KrakenEnvironment,
    pub base_url: Option<String>,
    pub ws_url: Option<String>,
    pub http_proxy: Option<String>,
    pub ws_proxy: Option<String>,
    pub timeout_secs: Option<u64>,
    pub heartbeat_interval_secs: Option<u64>,
}

impl KrakenExecClientConfig {
    pub fn http_base_url(&self) -> String {
        self.base_url
            .clone()
            .unwrap_or_else(|| get_http_base_url(self.product_type, self.environment).to_string())
    }

    pub fn ws_url(&self) -> String {
        self.ws_url
            .clone()
            .unwrap_or_else(|| get_ws_private_url(self.product_type, self.environment).to_string())
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`default()`**: Function defined in this file
- **`has_api_credentials()`**: Function defined in this file
- **`http_base_url()`**: Function defined in this file
- **`ws_public_url()`**: Function defined in this file
- **`ws_private_url()`**: Function defined in this file
- **`http_base_url()`**: Function defined in this file
- **`ws_url()`**: Function defined in this file

### Classes
- **`KrakenDataClientConfig`**: Class defined in this file
- **`KrakenExecClientConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `default`, `has_api_credentials`, `http_base_url`, `ws_private_url`, `ws_public_url`, `ws_url`
**Impls**: `Default`, `KrakenDataClientConfig`, `KrakenExecClientConfig`
**Structs**: `KrakenDataClientConfig`, `KrakenExecClientConfig`

## Related Files

This file is located in `crates/adapters/kraken/src/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:00.170137Z*
