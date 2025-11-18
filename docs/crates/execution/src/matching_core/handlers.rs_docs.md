# Documentation: handlers.rs

## File Metadata

- **Path**: `crates/execution/src/matching_core/handlers.rs`
- **Size**: 3,942 bytes
- **Lines**: 112
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

use nautilus_core::WeakCell;
use nautilus_model::orders::OrderAny;

use crate::{
    matching_engine::engine::OrderMatchingEngine, order_emulator::emulator::OrderEmulator,
};

pub trait FillMarketOrderHandler {
    fn fill_market_order(&mut self, order: &OrderAny);
}

#[derive(Clone, Debug)]
pub enum FillMarketOrderHandlerAny {
    OrderMatchingEngine(WeakCell<OrderMatchingEngine>),
    OrderEmulator(WeakCell<OrderEmulator>),
}

impl FillMarketOrderHandler for FillMarketOrderHandlerAny {
    fn fill_market_order(&mut self, order: &OrderAny) {
        match self {
            Self::OrderMatchingEngine(engine_weak) => {
                if let Some(engine) = engine_weak.upgrade() {
                    engine.borrow_mut().fill_market_order(&mut order.clone());
                }
            }
            Self::OrderEmulator(emulator_weak) => {
                if let Some(emulator) = emulator_weak.upgrade() {
                    emulator.borrow_mut().fill_market_order(&mut order.clone());
                }
            }
        }
    }
}

#[derive(Clone, Debug)]
pub struct ShareableFillMarketOrderHandler(pub FillMarketOrderHandlerAny);

pub trait FillLimitOrderHandler {
    fn fill_limit_order(&mut self, order: &mut OrderAny);
}

#[derive(Clone, Debug)]
pub enum FillLimitOrderHandlerAny {
    OrderMatchingEngine(WeakCell<OrderMatchingEngine>),
    OrderEmulator(WeakCell<OrderEmulator>),
}

impl FillLimitOrderHandler for FillLimitOrderHandlerAny {
    fn fill_limit_order(&mut self, order: &mut OrderAny) {
        match self {
            Self::OrderMatchingEngine(engine_weak) => {
                if let Some(engine) = engine_weak.upgrade() {
                    engine.borrow_mut().fill_limit_order(order);
                }
            }
            Self::OrderEmulator(emulator_weak) => {
                if let Some(emulator) = emulator_weak.upgrade() {
                    emulator.borrow_mut().fill_limit_order(order);
                }
            }
        }
    }
}

#[derive(Clone, Debug)]
pub struct ShareableFillLimitOrderHandler(pub FillLimitOrderHandlerAny);

pub trait TriggerStopOrderHandler {
    fn trigger_stop_order(&mut self, order: &mut OrderAny);
}

#[derive(Clone, Debug)]
pub enum TriggerStopOrderHandlerAny {
    OrderMatchingEngine(WeakCell<OrderMatchingEngine>),
    OrderEmulator(WeakCell<OrderEmulator>),
}

impl TriggerStopOrderHandler for TriggerStopOrderHandlerAny {
    fn trigger_stop_order(&mut self, order: &mut OrderAny) {
        match self {
            Self::OrderMatchingEngine(engine_weak) => {
                if let Some(engine) = engine_weak.upgrade() {
                    engine.borrow_mut().trigger_stop_order(order);
                }
            }
            Self::OrderEmulator(emulator_weak) => {
                if let Some(emulator) = emulator_weak.upgrade() {
                    emulator.borrow_mut().trigger_stop_order(order);
                }
            }
        }
    }
}

#[derive(Clone, Debug)]
pub struct ShareableTriggerStopOrderHandler(pub TriggerStopOrderHandlerAny);

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s) and 3 class(es).

## Detailed Walkthrough

### Functions
- **`fill_market_order()`**: Function defined in this file
- **`fill_market_order()`**: Function defined in this file
- **`fill_limit_order()`**: Function defined in this file
- **`fill_limit_order()`**: Function defined in this file
- **`trigger_stop_order()`**: Function defined in this file
- **`trigger_stop_order()`**: Function defined in this file

### Classes
- **`ShareableFillMarketOrderHandler`**: Class defined in this file
- **`ShareableFillLimitOrderHandler`**: Class defined in this file
- **`ShareableTriggerStopOrderHandler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Enums**: `FillLimitOrderHandlerAny`, `FillMarketOrderHandlerAny`, `TriggerStopOrderHandlerAny`
**Functions**: `fill_limit_order`, `fill_market_order`, `trigger_stop_order`
**Impls**: `FillLimitOrderHandler`, `FillMarketOrderHandler`, `TriggerStopOrderHandler`
**Structs**: `ShareableFillLimitOrderHandler`, `ShareableFillMarketOrderHandler`, `ShareableTriggerStopOrderHandler`
**Traits**: `FillLimitOrderHandler`, `FillMarketOrderHandler`, `TriggerStopOrderHandler`

## Related Files

This file is located in `crates/execution/src/matching_core/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.653326Z*
