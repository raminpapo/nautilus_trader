# Documentation: cancel.rs

## File Metadata

- **Path**: `crates/common/src/messages/execution/cancel.rs`
- **Size**: 5,450 bytes
- **Lines**: 187
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

use std::fmt::Display;

use derive_builder::Builder;
use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::{
    enums::OrderSide,
    identifiers::{ClientId, ClientOrderId, InstrumentId, StrategyId, TraderId, VenueOrderId},
};
use serde::{Deserialize, Serialize};

#[derive(Clone, PartialEq, Eq, Debug, Default, Serialize, Deserialize, Builder)]
#[builder(default)]
#[serde(tag = "type")]
pub struct CancelOrder {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub client_order_id: ClientOrderId,
    pub venue_order_id: VenueOrderId,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl CancelOrder {
    /// Creates a new [`CancelOrder`] instance.
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

impl Display for CancelOrder {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "CancelOrder(instrument_id={}, client_order_id={}, venue_order_id={})",
            self.instrument_id, self.client_order_id, self.venue_order_id,
        )
    }
}

#[derive(Clone, PartialEq, Eq, Debug, Default, Serialize, Deserialize, Builder)]
#[builder(default)]
#[serde(tag = "type")]
pub struct CancelAllOrders {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub order_side: OrderSide,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl CancelAllOrders {
    /// Creates a new [`CancelAllOrders`] instance.
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
        order_side: OrderSide,
        command_id: UUID4,
        ts_init: UnixNanos,
    ) -> anyhow::Result<Self> {
        Ok(Self {
            trader_id,
            client_id,
            strategy_id,
            instrument_id,
            order_side,
            command_id,
            ts_init,
        })
    }
}

impl Display for CancelAllOrders {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "CancelAllOrders(instrument_id={}, order_side={})",
            self.instrument_id, self.order_side,
        )
    }
}

#[derive(Clone, PartialEq, Eq, Debug, Default, Serialize, Deserialize, Builder)]
#[builder(default)]
#[serde(tag = "type")]
pub struct BatchCancelOrders {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub cancels: Vec<CancelOrder>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl BatchCancelOrders {
    /// Creates a new [`BatchCancelOrders`] instance.
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
        cancels: Vec<CancelOrder>,
        command_id: UUID4,
        ts_init: UnixNanos,
    ) -> anyhow::Result<Self> {
        Ok(Self {
            trader_id,
            client_id,
            strategy_id,
            instrument_id,
            cancels,
            command_id,
            ts_init,
        })
    }
}

impl Display for BatchCancelOrders {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "BatchCancelOrders(instrument_id={}, cancels=TBD)",
            self.instrument_id,
        )
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s) and 3 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file

### Classes
- **`CancelOrder`**: Class defined in this file
- **`CancelAllOrders`**: Class defined in this file
- **`BatchCancelOrders`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `fmt`, `new`
**Impls**: `BatchCancelOrders`, `CancelAllOrders`, `CancelOrder`, `Display`
**Structs**: `BatchCancelOrders`, `CancelAllOrders`, `CancelOrder`

## Related Files

This file is located in `crates/common/src/messages/execution/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.194890Z*
