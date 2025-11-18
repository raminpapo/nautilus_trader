# Documentation: engine.rs

## File Metadata

- **Path**: `crates/backtest/src/ffi/engine.rs`
- **Size**: 2,644 bytes
- **Lines**: 79
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`deref()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`deref_mut()`**: Function defined in this file
- **`time_event_accumulator_new()`**: Function defined in this file
- **`time_event_accumulator_drop()`**: Function defined in this file
- **`time_event_accumulator_advance_clock()`**: Function defined in this file
- **`time_event_accumulator_drain()`**: Function defined in this file

### Classes
- **`TimeEventAccumulatorAPI`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `deref`, `deref_mut`, `fmt`, `time_event_accumulator_advance_clock`, `time_event_accumulator_drain`, `time_event_accumulator_drop`, `time_event_accumulator_new`
**Impls**: `Debug`, `Deref`, `DerefMut`
**Structs**: `TimeEventAccumulatorAPI`

## Related Files

This file is located in `crates/backtest/src/ffi/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/backtest/src/ffi/engine.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.918959Z*
