# Documentation: `crates/adapters/blockchain/src/exchanges/arbitrum/fluid.rs`
**Generated:** 2025-11-15T19:40:00.502488Z
**File Size:** 2520 bytes
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

- **Path:** `crates/adapters/blockchain/src/exchanges/arbitrum/fluid.rs`
- **Size:** 2,520 bytes
- **Lines:** 69
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

use hypersync_client::simple_types::Log;
use nautilus_model::defi::{
    chain::chains,
    dex::{AmmType, Dex, DexType},
};

use crate::{
    events::pool_created::PoolCreatedEvent,
    exchanges::extended::DexExtended,
    hypersync::helpers::{
        extract_address_from_topic, extract_block_number, validate_event_signature_hash,
    },
};

const POOL_CREATED_EVENT_SIGNATURE_HASH: &str =
    "3fecd5f7aca6136a20a999e7d11ff5dcea4bd675cb125f93ccd7d53f98ec57e4";

/// Fluid DEX on Arbitrum.
pub static FLUID_DEX: LazyLock<DexExtended> = LazyLock::new(|| {
    let mut dex = DexExtended::new(Dex::new(
        chains::ARBITRUM.clone(),
        DexType::FluidDEX,
        "0x91716C4EDA1Fb55e84Bf8b4c7085f84285c19085",
        269528370,
        AmmType::CLAMM,
        "DexT1Deployed(address,uint256,address,address)",
        "",
        "",
        "",
        "",
    ));
    dex.set_pool_created_event_parsing(parse_fluid_dex_pool_created_event);
    dex
});

fn parse_fluid_dex_pool_created_event(log: Log) -> anyhow::Result<PoolCreatedEvent> {
    validate_event_signature_hash("DexT1Deployed", POOL_CREATED_EVENT_SIGNATURE_HASH, &log)?;

    let block_number = extract_block_number(&log)?;
    let pool_address = extract_address_from_topic(&log, 1, "pool")?;
    let supply_token_address = extract_address_from_topic(&log, 2, "supply_token")?;
    let borrow_token_address = extract_address_from_topic(&log, 3, "borrow_token")?;

    Ok(PoolCreatedEvent::new(
        block_number,
        supply_token_address,
        borrow_token_address,
        pool_address,
        None,
        None,
    ))
}
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/exchanges/arbitrum/fluid.rs` within the repository.

**Functions defined:** parse_fluid_dex_pool_created_event


---

## Detailed Analysis

### Functions

#### `parse_fluid_dex_pool_created_event(log: Log)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/exchanges/arbitrum`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.


