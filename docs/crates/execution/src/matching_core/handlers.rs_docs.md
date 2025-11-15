# Documentation: `crates/execution/src/matching_core/handlers.rs`
**Generated:** 2025-11-15T19:40:02.074038Z
**File Size:** 3942 bytes
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

- **Path:** `crates/execution/src/matching_core/handlers.rs`
- **Size:** 3,942 bytes
- **Lines:** 111
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 6
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


---

## Overview

This file is located at `crates/execution/src/matching_core/handlers.rs` within the repository.

**Classes defined:** ShareableFillMarketOrderHandler, ShareableFillLimitOrderHandler, ShareableTriggerStopOrderHandler, FillMarketOrderHandler, FillLimitOrderHandler, TriggerStopOrderHandler

**Functions defined:** fill_market_order, fill_market_order, fill_limit_order, fill_limit_order, trigger_stop_order, trigger_stop_order


---

## Detailed Analysis

### Classes

#### `ShareableFillMarketOrderHandler`

**Type:** struct


#### `ShareableFillLimitOrderHandler`

**Type:** struct


#### `ShareableTriggerStopOrderHandler`

**Type:** struct


#### `FillMarketOrderHandler`

**Type:** impl


#### `FillLimitOrderHandler`

**Type:** impl


#### `TriggerStopOrderHandler`

**Type:** impl


### Functions

#### `fill_market_order(&mut self, order: &OrderAny)`


#### `fill_market_order(&mut self, order: &OrderAny)`


#### `fill_limit_order(&mut self, order: &mut OrderAny)`


#### `fill_limit_order(&mut self, order: &mut OrderAny)`


#### `trigger_stop_order(&mut self, order: &mut OrderAny)`


#### `trigger_stop_order(&mut self, order: &mut OrderAny)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution/src/matching_core`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


