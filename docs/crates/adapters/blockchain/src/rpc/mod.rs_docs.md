# Documentation: `crates/adapters/blockchain/src/rpc/mod.rs`
**Generated:** 2025-11-15T19:40:00.587709Z
**File Size:** 2479 bytes
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

- **Path:** `crates/adapters/blockchain/src/rpc/mod.rs`
- **Size:** 2,479 bytes
- **Lines:** 63
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 6

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


---

## Overview

This file is located at `crates/adapters/blockchain/src/rpc/mod.rs` within the repository.

**Functions defined:** connect, subscribe_blocks, subscribe_swaps, unsubscribe_blocks, unsubscribe_swaps, next_rpc_message


---

## Detailed Analysis

### Functions

#### `connect(&mut self)`


#### `subscribe_blocks(&mut self)`


#### `subscribe_swaps(&mut self)`


#### `unsubscribe_blocks(&mut self)`


#### `unsubscribe_swaps(&mut self)`


#### `next_rpc_message(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/rpc`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


