# Documentation: mod.rs

## File Metadata

- **Path**: `crates/cli/src/blockchain/mod.rs`
- **Size**: 2,631 bytes
- **Lines**: 86
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

//! Blockchain management and synchronization utilities.

use crate::{
    blockchain::{
        analyze::run_analyze_pool,
        sync::{run_sync_blocks, run_sync_dex},
    },
    opt::{BlockchainCommand, BlockchainOpt},
};

pub mod analyze;
pub mod sync;

/// Runs blockchain commands based on the provided options.
///
/// # Errors
///
/// Returns an error if execution of the specified blockchain command fails.
pub async fn run_blockchain_command(opt: BlockchainOpt) -> anyhow::Result<()> {
    match opt.command {
        BlockchainCommand::SyncBlocks {
            chain,
            to_block,
            from_block,
            database,
        } => run_sync_blocks(chain, from_block, to_block, database).await,
        BlockchainCommand::SyncDex {
            chain,
            dex,
            rpc_url,
            database,
            reset,
            multicall_calls_per_rpc_request,
        } => {
            run_sync_dex(
                chain,
                dex,
                rpc_url,
                database,
                reset,
                multicall_calls_per_rpc_request,
            )
            .await
        }
        BlockchainCommand::AnalyzePool {
            chain,
            dex,
            address,
            from_block,
            to_block,
            rpc_url,
            reset,
            database,
            multicall_calls_per_rpc_request,
        } => {
            run_analyze_pool(
                chain,
                dex,
                address,
                from_block,
                to_block,
                rpc_url,
                database,
                reset,
                multicall_calls_per_rpc_request,
            )
            .await
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`run_blockchain_command()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `run_blockchain_command`

## Related Files

This file is located in `crates/cli/src/blockchain/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.936477Z*
