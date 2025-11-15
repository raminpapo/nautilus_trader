# Documentation: `crates/adapters/okx/bin/ws_data.rs`
**Generated:** 2025-11-15T19:40:01.213867Z
**File Size:** 3440 bytes
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

- **Path:** `crates/adapters/okx/bin/ws_data.rs`
- **Size:** 3,440 bytes
- **Lines:** 95
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

use futures_util::StreamExt;
use nautilus_model::identifiers::InstrumentId;
use nautilus_okx::{
    common::enums::OKXInstrumentType, http::client::OKXHttpClient, websocket::OKXWebSocketClient,
};
use tokio::{pin, signal};
use tracing::level_filters::LevelFilter;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    tracing_subscriber::fmt()
        .with_max_level(LevelFilter::TRACE)
        .init();

    let http_client = OKXHttpClient::from_env().unwrap();
    let instruments = http_client
        .request_instruments(OKXInstrumentType::Swap, None)
        .await?;

    let mut ws_client = OKXWebSocketClient::from_env().unwrap();
    ws_client.cache_instruments(instruments.clone());
    ws_client.connect().await?;

    let instrument_id = InstrumentId::from("BTC-USD-SWAP.OKX");

    // let mut client_business = OKXWebSocketClient::new(
    //     Some(OKX_WS_BUSINESS_URL),
    //     None,     // No API key for public feeds
    //     None,     // No API secret
    //     None,     // No API passphrase
    //     Some(10), // 10 second heartbeat
    // )
    // .unwrap();

    // client_business.connect_data(instruments).await?;
    // let bar_type = BarType::new(
    //     instrument_id,
    //     BAR_SPEC_1_MINUTE,
    //     AggregationSource::External,
    // );
    // client_business.subscribe_bars(bar_type).await?;

    ws_client
        .subscribe_instruments(OKXInstrumentType::Swap)
        .await?;
    // client.subscribe_tickers(instrument_id).await?;
    // client.subscribe_trades(instrument_id, true).await?;
    ws_client.subscribe_book(instrument_id).await?;
    // client.subscribe_quotes(instrument_id).await?;

    // tokio::time::sleep(Duration::from_secs(1)).await;

    // client.subscribe_book(instrument_id).await?;
    // client.subscribe_book_depth5(instrument_id).await?;
    // client.subscribe_quotes(instrument_id).await?;
    // client.subscribe_trades(instrument_id).await?;

    // Create a future that completes on CTRL+C
    let sigint = signal::ctrl_c();
    pin!(sigint);

    let stream = ws_client.stream();
    tokio::pin!(stream); // Pin the stream to allow polling in the loop

    loop {
        tokio::select! {
            Some(data) = stream.next() => {
                tracing::debug!("{data:?}");
            }
            _ = &mut sigint => {
                tracing::info!("Received SIGINT, closing connection...");
                ws_client.close().await?;
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

This file is located at `crates/adapters/okx/bin/ws_data.rs` within the repository.

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

**Directory:** `crates/adapters/okx/bin`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: secret. Ensure proper handling of secrets.


