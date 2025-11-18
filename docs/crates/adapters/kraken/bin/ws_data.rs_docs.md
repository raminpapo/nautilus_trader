# Documentation: ws_data.rs

## File Metadata

- **Path**: `crates/adapters/kraken/bin/ws_data.rs`
- **Size**: 2,509 bytes
- **Lines**: 75
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

//! Connects to the Kraken public WebSocket feed and streams market data.
//! Useful when manually validating the Rust WebSocket client implementation.

use futures_util::StreamExt;
use nautilus_kraken::{
    config::KrakenDataClientConfig,
    websocket::{client::KrakenWebSocketClient, enums::KrakenWsChannel},
};
use tokio::{pin, signal};
use tokio_util::sync::CancellationToken;
use tracing::level_filters::LevelFilter;
use ustr::Ustr;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    tracing_subscriber::fmt()
        .with_max_level(LevelFilter::INFO)
        .with_target(false)
        .compact()
        .init();

    let config = KrakenDataClientConfig::default();
    let token = CancellationToken::new();

    let mut client = KrakenWebSocketClient::new(config, token.clone());

    client.connect().await?;

    client
        .subscribe(KrakenWsChannel::Ticker, vec![Ustr::from("BTC/USD")], None)
        .await?;

    client
        .subscribe(KrakenWsChannel::Trade, vec![Ustr::from("BTC/USD")], None)
        .await?;

    let stream = client.stream();
    let shutdown = signal::ctrl_c();
    pin!(stream);
    pin!(shutdown);

    tracing::info!("Streaming Kraken market data; press Ctrl+C to exit");

    loop {
        tokio::select! {
            Some(msg) = stream.next() => {
                tracing::info!("Received: {:#?}", msg);
            }
            _ = &mut shutdown => {
                tracing::info!("Received Ctrl+C, closing connection");
                client.disconnect().await?;
                break;
            }
            else => break,
        }
    }

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

This file is located in `crates/adapters/kraken/bin/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:00.148373Z*
