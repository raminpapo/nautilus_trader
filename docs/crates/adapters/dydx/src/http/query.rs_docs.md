# Documentation: `crates/adapters/dydx/src/http/query.rs`
**Generated:** 2025-11-15T19:40:00.942238Z
**File Size:** 2147 bytes
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

- **Path:** `crates/adapters/dydx/src/http/query.rs`
- **Size:** 2,147 bytes
- **Lines:** 56
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4

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

//! Query parameter builders for dYdX v4 Indexer REST API endpoints.

use derive_builder::Builder;
use serde::Serialize;

use crate::common::enums::DydxCandleResolution;

/// Query parameters for fetching orderbook.
#[derive(Debug, Clone, Default, Serialize, Builder)]
#[builder(setter(into, strip_option), default)]
pub struct GetOrderbookParams {
    pub ticker: String,
}

/// Query parameters for fetching trades.
#[derive(Debug, Clone, Default, Serialize, Builder)]
#[builder(setter(into, strip_option), default)]
pub struct GetTradesParams {
    pub ticker: String,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub limit: Option<u32>,
}

/// Query parameters for fetching candles.
#[derive(Debug, Clone, Default, Serialize, Builder)]
#[builder(setter(into, strip_option), default)]
pub struct GetCandlesParams {
    pub ticker: String,
    pub resolution: DydxCandleResolution,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub limit: Option<u32>,
}

/// Query parameters for fetching subaccount.
#[derive(Debug, Clone, Default, Serialize, Builder)]
#[builder(setter(into, strip_option), default)]
pub struct GetSubaccountParams {
    pub address: String,
    #[serde(rename = "subaccountNumber")]
    pub subaccount_number: u32,
}
```


---

## Overview

This file is located at `crates/adapters/dydx/src/http/query.rs` within the repository.

**Classes defined:** GetOrderbookParams, GetTradesParams, GetCandlesParams, GetSubaccountParams


---

## Detailed Analysis

### Classes

#### `GetOrderbookParams`

**Type:** struct


#### `GetTradesParams`

**Type:** struct


#### `GetCandlesParams`

**Type:** struct


#### `GetSubaccountParams`

**Type:** struct



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


