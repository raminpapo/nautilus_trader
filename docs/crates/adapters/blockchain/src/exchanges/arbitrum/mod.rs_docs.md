# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/exchanges/arbitrum/mod.rs`
- **Size**: 2,051 bytes
- **Lines**: 54
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

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
*Generated on 2025-11-18T21:54:59.239194Z*
