# Documentation: `crates/common/src/messages/defi/unsubscribe.rs`
**Generated:** 2025-11-15T19:40:01.768988Z
**File Size:** 5657 bytes
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

- **Path:** `crates/common/src/messages/defi/unsubscribe.rs`
- **Size:** 5,657 bytes
- **Lines:** 199
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 12
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

use indexmap::IndexMap;
use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::{
    defi::chain::Blockchain,
    identifiers::{ClientId, InstrumentId},
};

#[derive(Debug, Clone)]
pub struct UnsubscribeBlocks {
    pub chain: Blockchain,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeBlocks {
    /// Creates a new [`UnsubscribeBlocks`] instance.
    #[must_use]
    pub const fn new(
        chain: Blockchain,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            chain,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from definition updates for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePool {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePool {
    /// Creates a new [`UnsubscribePool`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Debug, Clone)]
pub struct UnsubscribePoolSwaps {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolSwaps {
    /// Creates a new [`UnsubscribePoolSwaps`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from liquidity updates for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePoolLiquidityUpdates {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolLiquidityUpdates {
    /// Creates a new [`UnsubscribePoolLiquidityUpdates`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from fee-collect events for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePoolFeeCollects {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolFeeCollects {
    /// Creates a new [`UnsubscribePoolFeeCollects`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from flash-loan events for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePoolFlashEvents {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolFlashEvents {
    /// Creates a new [`UnsubscribePoolFlashEvents`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}
```


---

## Overview

This file is located at `crates/common/src/messages/defi/unsubscribe.rs` within the repository.

**Classes defined:** UnsubscribeBlocks, UnsubscribePool, UnsubscribePoolSwaps, UnsubscribePoolLiquidityUpdates, UnsubscribePoolFeeCollects, UnsubscribePoolFlashEvents, UnsubscribeBlocks, UnsubscribePool, UnsubscribePoolSwaps, UnsubscribePoolLiquidityUpdates and 2 more

**Functions defined:** new, new, new, new, new, new


---

## Detailed Analysis

### Classes

#### `UnsubscribeBlocks`

**Type:** struct


#### `UnsubscribePool`

**Type:** struct


#### `UnsubscribePoolSwaps`

**Type:** struct


#### `UnsubscribePoolLiquidityUpdates`

**Type:** struct


#### `UnsubscribePoolFeeCollects`

**Type:** struct


#### `UnsubscribePoolFlashEvents`

**Type:** struct


#### `UnsubscribeBlocks`

**Type:** impl


#### `UnsubscribePool`

**Type:** impl


#### `UnsubscribePoolSwaps`

**Type:** impl


#### `UnsubscribePoolLiquidityUpdates`

**Type:** impl


#### `UnsubscribePoolFeeCollects`

**Type:** impl


#### `UnsubscribePoolFlashEvents`

**Type:** impl


### Functions

#### `new(
        chain: Blockchain,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    )`


#### `new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    )`


#### `new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    )`


#### `new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    )`


#### `new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    )`


#### `new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    )`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/messages/defi`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


