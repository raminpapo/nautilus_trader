# Documentation: `crates/backtest/src/modules/mod.rs`
**Generated:** 2025-11-15T19:40:01.611696Z
**File Size:** 1976 bytes
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

- **Path:** `crates/backtest/src/modules/mod.rs`
- **Size:** 1,976 bytes
- **Lines:** 44
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 5

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

use nautilus_common::logging::logger::Logger;
use nautilus_core::UnixNanos;
use nautilus_model::data::Data;

use crate::exchange::SimulatedExchange;

/// Trait for custom simulation modules that extend backtesting functionality.
///
/// The `SimulationModule` trait allows for custom extensions to the backtesting
/// simulation environment. Implementations can add specialized behavior such as
/// market makers, price impact models, or other venue-specific simulation logic
/// that runs alongside the core backtesting engine.
#[warn(dead_code)]
pub trait SimulationModule {
    /// Registers a simulated exchange venue with this module.
    fn register_venue(&self, exchange: SimulatedExchange);

    /// Pre-processes market data before main simulation processing.
    fn pre_process(&self, data: Data);

    /// Processes simulation logic at the given timestamp.
    fn process(&self, ts_now: UnixNanos);

    /// Logs diagnostic information about the module's state.
    fn log_diagnostics(&self, logger: Logger);

    /// Resets the module to its initial state.
    fn reset(&self);
}
```


---

## Overview

This file is located at `crates/backtest/src/modules/mod.rs` within the repository.

**Functions defined:** register_venue, pre_process, process, log_diagnostics, reset


---

## Detailed Analysis

### Functions

#### `register_venue(&self, exchange: SimulatedExchange)`


#### `pre_process(&self, data: Data)`


#### `process(&self, ts_now: UnixNanos)`


#### `log_diagnostics(&self, logger: Logger)`


#### `reset(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/backtest/src/modules`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


