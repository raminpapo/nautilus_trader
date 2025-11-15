# Documentation: `crates/live/src/data.rs`
**Generated:** 2025-11-15T19:40:02.388984Z
**File Size:** 6543 bytes
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

- **Path:** `crates/live/src/data.rs`
- **Size:** 6,543 bytes
- **Lines:** 231
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 20

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

use std::{cell::Ref, fmt::Display};

use nautilus_common::{
    clock::Clock,
    messages::{
        DataEvent,
        data::{
            BarsResponse, BookResponse, DataResponse, InstrumentResponse, InstrumentsResponse,
            QuotesResponse, TradesResponse,
        },
    },
};
use nautilus_core::{UUID4, UnixNanos};
use nautilus_data::client::DataClient;
use nautilus_model::{
    data::{
        Bar, BarType, Data, IndexPriceUpdate, MarkPriceUpdate, OrderBookDelta, OrderBookDeltas_API,
        OrderBookDepth10, QuoteTick, TradeTick, close::InstrumentClose,
    },
    identifiers::{ClientId, InstrumentId, Venue},
    instruments::{Instrument, InstrumentAny},
    orderbook::OrderBook,
};

#[async_trait::async_trait]
pub trait LiveDataClient: DataClient {
    fn get_message_channel(&self) -> tokio::sync::mpsc::UnboundedSender<DataEvent>;

    fn get_clock(&self) -> Ref<'_, dyn Clock>;

    fn send_delta(&self, delta: OrderBookDelta) {
        self.send_data(Data::Delta(delta));
    }

    fn send_deltas(&self, deltas: OrderBookDeltas_API) {
        self.send_data(Data::Deltas(deltas));
    }

    fn send_depth10(&self, depth: OrderBookDepth10) {
        self.send_data(Data::Depth10(Box::new(depth)));
    }

    fn send_quote(&self, quote: QuoteTick) {
        self.send_data(Data::Quote(quote));
    }

    fn send_trade(&self, trade: TradeTick) {
        self.send_data(Data::Trade(trade));
    }

    fn send_bar(&self, bar: Bar) {
        self.send_data(Data::Bar(bar));
    }

    fn send_mark_price(&self, mark_price: MarkPriceUpdate) {
        self.send_data(Data::MarkPriceUpdate(mark_price));
    }

    fn send_index_price(&self, index_price: IndexPriceUpdate) {
        self.send_data(Data::IndexPriceUpdate(index_price));
    }

    fn send_instrument_close(&self, close: InstrumentClose) {
        self.send_data(Data::InstrumentClose(close));
    }

    fn send_data(&self, data: Data) {
        if let Err(e) = self.get_message_channel().send(DataEvent::Data(data)) {
            log_send_error(&self.client_id(), &e);
        }
    }

    fn send_instrument_response(
        &self,
        instrument: InstrumentAny,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) {
        let response = DataResponse::Instrument(Box::new(InstrumentResponse::new(
            correlation_id,
            self.client_id(),
            instrument.id(),
            instrument,
            start,
            end,
            self.get_clock().timestamp_ns(),
            None,
        )));

        self.send_response(response);
    }

    fn send_instruments_response(
        &self,
        venue: Venue,
        instruments: Vec<InstrumentAny>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) {
        let response = DataResponse::Instruments(InstrumentsResponse::new(
            correlation_id,
            self.client_id(),
            venue,
            instruments,
            start,
            end,
            self.get_clock().timestamp_ns(),
            None,
        ));

        self.send_response(response);
    }

    fn send_book_response(
        &self,
        book: OrderBook,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) {
        let response = DataResponse::Book(BookResponse::new(
            correlation_id,
            self.client_id(),
            book.instrument_id,
            book,
            start,
            end,
            self.get_clock().timestamp_ns(),
            None,
        ));

        self.send_response(response);
    }

    fn send_quotes_response(
        &self,
        instrument_id: InstrumentId,
        quotes: Vec<QuoteTick>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) {
        let response = DataResponse::Quotes(QuotesResponse::new(
            correlation_id,
            self.client_id(),
            instrument_id,
            quotes,
            start,
            end,
            self.get_clock().timestamp_ns(),
            None,
        ));

        self.send_response(response);
    }

    fn send_trades_response(
        &self,
        instrument_id: InstrumentId,
        trades: Vec<TradeTick>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) {
        let response = DataResponse::Trades(TradesResponse::new(
            correlation_id,
            self.client_id(),
            instrument_id,
            trades,
            start,
            end,
            self.get_clock().timestamp_ns(),
            None,
        ));

        self.send_response(response);
    }

    fn send_bars(
        &self,
        bar_type: BarType,
        bars: Vec<Bar>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) {
        let response = DataResponse::Bars(BarsResponse::new(
            correlation_id,
            self.client_id(),
            bar_type,
            bars,
            start,
            end,
            self.get_clock().timestamp_ns(),
            None,
        ));

        self.send_response(response);
    }

    fn send_response(&self, response: DataResponse) {
        if let Err(e) = self
            .get_message_channel()
            .send(DataEvent::Response(response))
        {
            log_send_error(&self.client_id(), &e);
        }
    }
}

#[inline(always)]
fn log_send_error<E: Display>(client_id: &ClientId, e: &E) {
    log::error!("DataClient-{client_id} failed to send message: {e}");
}
```


---

## Overview

This file is located at `crates/live/src/data.rs` within the repository.

**Functions defined:** get_message_channel, get_clock, send_delta, send_deltas, send_depth10, send_quote, send_trade, send_bar, send_mark_price, send_index_price and 10 more


---

## Detailed Analysis

### Functions

#### `get_message_channel(&self)`


#### `get_clock(&self)`


#### `send_delta(&self, delta: OrderBookDelta)`


#### `send_deltas(&self, deltas: OrderBookDeltas_API)`


#### `send_depth10(&self, depth: OrderBookDepth10)`


#### `send_quote(&self, quote: QuoteTick)`


#### `send_trade(&self, trade: TradeTick)`


#### `send_bar(&self, bar: Bar)`


#### `send_mark_price(&self, mark_price: MarkPriceUpdate)`


#### `send_index_price(&self, index_price: IndexPriceUpdate)`


#### `send_instrument_close(&self, close: InstrumentClose)`


#### `send_data(&self, data: Data)`


#### `send_instrument_response(
        &self,
        instrument: InstrumentAny,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `send_instruments_response(
        &self,
        venue: Venue,
        instruments: Vec<InstrumentAny>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `send_book_response(
        &self,
        book: OrderBook,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `send_quotes_response(
        &self,
        instrument_id: InstrumentId,
        quotes: Vec<QuoteTick>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `send_trades_response(
        &self,
        instrument_id: InstrumentId,
        trades: Vec<TradeTick>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `send_bars(
        &self,
        bar_type: BarType,
        bars: Vec<Bar>,
        correlation_id: UUID4,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `send_response(&self, response: DataResponse)`


#### `log_send_error(client_id: &ClientId, e: &E)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/live/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


