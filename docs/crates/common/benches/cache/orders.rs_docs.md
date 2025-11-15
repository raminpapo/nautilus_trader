# Documentation: `crates/common/benches/cache/orders.rs`
**Generated:** 2025-11-15T19:40:01.630594Z
**File Size:** 3182 bytes
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

- **Path:** `crates/common/benches/cache/orders.rs`
- **Size:** 3,182 bytes
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


---

## Overview

This file is located at `crates/common/benches/cache/orders.rs` within the repository.

**Functions defined:** cache_order_querying_venue_instrument, cache_orders_processing, bench_order_indexing, bench_order_processing


---

## Detailed Analysis

### Functions

#### `cache_order_querying_venue_instrument(
    cache: &Cache,
    venue: &Venue,
    instrument: Option<&InstrumentId>,
)`


#### `cache_orders_processing(orders: &[OrderAny])`


#### `bench_order_indexing(c: &mut Criterion)`


#### `bench_order_processing(c: &mut Criterion)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/benches/cache`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


