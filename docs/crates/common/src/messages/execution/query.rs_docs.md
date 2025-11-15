# Documentation: `crates/common/src/messages/execution/query.rs`
**Generated:** 2025-11-15T19:40:01.774705Z
**File Size:** 3906 bytes
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

- **Path:** `crates/common/src/messages/execution/query.rs`
- **Size:** 3,906 bytes
- **Lines:** 128
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 6
- **Functions:** 4

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

use std::fmt::Display;

use derive_builder::Builder;
use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::identifiers::{
    AccountId, ClientId, ClientOrderId, InstrumentId, StrategyId, TraderId, VenueOrderId,
};
use serde::{Deserialize, Serialize};

#[derive(Clone, PartialEq, Eq, Debug, Default, Serialize, Deserialize, Builder)]
#[builder(default)]
#[serde(tag = "type")]
pub struct QueryAccount {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub account_id: AccountId,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl QueryAccount {
    /// Creates a new [`QueryAccount`] instance.
    ///
    /// # Errors
    ///
    /// Returns an error if parameters are invalid.
    #[allow(clippy::too_many_arguments)]
    pub const fn new(
        trader_id: TraderId,
        client_id: ClientId,
        account_id: AccountId,
        command_id: UUID4,
        ts_init: UnixNanos,
    ) -> anyhow::Result<Self> {
        Ok(Self {
            trader_id,
            client_id,
            account_id,
            command_id,
            ts_init,
        })
    }
}

impl Display for QueryAccount {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "QueryAccount(client_id={}, account_id={})",
            self.client_id, self.account_id,
        )
    }
}

#[derive(Clone, PartialEq, Eq, Debug, Default, Serialize, Deserialize, Builder)]
#[builder(default)]
#[serde(tag = "type")]
pub struct QueryOrder {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub client_order_id: ClientOrderId,
    pub venue_order_id: VenueOrderId,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl QueryOrder {
    /// Creates a new [`QueryOrder`] instance.
    ///
    /// # Errors
    ///
    /// Returns an error if parameters are invalid.
    #[allow(clippy::too_many_arguments)]
    pub const fn new(
        trader_id: TraderId,
        client_id: ClientId,
        strategy_id: StrategyId,
        instrument_id: InstrumentId,
        client_order_id: ClientOrderId,
        venue_order_id: VenueOrderId,
        command_id: UUID4,
        ts_init: UnixNanos,
    ) -> anyhow::Result<Self> {
        Ok(Self {
            trader_id,
            client_id,
            strategy_id,
            instrument_id,
            client_order_id,
            venue_order_id,
            command_id,
            ts_init,
        })
    }
}

impl Display for QueryOrder {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "QueryOrder(instrument_id={}, client_order_id={}, venue_order_id={})",
            self.instrument_id, self.client_order_id, self.venue_order_id,
        )
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {}
```


---

## Overview

This file is located at `crates/common/src/messages/execution/query.rs` within the repository.

**Classes defined:** QueryAccount, QueryOrder, QueryAccount, Display, QueryOrder, Display

**Functions defined:** new, fmt, new, fmt


---

## Detailed Analysis

### Classes

#### `QueryAccount`

**Type:** struct


#### `QueryOrder`

**Type:** struct


#### `QueryAccount`

**Type:** impl


#### `Display`

**Type:** impl


#### `QueryOrder`

**Type:** impl


#### `Display`

**Type:** impl


### Functions

#### `new(
        trader_id: TraderId,
        client_id: ClientId,
        account_id: AccountId,
        command_id: UUID4,
        ts_init: UnixNanos,
    )`


#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `new(
        trader_id: TraderId,
        client_id: ClientId,
        strategy_id: StrategyId,
        instrument_id: InstrumentId,
        client_order_id: ClientOrderId,
        venue_order_id: VenueOrderId,
        command_id: UUID4,
        ts_init: UnixNanos,
    )`


#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/messages/execution`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


