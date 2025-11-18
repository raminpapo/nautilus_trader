# Documentation: ws_data.rs

## File Metadata

- **Path**: `crates/adapters/dydx/bin/ws_data.rs`
- **Size**: 5,342 bytes
- **Lines**: 140
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

//! Manual verification script for dYdX WebSocket public data streams.
//!
//! Exercises live subscriptions for trades, order book updates, and candles
//! for a single instrument to validate the end-to-end streaming pipeline.
//!
//! Usage:
//! ```bash
//! # Test against testnet (default)
//! cargo run --bin dydx-ws-data -p nautilus-dydx
//!
//! # Override endpoints or instrument
//! DYDX_HTTP_URL=https://indexer.v4testnet.dydx.exchange \
//! DYDX_WS_URL=wss://indexer.v4testnet.dydx.exchange/v4/ws \
//! DYDX_INSTRUMENT_ID=BTC-USD-PERP.DYDX \
//! cargo run --bin dydx-ws-data -p nautilus-dydx
//! ```

use std::time::Duration;

use nautilus_dydx::{
    common::consts::{DYDX_TESTNET_HTTP_URL, DYDX_TESTNET_WS_URL},
    http::client::DydxHttpClient,
    websocket::client::DydxWebSocketClient,
};
use nautilus_model::identifiers::InstrumentId;
use tokio::{pin, signal};
use tracing::level_filters::LevelFilter;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    tracing_subscriber::fmt()
        .with_max_level(LevelFilter::INFO)
        .init();

    // Resolve endpoints from environment, falling back to testnet defaults.
    let http_url =
        std::env::var("DYDX_HTTP_URL").unwrap_or_else(|_| DYDX_TESTNET_HTTP_URL.to_string());
    let ws_url = std::env::var("DYDX_WS_URL").unwrap_or_else(|_| DYDX_TESTNET_WS_URL.to_string());

    // Derive environment label from URLs.
    let is_testnet = http_url.contains("testnet") || ws_url.contains("testnet");

    tracing::info!("Connecting to dYdX HTTP API: {http_url}");
    tracing::info!("Connecting to dYdX WebSocket: {ws_url}");
    tracing::info!(
        "Environment: {}",
        if is_testnet { "TESTNET" } else { "MAINNET" }
    );

    // Create HTTP client and fetch instruments so the WebSocket client can
    // decode incoming market data using the shared instrument definitions.
    let http_client = DydxHttpClient::new(Some(http_url), Some(30), None, is_testnet, None)?;
    let instruments = http_client.request_instruments(None, None, None).await?;

    tracing::info!("Fetched {} instruments from HTTP", instruments.len());

    // Resolve instrument ID from env or use BTC-USD perpetual by default.
    let instrument_id = std::env::var("DYDX_INSTRUMENT_ID").map_or_else(
        |_| InstrumentId::from("BTC-USD-PERP.DYDX"),
        InstrumentId::from,
    );

    tracing::info!("Using instrument: {instrument_id}");

    // Initialize WebSocket client and cache instruments before connecting.
    let mut ws_client = DydxWebSocketClient::new_public(ws_url, Some(30));
    ws_client.cache_instruments(instruments);

    ws_client.connect().await?;
    tracing::info!("WebSocket connected");

    // Give the connection a brief moment to fully establish.
    tokio::time::sleep(Duration::from_millis(500)).await;

    // Subscribe to core public channels for the chosen instrument.
    tracing::info!("Subscribing to trades for {instrument_id}");
    ws_client.subscribe_trades(instrument_id).await?;

    tracing::info!("Subscribing to orderbook for {instrument_id}");
    ws_client.subscribe_orderbook(instrument_id).await?;

    tracing::info!("Subscribing to 1-minute candles for {instrument_id}");
    ws_client.subscribe_candles(instrument_id, "1MIN").await?;

    // Take ownership of the typed message stream.
    let Some(mut rx) = ws_client.take_receiver() else {
        tracing::warn!("No inbound WebSocket receiver available; exiting");
        return Ok(());
    };

    // Create a future that completes on CTRL+C.
    let sigint = signal::ctrl_c();
    pin!(sigint);

    let mut message_count: u64 = 0;

    tracing::info!("Streaming messages (CTRL+C to exit)...");

    loop {
        tokio::select! {
            _ = &mut sigint => {
                tracing::info!("Received SIGINT, closing connection...");
                ws_client.disconnect().await?;
                break;
            }
            maybe_msg = rx.recv() => {
                match maybe_msg {
                    Some(msg) => {
                        message_count += 1;
                        tracing::info!("Message #{message_count}: {msg:?}");
                    }
                    None => {
                        tracing::info!("WebSocket message stream closed");
                        break;
                    }
                }
            }
        }
    }

    tracing::info!("Received {message_count} total messages");

    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`main()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `main`

## Related Files

This file is located in `crates/adapters/dydx/bin/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.772797Z*
