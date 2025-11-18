# Documentation: orders.rs

## File Metadata

- **Path**: `crates/common/benches/cache/orders.rs`
- **Size**: 3,182 bytes
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

use std::hint::black_box;

use criterion::{Criterion, criterion_group, criterion_main};
use nautilus_common::cache::Cache;
use nautilus_model::{
    identifiers::{InstrumentId, Venue},
    orders::{OrderAny, stubs::create_order_list_sample},
};

fn cache_order_querying_venue_instrument(
    cache: &Cache,
    venue: &Venue,
    instrument: Option<&InstrumentId>,
) {
    let _ = cache.orders(Some(venue), instrument, None, None);
}

fn cache_orders_processing(orders: &[OrderAny]) {
    let mut cache = Cache::default();
    for order in orders {
        cache.add_order(order.clone(), None, None, false).unwrap();
    }
}

fn bench_order_indexing(c: &mut Criterion) {
    // Create 100k orders list and add it to the cache
    let all_orders = create_order_list_sample(5, 100, 200);
    let mut cache = Cache::default();
    for order in all_orders {
        cache.add_order(order, None, None, false).unwrap();
    }

    let venue = Venue::from("VENUE-1");
    let instrument = InstrumentId::from("SYMBOL-1.1");

    c.bench_function("Cache query by venue", |b| {
        b.iter(|| {
            cache_order_querying_venue_instrument(
                black_box(&cache),
                black_box(&venue),
                black_box(None),
            );
        });
    });

    c.bench_function("Cache query by venue + instrument", |b| {
        b.iter(|| {
            cache_order_querying_venue_instrument(
                black_box(&cache),
                black_box(&venue),
                black_box(Some(&instrument)),
            );
        });
    });
}

fn bench_order_processing(c: &mut Criterion) {
    // Generate list with 100k orders which we slice per test (5 * 100 * 200 = 100k)
    let all_orders = create_order_list_sample(5, 100, 200);

    c.bench_function("Cache order processing one order", |b| {
        b.iter(|| cache_orders_processing(black_box(&all_orders[..1])));
    });

    c.bench_function("Cache order processing 10k orders", |b| {
        b.iter(|| cache_orders_processing(black_box(&all_orders[..10000])));
    });

    c.bench_function("Cache order processing 100k orders", |b| {
        b.iter(|| cache_orders_processing(black_box(&all_orders)));
    });
}

criterion_group!(benches, bench_order_indexing, bench_order_processing);
criterion_main!(benches);

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`cache_order_querying_venue_instrument()`**: Function defined in this file
- **`cache_orders_processing()`**: Function defined in this file
- **`bench_order_indexing()`**: Function defined in this file
- **`bench_order_processing()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `bench_order_indexing`, `bench_order_processing`, `cache_order_querying_venue_instrument`, `cache_orders_processing`

## Related Files

This file is located in `crates/common/benches/cache/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.952398Z*
