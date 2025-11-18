# Documentation: error.rs

## File Metadata

- **Path**: `crates/model/src/orderbook/error.rs`
- **Size**: 2,193 bytes
- **Lines**: 48
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

//! Errors associated with order book operations and integrity.

use nautilus_core::UnixNanos;

use super::ladder::BookPrice;
use crate::enums::{BookType, OrderSide};

#[derive(thiserror::Error, Debug, PartialEq)]
pub enum InvalidBookOperation {
    #[error("Invalid book operation: cannot pre-process order for {0} book")]
    PreProcessOrder(BookType),
    #[error("Invalid book operation: cannot add order for {0} book")]
    Add(BookType),
    #[error("Invalid book operation: cannot update with tick for {0} book")]
    Update(BookType),
}

#[derive(thiserror::Error, Debug, PartialEq)]
pub enum BookIntegrityError {
    #[error("Integrity error: order not found: order_id={0}, sequence={1}, ts_event={2}")]
    OrderNotFound(u64, u64, UnixNanos),
    #[error("Integrity error: invalid `NoOrderSide` in book")]
    NoOrderSide,
    #[error("Integrity error: order_id={0} not found in book for side resolution")]
    OrderNotFoundForSideResolution(u64),
    #[error("Integrity error: orders in cross [{0} {1}]")]
    OrdersCrossed(BookPrice, BookPrice),
    #[error("Integrity error: number of {0} orders at level > 1 for L2_MBP book, was {1}")]
    TooManyOrders(OrderSide, usize),
    #[error("Integrity error: number of {0} levels > 1 for L1_MBP book, was {1}")]
    TooManyLevels(OrderSide, usize),
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Enums**: `BookIntegrityError`, `InvalidBookOperation`

## Related Files

This file is located in `crates/model/src/orderbook/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.758710Z*
