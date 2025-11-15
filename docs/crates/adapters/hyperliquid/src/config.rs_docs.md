# Documentation: `crates/adapters/hyperliquid/src/config.rs`
**Generated:** 2025-11-15T19:40:01.015322Z
**File Size:** 6041 bytes
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

- **Path:** `crates/adapters/hyperliquid/src/config.rs`
- **Size:** 6,041 bytes
- **Lines:** 174
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 6
- **Functions:** 10

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

//! Configuration structures for the Hyperliquid adapter.

use crate::common::consts::{info_url, ws_url};

/// Configuration for the Hyperliquid data client.
#[derive(Clone, Debug)]
pub struct HyperliquidDataClientConfig {
    /// Optional private key for authenticated endpoints.
    pub private_key: Option<String>,
    /// Override for the WebSocket URL.
    pub base_url_ws: Option<String>,
    /// Override for the HTTP info URL.
    pub base_url_http: Option<String>,
    /// Optional HTTP proxy URL.
    pub http_proxy_url: Option<String>,
    /// Optional WebSocket proxy URL.
    ///
    /// Note: WebSocket proxy support is not yet implemented. This field is reserved
    /// for future functionality. Use `http_proxy_url` for REST API proxy support.
    pub ws_proxy_url: Option<String>,
    /// When true the client will use Hyperliquid testnet endpoints.
    pub is_testnet: bool,
    /// HTTP timeout in seconds.
    pub http_timeout_secs: Option<u64>,
    /// WebSocket timeout in seconds.
    pub ws_timeout_secs: Option<u64>,
    /// Optional interval for refreshing instruments.
    pub update_instruments_interval_mins: Option<u64>,
}

impl Default for HyperliquidDataClientConfig {
    fn default() -> Self {
        Self {
            private_key: None,
            base_url_ws: None,
            base_url_http: None,
            http_proxy_url: None,
            ws_proxy_url: None,
            is_testnet: false,
            http_timeout_secs: Some(60),
            ws_timeout_secs: Some(30),
            update_instruments_interval_mins: Some(60),
        }
    }
}

impl HyperliquidDataClientConfig {
    /// Creates a new configuration with default settings.
    #[must_use]
    pub fn new() -> Self {
        Self::default()
    }

    /// Returns `true` when private key is populated.
    #[must_use]
    pub fn has_credentials(&self) -> bool {
        self.private_key.is_some()
    }

    /// Returns the WebSocket URL, respecting the testnet flag and overrides.
    #[must_use]
    pub fn ws_url(&self) -> String {
        self.base_url_ws
            .clone()
            .unwrap_or_else(|| ws_url(self.is_testnet).to_string())
    }

    /// Returns the HTTP info URL, respecting the testnet flag and overrides.
    #[must_use]
    pub fn http_url(&self) -> String {
        self.base_url_http
            .clone()
            .unwrap_or_else(|| info_url(self.is_testnet).to_string())
    }
}

/// Configuration for the Hyperliquid execution client.
#[derive(Clone, Debug)]
pub struct HyperliquidExecClientConfig {
    /// Private key for signing transactions (required for execution).
    pub private_key: String,
    /// Optional vault address for vault operations.
    pub vault_address: Option<String>,
    /// Override for the WebSocket URL.
    pub base_url_ws: Option<String>,
    /// Override for the HTTP info URL.
    pub base_url_http: Option<String>,
    /// Override for the exchange API URL.
    pub base_url_exchange: Option<String>,
    /// Optional HTTP proxy URL.
    pub http_proxy_url: Option<String>,
    /// Optional WebSocket proxy URL.
    ///
    /// Note: WebSocket proxy support is not yet implemented. This field is reserved
    /// for future functionality. Use `http_proxy_url` for REST API proxy support.
    pub ws_proxy_url: Option<String>,
    /// When true the client will use Hyperliquid testnet endpoints.
    pub is_testnet: bool,
    /// HTTP timeout in seconds.
    pub http_timeout_secs: u64,
    /// Maximum number of retry attempts for HTTP requests.
    pub max_retries: u32,
    /// Initial retry delay in milliseconds.
    pub retry_delay_initial_ms: u64,
    /// Maximum retry delay in milliseconds.
    pub retry_delay_max_ms: u64,
}

impl Default for HyperliquidExecClientConfig {
    fn default() -> Self {
        Self {
            private_key: String::new(),
            vault_address: None,
            base_url_ws: None,
            base_url_http: None,
            base_url_exchange: None,
            http_proxy_url: None,
            ws_proxy_url: None,
            is_testnet: false,
            http_timeout_secs: 60,
            max_retries: 3,
            retry_delay_initial_ms: 100,
            retry_delay_max_ms: 5000,
        }
    }
}

impl HyperliquidExecClientConfig {
    /// Creates a new configuration with the provided private key.
    #[must_use]
    pub fn new(private_key: String) -> Self {
        Self {
            private_key,
            ..Self::default()
        }
    }

    /// Returns `true` when private key is populated.
    #[must_use]
    pub fn has_credentials(&self) -> bool {
        !self.private_key.is_empty()
    }

    /// Returns the WebSocket URL, respecting the testnet flag and overrides.
    #[must_use]
    pub fn ws_url(&self) -> String {
        self.base_url_ws
            .clone()
            .unwrap_or_else(|| ws_url(self.is_testnet).to_string())
    }

    /// Returns the HTTP info URL, respecting the testnet flag and overrides.
    #[must_use]
    pub fn http_url(&self) -> String {
        self.base_url_http
            .clone()
            .unwrap_or_else(|| info_url(self.is_testnet).to_string())
    }
}
```


---

## Overview

This file is located at `crates/adapters/hyperliquid/src/config.rs` within the repository.

**Classes defined:** HyperliquidDataClientConfig, HyperliquidExecClientConfig, Default, HyperliquidDataClientConfig, Default, HyperliquidExecClientConfig

**Functions defined:** default, new, has_credentials, ws_url, http_url, default, new, has_credentials, ws_url, http_url


---

## Detailed Analysis

### Classes

#### `HyperliquidDataClientConfig`

**Type:** struct


#### `HyperliquidExecClientConfig`

**Type:** struct


#### `Default`

**Type:** impl


#### `HyperliquidDataClientConfig`

**Type:** impl


#### `Default`

**Type:** impl


#### `HyperliquidExecClientConfig`

**Type:** impl


### Functions

#### `default()`


#### `new()`


#### `has_credentials(&self)`


#### `ws_url(&self)`


#### `http_url(&self)`


#### `default()`


#### `new(private_key: String)`


#### `has_credentials(&self)`


#### `ws_url(&self)`


#### `http_url(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/hyperliquid/src`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: private_key, credential, auth. Ensure proper handling of secrets.


