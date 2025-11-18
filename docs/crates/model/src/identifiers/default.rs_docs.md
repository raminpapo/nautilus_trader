# Documentation: default.rs

## File Metadata

- **Path**: `crates/model/src/identifiers/default.rs`
- **Size**: 2,635 bytes
- **Lines**: 89
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

use crate::identifiers::{
    AccountId, ClientId, ClientOrderId, PositionId, StrategyId, Symbol, TradeId, TraderId, Venue,
    VenueOrderId,
};

impl Default for AccountId {
    /// Creates a new default [`AccountId`] instance for testing.
    fn default() -> Self {
        Self::from("SIM-001")
    }
}

impl Default for ClientId {
    /// Creates a new default [`ClientId`] instance for testing.
    fn default() -> Self {
        Self::from("SIM")
    }
}

impl Default for ClientOrderId {
    /// Creates a new default [`ClientOrderId`] instance for testing.
    fn default() -> Self {
        Self::from("O-19700101-000000-001-001-1")
    }
}

impl Default for PositionId {
    /// Creates a new default [`PositionId`] instance for testing.
    fn default() -> Self {
        Self::from("P-001")
    }
}

impl Default for StrategyId {
    /// Creates a new default [`StrategyId`] instance for testing.
    fn default() -> Self {
        Self::from("S-001")
    }
}

impl Default for TradeId {
    /// Creates a new default [`TradeId`] instance for testing.
    fn default() -> Self {
        Self::from("1")
    }
}

impl Default for TraderId {
    /// Creates a new default [`TraderId`] instance for testing.
    fn default() -> Self {
        Self::from("TRADER-001")
    }
}
impl Default for Symbol {
    /// Creates a new default [`Symbol`] instance for testing.
    fn default() -> Self {
        Self::from("AUD/USD")
    }
}

impl Default for Venue {
    /// Creates a new default [`Venue`] instance for testing.
    fn default() -> Self {
        Self::from("SIM")
    }
}

impl Default for VenueOrderId {
    /// Creates a new default [`VenueOrderId`] instance for testing.
    fn default() -> Self {
        Self::from("001")
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 10 function(s).

## Detailed Walkthrough

### Functions
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `default`
**Impls**: `Default`

## Related Files

This file is located in `crates/model/src/identifiers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.647528Z*
