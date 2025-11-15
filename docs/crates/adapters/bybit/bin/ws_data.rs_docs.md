# Documentation: `crates/adapters/bybit/bin/ws_data.rs`
**Generated:** 2025-11-15T19:40:00.602450Z
**File Size:** 7428 bytes
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

- **Path:** `crates/adapters/bybit/bin/ws_data.rs`
- **Size:** 7,428 bytes
- **Lines:** 158
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

//! Connects to the Bybit public WebSocket feed and streams specified market data topics.
//! Useful when manually validating the Rust WebSocket client implementation.

use std::error::Error;

use futures_util::StreamExt;
use nautilus_bybit::{
    common::enums::{BybitEnvironment, BybitProductType},
    websocket::{client::BybitWebSocketClient, messages::NautilusWsMessage},
};
use tokio::{pin, signal};
use tracing::level_filters::LevelFilter;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    tracing_subscriber::fmt()
        .with_max_level(LevelFilter::INFO)
        .with_target(false)
        .compact()
        .init();

    let mut client = BybitWebSocketClient::new_public_with(
        BybitProductType::Linear,
        BybitEnvironment::Mainnet,
        None,
        None,
    );
    client.connect().await?;

    client
        .subscribe(vec![
            "orderbook.1.BTCUSDT".to_string(),
            "publicTrade.BTCUSDT".to_string(),
            "tickers.BTCUSDT".to_string(),
        ])
        .await?;

    let stream = client.stream();
    let shutdown = signal::ctrl_c();
    pin!(stream);
    pin!(shutdown);

    tracing::info!("Streaming Bybit market data; press Ctrl+C to exit");

    loop {
        tokio::select! {
            Some(event) = stream.next() => {
                match event {
                    NautilusWsMessage::Data(data_vec) => {
                        tracing::info!(count = data_vec.len(), "data update");
                        for data in data_vec {
                            match data {
                                nautilus_model::data::Data::Trade(tick) => {
                                    tracing::info!(instrument = %tick.instrument_id, price = %tick.price, size = %tick.size, "trade");
                                }
                                nautilus_model::data::Data::Quote(quote) => {
                                    tracing::info!(instrument = %quote.instrument_id, bid = %quote.bid_price, ask = %quote.ask_price, "quote");
                                }
                                nautilus_model::data::Data::Bar(bar) => {
                                    tracing::info!(bar_type = %bar.bar_type, close = %bar.close, "bar");
                                }
                                _ => {
                                    tracing::debug!("other data type");
                                }
                            }
                        }
                    }
                    NautilusWsMessage::Deltas(deltas) => {
                        tracing::info!(instrument = %deltas.instrument_id, sequence = deltas.sequence, "orderbook deltas");
                    }
                    NautilusWsMessage::FundingRates(rates) => {
                        tracing::info!(count = rates.len(), "funding rate updates");
                        for rate in rates {
                            tracing::info!(
                                instrument = %rate.instrument_id,
                                rate = %rate.rate,
                                next_funding = ?rate.next_funding_ns,
                                "funding rate"
                            );
                        }
                    }
                    NautilusWsMessage::OrderStatusReports(reports) => {
                        tracing::info!(count = reports.len(), "order status reports");
                        for report in reports {
                            tracing::info!(
                                instrument = %report.instrument_id,
                                client_order_id = ?report.client_order_id,
                                venue_order_id = ?report.venue_order_id,
                                status = ?report.order_status,
                                "order status report"
                            );
                        }
                    }
                    NautilusWsMessage::FillReports(reports) => {
                        tracing::info!(count = reports.len(), "fill reports");
                        for report in reports {
                            tracing::info!(
                                instrument = %report.instrument_id,
                                client_order_id = ?report.client_order_id,
                                venue_order_id = ?report.venue_order_id,
                                last_qty = %report.last_qty,
                                last_px = %report.last_px,
                                "fill report"
                            );
                        }
                    }
                    NautilusWsMessage::PositionStatusReport(report) => {
                        tracing::info!(instrument = %report.instrument_id, quantity = %report.quantity, "position status report");
                    }
                    NautilusWsMessage::AccountState(state) => {
                        tracing::info!(account_id = %state.account_id, balances = state.balances.len(), "account state");
                    }
                    NautilusWsMessage::OrderRejected(event) => {
                        tracing::warn!(trader_id = %event.trader_id, client_order_id = %event.client_order_id, reason = %event.reason, "order rejected");
                    }
                    NautilusWsMessage::OrderCancelRejected(event) => {
                        tracing::warn!(trader_id = %event.trader_id, client_order_id = %event.client_order_id, reason = %event.reason, "order cancel rejected");
                    }
                    NautilusWsMessage::OrderModifyRejected(event) => {
                        tracing::warn!(trader_id = %event.trader_id, client_order_id = %event.client_order_id, reason = %event.reason, "order modify rejected");
                    }
                    NautilusWsMessage::Error(err) => {
                        tracing::error!(code = err.code, message = %err.message, "websocket error");
                    }
                    NautilusWsMessage::Reconnected => {
                        tracing::warn!("WebSocket reconnected");
                    }
                    NautilusWsMessage::Authenticated => {
                        tracing::info!("Authenticated successfully");
                    }
                }
            }
            _ = &mut shutdown => {
                tracing::info!("Received Ctrl+C, closing connection");
                client.close().await?;
                break;
            }
            else => break,
        }
    }

    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/bybit/bin/ws_data.rs` within the repository.

**Functions defined:** main


---

## Detailed Analysis

### Functions

#### `main()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/bin`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


