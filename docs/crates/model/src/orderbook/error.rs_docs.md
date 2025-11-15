# Documentation: `crates/model/src/orderbook/error.rs`
**Generated:** 2025-11-15T19:40:02.839616Z
**File Size:** 2193 bytes
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

- **Path:** `crates/model/src/orderbook/error.rs`
- **Size:** 2,193 bytes
- **Lines:** 47
- **Extension:** `.rs`
- **Type:** text

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


---

## Overview

This file is located at `crates/model/src/orderbook/error.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/orderbook`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


