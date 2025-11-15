# Documentation: `crates/adapters/blockchain/src/exchanges/arbitrum/pancakeswap_v3.rs`
**Generated:** 2025-11-15T19:40:00.505033Z
**File Size:** 1599 bytes
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

- **Path:** `crates/adapters/blockchain/src/exchanges/arbitrum/pancakeswap_v3.rs`
- **Size:** 1,599 bytes
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

use std::sync::LazyLock;

use nautilus_model::defi::{
    chain::chains,
    dex::{AmmType, Dex, DexType},
};

use crate::exchanges::{extended::DexExtended, parsing::uniswap_v3};

/// PancakeSwap V3 DEX on Arbitrum.
pub static PANCAKESWAP_V3: LazyLock<DexExtended> = LazyLock::new(|| {
    let mut dex = DexExtended::new(Dex::new(
        chains::ARBITRUM.clone(),
        DexType::PancakeSwapV3,
        "0x0BFbCF9fa4f9C56B0F40a671Ad40E0805A091865",
        105068129,
        AmmType::CLAMM,
        "PoolCreated(address,address,uint24,int24,address)",
        "",
        "",
        "",
        "",
    ));
    dex.set_pool_created_event_parsing(uniswap_v3::pool_created::parse_pool_created_event);
    dex
});
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/exchanges/arbitrum/pancakeswap_v3.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/exchanges/arbitrum`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


