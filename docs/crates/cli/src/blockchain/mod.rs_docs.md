# Documentation: `crates/cli/src/blockchain/mod.rs`
**Generated:** 2025-11-15T19:40:01.619283Z
**File Size:** 2631 bytes
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

- **Path:** `crates/cli/src/blockchain/mod.rs`
- **Size:** 2,631 bytes
- **Lines:** 85
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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


---

## Overview

This file is located at `crates/cli/src/blockchain/mod.rs` within the repository.

**Functions defined:** run_blockchain_command


---

## Detailed Analysis

### Functions

#### `run_blockchain_command(opt: BlockchainOpt)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cli/src/blockchain`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


