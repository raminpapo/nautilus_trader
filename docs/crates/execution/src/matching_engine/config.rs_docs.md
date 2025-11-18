# Documentation: config.rs

## File Metadata

- **Path**: `crates/execution/src/matching_engine/config.rs`
- **Size**: 2,775 bytes
- **Lines**: 80
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

/// Configuration for `OrderMatchingEngine` instances.
#[derive(Debug, Clone)]
pub struct OrderMatchingEngineConfig {
    pub bar_execution: bool,
    pub reject_stop_orders: bool,
    pub support_gtd_orders: bool,
    pub support_contingent_orders: bool,
    pub use_position_ids: bool,
    pub use_random_ids: bool,
    pub use_reduce_only: bool,
    pub price_protection_points: Option<u32>,
}

impl OrderMatchingEngineConfig {
    /// Creates a new default [`OrderMatchingEngineConfig`] instance.
    #[must_use]
    pub const fn new(
        bar_execution: bool,
        reject_stop_orders: bool,
        support_gtd_orders: bool,
        support_contingent_orders: bool,
        use_position_ids: bool,
        use_random_ids: bool,
        use_reduce_only: bool,
    ) -> Self {
        Self {
            bar_execution,
            reject_stop_orders,
            support_gtd_orders,
            support_contingent_orders,
            use_position_ids,
            use_random_ids,
            use_reduce_only,
            price_protection_points: None,
        }
    }

    /// Sets the price protection points for the matching engine.
    #[must_use]
    pub const fn with_price_protection_points(
        mut self,
        price_protection_points: Option<u32>,
    ) -> Self {
        self.price_protection_points = price_protection_points;
        self
    }
}

#[allow(clippy::derivable_impls)]
impl Default for OrderMatchingEngineConfig {
    /// Creates a new default [`OrderMatchingEngineConfig`] instance.
    fn default() -> Self {
        Self {
            bar_execution: false,
            reject_stop_orders: false,
            support_gtd_orders: false,
            support_contingent_orders: false,
            use_position_ids: false,
            use_random_ids: false,
            use_reduce_only: false,
            price_protection_points: None,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`with_price_protection_points()`**: Function defined in this file
- **`default()`**: Function defined in this file

### Classes
- **`OrderMatchingEngineConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `default`, `new`, `with_price_protection_points`
**Impls**: `Default`, `OrderMatchingEngineConfig`
**Structs**: `OrderMatchingEngineConfig`

## Related Files

This file is located in `crates/execution/src/matching_engine/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.662579Z*
