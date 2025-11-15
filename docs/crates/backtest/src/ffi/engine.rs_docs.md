# Documentation: `crates/backtest/src/ffi/engine.rs`
**Generated:** 2025-11-15T19:40:01.608090Z
**File Size:** 2644 bytes
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

- **Path:** `crates/backtest/src/ffi/engine.rs`
- **Size:** 2,644 bytes
- **Lines:** 78
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 7

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
    fmt::Debug,
    ops::{Deref, DerefMut},
};

use nautilus_common::ffi::{clock::TestClock_API, timer::TimeEventHandler};
use nautilus_core::{
    UnixNanos,
    ffi::{cvec::CVec, parsing::u8_as_bool},
};

use crate::accumulator::TimeEventAccumulator;

#[repr(C)]
pub struct TimeEventAccumulatorAPI(Box<TimeEventAccumulator>);

impl Deref for TimeEventAccumulatorAPI {
    type Target = TimeEventAccumulator;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

impl Debug for TimeEventAccumulatorAPI {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        // Print the type name plus a pointer-style hint so callers can at least
        // see that two wrappers refer to the same accumulator.
        write!(f, "TimeEventAccumulatorAPI({:p})", &*self.0)
    }
}

impl DerefMut for TimeEventAccumulatorAPI {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.0
    }
}

#[unsafe(no_mangle)]
pub extern "C" fn time_event_accumulator_new() -> TimeEventAccumulatorAPI {
    TimeEventAccumulatorAPI(Box::default())
}

#[unsafe(no_mangle)]
pub extern "C" fn time_event_accumulator_drop(accumulator: TimeEventAccumulatorAPI) {
    drop(accumulator); // Memory freed here
}

#[unsafe(no_mangle)]
pub extern "C" fn time_event_accumulator_advance_clock(
    accumulator: &mut TimeEventAccumulatorAPI,
    clock: &mut TestClock_API,
    to_time_ns: UnixNanos,
    set_time: u8,
) {
    accumulator.advance_clock(clock, to_time_ns, u8_as_bool(set_time));
}

#[unsafe(no_mangle)]
pub extern "C" fn time_event_accumulator_drain(accumulator: &mut TimeEventAccumulatorAPI) -> CVec {
    let handlers: Vec<TimeEventHandler> = accumulator.drain().into_iter().map(Into::into).collect();
    handlers.into()
}
```


---

## Overview

This file is located at `crates/backtest/src/ffi/engine.rs` within the repository.

**Classes defined:** TimeEventAccumulatorAPI, Deref, Debug, DerefMut

**Functions defined:** deref, fmt, deref_mut, time_event_accumulator_new, time_event_accumulator_drop, time_event_accumulator_advance_clock, time_event_accumulator_drain


---

## Detailed Analysis

### Classes

#### `TimeEventAccumulatorAPI`

**Type:** struct


#### `Deref`

**Type:** impl


#### `Debug`

**Type:** impl


#### `DerefMut`

**Type:** impl


### Functions

#### `deref(&self)`


#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `deref_mut(&mut self)`


#### `time_event_accumulator_new()`


#### `time_event_accumulator_drop(accumulator: TimeEventAccumulatorAPI)`


#### `time_event_accumulator_advance_clock(
    accumulator: &mut TimeEventAccumulatorAPI,
    clock: &mut TestClock_API,
    to_time_ns: UnixNanos,
    set_time: u8,
)`


#### `time_event_accumulator_drain(accumulator: &mut TimeEventAccumulatorAPI)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/backtest/src/ffi`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


