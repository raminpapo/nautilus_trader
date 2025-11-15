# Documentation: `crates/adapters/okx/src/config.rs`
**Generated:** 2025-11-15T19:40:01.258229Z
**File Size:** 9650 bytes
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

- **Path:** `crates/adapters/okx/src/config.rs`
- **Size:** 9,650 bytes
- **Lines:** 248
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 6
- **Functions:** 13

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

//! Configuration structures for the OKX adapter.

use crate::common::{
    enums::{OKXContractType, OKXInstrumentType, OKXMarginMode, OKXVipLevel},
    urls::{
        get_http_base_url, get_ws_base_url_business, get_ws_base_url_private,
        get_ws_base_url_public,
    },
};

/// Configuration for the OKX data client.
#[derive(Clone, Debug)]
pub struct OKXDataClientConfig {
    /// Optional API key for authenticated endpoints.
    pub api_key: Option<String>,
    /// Optional API secret for authenticated endpoints.
    pub api_secret: Option<String>,
    /// Optional API passphrase for authenticated endpoints.
    pub api_passphrase: Option<String>,
    /// Instrument types to load and subscribe to.
    pub instrument_types: Vec<OKXInstrumentType>,
    /// Contract type filter applied to loaded instruments.
    pub contract_types: Option<Vec<OKXContractType>>,
    /// Instrument families to load (e.g., "BTC-USD", "ETH-USD").
    /// Required for OPTIONS. Optional for FUTURES/SWAP. Not applicable for SPOT/MARGIN.
    pub instrument_families: Option<Vec<String>>,
    /// Optional override for the HTTP base URL.
    pub base_url_http: Option<String>,
    /// Optional override for the public WebSocket URL.
    pub base_url_ws_public: Option<String>,
    /// Optional override for the business WebSocket URL.
    pub base_url_ws_business: Option<String>,
    /// Optional HTTP proxy URL.
    pub http_proxy_url: Option<String>,
    /// Optional WebSocket proxy URL.
    ///
    /// Note: WebSocket proxy support is not yet implemented. This field is reserved
    /// for future functionality. Use `http_proxy_url` for REST API proxy support.
    pub ws_proxy_url: Option<String>,
    /// When true the client will use OKX demo endpoints.
    pub is_demo: bool,
    /// Optional HTTP timeout in seconds.
    pub http_timeout_secs: Option<u64>,
    /// Optional maximum retry attempts for requests.
    pub max_retries: Option<u32>,
    /// Optional initial retry delay in milliseconds.
    pub retry_delay_initial_ms: Option<u64>,
    /// Optional maximum retry delay in milliseconds.
    pub retry_delay_max_ms: Option<u64>,
    /// Optional interval for refreshing instruments.
    pub update_instruments_interval_mins: Option<u64>,
    /// Optional VIP level that unlocks additional subscriptions.
    pub vip_level: Option<OKXVipLevel>,
}

impl Default for OKXDataClientConfig {
    fn default() -> Self {
        Self {
            api_key: None,
            api_secret: None,
            api_passphrase: None,
            instrument_types: vec![OKXInstrumentType::Spot],
            contract_types: None,
            instrument_families: None,
            base_url_http: None,
            base_url_ws_public: None,
            base_url_ws_business: None,
            http_proxy_url: None,
            ws_proxy_url: None,
            is_demo: false,
            http_timeout_secs: Some(60),
            max_retries: Some(3),
            retry_delay_initial_ms: Some(1_000),
            retry_delay_max_ms: Some(10_000),
            update_instruments_interval_mins: Some(60),
            vip_level: None,
        }
    }
}

impl OKXDataClientConfig {
    /// Creates a new configuration with default settings.
    #[must_use]
    pub fn new() -> Self {
        Self::default()
    }

    /// Returns `true` when all API credential fields are populated.
    #[must_use]
    pub fn has_api_credentials(&self) -> bool {
        self.api_key.is_some() && self.api_secret.is_some() && self.api_passphrase.is_some()
    }

    /// Returns the HTTP base URL, falling back to the default when unset.
    #[must_use]
    pub fn http_base_url(&self) -> String {
        self.base_url_http.clone().unwrap_or_else(get_http_base_url)
    }

    /// Returns the public WebSocket URL, respecting the demo flag and overrides.
    #[must_use]
    pub fn ws_public_url(&self) -> String {
        self.base_url_ws_public
            .clone()
            .unwrap_or_else(|| get_ws_base_url_public(self.is_demo))
    }

    /// Returns the business WebSocket URL, respecting the demo flag and overrides.
    #[must_use]
    pub fn ws_business_url(&self) -> String {
        self.base_url_ws_business
            .clone()
            .unwrap_or_else(|| get_ws_base_url_business(self.is_demo))
    }

    /// Returns `true` when the business WebSocket should be instantiated.
    #[must_use]
    pub fn requires_business_ws(&self) -> bool {
        self.has_api_credentials()
    }
}

/// Configuration for the OKX execution client.
#[derive(Clone, Debug)]
pub struct OKXExecClientConfig {
    /// Optional API key for authenticated endpoints.
    pub api_key: Option<String>,
    /// Optional API secret for authenticated endpoints.
    pub api_secret: Option<String>,
    /// Optional API passphrase for authenticated endpoints.
    pub api_passphrase: Option<String>,
    /// Instrument types the execution client should support.
    pub instrument_types: Vec<OKXInstrumentType>,
    /// Contract type filter applied to operations.
    pub contract_types: Option<Vec<OKXContractType>>,
    /// Instrument families to load (e.g., "BTC-USD", "ETH-USD").
    /// Required for OPTIONS. Optional for FUTURES/SWAP. Not applicable for SPOT/MARGIN.
    pub instrument_families: Option<Vec<String>>,
    /// Optional override for the HTTP base URL.
    pub base_url_http: Option<String>,
    /// Optional override for the private WebSocket URL.
    pub base_url_ws_private: Option<String>,
    /// Optional override for the business WebSocket URL.
    pub base_url_ws_business: Option<String>,
    /// Optional HTTP proxy URL.
    pub http_proxy_url: Option<String>,
    /// Optional WebSocket proxy URL.
    ///
    /// Note: WebSocket proxy support is not yet implemented. This field is reserved
    /// for future functionality. Use `http_proxy_url` for REST API proxy support.
    pub ws_proxy_url: Option<String>,
    /// When true the client will use OKX demo endpoints.
    pub is_demo: bool,
    /// Optional HTTP timeout in seconds.
    pub http_timeout_secs: Option<u64>,
    /// Enables consumption of the fills WebSocket channel when true.
    pub use_fills_channel: bool,
    /// Enables mass-cancel support when true.
    pub use_mm_mass_cancel: bool,
    /// Optional maximum retry attempts for requests.
    pub max_retries: Option<u32>,
    /// Optional initial retry delay in milliseconds.
    pub retry_delay_initial_ms: Option<u64>,
    /// Optional maximum retry delay in milliseconds.
    pub retry_delay_max_ms: Option<u64>,
    /// Optional margin mode (CROSS or ISOLATED) for margin/derivative accounts.
    pub margin_mode: Option<OKXMarginMode>,
    /// Enables margin/leverage for SPOT trading when true.
    pub use_spot_margin: bool,
}

impl Default for OKXExecClientConfig {
    fn default() -> Self {
        Self {
            api_key: None,
            api_secret: None,
            api_passphrase: None,
            instrument_types: vec![OKXInstrumentType::Spot],
            contract_types: None,
            instrument_families: None,
            base_url_http: None,
            base_url_ws_private: None,
            base_url_ws_business: None,
            http_proxy_url: None,
            ws_proxy_url: None,
            is_demo: false,
            http_timeout_secs: Some(60),
            use_fills_channel: false,
            use_mm_mass_cancel: false,
            max_retries: Some(3),
            retry_delay_initial_ms: Some(1_000),
            retry_delay_max_ms: Some(10_000),
            margin_mode: None,
            use_spot_margin: false,
        }
    }
}

impl OKXExecClientConfig {
    /// Creates a new configuration with default settings.
    #[must_use]
    pub fn new() -> Self {
        Self::default()
    }

    /// Returns `true` when all API credential fields are populated.
    #[must_use]
    pub fn has_api_credentials(&self) -> bool {
        self.api_key.is_some() && self.api_secret.is_some() && self.api_passphrase.is_some()
    }

    /// Returns the HTTP base URL, falling back to the default when unset.
    #[must_use]
    pub fn http_base_url(&self) -> String {
        self.base_url_http.clone().unwrap_or_else(get_http_base_url)
    }

    /// Returns the private WebSocket URL, respecting the demo flag and overrides.
    #[must_use]
    pub fn ws_private_url(&self) -> String {
        self.base_url_ws_private
            .clone()
            .unwrap_or_else(|| get_ws_base_url_private(self.is_demo))
    }

    /// Returns the business WebSocket URL, respecting the demo flag and overrides.
    #[must_use]
    pub fn ws_business_url(&self) -> String {
        self.base_url_ws_business
            .clone()
            .unwrap_or_else(|| get_ws_base_url_business(self.is_demo))
    }
}
```


---

## Overview

This file is located at `crates/adapters/okx/src/config.rs` within the repository.

**Classes defined:** OKXDataClientConfig, OKXExecClientConfig, Default, OKXDataClientConfig, Default, OKXExecClientConfig

**Functions defined:** default, new, has_api_credentials, http_base_url, ws_public_url, ws_business_url, requires_business_ws, default, new, has_api_credentials and 3 more


---

## Detailed Analysis

### Classes

#### `OKXDataClientConfig`

**Type:** struct


#### `OKXExecClientConfig`

**Type:** struct


#### `Default`

**Type:** impl


#### `OKXDataClientConfig`

**Type:** impl


#### `Default`

**Type:** impl


#### `OKXExecClientConfig`

**Type:** impl


### Functions

#### `default()`


#### `new()`


#### `has_api_credentials(&self)`


#### `http_base_url(&self)`


#### `ws_public_url(&self)`


#### `ws_business_url(&self)`


#### `requires_business_ws(&self)`


#### `default()`


#### `new()`


#### `has_api_credentials(&self)`


#### `http_base_url(&self)`


#### `ws_private_url(&self)`


#### `ws_business_url(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/src`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key, credential, auth. Ensure proper handling of secrets.


