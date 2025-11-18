# Documentation: handlers.rs

## File Metadata

- **Path**: `crates/execution/src/order_emulator/handlers.rs`
- **Size**: 2,666 bytes
- **Lines**: 94
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file

### Classes
- **`OrderEmulatorExecuteHandler`**: Class defined in this file
- **`OrderEmulatorOnEventHandler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `as_any`, `handle`, `id`, `new`
**Impls**: `MessageHandler`, `OrderEmulatorExecuteHandler`, `OrderEmulatorOnEventHandler`
**Structs**: `OrderEmulatorExecuteHandler`, `OrderEmulatorOnEventHandler`

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

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:55:01.726214Z*
