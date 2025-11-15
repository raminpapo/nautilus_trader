# Documentation: `crates/execution/src/matching_engine/adapter.rs`
**Generated:** 2025-11-15T19:40:02.078374Z
**File Size:** 3934 bytes
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

- **Path:** `crates/execution/src/matching_engine/adapter.rs`
- **Size:** 3,934 bytes
- **Lines:** 116
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
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

use std::{
    cell::{Ref, RefCell, RefMut},
    rc::Rc,
};

use nautilus_common::{cache::Cache, clock::Clock};
use nautilus_core::WeakCell;
use nautilus_model::{
    enums::{AccountType, BookType, OmsType},
    instruments::InstrumentAny,
};

use crate::{
    matching_core::handlers::{
        FillLimitOrderHandlerAny, FillMarketOrderHandlerAny, ShareableFillLimitOrderHandler,
        ShareableFillMarketOrderHandler, ShareableTriggerStopOrderHandler,
        TriggerStopOrderHandlerAny,
    },
    matching_engine::{config::OrderMatchingEngineConfig, engine::OrderMatchingEngine},
    models::{fee::FeeModelAny, fill::FillModel},
};

#[derive(Debug)]
pub struct OrderEngineAdapter {
    engine: Rc<RefCell<OrderMatchingEngine>>,
}

impl OrderEngineAdapter {
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument: InstrumentAny,
        raw_id: u32,
        fill_model: FillModel,
        fee_model: FeeModelAny,
        book_type: BookType,
        oms_type: OmsType,
        account_type: AccountType,
        clock: Rc<RefCell<dyn Clock>>,
        cache: Rc<RefCell<Cache>>,
        config: OrderMatchingEngineConfig,
    ) -> Self {
        let engine = Rc::new(RefCell::new(OrderMatchingEngine::new(
            instrument,
            raw_id,
            fill_model,
            fee_model,
            book_type,
            oms_type,
            account_type,
            clock,
            cache,
            config,
        )));

        Self::initialize_fill_order_handler(engine.clone());
        Self::initialize_fill_market_order_handler(engine.clone());
        Self::initialize_trigger_stop_order_handler(engine.clone());

        Self { engine }
    }

    fn initialize_fill_order_handler(engine: Rc<RefCell<OrderMatchingEngine>>) {
        let handler = ShareableFillLimitOrderHandler(
            FillLimitOrderHandlerAny::OrderMatchingEngine(WeakCell::from(Rc::downgrade(&engine))),
        );
        engine
            .borrow_mut()
            .core
            .set_fill_limit_order_handler(handler);
    }

    fn initialize_fill_market_order_handler(engine: Rc<RefCell<OrderMatchingEngine>>) {
        let handler = ShareableFillMarketOrderHandler(
            FillMarketOrderHandlerAny::OrderMatchingEngine(WeakCell::from(Rc::downgrade(&engine))),
        );
        engine
            .borrow_mut()
            .core
            .set_fill_market_order_handler(handler);
    }

    fn initialize_trigger_stop_order_handler(engine: Rc<RefCell<OrderMatchingEngine>>) {
        let handler = ShareableTriggerStopOrderHandler(
            TriggerStopOrderHandlerAny::OrderMatchingEngine(WeakCell::from(Rc::downgrade(&engine))),
        );
        engine
            .borrow_mut()
            .core
            .set_trigger_stop_order_handler(handler);
    }

    #[must_use]
    pub fn get_engine(&self) -> Ref<'_, OrderMatchingEngine> {
        self.engine.borrow()
    }

    #[must_use]
    pub fn get_engine_mut(&self) -> RefMut<'_, OrderMatchingEngine> {
        self.engine.borrow_mut()
    }
}
```


---

## Overview

This file is located at `crates/execution/src/matching_engine/adapter.rs` within the repository.

**Classes defined:** OrderEngineAdapter, OrderEngineAdapter

**Functions defined:** new, initialize_fill_order_handler, initialize_fill_market_order_handler, initialize_trigger_stop_order_handler, get_engine, get_engine_mut


---

## Detailed Analysis

### Classes

#### `OrderEngineAdapter`

**Type:** struct


#### `OrderEngineAdapter`

**Type:** impl


### Functions

#### `new(
        instrument: InstrumentAny,
        raw_id: u32,
        fill_model: FillModel,
        fee_model: FeeModelAny,
        book_type: BookType,
        oms_type: OmsType,
        account_type: AccountType,
        clock: Rc<RefCell<dyn Clock>>,
        cache: Rc<RefCell<Cache>>,
        config: OrderMatchingEngineConfig,
    )`


#### `initialize_fill_order_handler(engine: Rc<RefCell<OrderMatchingEngine>>)`


#### `initialize_fill_market_order_handler(engine: Rc<RefCell<OrderMatchingEngine>>)`


#### `initialize_trigger_stop_order_handler(engine: Rc<RefCell<OrderMatchingEngine>>)`


#### `get_engine(&self)`


#### `get_engine_mut(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution/src/matching_engine`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


