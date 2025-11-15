# Documentation: `crates/backtest/src/data_client.rs`
**Generated:** 2025-11-15T19:40:01.593958Z
**File Size:** 7712 bytes
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

- **Path:** `crates/backtest/src/data_client.rs`
- **Size:** 7,712 bytes
- **Lines:** 262
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 5
- **Functions:** 44

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

//! Provides a `BacktestDataClient` implementation for backtesting.

// Under development
#![allow(dead_code)]
#![allow(unused_variables)]

use std::{cell::RefCell, rc::Rc};

use nautilus_common::{
    cache::Cache,
    messages::data::{
        RequestBars, RequestBookSnapshot, RequestCustomData, RequestInstrument, RequestInstruments,
        RequestQuotes, RequestTrades, SubscribeBars, SubscribeBookDeltas, SubscribeBookDepth10,
        SubscribeBookSnapshots, SubscribeCustomData, SubscribeIndexPrices, SubscribeInstrument,
        SubscribeInstrumentClose, SubscribeInstrumentStatus, SubscribeInstruments,
        SubscribeMarkPrices, SubscribeQuotes, SubscribeTrades, UnsubscribeBars,
        UnsubscribeBookDeltas, UnsubscribeBookDepth10, UnsubscribeBookSnapshots,
        UnsubscribeCustomData, UnsubscribeIndexPrices, UnsubscribeInstrument,
        UnsubscribeInstrumentClose, UnsubscribeInstrumentStatus, UnsubscribeInstruments,
        UnsubscribeMarkPrices, UnsubscribeQuotes, UnsubscribeTrades,
    },
};
use nautilus_data::client::DataClient;
use nautilus_model::identifiers::{ClientId, Venue};

#[derive(Debug)]
/// Data client implementation for backtesting market data operations.
///
/// The `BacktestDataClient` provides a data client interface specifically designed
/// for backtesting environments. It handles market data subscriptions and requests
/// during backtesting, coordinating with the backtesting engine to provide
/// historical data replay functionality.
pub struct BacktestDataClient {
    pub client_id: ClientId,
    pub venue: Venue,
    cache: Rc<RefCell<Cache>>,
}

impl BacktestDataClient {
    pub const fn new(client_id: ClientId, venue: Venue, cache: Rc<RefCell<Cache>>) -> Self {
        Self {
            client_id,
            venue,
            cache,
        }
    }
}

#[async_trait::async_trait]
impl DataClient for BacktestDataClient {
    fn client_id(&self) -> ClientId {
        self.client_id
    }

    fn venue(&self) -> Option<Venue> {
        Some(self.venue)
    }

    fn start(&mut self) -> anyhow::Result<()> {
        Ok(())
    }

    fn stop(&mut self) -> anyhow::Result<()> {
        Ok(())
    }

    fn reset(&mut self) -> anyhow::Result<()> {
        Ok(())
    }

    fn dispose(&mut self) -> anyhow::Result<()> {
        Ok(())
    }

    async fn connect(&mut self) -> anyhow::Result<()> {
        Ok(())
    }

    async fn disconnect(&mut self) -> anyhow::Result<()> {
        Ok(())
    }

    fn is_connected(&self) -> bool {
        true
    }

    fn is_disconnected(&self) -> bool {
        false
    }

    // -- COMMAND HANDLERS ---------------------------------------------------------------------------

    fn subscribe(&mut self, _cmd: &SubscribeCustomData) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_instruments(&mut self, _cmd: &SubscribeInstruments) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_instrument(&mut self, _cmd: &SubscribeInstrument) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_book_deltas(&mut self, _cmd: &SubscribeBookDeltas) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_book_depth10(&mut self, _cmd: &SubscribeBookDepth10) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_book_snapshots(&mut self, _cmd: &SubscribeBookSnapshots) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_quotes(&mut self, _cmd: &SubscribeQuotes) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_trades(&mut self, _cmd: &SubscribeTrades) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_bars(&mut self, _cmd: &SubscribeBars) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_mark_prices(&mut self, _cmd: &SubscribeMarkPrices) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_index_prices(&mut self, _cmd: &SubscribeIndexPrices) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_instrument_status(
        &mut self,
        _cmd: &SubscribeInstrumentStatus,
    ) -> anyhow::Result<()> {
        Ok(())
    }

    fn subscribe_instrument_close(
        &mut self,
        _cmd: &SubscribeInstrumentClose,
    ) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe(&mut self, _cmd: &UnsubscribeCustomData) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_instruments(&mut self, _cmd: &UnsubscribeInstruments) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_instrument(&mut self, _cmd: &UnsubscribeInstrument) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_book_deltas(&mut self, _cmd: &UnsubscribeBookDeltas) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_book_depth10(&mut self, _cmd: &UnsubscribeBookDepth10) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_book_snapshots(
        &mut self,
        _cmd: &UnsubscribeBookSnapshots,
    ) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_quotes(&mut self, _cmd: &UnsubscribeQuotes) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_trades(&mut self, _cmd: &UnsubscribeTrades) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_bars(&mut self, _cmd: &UnsubscribeBars) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_mark_prices(&mut self, _cmd: &UnsubscribeMarkPrices) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_index_prices(&mut self, _cmd: &UnsubscribeIndexPrices) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_instrument_status(
        &mut self,
        _cmd: &UnsubscribeInstrumentStatus,
    ) -> anyhow::Result<()> {
        Ok(())
    }

    fn unsubscribe_instrument_close(
        &mut self,
        _cmd: &UnsubscribeInstrumentClose,
    ) -> anyhow::Result<()> {
        Ok(())
    }

    // -- DATA REQUEST HANDLERS ---------------------------------------------------------------------------

    fn request_data(&self, request: &RequestCustomData) -> anyhow::Result<()> {
        todo!()
    }

    fn request_instruments(&self, request: &RequestInstruments) -> anyhow::Result<()> {
        todo!()
    }

    fn request_instrument(&self, request: &RequestInstrument) -> anyhow::Result<()> {
        todo!()
    }

    fn request_book_snapshot(&self, request: &RequestBookSnapshot) -> anyhow::Result<()> {
        todo!()
    }

    fn request_quotes(&self, request: &RequestQuotes) -> anyhow::Result<()> {
        todo!()
    }

    fn request_trades(&self, request: &RequestTrades) -> anyhow::Result<()> {
        todo!()
    }

    fn request_bars(&self, request: &RequestBars) -> anyhow::Result<()> {
        todo!()
    }
}

// SAFETY: Cannot be sent across thread boundaries
#[allow(unsafe_code)]
unsafe impl Send for BacktestDataClient {}
#[allow(unsafe_code)]
unsafe impl Sync for BacktestDataClient {}
```


---

## Overview

This file is located at `crates/backtest/src/data_client.rs` within the repository.

**Classes defined:** BacktestDataClient, BacktestDataClient, DataClient, Send, Sync

**Functions defined:** new, client_id, venue, start, stop, reset, dispose, connect, disconnect, is_connected and 34 more


---

## Detailed Analysis

### Classes

#### `BacktestDataClient`

**Type:** struct


#### `BacktestDataClient`

**Type:** impl


#### `DataClient`

**Type:** impl


#### `Send`

**Type:** impl


#### `Sync`

**Type:** impl


### Functions

#### `new(client_id: ClientId, venue: Venue, cache: Rc<RefCell<Cache>>)`


#### `client_id(&self)`


#### `venue(&self)`


#### `start(&mut self)`


#### `stop(&mut self)`


#### `reset(&mut self)`


#### `dispose(&mut self)`


#### `connect(&mut self)`


#### `disconnect(&mut self)`


#### `is_connected(&self)`


#### `is_disconnected(&self)`


#### `subscribe(&mut self, _cmd: &SubscribeCustomData)`


#### `subscribe_instruments(&mut self, _cmd: &SubscribeInstruments)`


#### `subscribe_instrument(&mut self, _cmd: &SubscribeInstrument)`


#### `subscribe_book_deltas(&mut self, _cmd: &SubscribeBookDeltas)`


#### `subscribe_book_depth10(&mut self, _cmd: &SubscribeBookDepth10)`


#### `subscribe_book_snapshots(&mut self, _cmd: &SubscribeBookSnapshots)`


#### `subscribe_quotes(&mut self, _cmd: &SubscribeQuotes)`


#### `subscribe_trades(&mut self, _cmd: &SubscribeTrades)`


#### `subscribe_bars(&mut self, _cmd: &SubscribeBars)`


#### `subscribe_mark_prices(&mut self, _cmd: &SubscribeMarkPrices)`


#### `subscribe_index_prices(&mut self, _cmd: &SubscribeIndexPrices)`


#### `subscribe_instrument_status(
        &mut self,
        _cmd: &SubscribeInstrumentStatus,
    )`


#### `subscribe_instrument_close(
        &mut self,
        _cmd: &SubscribeInstrumentClose,
    )`


#### `unsubscribe(&mut self, _cmd: &UnsubscribeCustomData)`


#### `unsubscribe_instruments(&mut self, _cmd: &UnsubscribeInstruments)`


#### `unsubscribe_instrument(&mut self, _cmd: &UnsubscribeInstrument)`


#### `unsubscribe_book_deltas(&mut self, _cmd: &UnsubscribeBookDeltas)`


#### `unsubscribe_book_depth10(&mut self, _cmd: &UnsubscribeBookDepth10)`


#### `unsubscribe_book_snapshots(
        &mut self,
        _cmd: &UnsubscribeBookSnapshots,
    )`


#### `unsubscribe_quotes(&mut self, _cmd: &UnsubscribeQuotes)`


#### `unsubscribe_trades(&mut self, _cmd: &UnsubscribeTrades)`


#### `unsubscribe_bars(&mut self, _cmd: &UnsubscribeBars)`


#### `unsubscribe_mark_prices(&mut self, _cmd: &UnsubscribeMarkPrices)`


#### `unsubscribe_index_prices(&mut self, _cmd: &UnsubscribeIndexPrices)`


#### `unsubscribe_instrument_status(
        &mut self,
        _cmd: &UnsubscribeInstrumentStatus,
    )`


#### `unsubscribe_instrument_close(
        &mut self,
        _cmd: &UnsubscribeInstrumentClose,
    )`


#### `request_data(&self, request: &RequestCustomData)`


#### `request_instruments(&self, request: &RequestInstruments)`


#### `request_instrument(&self, request: &RequestInstrument)`


#### `request_book_snapshot(&self, request: &RequestBookSnapshot)`


#### `request_quotes(&self, request: &RequestQuotes)`


#### `request_trades(&self, request: &RequestTrades)`


#### `request_bars(&self, request: &RequestBars)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/backtest/src`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


