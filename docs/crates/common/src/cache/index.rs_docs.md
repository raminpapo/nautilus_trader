# Documentation: `crates/common/src/cache/index.rs`
**Generated:** 2025-11-15T19:40:01.666898Z
**File Size:** 5594 bytes
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

- **Path:** `crates/common/src/cache/index.rs`
- **Size:** 5,594 bytes
- **Lines:** 123
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
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

use ahash::{AHashMap, AHashSet};
use nautilus_model::identifiers::{
    AccountId, ClientId, ClientOrderId, ComponentId, ExecAlgorithmId, InstrumentId, PositionId,
    StrategyId, Venue, VenueOrderId,
};

/// A key-value lookup index for a `Cache`.
#[derive(Debug)]
pub struct CacheIndex {
    pub(crate) venue_account: AHashMap<Venue, AccountId>,
    pub(crate) venue_orders: AHashMap<Venue, AHashSet<ClientOrderId>>,
    pub(crate) venue_positions: AHashMap<Venue, AHashSet<PositionId>>,
    pub(crate) venue_order_ids: AHashMap<VenueOrderId, ClientOrderId>,
    pub(crate) client_order_ids: AHashMap<ClientOrderId, VenueOrderId>,
    pub(crate) order_position: AHashMap<ClientOrderId, PositionId>,
    pub(crate) order_strategy: AHashMap<ClientOrderId, StrategyId>,
    pub(crate) order_client: AHashMap<ClientOrderId, ClientId>,
    pub(crate) position_strategy: AHashMap<PositionId, StrategyId>,
    pub(crate) position_orders: AHashMap<PositionId, AHashSet<ClientOrderId>>,
    pub(crate) instrument_orders: AHashMap<InstrumentId, AHashSet<ClientOrderId>>,
    pub(crate) instrument_positions: AHashMap<InstrumentId, AHashSet<PositionId>>,
    pub(crate) strategy_orders: AHashMap<StrategyId, AHashSet<ClientOrderId>>,
    pub(crate) strategy_positions: AHashMap<StrategyId, AHashSet<PositionId>>,
    pub(crate) exec_algorithm_orders: AHashMap<ExecAlgorithmId, AHashSet<ClientOrderId>>,
    pub(crate) exec_spawn_orders: AHashMap<ClientOrderId, AHashSet<ClientOrderId>>,
    pub(crate) orders: AHashSet<ClientOrderId>,
    pub(crate) orders_open: AHashSet<ClientOrderId>,
    pub(crate) orders_closed: AHashSet<ClientOrderId>,
    pub(crate) orders_emulated: AHashSet<ClientOrderId>,
    pub(crate) orders_inflight: AHashSet<ClientOrderId>,
    pub(crate) orders_pending_cancel: AHashSet<ClientOrderId>,
    pub(crate) positions: AHashSet<PositionId>,
    pub(crate) positions_open: AHashSet<PositionId>,
    pub(crate) positions_closed: AHashSet<PositionId>,
    pub(crate) actors: AHashSet<ComponentId>,
    pub(crate) strategies: AHashSet<StrategyId>,
    pub(crate) exec_algorithms: AHashSet<ExecAlgorithmId>,
}

impl Default for CacheIndex {
    /// Creates a new default [`CacheIndex`] instance.
    fn default() -> Self {
        Self {
            venue_account: AHashMap::new(),
            venue_orders: AHashMap::new(),
            venue_positions: AHashMap::new(),
            venue_order_ids: AHashMap::new(),
            client_order_ids: AHashMap::new(),
            order_position: AHashMap::new(),
            order_strategy: AHashMap::new(),
            order_client: AHashMap::new(),
            position_strategy: AHashMap::new(),
            position_orders: AHashMap::new(),
            instrument_orders: AHashMap::new(),
            instrument_positions: AHashMap::new(),
            strategy_orders: AHashMap::new(),
            strategy_positions: AHashMap::new(),
            exec_algorithm_orders: AHashMap::new(),
            exec_spawn_orders: AHashMap::new(),
            orders: AHashSet::new(),
            orders_open: AHashSet::new(),
            orders_closed: AHashSet::new(),
            orders_emulated: AHashSet::new(),
            orders_inflight: AHashSet::new(),
            orders_pending_cancel: AHashSet::new(),
            positions: AHashSet::new(),
            positions_open: AHashSet::new(),
            positions_closed: AHashSet::new(),
            actors: AHashSet::new(),
            strategies: AHashSet::new(),
            exec_algorithms: AHashSet::new(),
        }
    }
}

impl CacheIndex {
    /// Clears the index which will clear/reset all internal state.
    pub fn clear(&mut self) {
        self.venue_account.clear();
        self.venue_orders.clear();
        self.venue_positions.clear();
        self.venue_order_ids.clear();
        self.client_order_ids.clear();
        self.order_position.clear();
        self.order_strategy.clear();
        self.order_client.clear();
        self.position_strategy.clear();
        self.position_orders.clear();
        self.instrument_orders.clear();
        self.instrument_positions.clear();
        self.strategy_orders.clear();
        self.strategy_positions.clear();
        self.exec_algorithm_orders.clear();
        self.exec_spawn_orders.clear();
        self.orders.clear();
        self.orders_open.clear();
        self.orders_closed.clear();
        self.orders_emulated.clear();
        self.orders_inflight.clear();
        self.orders_pending_cancel.clear();
        self.positions.clear();
        self.positions_open.clear();
        self.positions_closed.clear();
        self.actors.clear();
        self.strategies.clear();
        self.exec_algorithms.clear();
    }
}
```


---

## Overview

This file is located at `crates/common/src/cache/index.rs` within the repository.

**Classes defined:** CacheIndex, Default, CacheIndex

**Functions defined:** default, clear


---

## Detailed Analysis

### Classes

#### `CacheIndex`

**Type:** struct


#### `Default`

**Type:** impl


#### `CacheIndex`

**Type:** impl


### Functions

#### `default()`


#### `clear(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/cache`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


