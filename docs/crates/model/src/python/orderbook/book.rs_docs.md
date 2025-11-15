# Documentation: `crates/model/src/python/orderbook/book.rs`
**Generated:** 2025-11-15T19:40:03.088066Z
**File Size:** 10903 bytes
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

- **Path:** `crates/model/src/python/orderbook/book.rs`
- **Size:** 10,903 bytes
- **Lines:** 352
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 45

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

use std::collections::HashSet;

use indexmap::IndexMap;
use nautilus_core::python::{to_pyruntime_err, to_pyvalue_err};
use pyo3::prelude::*;
use rust_decimal::Decimal;

use crate::{
    data::{BookOrder, OrderBookDelta, OrderBookDeltas, OrderBookDepth10, QuoteTick, TradeTick},
    enums::{BookType, OrderSide, OrderStatus},
    identifiers::InstrumentId,
    orderbook::{BookLevel, OrderBook, analysis::book_check_integrity, own::OwnOrderBook},
    types::{Price, Quantity},
};

#[pymethods]
impl OrderBook {
    #[new]
    fn py_new(instrument_id: InstrumentId, book_type: BookType) -> Self {
        Self::new(instrument_id, book_type)
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }

    fn __str__(&self) -> String {
        self.to_string()
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    fn py_instrument_id(&self) -> InstrumentId {
        self.instrument_id
    }

    #[getter]
    #[pyo3(name = "book_type")]
    fn py_book_type(&self) -> BookType {
        self.book_type
    }

    #[getter]
    #[pyo3(name = "sequence")]
    fn py_sequence(&self) -> u64 {
        self.sequence
    }

    #[getter]
    #[pyo3(name = "ts_event")]
    fn py_ts_event(&self) -> u64 {
        self.ts_last.as_u64()
    }

    #[getter]
    #[pyo3(name = "ts_init")]
    fn py_ts_init(&self) -> u64 {
        self.ts_last.as_u64()
    }

    #[getter]
    #[pyo3(name = "ts_last")]
    fn py_ts_last(&self) -> u64 {
        self.ts_last.as_u64()
    }

    #[getter]
    #[pyo3(name = "update_count")]
    fn py_update_count(&self) -> u64 {
        self.update_count
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }

    #[pyo3(name = "add")]
    #[pyo3(signature = (order, flags, sequence, ts_event))]
    fn py_add(&mut self, order: BookOrder, flags: u8, sequence: u64, ts_event: u64) {
        self.add(order, flags, sequence, ts_event.into());
    }

    #[pyo3(name = "update")]
    #[pyo3(signature = (order, flags, sequence, ts_event))]
    fn py_update(&mut self, order: BookOrder, flags: u8, sequence: u64, ts_event: u64) {
        self.update(order, flags, sequence, ts_event.into());
    }

    #[pyo3(name = "delete")]
    #[pyo3(signature = (order, flags, sequence, ts_event))]
    fn py_delete(&mut self, order: BookOrder, flags: u8, sequence: u64, ts_event: u64) {
        self.delete(order, flags, sequence, ts_event.into());
    }

    #[pyo3(name = "clear")]
    #[pyo3(signature = (sequence, ts_event))]
    fn py_clear(&mut self, sequence: u64, ts_event: u64) {
        self.clear(sequence, ts_event.into());
    }

    #[pyo3(name = "clear_bids")]
    #[pyo3(signature = (sequence, ts_event))]
    fn py_clear_bids(&mut self, sequence: u64, ts_event: u64) {
        self.clear_bids(sequence, ts_event.into());
    }

    #[pyo3(name = "clear_asks")]
    #[pyo3(signature = (sequence, ts_event))]
    fn py_clear_asks(&mut self, sequence: u64, ts_event: u64) {
        self.clear_asks(sequence, ts_event.into());
    }

    #[pyo3(name = "clear_stale_levels")]
    #[pyo3(signature = (side=None))]
    fn py_clear_stale_levels(&mut self, side: Option<OrderSide>) -> Option<Vec<BookLevel>> {
        self.clear_stale_levels(side)
    }

    #[pyo3(name = "apply_delta")]
    fn py_apply_delta(&mut self, delta: &OrderBookDelta) -> PyResult<()> {
        self.apply_delta(delta).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "apply_deltas")]
    fn py_apply_deltas(&mut self, deltas: &OrderBookDeltas) -> PyResult<()> {
        self.apply_deltas(deltas).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "apply_depth")]
    fn py_apply_depth(&mut self, depth: &OrderBookDepth10) {
        self.apply_depth(depth);
    }

    #[pyo3(name = "check_integrity")]
    fn py_check_integrity(&mut self) -> PyResult<()> {
        book_check_integrity(self).map_err(to_pyruntime_err)
    }

    #[pyo3(name = "bids")]
    #[pyo3(signature = (depth=None))]
    fn py_bids(&self, depth: Option<usize>) -> Vec<BookLevel> {
        self.bids(depth)
            .map(|level_ref| (*level_ref).clone())
            .collect()
    }

    #[pyo3(name = "asks")]
    #[pyo3(signature = (depth=None))]
    fn py_asks(&self, depth: Option<usize>) -> Vec<BookLevel> {
        self.asks(depth)
            .map(|level_ref| (*level_ref).clone())
            .collect()
    }

    #[pyo3(name = "bids_to_dict")]
    #[pyo3(signature = (depth=None))]
    fn py_bids_to_dict(&self, depth: Option<usize>) -> IndexMap<Decimal, Decimal> {
        self.bids_as_map(depth)
    }

    #[pyo3(name = "asks_to_dict")]
    #[pyo3(signature = (depth=None))]
    fn py_asks_to_dict(&self, depth: Option<usize>) -> IndexMap<Decimal, Decimal> {
        self.asks_as_map(depth)
    }

    #[pyo3(name = "group_bids")]
    #[pyo3(signature = (group_size, depth=None))]
    pub fn py_group_bids(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
    ) -> IndexMap<Decimal, Decimal> {
        self.group_bids(group_size, depth)
    }

    #[pyo3(name = "group_asks")]
    #[pyo3(signature = (group_size, depth=None))]
    pub fn py_group_asks(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
    ) -> IndexMap<Decimal, Decimal> {
        self.group_asks(group_size, depth)
    }

    #[pyo3(name = "bids_filtered_to_dict")]
    #[pyo3(signature = (depth=None, own_book=None, status=None, accepted_buffer_ns=None, ts_now=None))]
    fn py_bids_filtered_to_dict(
        &self,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    ) -> IndexMap<Decimal, Decimal> {
        self.bids_filtered_as_map(depth, own_book, status, accepted_buffer_ns, ts_now)
    }

    #[pyo3(name = "asks_filtered_to_dict")]
    #[pyo3(signature = (depth=None, own_book=None, status=None, accepted_buffer_ns=None, ts_now=None))]
    fn py_asks_filtered_to_dict(
        &self,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    ) -> IndexMap<Decimal, Decimal> {
        self.asks_filtered_as_map(depth, own_book, status, accepted_buffer_ns, ts_now)
    }

    #[pyo3(name = "group_bids_filtered")]
    #[pyo3(signature = (group_size, depth=None, own_book=None, status=None, accepted_buffer_ns=None, ts_now=None))]
    fn py_group_bids_filered(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    ) -> IndexMap<Decimal, Decimal> {
        self.group_bids_filtered(
            group_size,
            depth,
            own_book,
            status,
            accepted_buffer_ns,
            ts_now,
        )
    }

    #[pyo3(name = "group_asks_filtered")]
    #[pyo3(signature = (group_size, depth=None, own_book=None, status=None, accepted_buffer_ns=None, ts_now=None))]
    fn py_group_asks_filtered(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    ) -> IndexMap<Decimal, Decimal> {
        self.group_asks_filtered(
            group_size,
            depth,
            own_book,
            status,
            accepted_buffer_ns,
            ts_now,
        )
    }

    #[pyo3(name = "best_bid_price")]
    fn py_best_bid_price(&self) -> Option<Price> {
        self.best_bid_price()
    }

    #[pyo3(name = "best_ask_price")]
    fn py_best_ask_price(&self) -> Option<Price> {
        self.best_ask_price()
    }

    #[pyo3(name = "best_bid_size")]
    fn py_best_bid_size(&self) -> Option<Quantity> {
        self.best_bid_size()
    }

    #[pyo3(name = "best_ask_size")]
    fn py_best_ask_size(&self) -> Option<Quantity> {
        self.best_ask_size()
    }

    #[pyo3(name = "spread")]
    fn py_spread(&self) -> Option<f64> {
        self.spread()
    }

    #[pyo3(name = "midpoint")]
    fn py_midpoint(&self) -> Option<f64> {
        self.midpoint()
    }

    #[pyo3(name = "get_avg_px_for_quantity")]
    fn py_get_avg_px_for_quantity(&self, qty: Quantity, order_side: OrderSide) -> f64 {
        self.get_avg_px_for_quantity(qty, order_side)
    }

    #[pyo3(name = "get_avg_px_qty_for_exposure")]
    fn py_get_avg_px_qty_for_exposure(
        &self,
        qty: Quantity,
        order_side: OrderSide,
    ) -> (f64, f64, f64) {
        self.get_avg_px_qty_for_exposure(qty, order_side)
    }

    #[pyo3(name = "get_quantity_for_price")]
    fn py_get_quantity_for_price(&self, price: Price, order_side: OrderSide) -> f64 {
        self.get_quantity_for_price(price, order_side)
    }

    #[pyo3(name = "simulate_fills")]
    fn py_simulate_fills(&self, order: &BookOrder) -> Vec<(Price, Quantity)> {
        self.simulate_fills(order)
    }

    #[pyo3(name = "pprint")]
    #[pyo3(signature = (num_levels=3, group_size=None))]
    fn py_pprint(&self, num_levels: usize, group_size: Option<Decimal>) -> String {
        self.pprint(num_levels, group_size)
    }
}

/// Updates the `OrderBook` with a [`QuoteTick`].
///
/// # Errors
///
/// Returns a `PyErr` if the update operation fails.
#[pyfunction()]
#[pyo3(name = "update_book_with_quote_tick")]
pub fn py_update_book_with_quote_tick(book: &mut OrderBook, quote: &QuoteTick) -> PyResult<()> {
    book.update_quote_tick(quote).map_err(to_pyvalue_err)
}

/// Updates the `OrderBook` with a [`TradeTick`].
///
/// # Errors
///
/// Returns a `PyErr` if the update operation fails.
#[pyfunction()]
#[pyo3(name = "update_book_with_trade_tick")]
pub fn py_update_book_with_trade_tick(book: &mut OrderBook, trade: &TradeTick) -> PyResult<()> {
    book.update_trade_tick(trade).map_err(to_pyvalue_err)
}
```


---

## Overview

This file is located at `crates/model/src/python/orderbook/book.rs` within the repository.

**Classes defined:** OrderBook

**Functions defined:** py_new, __repr__, __str__, py_instrument_id, py_book_type, py_sequence, py_ts_event, py_ts_init, py_ts_last, py_update_count and 35 more


---

## Detailed Analysis

### Classes

#### `OrderBook`

**Type:** impl


### Functions

#### `py_new(instrument_id: InstrumentId, book_type: BookType)`


#### `__repr__(&self)`


#### `__str__(&self)`


#### `py_instrument_id(&self)`


#### `py_book_type(&self)`


#### `py_sequence(&self)`


#### `py_ts_event(&self)`


#### `py_ts_init(&self)`


#### `py_ts_last(&self)`


#### `py_update_count(&self)`


#### `py_reset(&mut self)`


#### `py_add(&mut self, order: BookOrder, flags: u8, sequence: u64, ts_event: u64)`


#### `py_update(&mut self, order: BookOrder, flags: u8, sequence: u64, ts_event: u64)`


#### `py_delete(&mut self, order: BookOrder, flags: u8, sequence: u64, ts_event: u64)`


#### `py_clear(&mut self, sequence: u64, ts_event: u64)`


#### `py_clear_bids(&mut self, sequence: u64, ts_event: u64)`


#### `py_clear_asks(&mut self, sequence: u64, ts_event: u64)`


#### `py_clear_stale_levels(&mut self, side: Option<OrderSide>)`


#### `py_apply_delta(&mut self, delta: &OrderBookDelta)`


#### `py_apply_deltas(&mut self, deltas: &OrderBookDeltas)`


#### `py_apply_depth(&mut self, depth: &OrderBookDepth10)`


#### `py_check_integrity(&mut self)`


#### `py_bids(&self, depth: Option<usize>)`


#### `py_asks(&self, depth: Option<usize>)`


#### `py_bids_to_dict(&self, depth: Option<usize>)`


#### `py_asks_to_dict(&self, depth: Option<usize>)`


#### `py_group_bids(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
    )`


#### `py_group_asks(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
    )`


#### `py_bids_filtered_to_dict(
        &self,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    )`


#### `py_asks_filtered_to_dict(
        &self,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    )`


#### `py_group_bids_filered(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    )`


#### `py_group_asks_filtered(
        &self,
        group_size: Decimal,
        depth: Option<usize>,
        own_book: Option<&OwnOrderBook>,
        status: Option<HashSet<OrderStatus>>,
        accepted_buffer_ns: Option<u64>,
        ts_now: Option<u64>,
    )`


#### `py_best_bid_price(&self)`


#### `py_best_ask_price(&self)`


#### `py_best_bid_size(&self)`


#### `py_best_ask_size(&self)`


#### `py_spread(&self)`


#### `py_midpoint(&self)`


#### `py_get_avg_px_for_quantity(&self, qty: Quantity, order_side: OrderSide)`


#### `py_get_avg_px_qty_for_exposure(
        &self,
        qty: Quantity,
        order_side: OrderSide,
    )`


#### `py_get_quantity_for_price(&self, price: Price, order_side: OrderSide)`


#### `py_simulate_fills(&self, order: &BookOrder)`


#### `py_pprint(&self, num_levels: usize, group_size: Option<Decimal>)`


#### `py_update_book_with_quote_tick(book: &mut OrderBook, quote: &QuoteTick)`


#### `py_update_book_with_trade_tick(book: &mut OrderBook, trade: &TradeTick)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/orderbook`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


