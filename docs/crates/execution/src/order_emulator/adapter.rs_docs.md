# Documentation: `crates/execution/src/order_emulator/adapter.rs`
**Generated:** 2025-11-15T19:40:02.110046Z
**File Size:** 3619 bytes
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

- **Path:** `crates/execution/src/order_emulator/adapter.rs`
- **Size:** 3,619 bytes
- **Lines:** 95
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 8

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


---

## Overview

This file is located at `crates/execution/src/order_emulator/adapter.rs` within the repository.

**Classes defined:** OrderEmulatorAdapter, OrderEmulatorAdapter

**Functions defined:** new, initialize_submit_order_handler, initialize_cancel_order_handler, initialize_modify_order_handler, initialize_execute_handler, initialize_on_event_handler, get_emulator, get_emulator_mut


---

## Detailed Analysis

### Classes

#### `OrderEmulatorAdapter`

**Type:** struct


#### `OrderEmulatorAdapter`

**Type:** impl


### Functions

#### `new(clock: Rc<RefCell<dyn Clock>>, cache: Rc<RefCell<Cache>>)`


#### `initialize_submit_order_handler(emulator: Rc<RefCell<OrderEmulator>>)`


#### `initialize_cancel_order_handler(emulator: Rc<RefCell<OrderEmulator>>)`


#### `initialize_modify_order_handler(emulator: Rc<RefCell<OrderEmulator>>)`


#### `initialize_execute_handler(emulator: Rc<RefCell<OrderEmulator>>)`


#### `initialize_on_event_handler(emulator: Rc<RefCell<OrderEmulator>>)`


#### `get_emulator(&self)`


#### `get_emulator_mut(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution/src/order_emulator`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


