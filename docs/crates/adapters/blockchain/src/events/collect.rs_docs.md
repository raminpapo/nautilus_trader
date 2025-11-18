# Documentation: collect.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/events/collect.rs`
- **Size**: 3,777 bytes
- **Lines**: 114
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

use alloy::primitives::Address;
use nautilus_core::UnixNanos;
use nautilus_model::{
    defi::{SharedChain, SharedDex, data::PoolFeeCollect},
    identifiers::InstrumentId,
};

/// Represents a collect event that occurs when fees are collected from a position in a liquidity pool.
#[derive(Debug, Clone)]
pub struct CollectEvent {
    /// The decentralized exchange where the event happened.
    pub dex: SharedDex,
    /// The address of the smart contract which emitted the event.
    pub pool_address: Address,
    /// The block number when the collect occurred.
    pub block_number: u64,
    /// The unique hash identifier of the transaction containing this event.
    pub transaction_hash: String,
    /// The position of this transaction within the block.
    pub transaction_index: u32,
    /// The position of this event log within the transaction.
    pub log_index: u32,
    /// The owner of the position.
    pub owner: Address,
    /// The recipient of the collected fees.
    pub recipient: Address,
    /// The lower tick boundary of the position.
    pub tick_lower: i32,
    /// The upper tick boundary of the position.
    pub tick_upper: i32,
    /// The amount of token0 fees collected.
    pub amount0: u128,
    /// The amount of token1 fees collected.
    pub amount1: u128,
}

impl CollectEvent {
    /// Creates a new [`CollectEvent`] instance with the specified parameters.
    #[must_use]
    #[allow(clippy::too_many_arguments)]
    pub const fn new(
        dex: SharedDex,
        pool_address: Address,
        block_number: u64,
        transaction_hash: String,
        transaction_index: u32,
        log_index: u32,
        owner: Address,
        recipient: Address,
        tick_lower: i32,
        tick_upper: i32,
        amount0: u128,
        amount1: u128,
    ) -> Self {
        Self {
            dex,
            pool_address,
            block_number,
            transaction_hash,
            transaction_index,
            log_index,
            owner,
            recipient,
            tick_lower,
            tick_upper,
            amount0,
            amount1,
        }
    }

    /// Converts a collect event into a `PoolFeeCollect`.
    #[allow(clippy::too_many_arguments)]
    pub fn to_pool_fee_collect(
        &self,
        chain: SharedChain,
        dex: SharedDex,
        instrument_id: InstrumentId,
        pool_address: Address,
        timestamp: Option<UnixNanos>,
    ) -> PoolFeeCollect {
        PoolFeeCollect::new(
            chain,
            dex,
            instrument_id,
            pool_address,
            self.block_number,
            self.transaction_hash.clone(),
            self.transaction_index,
            self.log_index,
            self.owner,
            self.amount0,
            self.amount1,
            self.tick_lower,
            self.tick_upper,
            timestamp,
        )
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`to_pool_fee_collect()`**: Function defined in this file

### Classes
- **`CollectEvent`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `new`, `to_pool_fee_collect`
**Impls**: `CollectEvent`
**Structs**: `CollectEvent`

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
*Generated on 2025-11-18T21:54:59.223075Z*
