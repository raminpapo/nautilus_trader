# Documentation: data_client.rs

## File Metadata

- **Path**: `crates/backtest/src/data_client.rs`
- **Size**: 7,712 bytes
- **Lines**: 263
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 44 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`client_id()`**: Function defined in this file
- **`venue()`**: Function defined in this file
- **`start()`**: Function defined in this file
- **`stop()`**: Function defined in this file
- **`reset()`**: Function defined in this file
- **`dispose()`**: Function defined in this file
- **`connect()`**: Function defined in this file
- **`disconnect()`**: Function defined in this file
- **`is_connected()`**: Function defined in this file
- **`is_disconnected()`**: Function defined in this file
- **`subscribe()`**: Function defined in this file
- **`subscribe_instruments()`**: Function defined in this file
- **`subscribe_instrument()`**: Function defined in this file
- **`subscribe_book_deltas()`**: Function defined in this file
- **`subscribe_book_depth10()`**: Function defined in this file
- **`subscribe_book_snapshots()`**: Function defined in this file
- **`subscribe_quotes()`**: Function defined in this file
- **`subscribe_trades()`**: Function defined in this file
- **`subscribe_bars()`**: Function defined in this file

*...and 24 more functions*

### Classes
- **`BacktestDataClient`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 48


**Functions**: `client_id`, `connect`, `disconnect`, `dispose`, `is_connected`, `is_disconnected`, `new`, `request_bars`, `request_book_snapshot`, `request_data`, `request_instrument`, `request_instruments`, `request_quotes`, `request_trades`, `reset`, `start`, `stop`, `subscribe`, `subscribe_bars`, `subscribe_book_deltas`, `subscribe_book_depth10`, `subscribe_book_snapshots`, `subscribe_index_prices`, `subscribe_instrument`, `subscribe_instrument_close`, `subscribe_instrument_status`, `subscribe_instruments`, `subscribe_mark_prices`, `subscribe_quotes`, `subscribe_trades` *(+14 more)*
**Impls**: `BacktestDataClient`, `DataClient`, `Send`, `Sync`
**Structs**: `BacktestDataClient`

## Related Files

This file is located in `crates/backtest/src/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/backtest/src/data_client.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.896932Z*
