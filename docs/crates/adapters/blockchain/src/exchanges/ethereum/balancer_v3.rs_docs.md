# Documentation: `crates/adapters/blockchain/src/exchanges/ethereum/balancer_v3.rs`
**Generated:** 2025-11-15T19:40:00.526862Z
**File Size:** 1423 bytes
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

- **Path:** `crates/adapters/blockchain/src/exchanges/ethereum/balancer_v3.rs`
- **Size:** 1,423 bytes
- **Lines:** 40
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

use crate::exchanges::extended::DexExtended;

/// Balancer V3 DEX on Ethereum.
pub static BALANCER_V3: LazyLock<DexExtended> = LazyLock::new(|| {
    let dex = Dex::new(
        chains::ETHEREUM.clone(),
        DexType::BalancerV3,
        "0x43A0F3e8F0E2d9F35E82A5092D5B3CfB9C041CcC",
        0,
        AmmType::ComposablePool,
        "",
        "",
        "",
        "",
        "",
    );
    DexExtended::new(dex)
});
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/exchanges/ethereum/balancer_v3.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/exchanges/ethereum`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


