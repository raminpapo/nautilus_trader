# Documentation: `crates/adapters/bitmex/src/common/urls.rs`
**Generated:** 2025-11-15T19:40:00.306052Z
**File Size:** 2076 bytes
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

- **Path:** `crates/adapters/bitmex/src/common/urls.rs`
- **Size:** 2,076 bytes
- **Lines:** 61
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 4

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

//! URL helpers for BitMEX services.

use super::consts::{
    BITMEX_HTTP_TESTNET_URL, BITMEX_HTTP_URL, BITMEX_WS_TESTNET_URL, BITMEX_WS_URL,
};

/// Gets the BitMEX HTTP base URL.
pub fn get_http_base_url(testnet: bool) -> String {
    if testnet {
        BITMEX_HTTP_TESTNET_URL.to_string()
    } else {
        BITMEX_HTTP_URL.to_string()
    }
}

/// Gets the BitMEX WebSocket URL.
pub fn get_ws_url(testnet: bool) -> String {
    if testnet {
        BITMEX_WS_TESTNET_URL.to_string()
    } else {
        BITMEX_WS_URL.to_string()
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_http_urls() {
        assert_eq!(get_http_base_url(false), "https://www.bitmex.com/api/v1");
        assert_eq!(get_http_base_url(true), "https://testnet.bitmex.com/api/v1");
    }

    #[rstest]
    fn test_ws_urls() {
        assert_eq!(get_ws_url(false), "wss://ws.bitmex.com/realtime");
        assert_eq!(get_ws_url(true), "wss://ws.testnet.bitmex.com/realtime");
    }
}
```


---

## Overview

This file is located at `crates/adapters/bitmex/src/common/urls.rs` within the repository.

**Functions defined:** get_http_base_url, get_ws_url, test_http_urls, test_ws_urls


---

## Detailed Analysis

### Functions

#### `get_http_base_url(testnet: bool)`


#### `get_ws_url(testnet: bool)`


#### `test_http_urls()`


#### `test_ws_urls()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/src/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


