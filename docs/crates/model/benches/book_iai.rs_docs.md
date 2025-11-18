# Documentation: book_iai.rs

## File Metadata

- **Path**: `crates/model/benches/book_iai.rs`
- **Size**: 3,110 bytes
- **Lines**: 91
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`bench_orderbook_add()`**: Function defined in this file
- **`bench_orderbook_update()`**: Function defined in this file
- **`bench_orderbook_delete()`**: Function defined in this file
- **`bench_orderbook_apply_deltas()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `bench_orderbook_add`, `bench_orderbook_apply_deltas`, `bench_orderbook_delete`, `bench_orderbook_update`

## Related Files

This file is located in `crates/model/benches/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.158792Z*
