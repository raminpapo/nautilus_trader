# Documentation: fluid.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/exchanges/arbitrum/fluid.rs`
- **Size**: 2,520 bytes
- **Lines**: 70
- **Language**: Rust

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`parse_fluid_dex_pool_created_event()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `parse_fluid_dex_pool_created_event`

## Related Files

This file is located in `crates/adapters/blockchain/src/exchanges/arbitrum/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.237729Z*
