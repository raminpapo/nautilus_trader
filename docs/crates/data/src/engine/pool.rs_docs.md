# Documentation: `crates/data/src/engine/pool.rs`
**Generated:** 2025-11-15T19:40:02.002056Z
**File Size:** 4685 bytes
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

- **Path:** `crates/data/src/engine/pool.rs`
- **Size:** 4,685 bytes
- **Lines:** 130
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 8

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

//! Message handler that maintains the `Pool` state stored in the global [`Cache`].
//!
//! The handler is functionally equivalent to `BookUpdater` but for DeFi liquidity
//! pools. Whenever a [`PoolSwap`] or [`PoolLiquidityUpdate`] is published on the
//! message bus the handler looks up the corresponding `Pool` instance in the
//! cache and applies the change in-place (for now we only update the `ts_init`
//! timestamp so that consumers can tell the pool has been touched).

use std::{any::Any, cell::RefCell, rc::Rc};

use nautilus_common::{cache::Cache, msgbus::handler::MessageHandler};
use nautilus_model::{
    defi::{PoolFeeCollect, PoolFlash, PoolLiquidityUpdate, PoolLiquidityUpdateType, PoolSwap},
    identifiers::InstrumentId,
};
use ustr::Ustr;

/// Handles [`PoolSwap`]s and [`PoolLiquidityUpdate`]s for a single AMM pool.
#[derive(Debug)]
pub struct PoolUpdater {
    id: Ustr,
    instrument_id: InstrumentId,
    cache: Rc<RefCell<Cache>>,
}

impl PoolUpdater {
    /// Creates a new [`PoolUpdater`] bound to the given `instrument_id` and `cache`.
    #[must_use]
    pub fn new(instrument_id: &InstrumentId, cache: Rc<RefCell<Cache>>) -> Self {
        Self {
            id: Ustr::from(&format!("{}-{}", stringify!(PoolUpdater), instrument_id)),
            instrument_id: *instrument_id,
            cache,
        }
    }

    fn handle_pool_swap(&self, swap: &PoolSwap) {
        if let Some(pool_profiler) = self
            .cache
            .borrow_mut()
            .pool_profiler_mut(&self.instrument_id)
            && let Err(e) = pool_profiler.process_swap(swap)
        {
            log::error!("Failed to process pool swap: {e}");
        }
    }

    fn handle_pool_liquidity_update(&self, update: &PoolLiquidityUpdate) {
        if let Some(pool_profiler) = self
            .cache
            .borrow_mut()
            .pool_profiler_mut(&self.instrument_id)
            && let Err(e) = match update.kind {
                PoolLiquidityUpdateType::Mint => pool_profiler.process_mint(update),
                PoolLiquidityUpdateType::Burn => pool_profiler.process_burn(update),
                _ => panic!("Liquidity update operation {} not implemented", update.kind),
            }
        {
            log::error!("Failed to process pool liquidity update: {e}");
        }
    }

    fn handle_pool_fee_collect(&self, event: &PoolFeeCollect) {
        if let Some(pool_profiler) = self
            .cache
            .borrow_mut()
            .pool_profiler_mut(&self.instrument_id)
            && let Err(e) = pool_profiler.process_collect(event)
        {
            log::error!("Failed to process pool fee collect: {e}");
        }
    }

    fn handle_pool_flash(&self, event: &PoolFlash) {
        if let Some(pool_profiler) = self
            .cache
            .borrow_mut()
            .pool_profiler_mut(&self.instrument_id)
            && let Err(e) = pool_profiler.process_flash(event)
        {
            log::error!("Failed to process pool flash: {e}");
        }
    }
}

impl MessageHandler for PoolUpdater {
    fn id(&self) -> Ustr {
        self.id
    }

    fn handle(&self, message: &dyn Any) {
        if let Some(swap) = message.downcast_ref::<PoolSwap>() {
            self.handle_pool_swap(swap);
            return;
        }

        if let Some(update) = message.downcast_ref::<PoolLiquidityUpdate>() {
            self.handle_pool_liquidity_update(update);
            return;
        }

        if let Some(update) = message.downcast_ref::<PoolFeeCollect>() {
            self.handle_pool_fee_collect(update);
            return;
        }

        if let Some(flash) = message.downcast_ref::<PoolFlash>() {
            self.handle_pool_flash(flash);
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}
```


---

## Overview

This file is located at `crates/data/src/engine/pool.rs` within the repository.

**Classes defined:** PoolUpdater, PoolUpdater, MessageHandler

**Functions defined:** new, handle_pool_swap, handle_pool_liquidity_update, handle_pool_fee_collect, handle_pool_flash, id, handle, as_any


---

## Detailed Analysis

### Classes

#### `PoolUpdater`

**Type:** struct


#### `PoolUpdater`

**Type:** impl


#### `MessageHandler`

**Type:** impl


### Functions

#### `new(instrument_id: &InstrumentId, cache: Rc<RefCell<Cache>>)`


#### `handle_pool_swap(&self, swap: &PoolSwap)`


#### `handle_pool_liquidity_update(&self, update: &PoolLiquidityUpdate)`


#### `handle_pool_fee_collect(&self, event: &PoolFeeCollect)`


#### `handle_pool_flash(&self, event: &PoolFlash)`


#### `id(&self)`


#### `handle(&self, message: &dyn Any)`


#### `as_any(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/data/src/engine`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


