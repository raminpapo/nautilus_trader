# Documentation: flash.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/events/flash.rs`
- **Size**: 3,894 bytes
- **Lines**: 117
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

use alloy::primitives::{Address, U256};
use nautilus_core::UnixNanos;
use nautilus_model::{
    defi::{SharedChain, SharedDex, data::PoolFlash},
    identifiers::InstrumentId,
};

/// Represents a flash loan event from liquidity pools emitted from smart contract.
///
/// This struct captures the essential data from a flash loan transaction on decentralized
/// exchanges (DEXs) that support flash loans.
#[derive(Debug, Clone)]
pub struct FlashEvent {
    /// The decentralized exchange where the event happened.
    pub dex: SharedDex,
    /// The address of the smart contract which emitted the event.
    pub pool_address: Address,
    /// The block number in which this flash loan transaction was included.
    pub block_number: u64,
    /// The unique hash identifier of the transaction containing this event.
    pub transaction_hash: String,
    /// The position of this transaction within the block.
    pub transaction_index: u32,
    /// The position of this event log within the transaction.
    pub log_index: u32,
    /// The address that initiated the flash loan transaction.
    pub sender: Address,
    /// The address that received the flash loan.
    pub recipient: Address,
    /// The amount of token0 borrowed.
    pub amount0: U256,
    /// The amount of token1 borrowed.
    pub amount1: U256,
    /// The amount of token0 paid back (including fees).
    pub paid0: U256,
    /// The amount of token1 paid back (including fees).
    pub paid1: U256,
}

impl FlashEvent {
    /// Creates a new [`FlashEvent`] instance with the specified parameters.
    #[must_use]
    #[allow(clippy::too_many_arguments)]
    pub const fn new(
        dex: SharedDex,
        pool_address: Address,
        block_number: u64,
        transaction_hash: String,
        transaction_index: u32,
        log_index: u32,
        sender: Address,
        recipient: Address,
        amount0: U256,
        amount1: U256,
        paid0: U256,
        paid1: U256,
    ) -> Self {
        Self {
            dex,
            pool_address,
            block_number,
            transaction_hash,
            transaction_index,
            log_index,
            sender,
            recipient,
            amount0,
            amount1,
            paid0,
            paid1,
        }
    }

    /// Converts a flash event into a `PoolFlash`.
    #[must_use]
    pub fn to_pool_flash(
        &self,
        chain: SharedChain,
        instrument_id: InstrumentId,
        pool_address: Address,
        timestamp: Option<UnixNanos>,
    ) -> PoolFlash {
        PoolFlash::new(
            chain,
            self.dex.clone(),
            instrument_id,
            pool_address,
            self.block_number,
            self.transaction_hash.clone(),
            self.transaction_index,
            self.log_index,
            timestamp,
            self.sender,
            self.recipient,
            self.amount0,
            self.amount1,
            self.paid0,
            self.paid1,
        )
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`to_pool_flash()`**: Function defined in this file

### Classes
- **`captures`**: Class defined in this file
- **`FlashEvent`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `new`, `to_pool_flash`
**Impls**: `FlashEvent`
**Structs**: `FlashEvent`, `captures`

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
*Generated on 2025-11-18T21:54:59.224897Z*
