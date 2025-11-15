# Documentation: `crates/model/benches/book_iai.rs`
**Generated:** 2025-11-15T19:40:02.425790Z
**File Size:** 3110 bytes
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

- **Path:** `crates/model/benches/book_iai.rs`
- **Size:** 3,110 bytes
- **Lines:** 90
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

use iai::black_box;
use nautilus_model::{
    data::{BookOrder, OrderBookDelta, OrderBookDeltas},
    enums::{BookAction, BookType, OrderSide},
    identifiers::InstrumentId,
    orderbook::OrderBook,
    types::{Price, Quantity},
};

fn bench_orderbook_add() {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let mut book = OrderBook::new(instrument_id, BookType::L3_MBO);
    let order = BookOrder::new(OrderSide::Buy, Price::from("100.0"), Quantity::from(100), 1);

    book.add(order, 0, 1, 1.into());
    black_box(());
}

fn bench_orderbook_update() {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let mut book = OrderBook::new(instrument_id, BookType::L3_MBO);
    let order = BookOrder::new(OrderSide::Buy, Price::from("100.0"), Quantity::from(100), 1);
    book.add(order, 0, 1, 1.into());

    let updated_order = BookOrder::new(
        OrderSide::Buy,
        Price::from("101.0"),
        Quantity::from("2.0"),
        1,
    );

    book.update(updated_order, 0, 2, 2.into());
    black_box(());
}

fn bench_orderbook_delete() {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let mut book = OrderBook::new(instrument_id, BookType::L3_MBO);
    let order = BookOrder::new(OrderSide::Buy, Price::from("100.0"), Quantity::from(100), 1);
    book.add(order, 0, 1, 1.into());

    book.delete(order, 0, 2, 2.into());
    black_box(());
}

fn bench_orderbook_apply_deltas() {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let mut book = OrderBook::new(instrument_id, BookType::L3_MBO);
    let deltas = OrderBookDeltas {
        instrument_id,
        deltas: vec![OrderBookDelta {
            instrument_id,
            action: BookAction::Add,
            order: BookOrder::new(OrderSide::Buy, Price::from("100.0"), Quantity::from(100), 1),
            flags: 0,
            sequence: 1,
            ts_event: 1.into(),
            ts_init: 2.into(),
        }],
        flags: 0,
        sequence: 1,
        ts_event: 1.into(),
        ts_init: 2.into(),
    };

    book.apply_deltas(&deltas).unwrap();
    black_box(());
}

iai::main!(
    bench_orderbook_add,
    bench_orderbook_update,
    bench_orderbook_delete,
    bench_orderbook_apply_deltas,
);
```


---

## Overview

This file is located at `crates/model/benches/book_iai.rs` within the repository.

**Functions defined:** bench_orderbook_add, bench_orderbook_update, bench_orderbook_delete, bench_orderbook_apply_deltas


---

## Detailed Analysis

### Functions

#### `bench_orderbook_add()`


#### `bench_orderbook_update()`


#### `bench_orderbook_delete()`


#### `bench_orderbook_apply_deltas()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/benches`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


