# Documentation: `crates/execution/src/order_emulator/handlers.rs`
**Generated:** 2025-11-15T19:40:02.116268Z
**File Size:** 2666 bytes
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

- **Path:** `crates/execution/src/order_emulator/handlers.rs`
- **Size:** 2,666 bytes
- **Lines:** 93
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 6
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

use std::any::Any;

use nautilus_common::{messages::execution::TradingCommand, msgbus::handler::MessageHandler};
use nautilus_core::WeakCell;
use nautilus_model::events::OrderEventAny;
use ustr::Ustr;

use super::emulator::OrderEmulator;

#[derive(Debug)]
pub struct OrderEmulatorExecuteHandler {
    id: Ustr,
    emulator: WeakCell<OrderEmulator>,
}

impl OrderEmulatorExecuteHandler {
    #[inline]
    #[must_use]
    pub const fn new(id: Ustr, emulator: WeakCell<OrderEmulator>) -> Self {
        Self { id, emulator }
    }
}

impl MessageHandler for OrderEmulatorExecuteHandler {
    fn id(&self) -> Ustr {
        self.id
    }

    fn handle(&self, msg: &dyn Any) {
        if let Some(emulator) = self.emulator.upgrade() {
            emulator.borrow_mut().execute(
                msg.downcast_ref::<&TradingCommand>()
                    .unwrap()
                    .to_owned()
                    .clone(),
            );
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

#[derive(Debug)]
pub struct OrderEmulatorOnEventHandler {
    id: Ustr,
    emulator: WeakCell<OrderEmulator>,
}

impl OrderEmulatorOnEventHandler {
    #[inline]
    #[must_use]
    pub const fn new(id: Ustr, emulator: WeakCell<OrderEmulator>) -> Self {
        Self { id, emulator }
    }
}

impl MessageHandler for OrderEmulatorOnEventHandler {
    fn id(&self) -> Ustr {
        self.id
    }

    fn handle(&self, msg: &dyn Any) {
        if let Some(emulator) = self.emulator.upgrade() {
            emulator.borrow_mut().on_event(
                msg.downcast_ref::<&OrderEventAny>()
                    .unwrap()
                    .to_owned()
                    .clone(),
            );
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}
```


---

## Overview

This file is located at `crates/execution/src/order_emulator/handlers.rs` within the repository.

**Classes defined:** OrderEmulatorExecuteHandler, OrderEmulatorOnEventHandler, OrderEmulatorExecuteHandler, MessageHandler, OrderEmulatorOnEventHandler, MessageHandler

**Functions defined:** new, id, handle, as_any, new, id, handle, as_any


---

## Detailed Analysis

### Classes

#### `OrderEmulatorExecuteHandler`

**Type:** struct


#### `OrderEmulatorOnEventHandler`

**Type:** struct


#### `OrderEmulatorExecuteHandler`

**Type:** impl


#### `MessageHandler`

**Type:** impl


#### `OrderEmulatorOnEventHandler`

**Type:** impl


#### `MessageHandler`

**Type:** impl


### Functions

#### `new(id: Ustr, emulator: WeakCell<OrderEmulator>)`


#### `id(&self)`


#### `handle(&self, msg: &dyn Any)`


#### `as_any(&self)`


#### `new(id: Ustr, emulator: WeakCell<OrderEmulator>)`


#### `id(&self)`


#### `handle(&self, msg: &dyn Any)`


#### `as_any(&self)`



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


