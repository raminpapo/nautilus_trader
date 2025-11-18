# Documentation: serialization_comparison.rs

## File Metadata

- **Path**: `crates/serialization/benches/serialization_comparison.rs`
- **Size**: 11,780 bytes
- **Lines**: 348
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

//! Comparison benchmarks across different serialization formats.

use std::hint::black_box;

use criterion::{Criterion, criterion_group, criterion_main};
use nautilus_core::serialization::{FromMsgPack, Serializable, ToMsgPack};
use nautilus_model::{
    data::{
        QuoteTick, TradeTick,
        bar::{Bar, BarSpecification, BarType},
    },
    enums::{AggregationSource, AggressorSide, BarAggregation, PriceType},
    identifiers::{InstrumentId, TradeId},
    types::{Price, Quantity},
};
#[cfg(feature = "capnp")]
use nautilus_serialization::capnp::{FromCapnp, ToCapnp, market_capnp};

fn create_quote_tick() -> QuoteTick {
    QuoteTick {
        instrument_id: InstrumentId::from("AAPL.XNAS"),
        bid_price: Price::from("100.50"),
        ask_price: Price::from("100.55"),
        bid_size: Quantity::from("100"),
        ask_size: Quantity::from("100"),
        ts_event: 1_609_459_200_000_000_000.into(),
        ts_init: 1_609_459_200_000_000_000.into(),
    }
}

fn create_trade_tick() -> TradeTick {
    TradeTick {
        instrument_id: InstrumentId::from("ETHUSDT.BINANCE"),
        price: Price::from("2500.75"),
        size: Quantity::from("1.5"),
        aggressor_side: AggressorSide::Buyer,
        trade_id: TradeId::from("12345"),
        ts_event: 1_609_459_200_000_000_000.into(),
        ts_init: 1_609_459_200_000_000_000.into(),
    }
}

fn create_bar() -> Bar {
    let bar_type = BarType::new(
        InstrumentId::from("AAPL.XNAS"),
        BarSpecification::new(1, BarAggregation::Minute, PriceType::Last),
        AggregationSource::Internal,
    );
    Bar::new(
        bar_type,
        Price::from("150.00"),
        Price::from("152.50"),
        Price::from("149.75"),
        Price::from("151.25"),
        Quantity::from("100000"),
        1_609_459_200_000_000_000.into(),
        1_609_459_200_000_000_000.into(),
    )
}

// QuoteTick benchmarks

fn bench_quote_tick_json_serialize(c: &mut Criterion) {
    let quote = create_quote_tick();
    c.bench_function("QuoteTick::json_serialize", |b| {
        b.iter(|| black_box(black_box(&quote).to_json_bytes().unwrap()));
    });
}

fn bench_quote_tick_json_deserialize(c: &mut Criterion) {
    let quote = create_quote_tick();
    let bytes = quote.to_json_bytes().unwrap();
    c.bench_function("QuoteTick::json_deserialize", |b| {
        b.iter(|| black_box(QuoteTick::from_json_bytes(black_box(&bytes)).unwrap()));
    });
}

fn bench_quote_tick_msgpack_serialize(c: &mut Criterion) {
    let quote = create_quote_tick();
    c.bench_function("QuoteTick::msgpack_serialize", |b| {
        b.iter(|| black_box(black_box(&quote).to_msgpack_bytes().unwrap()));
    });
}

fn bench_quote_tick_msgpack_deserialize(c: &mut Criterion) {
    let quote = create_quote_tick();
    let bytes = quote.to_msgpack_bytes().unwrap();
    c.bench_function("QuoteTick::msgpack_deserialize", |b| {
        b.iter(|| black_box(QuoteTick::from_msgpack_bytes(black_box(&bytes)).unwrap()));
    });
}

#[cfg(feature = "capnp")]
fn bench_quote_tick_capnp_serialize(c: &mut Criterion) {
    let quote = create_quote_tick();
    c.bench_function("QuoteTick::capnp_serialize", |b| {
        b.iter(|| {
            let mut message = capnp::message::Builder::new_default();
            let builder = message.init_root::<market_capnp::quote_tick::Builder>();
            black_box(&quote).to_capnp(builder);
            let mut bytes = Vec::new();
            capnp::serialize::write_message(&mut bytes, &message).unwrap();
            black_box(bytes)
        });
    });
}

#[cfg(feature = "capnp")]
fn bench_quote_tick_capnp_deserialize(c: &mut Criterion) {
    let quote = create_quote_tick();
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<market_capnp::quote_tick::Builder>();
    quote.to_capnp(builder);
    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    c.bench_function("QuoteTick::capnp_deserialize", |b| {
        b.iter(|| {
            let reader = capnp::serialize::read_message(
                &mut black_box(&bytes[..]),
                capnp::message::ReaderOptions::new(),
            )
            .unwrap();
            let root = reader
                .get_root::<market_capnp::quote_tick::Reader>()
                .unwrap();
            black_box(QuoteTick::from_capnp(root).unwrap())
        });
    });
}

// TradeTick benchmarks

fn bench_trade_tick_json_serialize(c: &mut Criterion) {
    let trade = create_trade_tick();
    c.bench_function("TradeTick::json_serialize", |b| {
        b.iter(|| black_box(black_box(&trade).to_json_bytes().unwrap()));
    });
}

fn bench_trade_tick_json_deserialize(c: &mut Criterion) {
    let trade = create_trade_tick();
    let bytes = trade.to_json_bytes().unwrap();
    c.bench_function("TradeTick::json_deserialize", |b| {
        b.iter(|| black_box(TradeTick::from_json_bytes(black_box(&bytes)).unwrap()));
    });
}

fn bench_trade_tick_msgpack_serialize(c: &mut Criterion) {
    let trade = create_trade_tick();
    c.bench_function("TradeTick::msgpack_serialize", |b| {
        b.iter(|| black_box(black_box(&trade).to_msgpack_bytes().unwrap()));
    });
}

fn bench_trade_tick_msgpack_deserialize(c: &mut Criterion) {
    let trade = create_trade_tick();
    let bytes = trade.to_msgpack_bytes().unwrap();
    c.bench_function("TradeTick::msgpack_deserialize", |b| {
        b.iter(|| black_box(TradeTick::from_msgpack_bytes(black_box(&bytes)).unwrap()));
    });
}

#[cfg(feature = "capnp")]
fn bench_trade_tick_capnp_serialize(c: &mut Criterion) {
    let trade = create_trade_tick();
    c.bench_function("TradeTick::capnp_serialize", |b| {
        b.iter(|| {
            let mut message = capnp::message::Builder::new_default();
            let builder = message.init_root::<market_capnp::trade_tick::Builder>();
            black_box(&trade).to_capnp(builder);
            let mut bytes = Vec::new();
            capnp::serialize::write_message(&mut bytes, &message).unwrap();
            black_box(bytes)
        });
    });
}

#[cfg(feature = "capnp")]
fn bench_trade_tick_capnp_deserialize(c: &mut Criterion) {
    let trade = create_trade_tick();
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<market_capnp::trade_tick::Builder>();
    trade.to_capnp(builder);
    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    c.bench_function("TradeTick::capnp_deserialize", |b| {
        b.iter(|| {
            let reader = capnp::serialize::read_message(
                &mut black_box(&bytes[..]),
                capnp::message::ReaderOptions::new(),
            )
            .unwrap();
            let root = reader
                .get_root::<market_capnp::trade_tick::Reader>()
                .unwrap();
            black_box(TradeTick::from_capnp(root).unwrap())
        });
    });
}

// Bar benchmarks

fn bench_bar_json_serialize(c: &mut Criterion) {
    let bar = create_bar();
    c.bench_function("Bar::json_serialize", |b| {
        b.iter(|| black_box(black_box(&bar).to_json_bytes().unwrap()));
    });
}

fn bench_bar_json_deserialize(c: &mut Criterion) {
    let bar = create_bar();
    let bytes = bar.to_json_bytes().unwrap();
    c.bench_function("Bar::json_deserialize", |b| {
        b.iter(|| black_box(Bar::from_json_bytes(black_box(&bytes)).unwrap()));
    });
}

fn bench_bar_msgpack_serialize(c: &mut Criterion) {
    let bar = create_bar();
    c.bench_function("Bar::msgpack_serialize", |b| {
        b.iter(|| black_box(black_box(&bar).to_msgpack_bytes().unwrap()));
    });
}

fn bench_bar_msgpack_deserialize(c: &mut Criterion) {
    let bar = create_bar();
    let bytes = bar.to_msgpack_bytes().unwrap();
    c.bench_function("Bar::msgpack_deserialize", |b| {
        b.iter(|| black_box(Bar::from_msgpack_bytes(black_box(&bytes)).unwrap()));
    });
}

#[cfg(feature = "capnp")]
fn bench_bar_capnp_serialize(c: &mut Criterion) {
    let bar = create_bar();
    c.bench_function("Bar::capnp_serialize", |b| {
        b.iter(|| {
            let mut message = capnp::message::Builder::new_default();
            let builder = message.init_root::<market_capnp::bar::Builder>();
            black_box(&bar).to_capnp(builder);
            let mut bytes = Vec::new();
            capnp::serialize::write_message(&mut bytes, &message).unwrap();
            black_box(bytes)
        });
    });
}

#[cfg(feature = "capnp")]
fn bench_bar_capnp_deserialize(c: &mut Criterion) {
    let bar = create_bar();
    let mut message = capnp::message::Builder::new_default();
    let builder = message.init_root::<market_capnp::bar::Builder>();
    bar.to_capnp(builder);
    let mut bytes = Vec::new();
    capnp::serialize::write_message(&mut bytes, &message).unwrap();

    c.bench_function("Bar::capnp_deserialize", |b| {
        b.iter(|| {
            let reader = capnp::serialize::read_message(
                &mut black_box(&bytes[..]),
                capnp::message::ReaderOptions::new(),
            )
            .unwrap();
            let root = reader.get_root::<market_capnp::bar::Reader>().unwrap();
            black_box(Bar::from_capnp(root).unwrap())
        });
    });
}

#[cfg(feature = "capnp")]
criterion_group!(
    quote_tick_benches,
    bench_quote_tick_json_serialize,
    bench_quote_tick_json_deserialize,
    bench_quote_tick_msgpack_serialize,
    bench_quote_tick_msgpack_deserialize,
    bench_quote_tick_capnp_serialize,
    bench_quote_tick_capnp_deserialize,
);

#[cfg(not(feature = "capnp"))]
criterion_group!(
    quote_tick_benches,
    bench_quote_tick_json_serialize,
    bench_quote_tick_json_deserialize,
    bench_quote_tick_msgpack_serialize,
    bench_quote_tick_msgpack_deserialize,
);

#[cfg(feature = "capnp")]
criterion_group!(
    trade_tick_benches,
    bench_trade_tick_json_serialize,
    bench_trade_tick_json_deserialize,
    bench_trade_tick_msgpack_serialize,
    bench_trade_tick_msgpack_deserialize,
    bench_trade_tick_capnp_serialize,
    bench_trade_tick_capnp_deserialize,
);

#[cfg(not(feature = "capnp"))]
criterion_group!(
    trade_tick_benches,
    bench_trade_tick_json_serialize,
    bench_trade_tick_json_deserialize,
    bench_trade_tick_msgpack_serialize,
    bench_trade_tick_msgpack_deserialize,
);

#[cfg(feature = "capnp")]
criterion_group!(
    bar_benches,
    bench_bar_json_serialize,
    bench_bar_json_deserialize,
    bench_bar_msgpack_serialize,
    bench_bar_msgpack_deserialize,
    bench_bar_capnp_serialize,
    bench_bar_capnp_deserialize,
);

#[cfg(not(feature = "capnp"))]
criterion_group!(
    bar_benches,
    bench_bar_json_serialize,
    bench_bar_json_deserialize,
    bench_bar_msgpack_serialize,
    bench_bar_msgpack_deserialize,
);

criterion_main!(quote_tick_benches, trade_tick_benches, bar_benches);

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 21 function(s).

## Detailed Walkthrough

### Functions
- **`create_quote_tick()`**: Function defined in this file
- **`create_trade_tick()`**: Function defined in this file
- **`create_bar()`**: Function defined in this file
- **`bench_quote_tick_json_serialize()`**: Function defined in this file
- **`bench_quote_tick_json_deserialize()`**: Function defined in this file
- **`bench_quote_tick_msgpack_serialize()`**: Function defined in this file
- **`bench_quote_tick_msgpack_deserialize()`**: Function defined in this file
- **`bench_quote_tick_capnp_serialize()`**: Function defined in this file
- **`bench_quote_tick_capnp_deserialize()`**: Function defined in this file
- **`bench_trade_tick_json_serialize()`**: Function defined in this file
- **`bench_trade_tick_json_deserialize()`**: Function defined in this file
- **`bench_trade_tick_msgpack_serialize()`**: Function defined in this file
- **`bench_trade_tick_msgpack_deserialize()`**: Function defined in this file
- **`bench_trade_tick_capnp_serialize()`**: Function defined in this file
- **`bench_trade_tick_capnp_deserialize()`**: Function defined in this file
- **`bench_bar_json_serialize()`**: Function defined in this file
- **`bench_bar_json_deserialize()`**: Function defined in this file
- **`bench_bar_msgpack_serialize()`**: Function defined in this file
- **`bench_bar_msgpack_deserialize()`**: Function defined in this file
- **`bench_bar_capnp_serialize()`**: Function defined in this file

*...and 1 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 21


**Functions**: `bench_bar_capnp_deserialize`, `bench_bar_capnp_serialize`, `bench_bar_json_deserialize`, `bench_bar_json_serialize`, `bench_bar_msgpack_deserialize`, `bench_bar_msgpack_serialize`, `bench_quote_tick_capnp_deserialize`, `bench_quote_tick_capnp_serialize`, `bench_quote_tick_json_deserialize`, `bench_quote_tick_json_serialize`, `bench_quote_tick_msgpack_deserialize`, `bench_quote_tick_msgpack_serialize`, `bench_trade_tick_capnp_deserialize`, `bench_trade_tick_capnp_serialize`, `bench_trade_tick_json_deserialize`, `bench_trade_tick_json_serialize`, `bench_trade_tick_msgpack_deserialize`, `bench_trade_tick_msgpack_serialize`, `create_bar`, `create_quote_tick`, `create_trade_tick`

## Related Files

This file is located in `crates/serialization/benches/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.679318Z*
