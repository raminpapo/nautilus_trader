# Documentation: handler.rs

## File Metadata

- **Path**: `crates/common/src/msgbus/handler.rs`
- **Size**: 5,195 bytes
- **Lines**: 168
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

//! Message handler functionality for the message bus system.
//!
//! This module provides a trait and implementations for handling messages
//! in a type-safe manner, enabling both typed and untyped message processing.

use std::{
    any::{Any, type_name},
    fmt::Debug,
    marker::PhantomData,
    rc::Rc,
};

use nautilus_core::UUID4;
use ustr::Ustr;

pub trait MessageHandler: Any {
    /// Returns the unique identifier for this handler.
    fn id(&self) -> Ustr;
    /// Handles a message of any type.
    fn handle(&self, message: &dyn Any);
    /// Returns this handler as a trait object.
    fn as_any(&self) -> &dyn Any;
}

impl PartialEq for dyn MessageHandler {
    fn eq(&self, other: &Self) -> bool {
        self.id() == other.id()
    }
}

impl Eq for dyn MessageHandler {}

#[derive(Debug)]
pub struct TypedMessageHandler<T: 'static + ?Sized, F: Fn(&T) + 'static> {
    id: Ustr,
    callback: F,
    _phantom: PhantomData<T>,
}

impl<T: 'static, F: Fn(&T) + 'static> TypedMessageHandler<T, F> {
    /// Creates a new handler with an optional custom ID.
    pub fn new<S: AsRef<str>>(id: Option<S>, callback: F) -> Self {
        let id_ustr = id.map_or_else(
            || generate_handler_id(&callback),
            |s| Ustr::from(s.as_ref()),
        );

        Self {
            id: id_ustr,
            callback,
            _phantom: PhantomData,
        }
    }

    /// Creates a new handler with an auto-generated ID.
    pub fn from(callback: F) -> Self {
        Self::new::<Ustr>(None, callback)
    }
}

impl<T: 'static, F: Fn(&T) + 'static> MessageHandler for TypedMessageHandler<T, F> {
    fn id(&self) -> Ustr {
        self.id
    }

    fn handle(&self, message: &dyn Any) {
        if let Some(typed_msg) = message.downcast_ref::<T>() {
            (self.callback)(typed_msg);
        } else {
            log::error!("Expected message of type {}", type_name::<T>());
        }
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

impl<F: Fn(&dyn Any) + 'static> TypedMessageHandler<dyn Any, F> {
    /// Creates a new handler for dynamic Any messages with an optional custom ID.
    pub fn new_any<S: AsRef<str>>(id: Option<S>, callback: F) -> Self {
        let id_ustr = id.map_or_else(
            || generate_handler_id(&callback),
            |s| Ustr::from(s.as_ref()),
        );

        Self {
            id: id_ustr,
            callback,
            _phantom: PhantomData,
        }
    }

    /// Creates a handler for Any messages with an optional ID.
    pub fn from_any<S: AsRef<str>>(id_opt: Option<S>, callback: F) -> Self {
        Self::new_any(id_opt, callback)
    }

    /// Creates a handler for Any messages with an auto-generated ID.
    pub fn with_any(callback: F) -> Self {
        Self::new_any::<&str>(None, callback)
    }
}

impl<F: Fn(&dyn Any) + 'static> MessageHandler for TypedMessageHandler<dyn Any, F> {
    fn id(&self) -> Ustr {
        self.id
    }

    fn handle(&self, message: &dyn Any) {
        (self.callback)(message);
    }

    fn as_any(&self) -> &dyn Any {
        self
    }
}

fn generate_handler_id<T: 'static + ?Sized, F: 'static + Fn(&T)>(callback: &F) -> Ustr {
    let callback_ptr = std::ptr::from_ref(callback);
    let uuid = UUID4::new();
    Ustr::from(&format!("<{callback_ptr:?}>-{uuid}"))
}

// ShareableMessageHandler contains Rc<dyn MessageHandler> which is not Send/Sync.
// This is intentional - message handlers are designed for single-threaded use within
// each async runtime. The MessageBus uses thread-local storage to ensure each thread
// gets its own handlers, eliminating the need for unsafe Send/Sync implementations.
#[repr(transparent)]
#[derive(Clone)]
pub struct ShareableMessageHandler(pub Rc<dyn MessageHandler>);

impl ShareableMessageHandler {
    pub fn id(&self) -> Ustr {
        self.0.id()
    }
}

impl Debug for ShareableMessageHandler {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct(stringify!(ShareableMessageHandler))
            .field("id", &self.0.id())
            .field("type", &std::any::type_name::<Self>().to_string())
            .finish()
    }
}

impl From<Rc<dyn MessageHandler>> for ShareableMessageHandler {
    fn from(value: Rc<dyn MessageHandler>) -> Self {
        Self(value)
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 19 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file
- **`eq()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file
- **`new_any()`**: Function defined in this file
- **`from_any()`**: Function defined in this file
- **`with_any()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`handle()`**: Function defined in this file
- **`as_any()`**: Function defined in this file
- **`generate_handler_id()`**: Function defined in this file
- **`id()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`from()`**: Function defined in this file

### Classes
- **`TypedMessageHandler`**: Class defined in this file
- **`ShareableMessageHandler`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 20


**Functions**: `as_any`, `eq`, `fmt`, `from`, `from_any`, `generate_handler_id`, `handle`, `id`, `new`, `new_any`, `with_any`
**Impls**: `Debug`, `Eq`, `From`, `MessageHandler`, `PartialEq`, `ShareableMessageHandler`, `TypedMessageHandler`
**Structs**: `ShareableMessageHandler`, `TypedMessageHandler`
**Traits**: `MessageHandler`, `and`, `object`

## Related Files

This file is located in `crates/common/src/msgbus/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.223077Z*
