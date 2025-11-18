# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/rpc/mod.rs`
- **Size**: 2,479 bytes
- **Lines**: 64
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

//! RPC client implementations for blockchain network communication.
//!
//! This module provides JSON-RPC client implementations for communicating with various
//! blockchain networks via HTTP and WebSocket connections. It includes specialized
//! clients for different networks (Ethereum, Polygon, Arbitrum, Base) and common
//! utilities for handling RPC requests and responses.

use enum_dispatch::enum_dispatch;

use crate::rpc::{
    chains::{
        arbitrum::ArbitrumRpcClient, base::BaseRpcClient, ethereum::EthereumRpcClient,
        polygon::PolygonRpcClient,
    },
    error::BlockchainRpcClientError,
    types::BlockchainMessage,
};

pub mod chains;
pub mod core;
pub mod error;
pub mod http;
pub mod types;
pub mod utils;

#[enum_dispatch(BlockchainRpcClient)]
#[derive(Debug)]
pub enum BlockchainRpcClientAny {
    Arbitrum(ArbitrumRpcClient),
    Base(BaseRpcClient),
    Ethereum(EthereumRpcClient),
    Polygon(PolygonRpcClient),
}

#[async_trait::async_trait]
#[enum_dispatch]
pub trait BlockchainRpcClient {
    async fn connect(&mut self) -> anyhow::Result<()>;
    async fn subscribe_blocks(&mut self) -> Result<(), BlockchainRpcClientError>;
    async fn subscribe_swaps(&mut self) -> Result<(), BlockchainRpcClientError> {
        todo!("Not implemented")
    }
    async fn unsubscribe_blocks(&mut self) -> Result<(), BlockchainRpcClientError>;
    async fn unsubscribe_swaps(&mut self) -> Result<(), BlockchainRpcClientError> {
        todo!("Not implemented")
    }
    async fn next_rpc_message(&mut self) -> Result<BlockchainMessage, BlockchainRpcClientError>;
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s).

## Detailed Walkthrough

### Functions
- **`connect()`**: Function defined in this file
- **`subscribe_blocks()`**: Function defined in this file
- **`subscribe_swaps()`**: Function defined in this file
- **`unsubscribe_blocks()`**: Function defined in this file
- **`unsubscribe_swaps()`**: Function defined in this file
- **`next_rpc_message()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Enums**: `BlockchainRpcClientAny`
**Functions**: `connect`, `next_rpc_message`, `subscribe_blocks`, `subscribe_swaps`, `unsubscribe_blocks`, `unsubscribe_swaps`
**Traits**: `BlockchainRpcClient`

## Related Files

This file is located in `crates/adapters/blockchain/src/rpc/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.336190Z*
