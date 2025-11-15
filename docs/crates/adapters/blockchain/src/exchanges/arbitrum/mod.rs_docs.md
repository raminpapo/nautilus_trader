# Documentation: `crates/adapters/blockchain/src/exchanges/arbitrum/mod.rs`
**Generated:** 2025-11-15T19:40:00.503739Z
**File Size:** 2051 bytes
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

- **Path:** `crates/adapters/blockchain/src/exchanges/arbitrum/mod.rs`
- **Size:** 2,051 bytes
- **Lines:** 53
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

use std::{collections::HashMap, sync::LazyLock};

use nautilus_model::defi::DexType;

use crate::exchanges::extended::DexExtended;

mod camelot_v3;
mod curve_finance;
mod fluid;
mod pancakeswap_v3;
mod sushiswap_v2;
mod sushiswap_v3;
mod uniswap_v3;
mod uniswap_v4;

pub use camelot_v3::CAMELOT_V3;
pub use curve_finance::CURVE_FINANCE;
pub use fluid::FLUID_DEX;
pub use pancakeswap_v3::PANCAKESWAP_V3;
pub use sushiswap_v2::SUSHISWAP_V2;
pub use sushiswap_v3::SUSHISWAP_V3;
pub use uniswap_v3::UNISWAP_V3;
pub use uniswap_v4::UNISWAP_V4;

pub static ARBITRUM_DEX_EXTENDED_MAP: LazyLock<HashMap<DexType, &'static DexExtended>> =
    LazyLock::new(|| {
        let mut map = HashMap::new();
        map.insert(CAMELOT_V3.dex.name, &*CAMELOT_V3);
        map.insert(CURVE_FINANCE.dex.name, &*CURVE_FINANCE);
        map.insert(FLUID_DEX.dex.name, &*FLUID_DEX);
        map.insert(PANCAKESWAP_V3.name, &*PANCAKESWAP_V3);
        map.insert(SUSHISWAP_V2.dex.name, &*SUSHISWAP_V2);
        map.insert(SUSHISWAP_V3.dex.name, &*SUSHISWAP_V3);
        map.insert(UNISWAP_V3.dex.name, &*UNISWAP_V3);
        map.insert(UNISWAP_V4.dex.name, &*UNISWAP_V4);

        map
    });
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/exchanges/arbitrum/mod.rs` within the repository.


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


