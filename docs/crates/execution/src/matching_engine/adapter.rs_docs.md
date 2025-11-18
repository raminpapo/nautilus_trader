# Documentation: adapter.rs

## File Metadata

- **Path**: `crates/execution/src/matching_engine/adapter.rs`
- **Size**: 3,934 bytes
- **Lines**: 117
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`initialize_fill_order_handler()`**: Function defined in this file
- **`initialize_fill_market_order_handler()`**: Function defined in this file
- **`initialize_trigger_stop_order_handler()`**: Function defined in this file
- **`get_engine()`**: Function defined in this file
- **`get_engine_mut()`**: Function defined in this file

### Classes
- **`OrderEngineAdapter`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `get_engine`, `get_engine_mut`, `initialize_fill_market_order_handler`, `initialize_fill_order_handler`, `initialize_trigger_stop_order_handler`, `new`
**Impls**: `OrderEngineAdapter`
**Structs**: `OrderEngineAdapter`

## Related Files

This file is located in `crates/execution/src/matching_engine/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.660705Z*
