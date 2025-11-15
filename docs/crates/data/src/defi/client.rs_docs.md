# Documentation: `crates/data/src/defi/client.rs`
**Generated:** 2025-11-15T19:40:01.984242Z
**File Size:** 10507 bytes
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

- **Path:** `crates/data/src/defi/client.rs`
- **Size:** 10,507 bytes
- **Lines:** 281
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 17

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

//! DeFi-specific data client functionality.
//!
//! This module provides DeFi subscription and request helper methods
//! for the `DataClientAdapter`. All code in this module requires the `defi` feature flag.

use std::fmt::{Debug, Display};

use nautilus_common::messages::defi::{
    DefiRequestCommand, DefiSubscribeCommand, DefiUnsubscribeCommand, RequestPoolSnapshot,
    SubscribeBlocks, SubscribePool, SubscribePoolFeeCollects, SubscribePoolFlashEvents,
    SubscribePoolLiquidityUpdates, SubscribePoolSwaps, UnsubscribeBlocks, UnsubscribePool,
    UnsubscribePoolFeeCollects, UnsubscribePoolFlashEvents, UnsubscribePoolLiquidityUpdates,
    UnsubscribePoolSwaps,
};

use crate::client::DataClientAdapter;

impl DataClientAdapter {
    #[inline]
    pub fn execute_defi_subscribe(&mut self, cmd: &DefiSubscribeCommand) {
        if let Err(e) = match cmd {
            DefiSubscribeCommand::Blocks(cmd) => self.subscribe_blocks(cmd),
            DefiSubscribeCommand::Pool(cmd) => self.subscribe_pool(cmd),
            DefiSubscribeCommand::PoolSwaps(cmd) => self.subscribe_pool_swaps(cmd),
            DefiSubscribeCommand::PoolLiquidityUpdates(cmd) => {
                self.subscribe_pool_liquidity_updates(cmd)
            }
            DefiSubscribeCommand::PoolFeeCollects(cmd) => self.subscribe_pool_fee_collects(cmd),
            DefiSubscribeCommand::PoolFlashEvents(cmd) => self.subscribe_pool_flash_events(cmd),
        } {
            log_command_error(&cmd, &e);
        }
    }

    #[inline]
    pub fn execute_defi_unsubscribe(&mut self, cmd: &DefiUnsubscribeCommand) {
        if let Err(e) = match cmd {
            DefiUnsubscribeCommand::Blocks(cmd) => self.unsubscribe_blocks(cmd),
            DefiUnsubscribeCommand::Pool(cmd) => self.unsubscribe_pool(cmd),
            DefiUnsubscribeCommand::PoolSwaps(cmd) => self.unsubscribe_pool_swaps(cmd),
            DefiUnsubscribeCommand::PoolLiquidityUpdates(cmd) => {
                self.unsubscribe_pool_liquidity_updates(cmd)
            }
            DefiUnsubscribeCommand::PoolFeeCollects(cmd) => self.unsubscribe_pool_fee_collects(cmd),
            DefiUnsubscribeCommand::PoolFlashEvents(cmd) => self.unsubscribe_pool_flash_events(cmd),
        } {
            log_command_error(&cmd, &e);
        }
    }

    /// Executes a DeFi data request command by dispatching to the appropriate handler.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client request fails.
    #[inline]
    pub fn execute_defi_request(&self, cmd: &DefiRequestCommand) -> anyhow::Result<()> {
        match cmd {
            DefiRequestCommand::PoolSnapshot(cmd) => self.request_pool_snapshot(cmd),
        }
    }

    /// Subscribes to block events for the specified blockchain.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client subscribe operation fails.
    fn subscribe_blocks(&mut self, cmd: &SubscribeBlocks) -> anyhow::Result<()> {
        if !self.subscriptions_blocks.contains(&cmd.chain) {
            self.subscriptions_blocks.insert(cmd.chain);
            self.client.subscribe_blocks(cmd)?;
        }
        Ok(())
    }

    /// Unsubscribes from block events for the specified blockchain.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client unsubscribe operation fails.
    fn unsubscribe_blocks(&mut self, cmd: &UnsubscribeBlocks) -> anyhow::Result<()> {
        if self.subscriptions_blocks.contains(&cmd.chain) {
            self.subscriptions_blocks.remove(&cmd.chain);
            self.client.unsubscribe_blocks(cmd)?;
        }
        Ok(())
    }

    /// Subscribes to pool definition updates for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client subscribe operation fails.
    fn subscribe_pool(&mut self, cmd: &SubscribePool) -> anyhow::Result<()> {
        if !self.subscriptions_pools.contains(&cmd.instrument_id) {
            self.subscriptions_pools.insert(cmd.instrument_id);
            self.client.subscribe_pool(cmd)?;
        }
        Ok(())
    }

    /// Subscribes to pool swap events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client subscribe operation fails.
    fn subscribe_pool_swaps(&mut self, cmd: &SubscribePoolSwaps) -> anyhow::Result<()> {
        if !self.subscriptions_pool_swaps.contains(&cmd.instrument_id) {
            self.subscriptions_pool_swaps.insert(cmd.instrument_id);
            self.client.subscribe_pool_swaps(cmd)?;
        }
        Ok(())
    }

    /// Subscribes to pool liquidity update events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client subscribe operation fails.
    fn subscribe_pool_liquidity_updates(
        &mut self,
        cmd: &SubscribePoolLiquidityUpdates,
    ) -> anyhow::Result<()> {
        if !self
            .subscriptions_pool_liquidity_updates
            .contains(&cmd.instrument_id)
        {
            self.subscriptions_pool_liquidity_updates
                .insert(cmd.instrument_id);
            self.client.subscribe_pool_liquidity_updates(cmd)?;
        }
        Ok(())
    }

    /// Subscribes to pool fee collect events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client subscribe operation fails.
    fn subscribe_pool_fee_collects(
        &mut self,
        cmd: &SubscribePoolFeeCollects,
    ) -> anyhow::Result<()> {
        if !self
            .subscriptions_pool_fee_collects
            .contains(&cmd.instrument_id)
        {
            self.subscriptions_pool_fee_collects
                .insert(cmd.instrument_id);
            self.client.subscribe_pool_fee_collects(cmd)?;
        }
        Ok(())
    }

    /// Subscribes to pool flash loan events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client subscribe operation fails.
    fn subscribe_pool_flash_events(
        &mut self,
        cmd: &SubscribePoolFlashEvents,
    ) -> anyhow::Result<()> {
        if !self.subscriptions_pool_flash.contains(&cmd.instrument_id) {
            self.subscriptions_pool_flash.insert(cmd.instrument_id);
            self.client.subscribe_pool_flash_events(cmd)?;
        }
        Ok(())
    }

    /// Unsubscribes from pool definition updates for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client unsubscribe operation fails.
    fn unsubscribe_pool(&mut self, cmd: &UnsubscribePool) -> anyhow::Result<()> {
        if self.subscriptions_pools.contains(&cmd.instrument_id) {
            self.subscriptions_pools.remove(&cmd.instrument_id);
            self.client.unsubscribe_pool(cmd)?;
        }
        Ok(())
    }

    /// Unsubscribes from swap events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client unsubscribe operation fails.
    fn unsubscribe_pool_swaps(&mut self, cmd: &UnsubscribePoolSwaps) -> anyhow::Result<()> {
        if self.subscriptions_pool_swaps.contains(&cmd.instrument_id) {
            self.subscriptions_pool_swaps.remove(&cmd.instrument_id);
            self.client.unsubscribe_pool_swaps(cmd)?;
        }
        Ok(())
    }

    /// Unsubscribes from pool liquidity update events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client unsubscribe operation fails.
    fn unsubscribe_pool_liquidity_updates(
        &mut self,
        cmd: &UnsubscribePoolLiquidityUpdates,
    ) -> anyhow::Result<()> {
        if self
            .subscriptions_pool_liquidity_updates
            .contains(&cmd.instrument_id)
        {
            self.subscriptions_pool_liquidity_updates
                .remove(&cmd.instrument_id);
            self.client.unsubscribe_pool_liquidity_updates(cmd)?;
        }
        Ok(())
    }

    /// Unsubscribes from pool fee collect events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client unsubscribe operation fails.
    fn unsubscribe_pool_fee_collects(
        &mut self,
        cmd: &UnsubscribePoolFeeCollects,
    ) -> anyhow::Result<()> {
        if self
            .subscriptions_pool_fee_collects
            .contains(&cmd.instrument_id)
        {
            self.subscriptions_pool_fee_collects
                .remove(&cmd.instrument_id);
            self.client.unsubscribe_pool_fee_collects(cmd)?;
        }
        Ok(())
    }

    /// Unsubscribes from pool flash loan events for the specified AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the underlying client unsubscribe operation fails.
    fn unsubscribe_pool_flash_events(
        &mut self,
        cmd: &UnsubscribePoolFlashEvents,
    ) -> anyhow::Result<()> {
        if self.subscriptions_pool_flash.contains(&cmd.instrument_id) {
            self.subscriptions_pool_flash.remove(&cmd.instrument_id);
            self.client.unsubscribe_pool_flash_events(cmd)?;
        }
        Ok(())
    }

    /// Sends a pool snapshot request for a given AMM pool.
    ///
    /// # Errors
    ///
    /// Returns an error if the client fails to process the pool snapshot request.
    pub fn request_pool_snapshot(&self, req: &RequestPoolSnapshot) -> anyhow::Result<()> {
        self.client.request_pool_snapshot(req)
    }
}

#[inline(always)]
fn log_command_error<C: Debug, E: Display>(cmd: &C, e: &E) {
    log::error!("Error on {cmd:?}: {e}");
}
```


---

## Overview

This file is located at `crates/data/src/defi/client.rs` within the repository.

**Classes defined:** DataClientAdapter

**Functions defined:** execute_defi_subscribe, execute_defi_unsubscribe, execute_defi_request, subscribe_blocks, unsubscribe_blocks, subscribe_pool, subscribe_pool_swaps, subscribe_pool_liquidity_updates, subscribe_pool_fee_collects, subscribe_pool_flash_events and 7 more


---

## Detailed Analysis

### Classes

#### `DataClientAdapter`

**Type:** impl


### Functions

#### `execute_defi_subscribe(&mut self, cmd: &DefiSubscribeCommand)`


#### `execute_defi_unsubscribe(&mut self, cmd: &DefiUnsubscribeCommand)`


#### `execute_defi_request(&self, cmd: &DefiRequestCommand)`


#### `subscribe_blocks(&mut self, cmd: &SubscribeBlocks)`


#### `unsubscribe_blocks(&mut self, cmd: &UnsubscribeBlocks)`


#### `subscribe_pool(&mut self, cmd: &SubscribePool)`


#### `subscribe_pool_swaps(&mut self, cmd: &SubscribePoolSwaps)`


#### `subscribe_pool_liquidity_updates(
        &mut self,
        cmd: &SubscribePoolLiquidityUpdates,
    )`


#### `subscribe_pool_fee_collects(
        &mut self,
        cmd: &SubscribePoolFeeCollects,
    )`


#### `subscribe_pool_flash_events(
        &mut self,
        cmd: &SubscribePoolFlashEvents,
    )`


#### `unsubscribe_pool(&mut self, cmd: &UnsubscribePool)`


#### `unsubscribe_pool_swaps(&mut self, cmd: &UnsubscribePoolSwaps)`


#### `unsubscribe_pool_liquidity_updates(
        &mut self,
        cmd: &UnsubscribePoolLiquidityUpdates,
    )`


#### `unsubscribe_pool_fee_collects(
        &mut self,
        cmd: &UnsubscribePoolFeeCollects,
    )`


#### `unsubscribe_pool_flash_events(
        &mut self,
        cmd: &UnsubscribePoolFlashEvents,
    )`


#### `request_pool_snapshot(&self, req: &RequestPoolSnapshot)`


#### `log_command_error(cmd: &C, e: &E)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/data/src/defi`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


