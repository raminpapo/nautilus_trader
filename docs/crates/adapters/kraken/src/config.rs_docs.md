# Documentation: `crates/adapters/kraken/src/config.rs`
**Generated:** 2025-11-15T19:40:01.134285Z
**File Size:** 3633 bytes
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

- **Path:** `crates/adapters/kraken/src/config.rs`
- **Size:** 3,633 bytes
- **Lines:** 106
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 5
- **Functions:** 7

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


---

## Overview

This file is located at `crates/adapters/kraken/src/config.rs` within the repository.

**Classes defined:** KrakenDataClientConfig, KrakenExecClientConfig, Default, KrakenDataClientConfig, KrakenExecClientConfig

**Functions defined:** default, has_api_credentials, http_base_url, ws_public_url, ws_private_url, http_base_url, ws_url


---

## Detailed Analysis

### Classes

#### `KrakenDataClientConfig`

**Type:** struct


#### `KrakenExecClientConfig`

**Type:** struct


#### `Default`

**Type:** impl


#### `KrakenDataClientConfig`

**Type:** impl


#### `KrakenExecClientConfig`

**Type:** impl


### Functions

#### `default()`


#### `has_api_credentials(&self)`


#### `http_base_url(&self)`


#### `ws_public_url(&self)`


#### `ws_private_url(&self)`


#### `http_base_url(&self)`


#### `ws_url(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret, api_key, credential. Ensure proper handling of secrets.


