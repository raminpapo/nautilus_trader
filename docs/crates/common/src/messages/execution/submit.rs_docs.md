# Documentation: submit.rs

## File Metadata

- **Path**: `crates/common/src/messages/execution/submit.rs`
- **Size**: 5,046 bytes
- **Lines**: 160
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

use std::{collections::HashMap, fmt::Display};

use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::{
    identifiers::{
        ClientId, ClientOrderId, ExecAlgorithmId, InstrumentId, PositionId, StrategyId, TraderId,
        VenueOrderId,
    },
    orders::{OrderAny, OrderList},
};
use serde::{Deserialize, Serialize};

// Fix: equality and default and builder
#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
// #[builder(default)]
#[serde(tag = "type")]
pub struct SubmitOrder {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub client_order_id: ClientOrderId,
    pub venue_order_id: VenueOrderId,
    pub order: OrderAny,
    pub exec_algorithm_id: Option<ExecAlgorithmId>,
    pub position_id: Option<PositionId>,
    pub params: Option<HashMap<String, String>>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl SubmitOrder {
    /// Creates a new [`SubmitOrder`] instance.
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
        order: OrderAny,
        exec_algorithm_id: Option<ExecAlgorithmId>,
        position_id: Option<PositionId>,
        params: Option<HashMap<String, String>>,
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
            order,
            exec_algorithm_id,
            position_id,
            params,
            command_id,
            ts_init,
        })
    }
}

impl Display for SubmitOrder {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "SubmitOrder(instrument_id={}, order=TBD, position_id={})",
            self.instrument_id,
            self.position_id
                .map_or("None".to_string(), |position_id| format!("{position_id}")),
        )
    }
}

#[derive(Clone, PartialEq, Eq, Debug, Serialize, Deserialize)]
#[serde(tag = "type")]
pub struct SubmitOrderList {
    pub trader_id: TraderId,
    pub client_id: ClientId,
    pub strategy_id: StrategyId,
    pub instrument_id: InstrumentId,
    pub client_order_id: ClientOrderId,
    pub venue_order_id: VenueOrderId,
    pub order_list: OrderList,
    pub exec_algorithm_id: Option<ExecAlgorithmId>,
    pub position_id: Option<PositionId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
}

impl SubmitOrderList {
    /// Creates a new [`SubmitOrderList`] instance.
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
        order_list: OrderList,
        exec_algorithm_id: Option<ExecAlgorithmId>,
        position_id: Option<PositionId>,
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
            order_list,
            exec_algorithm_id,
            position_id,
            command_id,
            ts_init,
        })
    }
}

impl Display for SubmitOrderList {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "SubmitOrderList(instrument_id={}, order_list=TBD, position_id={})",
            self.instrument_id,
            self.position_id
                .map_or("None".to_string(), |position_id| format!("{position_id}")),
        )
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file

### Classes
- **`SubmitOrder`**: Class defined in this file
- **`SubmitOrderList`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `fmt`, `new`
**Impls**: `Display`, `SubmitOrder`, `SubmitOrderList`
**Structs**: `SubmitOrder`, `SubmitOrderList`

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
*Generated on 2025-11-18T21:55:01.205738Z*
