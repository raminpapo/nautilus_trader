# Documentation: `crates/adapters/kraken/src/common/consts.rs`
**Generated:** 2025-11-15T19:40:01.122970Z
**File Size:** 1870 bytes
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

- **Path:** `crates/adapters/kraken/src/common/consts.rs`
- **Size:** 1,870 bytes
- **Lines:** 41
- **Extension:** `.rs`
- **Type:** text

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

//! Core constants shared across the Kraken adapter components.

use std::sync::LazyLock;

use nautilus_model::identifiers::Venue;
use ustr::Ustr;

pub const KRAKEN: &str = "KRAKEN";
pub static KRAKEN_VENUE: LazyLock<Venue> = LazyLock::new(|| Venue::new(Ustr::from(KRAKEN)));

// WebSocket-specific constants
pub const KRAKEN_PONG: &str = "pong";
pub const KRAKEN_WS_TOPIC_DELIMITER: char = '.';

// Spot API URLs (v2)
pub const KRAKEN_SPOT_HTTP_URL: &str = "https://api.kraken.com";
pub const KRAKEN_SPOT_WS_PUBLIC_URL: &str = "wss://ws.kraken.com/v2";
pub const KRAKEN_SPOT_WS_PRIVATE_URL: &str = "wss://ws-auth.kraken.com/v2";

// Futures API URLs
pub const KRAKEN_FUTURES_HTTP_URL: &str = "https://futures.kraken.com";
pub const KRAKEN_FUTURES_WS_URL: &str = "wss://futures.kraken.com/ws/v1";

// Testnet URLs
pub const KRAKEN_FUTURES_TESTNET_HTTP_URL: &str = "https://demo-futures.kraken.com";
pub const KRAKEN_FUTURES_TESTNET_WS_URL: &str = "wss://demo-futures.kraken.com/ws/v1";
```


---

## Overview

This file is located at `crates/adapters/kraken/src/common/consts.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


