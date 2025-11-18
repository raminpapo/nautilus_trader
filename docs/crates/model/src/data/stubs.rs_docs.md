# Documentation: stubs.rs

## File Metadata

- **Path**: `crates/model/src/data/stubs.rs`
- **Size**: 12,073 bytes
- **Lines**: 448
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

//! Type stubs to facilitate testing.

use nautilus_core::UnixNanos;
use rstest::fixture;

use super::{
    Bar, BarSpecification, BarType, DEPTH10_LEN, InstrumentStatus, OrderBookDelta, OrderBookDeltas,
    OrderBookDepth10, QuoteTick, TradeTick, close::InstrumentClose,
};
use crate::{
    data::order::BookOrder,
    enums::{
        AggregationSource, AggressorSide, BarAggregation, BookAction, InstrumentCloseType,
        MarketStatusAction, OrderSide, PriceType,
    },
    identifiers::{InstrumentId, Symbol, TradeId, Venue},
    types::{Price, Quantity},
};

impl Default for QuoteTick {
    /// Creates a new default [`QuoteTick`] instance for testing.
    fn default() -> Self {
        Self {
            instrument_id: InstrumentId::from("AUDUSD.SIM"),
            bid_price: Price::from("1.00000"),
            ask_price: Price::from("1.00000"),
            bid_size: Quantity::from(100_000),
            ask_size: Quantity::from(100_000),
            ts_event: UnixNanos::default(),
            ts_init: UnixNanos::default(),
        }
    }
}

impl Default for TradeTick {
    /// Creates a new default [`TradeTick`] instance for testing.
    fn default() -> Self {
        Self {
            instrument_id: InstrumentId::from("AUDUSD.SIM"),
            price: Price::from("1.00000"),
            size: Quantity::from(100_000),
            aggressor_side: AggressorSide::Buyer,
            trade_id: TradeId::new("123456789"),
            ts_event: UnixNanos::default(),
            ts_init: UnixNanos::default(),
        }
    }
}

impl Default for Bar {
    /// Creates a new default [`Bar`] instance for testing.
    fn default() -> Self {
        Self {
            bar_type: BarType::from("AUDUSD.SIM-1-MINUTE-LAST-INTERNAL"),
            open: Price::from("1.00010"),
            high: Price::from("1.00020"),
            low: Price::from("1.00000"),
            close: Price::from("1.00010"),
            volume: Quantity::from(100_000),
            ts_event: UnixNanos::default(),
            ts_init: UnixNanos::default(),
        }
    }
}

#[fixture]
pub fn stub_delta() -> OrderBookDelta {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let action = BookAction::Add;
    let price = Price::from("100.00");
    let size = Quantity::from("10");
    let side = OrderSide::Buy;
    let order_id = 123_456;
    let flags = 0;
    let sequence = 1;
    let ts_event = 1;
    let ts_init = 2;

    let order = BookOrder::new(side, price, size, order_id);
    OrderBookDelta::new(
        instrument_id,
        action,
        order,
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    )
}

#[fixture]
pub fn stub_deltas() -> OrderBookDeltas {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let flags = 32; // Snapshot flag
    let sequence = 0;
    let ts_event = 1;
    let ts_init = 2;

    let delta0 = OrderBookDelta::clear(instrument_id, sequence, ts_event.into(), ts_init.into());
    let delta1 = OrderBookDelta::new(
        instrument_id,
        BookAction::Add,
        BookOrder::new(
            OrderSide::Sell,
            Price::from("102.00"),
            Quantity::from("300"),
            1,
        ),
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    );
    let delta2 = OrderBookDelta::new(
        instrument_id,
        BookAction::Add,
        BookOrder::new(
            OrderSide::Sell,
            Price::from("101.00"),
            Quantity::from("200"),
            2,
        ),
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    );
    let delta3 = OrderBookDelta::new(
        instrument_id,
        BookAction::Add,
        BookOrder::new(
            OrderSide::Sell,
            Price::from("100.00"),
            Quantity::from("100"),
            3,
        ),
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    );
    let delta4 = OrderBookDelta::new(
        instrument_id,
        BookAction::Add,
        BookOrder::new(
            OrderSide::Buy,
            Price::from("99.00"),
            Quantity::from("100"),
            4,
        ),
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    );
    let delta5 = OrderBookDelta::new(
        instrument_id,
        BookAction::Add,
        BookOrder::new(
            OrderSide::Buy,
            Price::from("98.00"),
            Quantity::from("200"),
            5,
        ),
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    );
    let delta6 = OrderBookDelta::new(
        instrument_id,
        BookAction::Add,
        BookOrder::new(
            OrderSide::Buy,
            Price::from("97.00"),
            Quantity::from("300"),
            6,
        ),
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    );

    let deltas = vec![delta0, delta1, delta2, delta3, delta4, delta5, delta6];

    OrderBookDeltas::new(instrument_id, deltas)
}

#[fixture]
pub fn stub_depth10() -> OrderBookDepth10 {
    let instrument_id = InstrumentId::from("AAPL.XNAS");
    let flags = 0;
    let sequence = 0;
    let ts_event = 1;
    let ts_init = 2;

    let mut bids: [BookOrder; DEPTH10_LEN] = [BookOrder::default(); DEPTH10_LEN];
    let mut asks: [BookOrder; DEPTH10_LEN] = [BookOrder::default(); DEPTH10_LEN];

    // Create bids
    let mut price = 99.00;
    let mut quantity = 100.0;
    let mut order_id = 1;

    #[allow(clippy::needless_range_loop)]
    for i in 0..DEPTH10_LEN {
        let order = BookOrder::new(
            OrderSide::Buy,
            Price::new(price, 2),
            Quantity::new(quantity, 0),
            order_id,
        );

        bids[i] = order;

        price -= 1.0;
        quantity += 100.0;
        order_id += 1;
    }

    // Create asks
    let mut price = 100.00;
    let mut quantity = 100.0;
    let mut order_id = 11;

    #[allow(clippy::needless_range_loop)]
    for i in 0..DEPTH10_LEN {
        let order = BookOrder::new(
            OrderSide::Sell,
            Price::new(price, 2),
            Quantity::new(quantity, 0),
            order_id,
        );

        asks[i] = order;

        price += 1.0;
        quantity += 100.0;
        order_id += 1;
    }

    let bid_counts: [u32; DEPTH10_LEN] = [1; DEPTH10_LEN];
    let ask_counts: [u32; DEPTH10_LEN] = [1; DEPTH10_LEN];

    OrderBookDepth10::new(
        instrument_id,
        bids,
        asks,
        bid_counts,
        ask_counts,
        flags,
        sequence,
        ts_event.into(),
        ts_init.into(),
    )
}

#[fixture]
pub fn stub_book_order() -> BookOrder {
    let price = Price::from("100.00");
    let size = Quantity::from("10");
    let side = OrderSide::Buy;
    let order_id = 123_456;

    BookOrder::new(side, price, size, order_id)
}

#[fixture]
pub fn quote_ethusdt_binance() -> QuoteTick {
    QuoteTick {
        instrument_id: InstrumentId::from("ETHUSDT-PERP.BINANCE"),
        bid_price: Price::from("10000.0000"),
        ask_price: Price::from("10001.0000"),
        bid_size: Quantity::from("1.00000000"),
        ask_size: Quantity::from("1.00000000"),
        ts_event: UnixNanos::default(),
        ts_init: UnixNanos::from(1),
    }
}

#[fixture]
pub fn quote_audusd() -> QuoteTick {
    QuoteTick {
        instrument_id: InstrumentId::from("AUD/USD.SIM"),
        bid_price: Price::from("100.0000"),
        ask_price: Price::from("101.0000"),
        bid_size: Quantity::from("1.00000000"),
        ask_size: Quantity::from("1.00000000"),
        ts_event: UnixNanos::default(),
        ts_init: UnixNanos::from(1),
    }
}

#[fixture]
pub fn stub_trade_ethusdt_buyer() -> TradeTick {
    TradeTick {
        instrument_id: InstrumentId::from("ETHUSDT-PERP.BINANCE"),
        price: Price::from("10000.0000"),
        size: Quantity::from("1.00000000"),
        aggressor_side: AggressorSide::Buyer,
        trade_id: TradeId::new("123456789"),
        ts_event: UnixNanos::default(),
        ts_init: UnixNanos::from(1),
    }
}

#[fixture]
pub fn stub_bar() -> Bar {
    let instrument_id = InstrumentId {
        symbol: Symbol::new("AUD/USD"),
        venue: Venue::new("SIM"),
    };
    let bar_spec = BarSpecification::new(1, BarAggregation::Minute, PriceType::Bid);
    let bar_type = BarType::Standard {
        instrument_id,
        spec: bar_spec,
        aggregation_source: AggregationSource::External,
    };
    Bar {
        bar_type,
        open: Price::from("1.00002"),
        high: Price::from("1.00004"),
        low: Price::from("1.00001"),
        close: Price::from("1.00003"),
        volume: Quantity::from("100000"),
        ts_event: UnixNanos::default(),
        ts_init: UnixNanos::from(1),
    }
}

#[fixture]
pub fn stub_instrument_status() -> InstrumentStatus {
    let instrument_id = InstrumentId::from("MSFT.XNAS");
    InstrumentStatus::new(
        instrument_id,
        MarketStatusAction::Trading,
        UnixNanos::from(1),
        UnixNanos::from(2),
        None,
        None,
        None,
        None,
        None,
    )
}

#[fixture]
pub fn stub_instrument_close() -> InstrumentClose {
    let instrument_id = InstrumentId::from("MSFT.XNAS");
    InstrumentClose::new(
        instrument_id,
        Price::from("100.50"),
        InstrumentCloseType::EndOfSession,
        UnixNanos::from(1),
        UnixNanos::from(2),
    )
}

#[derive(Debug)]
pub struct OrderBookDeltaTestBuilder {
    instrument_id: InstrumentId,
    action: Option<BookAction>,
    book_order: Option<BookOrder>,
    flags: Option<u8>,
    sequence: Option<u64>,
}

impl OrderBookDeltaTestBuilder {
    pub fn new(instrument_id: InstrumentId) -> Self {
        Self {
            instrument_id,
            action: None,
            book_order: None,
            flags: None,
            sequence: None,
        }
    }

    pub fn book_action(&mut self, action: BookAction) -> &mut Self {
        self.action = Some(action);
        self
    }

    fn get_book_action(&self) -> BookAction {
        self.action.unwrap_or(BookAction::Add)
    }

    pub fn book_order(&mut self, book_order: BookOrder) -> &mut Self {
        self.book_order = Some(book_order);
        self
    }

    fn get_book_order(&self) -> BookOrder {
        self.book_order.unwrap_or(BookOrder::new(
            OrderSide::Sell,
            Price::from("1500.00"),
            Quantity::from("1"),
            1,
        ))
    }

    pub fn flags(&mut self, flags: u8) -> &mut Self {
        self.flags = Some(flags);
        self
    }

    fn get_flags(&self) -> u8 {
        self.flags.unwrap_or(0)
    }

    pub fn sequence(&mut self, sequence: u64) -> &mut Self {
        self.sequence = Some(sequence);
        self
    }

    fn get_sequence(&self) -> u64 {
        self.sequence.unwrap_or(1)
    }

    pub fn build(&self) -> OrderBookDelta {
        OrderBookDelta::new(
            self.instrument_id,
            self.get_book_action(),
            self.get_book_order(),
            self.get_flags(),
            self.get_sequence(),
            UnixNanos::from(1),
            UnixNanos::from(2),
        )
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 23 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`default()`**: Function defined in this file
- **`stub_delta()`**: Function defined in this file
- **`stub_deltas()`**: Function defined in this file
- **`stub_depth10()`**: Function defined in this file
- **`stub_book_order()`**: Function defined in this file
- **`quote_ethusdt_binance()`**: Function defined in this file
- **`quote_audusd()`**: Function defined in this file
- **`stub_trade_ethusdt_buyer()`**: Function defined in this file
- **`stub_bar()`**: Function defined in this file
- **`stub_instrument_status()`**: Function defined in this file
- **`stub_instrument_close()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`book_action()`**: Function defined in this file
- **`get_book_action()`**: Function defined in this file
- **`book_order()`**: Function defined in this file
- **`get_book_order()`**: Function defined in this file
- **`flags()`**: Function defined in this file
- **`get_flags()`**: Function defined in this file

*...and 3 more functions*

### Classes
- **`OrderBookDeltaTestBuilder`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 23


**Functions**: `book_action`, `book_order`, `build`, `default`, `flags`, `get_book_action`, `get_book_order`, `get_flags`, `get_sequence`, `new`, `quote_audusd`, `quote_ethusdt_binance`, `sequence`, `stub_bar`, `stub_book_order`, `stub_delta`, `stub_deltas`, `stub_depth10`, `stub_instrument_close`, `stub_instrument_status`, `stub_trade_ethusdt_buyer`
**Impls**: `Default`, `OrderBookDeltaTestBuilder`
**Structs**: `OrderBookDeltaTestBuilder`

## Related Files

This file is located in `crates/model/src/data/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.284838Z*
