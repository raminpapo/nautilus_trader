# Documentation: modify.rs

## File Metadata

- **Path**: `crates/common/src/messages/execution/modify.rs`
- **Size**: 3,532 bytes
- **Lines**: 104
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
    identifiers::{ClientId, ClientOrderId, InstrumentId, StrategyId, TraderId, VenueOrderId},
    types::{Price, Quantity},
};
use serde::{Deserialize, Serialize};

#[derive(Clone, PartialEq, Eq, Debug, Default, Serialize, Deserialize, Builder)]
#[builder(default)]
#[serde(tag = "type")]
pub struct ModifyOrder {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub client_order_id: ClientOrderId,
    pub venue_order_id: VenueOrderId,
    pub quantity: Option<Quantity>,
    pub price: Option<Price>,
    pub trigger_price: Option<Price>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl ModifyOrder {
    /// Creates a new [`ModifyOrder`] instance.
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
        quantity: Option<Quantity>,
        price: Option<Price>,
        trigger_price: Option<Price>,
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
            quantity,
            price,
            trigger_price,
            command_id,
            ts_init,
        })
    }
}

impl Display for ModifyOrder {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "ModifyOrder(instrument_id={}, client_order_id={}, venue_order_id={}, quantity={}, price={}, trigger_price={})",
            self.instrument_id,
            self.client_order_id,
            self.venue_order_id,
            self.quantity
                .map_or("None".to_string(), |quantity| format!("{quantity}")),
            self.price
                .map_or("None".to_string(), |price| format!("{price}")),
            self.trigger_price
                .map_or("None".to_string(), |trigger_price| format!(
                    "{trigger_price}"
                )),
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

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file

### Classes
- **`ModifyOrder`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `fmt`, `new`
**Impls**: `Display`, `ModifyOrder`
**Structs**: `ModifyOrder`

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
*Generated on 2025-11-18T21:55:01.198889Z*
