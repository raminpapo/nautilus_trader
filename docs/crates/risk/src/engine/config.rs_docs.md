# Documentation: config.rs

## File Metadata

- **Path**: `crates/risk/src/engine/config.rs`
- **Size**: 1,836 bytes
- **Lines**: 47
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

//! Provides a configuration for `RiskEngine` instances.

use std::collections::HashMap;

use nautilus_common::throttler::RateLimit;
use nautilus_core::datetime::NANOSECONDS_IN_SECOND;
use nautilus_model::identifiers::InstrumentId;
use rust_decimal::Decimal;

#[derive(Debug, Clone)]
/// Configuration for `RiskEngineConfig` instances.
pub struct RiskEngineConfig {
    pub bypass: bool,
    pub max_order_submit: RateLimit,
    pub max_order_modify: RateLimit,
    pub max_notional_per_order: HashMap<InstrumentId, Decimal>,
    pub debug: bool,
}

impl Default for RiskEngineConfig {
    /// Creates a new [`RiskEngineConfig`] instance.
    fn default() -> Self {
        Self {
            bypass: false,
            max_order_submit: RateLimit::new(100, NANOSECONDS_IN_SECOND),
            max_order_modify: RateLimit::new(100, NANOSECONDS_IN_SECOND),
            max_notional_per_order: HashMap::new(),
            debug: false,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`default()`**: Function defined in this file

### Classes
- **`RiskEngineConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `default`
**Impls**: `Default`
**Structs**: `RiskEngineConfig`

## Related Files

This file is located in `crates/risk/src/engine/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.633453Z*
