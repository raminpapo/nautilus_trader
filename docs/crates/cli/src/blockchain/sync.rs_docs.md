# Documentation: `crates/cli/src/blockchain/sync.rs`
**Generated:** 2025-11-15T19:40:01.620568Z
**File Size:** 4969 bytes
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

- **Path:** `crates/cli/src/blockchain/sync.rs`
- **Size:** 4,969 bytes
- **Lines:** 139
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

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

use std::sync::Arc;

use nautilus_blockchain::{
    config::BlockchainDataClientConfig,
    data::core::BlockchainDataClientCore,
    exchanges::{find_dex_type_case_insensitive, get_supported_dexes_for_chain},
};
use nautilus_infrastructure::sql::pg::get_postgres_connect_options;
use nautilus_model::defi::chain::Chain;

use crate::opt::DatabaseConfig;

pub async fn run_sync_dex(
    chain: String,
    dex: String,
    rpc_url: Option<String>,
    database: DatabaseConfig,
    reset: bool,
    multicall_calls_per_rpc_request: Option<u32>,
) -> anyhow::Result<()> {
    let chain = Chain::from_chain_name(&chain)
        .ok_or_else(|| anyhow::anyhow!("Invalid chain name: {}", chain))?;

    let dex_type = find_dex_type_case_insensitive(&dex, chain).ok_or_else(|| {
        let supported_dexes = get_supported_dexes_for_chain(chain.name);
        if supported_dexes.is_empty() {
            anyhow::anyhow!("Invalid DEX name '{}' (case-insensitive). Chain '{}' is not supported for pool syncing.",dex, chain.name)
        } else {
            anyhow::anyhow!("Invalid DEX name '{}' (case-insensitive). Supported DEXes for chain '{}': {}",dex,chain.name,supported_dexes.join(", "))
        }
    })?;

    let postgres_connect_options = get_postgres_connect_options(
        database.host,
        database.port,
        database.username,
        database.password,
        database.database,
    );
    // Get RPC HTTP URL from CLI argument or environment variable
    let rpc_http_url = rpc_url
        .or_else(|| std::env::var("RPC_HTTP_URL").ok())
        .unwrap_or_default();

    log::info!("Using RPC HTTP URL: '{rpc_http_url}'");

    if rpc_http_url.is_empty() {
        log::warn!(
            "No RPC HTTP URL provided via --rpc-url or RPC_HTTP_URL environment variable - some operations may fail"
        );
    }

    let config = BlockchainDataClientConfig::new(
        Arc::new(chain.to_owned()),
        vec![dex_type],
        rpc_http_url,
        None,
        multicall_calls_per_rpc_request,
        None,
        true,
        None,
        None,
        Some(postgres_connect_options),
    );
    let cancellation_token = tokio_util::sync::CancellationToken::new();
    let mut data_client = BlockchainDataClientCore::new(config, None, None, cancellation_token);
    data_client.initialize_cache_database().await;

    data_client.cache.initialize_chain().await;
    data_client
        .register_dex_exchange(dex_type)
        .await
        .map_err(|e| anyhow::anyhow!("Failed to register DEX exchange: {}", e))?;
    // We want to have full pool sync, so from 0 to last.
    data_client
        .sync_exchange_pools(&dex_type, 0, None, reset)
        .await
        .map_err(|e| anyhow::anyhow!("Failed to sync pools: {}", e))?;

    Ok(())
}

pub async fn run_sync_blocks(
    chain: String,
    from_block: Option<u64>,
    to_block: Option<u64>,
    database: DatabaseConfig,
) -> anyhow::Result<()> {
    let chain = Chain::from_chain_name(&chain)
        .ok_or_else(|| anyhow::anyhow!("Invalid chain name: {}", chain))?;
    let chain = Arc::new(chain.to_owned());
    let from_block = from_block.unwrap_or(0);

    let postgres_connect_options = get_postgres_connect_options(
        database.host,
        database.port,
        database.username,
        database.password,
        database.database,
    );
    let config = BlockchainDataClientConfig::new(
        chain.clone(),
        vec![],
        "".to_string(), // we dont need to http rpc url for block syncing
        None,
        None,
        None,
        true,
        None,
        None,
        Some(postgres_connect_options),
    );
    let cancellation_token = tokio_util::sync::CancellationToken::new();
    let mut data_client = BlockchainDataClientCore::new(config, None, None, cancellation_token);
    data_client.initialize_cache_database().await;

    data_client.cache.initialize_chain().await;
    data_client
        .sync_blocks_checked(from_block, to_block)
        .await
        .map_err(|e| anyhow::anyhow!("Failed to sync blocks: {}", e))?;

    Ok(())
}
```


---

## Overview

This file is located at `crates/cli/src/blockchain/sync.rs` within the repository.

**Functions defined:** run_sync_dex, run_sync_blocks


---

## Detailed Analysis

### Functions

#### `run_sync_dex(
    chain: String,
    dex: String,
    rpc_url: Option<String>,
    database: DatabaseConfig,
    reset: bool,
    multicall_calls_per_rpc_request: Option<u32>,
)`


#### `run_sync_blocks(
    chain: String,
    from_block: Option<u64>,
    to_block: Option<u64>,
    database: DatabaseConfig,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cli/src/blockchain`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: password, token. Ensure proper handling of secrets.


