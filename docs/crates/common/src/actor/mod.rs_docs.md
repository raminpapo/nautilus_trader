# Documentation: `crates/common/src/actor/mod.rs`
**Generated:** 2025-11-15T19:40:01.651903Z
**File Size:** 2135 bytes
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

- **Path:** `crates/common/src/actor/mod.rs`
- **Size:** 2,135 bytes
- **Lines:** 61
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 4

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

//! Actor system for event-driven message processing.
//!
//! This module provides the actor framework used throughout NautilusTrader for handling
//! data processing, event management, and asynchronous message handling. Actors are
//! lightweight components that process messages in isolation.

#![allow(unsafe_code)]

use std::{any::Any, fmt::Debug};

use ustr::Ustr;

pub mod data_actor;
#[cfg(feature = "indicators")]
pub(crate) mod indicators;
pub mod registry;

#[cfg(test)]
mod tests;

// Re-exports
pub use data_actor::{DataActor, DataActorCore};

pub use crate::component::Component;

pub trait Actor: Any + Debug {
    /// The unique identifier for the actor.
    fn id(&self) -> Ustr;
    /// Handles the `msg`.
    fn handle(&mut self, msg: &dyn Any);
    /// Returns a reference to `self` as `Any`, for downcasting support.
    fn as_any(&self) -> &dyn Any;
    /// Returns a mutable reference to `self` as `Any`, for downcasting support.
    ///
    /// Default implementation simply coerces `&mut Self` to `&mut dyn Any`.
    ///
    /// # Note
    ///
    /// This method is not object-safe and thus only available on sized `Self`.
    fn as_any_mut(&mut self) -> &mut dyn Any
    where
        Self: Sized,
    {
        self
    }
}
```


---

## Overview

This file is located at `crates/common/src/actor/mod.rs` within the repository.

**Functions defined:** id, handle, as_any, as_any_mut


---

## Detailed Analysis

### Functions

#### `id(&self)`


#### `handle(&mut self, msg: &dyn Any)`


#### `as_any(&self)`


#### `as_any_mut(&mut self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/actor`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


