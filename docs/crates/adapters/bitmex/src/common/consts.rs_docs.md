# Documentation: `crates/adapters/bitmex/src/common/consts.rs`
**Generated:** 2025-11-15T19:40:00.291766Z
**File Size:** 1513 bytes
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

- **Path:** `crates/adapters/bitmex/src/common/consts.rs`
- **Size:** 1,513 bytes
- **Lines:** 32
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

//! BitMEX adapter constants including base URLs and the venue identifier.

use std::sync::LazyLock;

use nautilus_model::identifiers::Venue;
use ustr::Ustr;

pub const BITMEX: &str = "BITMEX";

pub const BITMEX_WS_URL: &str = "wss://ws.bitmex.com/realtime";
pub const BITMEX_WS_TESTNET_URL: &str = "wss://ws.testnet.bitmex.com/realtime";
pub const BITMEX_HTTP_URL: &str = "https://www.bitmex.com/api/v1";
pub const BITMEX_HTTP_TESTNET_URL: &str = "https://testnet.bitmex.com/api/v1";

pub const BITMEX_WS_TOPIC_DELIMITER: char = ':';

pub static BITMEX_VENUE: LazyLock<Venue> = LazyLock::new(|| Venue::new(Ustr::from(BITMEX)));
```


---

## Overview

This file is located at `crates/adapters/bitmex/src/common/consts.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


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


