# Documentation: adapter.rs

## File Metadata

- **Path**: `crates/execution/src/order_emulator/adapter.rs`
- **Size**: 3,619 bytes
- **Lines**: 96
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

use nautilus_common::{
    cache::Cache,
    clock::Clock,
    msgbus::{handler::ShareableMessageHandler, register},
};
use nautilus_core::{UUID4, WeakCell};
use ustr::Ustr;

use crate::order_emulator::{
    emulator::OrderEmulator,
    handlers::{OrderEmulatorExecuteHandler, OrderEmulatorOnEventHandler},
};

#[derive(Debug)]
pub struct OrderEmulatorAdapter {
    emulator: Rc<RefCell<OrderEmulator>>,
}

impl OrderEmulatorAdapter {
    pub fn new(clock: Rc<RefCell<dyn Clock>>, cache: Rc<RefCell<Cache>>) -> Self {
        let emulator = Rc::new(RefCell::new(OrderEmulator::new(clock, cache)));

        Self::initialize_execute_handler(emulator.clone());
        Self::initialize_on_event_handler(emulator.clone());
        // Self::initialize_submit_order_handler(emulator.clone());
        // Self::initialize_cancel_order_handler(emulator.clone());
        // Self::initialize_modify_order_handler(emulator.clone());

        Self { emulator }
    }

    // TODO: WIP: Revisit with actor framework
    // fn initialize_submit_order_handler(emulator: Rc<RefCell<OrderEmulator>>) {
    //     let handler = SubmitOrderHandlerAny::OrderEmulator(emulator.clone());
    //     emulator.borrow_mut().set_submit_order_handler(handler);
    // }
    //
    // fn initialize_cancel_order_handler(emulator: Rc<RefCell<OrderEmulator>>) {
    //     let handler = CancelOrderHandlerAny::OrderEmulator(emulator.clone());
    //     emulator.borrow_mut().set_cancel_order_handler(handler);
    // }
    //
    // fn initialize_modify_order_handler(emulator: Rc<RefCell<OrderEmulator>>) {
    //     let handler = ModifyOrderHandlerAny::OrderEmulator(emulator.clone());
    //     emulator.borrow_mut().set_modify_order_handler(handler);
    // }

    fn initialize_execute_handler(emulator: Rc<RefCell<OrderEmulator>>) {
        let handler = ShareableMessageHandler(Rc::new(OrderEmulatorExecuteHandler::new(
            Ustr::from(&UUID4::new().to_string()),
            WeakCell::from(Rc::downgrade(&emulator)),
        )));

        register("OrderEmulator.execute".into(), handler);
    }

    fn initialize_on_event_handler(emulator: Rc<RefCell<OrderEmulator>>) {
        let handler = ShareableMessageHandler(Rc::new(OrderEmulatorOnEventHandler::new(
            Ustr::from(&UUID4::new().to_string()),
            WeakCell::from(Rc::downgrade(&emulator)),
        )));

        register("OrderEmulator.on_event".into(), handler);
    }

    #[must_use]
    pub fn get_emulator(&self) -> Ref<'_, OrderEmulator> {
        self.emulator.borrow()
    }

    #[must_use]
    pub fn get_emulator_mut(&self) -> RefMut<'_, OrderEmulator> {
        self.emulator.borrow_mut()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`initialize_submit_order_handler()`**: Function defined in this file
- **`initialize_cancel_order_handler()`**: Function defined in this file
- **`initialize_modify_order_handler()`**: Function defined in this file
- **`initialize_execute_handler()`**: Function defined in this file
- **`initialize_on_event_handler()`**: Function defined in this file
- **`get_emulator()`**: Function defined in this file
- **`get_emulator_mut()`**: Function defined in this file

### Classes
- **`OrderEmulatorAdapter`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `get_emulator`, `get_emulator_mut`, `initialize_cancel_order_handler`, `initialize_execute_handler`, `initialize_modify_order_handler`, `initialize_on_event_handler`, `initialize_submit_order_handler`, `new`
**Impls**: `OrderEmulatorAdapter`
**Structs**: `OrderEmulatorAdapter`

## Related Files

This file is located in `crates/execution/src/order_emulator/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.716329Z*
