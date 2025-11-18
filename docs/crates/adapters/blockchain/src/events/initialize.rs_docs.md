# Documentation: initialize.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/events/initialize.rs`
- **Size**: 1,802 bytes
- **Lines**: 45
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

use alloy::primitives::{Address, U160};
use nautilus_model::defi::SharedDex;

/// Event emitted when a liquidity pool is initialized on a DEX.
///
/// This event typically occurs when a new pool is created and
/// the initial price and tick are set.
#[derive(Debug, Clone)]
pub struct InitializeEvent {
    /// The decentralized exchange where the event happened.
    pub dex: SharedDex,
    /// The address of the smart contract which emitted the event.
    pub pool_address: Address,
    /// The square root of the price ratio encoded as a fixed point number with 96 fractional bits.
    pub sqrt_price_x96: U160,
    /// The current tick of the pool.
    pub tick: i32,
}

impl InitializeEvent {
    pub fn new(dex: SharedDex, pool_address: Address, sqrt_price_x96: U160, tick: i32) -> Self {
        Self {
            dex,
            pool_address,
            sqrt_price_x96,
            tick,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file

### Classes
- **`InitializeEvent`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `new`
**Impls**: `InitializeEvent`
**Structs**: `InitializeEvent`

## Related Files

This file is located in `crates/adapters/blockchain/src/events/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.226381Z*
