# Documentation: arbitrum.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/rpc/chains/arbitrum.rs`
- **Size**: 1,986 bytes
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`connect()`**: Function defined in this file
- **`subscribe_blocks()`**: Function defined in this file
- **`unsubscribe_blocks()`**: Function defined in this file
- **`next_rpc_message()`**: Function defined in this file

### Classes
- **`ArbitrumRpcClient`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `connect`, `new`, `next_rpc_message`, `subscribe_blocks`, `unsubscribe_blocks`
**Impls**: `ArbitrumRpcClient`, `BlockchainRpcClient`
**Structs**: `ArbitrumRpcClient`

## Related Files

This file is located in `crates/adapters/blockchain/src/rpc/chains/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.321544Z*
