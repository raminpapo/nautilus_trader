# Documentation: `crates/adapters/blockchain/src/rpc/chains/arbitrum.rs`
**Generated:** 2025-11-15T19:40:00.575231Z
**File Size:** 1986 bytes
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

- **Path:** `crates/adapters/blockchain/src/rpc/chains/arbitrum.rs`
- **Size:** 1,986 bytes
- **Lines:** 53
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 5

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

use nautilus_model::defi::chain::chains;

use crate::rpc::{
    BlockchainRpcClient, core::CoreBlockchainRpcClient, error::BlockchainRpcClientError,
    types::BlockchainMessage,
};

#[derive(Debug)]
pub struct ArbitrumRpcClient {
    base_client: CoreBlockchainRpcClient,
}

impl ArbitrumRpcClient {
    pub fn new(wss_rpc_url: String) -> Self {
        let base_client = CoreBlockchainRpcClient::new(chains::ARBITRUM.clone(), wss_rpc_url);

        Self { base_client }
    }
}

#[async_trait::async_trait]
impl BlockchainRpcClient for ArbitrumRpcClient {
    async fn connect(&mut self) -> anyhow::Result<()> {
        self.base_client.connect().await
    }

    async fn subscribe_blocks(&mut self) -> Result<(), BlockchainRpcClientError> {
        self.base_client.subscribe_blocks().await
    }

    async fn unsubscribe_blocks(&mut self) -> Result<(), BlockchainRpcClientError> {
        self.base_client.unsubscribe_blocks().await
    }

    async fn next_rpc_message(&mut self) -> Result<BlockchainMessage, BlockchainRpcClientError> {
        self.base_client.next_rpc_message().await
    }
}
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/rpc/chains/arbitrum.rs` within the repository.

**Classes defined:** ArbitrumRpcClient, ArbitrumRpcClient, BlockchainRpcClient

**Functions defined:** new, connect, subscribe_blocks, unsubscribe_blocks, next_rpc_message


---

## Detailed Analysis

### Classes

#### `ArbitrumRpcClient`

**Type:** struct


#### `ArbitrumRpcClient`

**Type:** impl


#### `BlockchainRpcClient`

**Type:** impl


### Functions

#### `new(wss_rpc_url: String)`


#### `connect(&mut self)`


#### `subscribe_blocks(&mut self)`


#### `unsubscribe_blocks(&mut self)`


#### `next_rpc_message(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/rpc/chains`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


