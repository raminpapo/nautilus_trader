# Documentation: `crates/adapters/tardis/bin/example_http.rs`
**Generated:** 2025-11-15T19:40:01.431421Z
**File Size:** 3101 bytes
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

- **Path:** `crates/adapters/tardis/bin/example_http.rs`
- **Size:** 3,101 bytes
- **Lines:** 91
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

use nautilus_core::UnixNanos;
use nautilus_model::instruments::Instrument;
use nautilus_tardis::{
    enums::TardisExchange,
    http::{client::TardisHttpClient, query::InstrumentFilterBuilder},
};

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::DEBUG)
        .init();

    let client = TardisHttpClient::new(None, None, None, true).unwrap();

    // Tardis instrument definitions
    let resp = client
        .instruments_info(TardisExchange::Binance, None, None)
        .await;
    println!("Received: {resp:?}");

    let start = UnixNanos::from("2020-1-1");
    let filter = InstrumentFilterBuilder::default()
        .available_since(Some(start.into()))
        .build()
        .unwrap();

    let resp = client
        .instruments_info(TardisExchange::Binance, Some("BTCUSDT"), Some(&filter))
        .await;
    println!("Received: {resp:?}");

    let filter = InstrumentFilterBuilder::default()
        .instrument_type(Some(vec!["perpetual".to_string()]))
        .build()
        .unwrap();
    let resp = client
        .instruments_info(TardisExchange::Bitmex, Some("XBTUSD"), Some(&filter))
        .await;

    for inst in resp.unwrap() {
        println!("{inst:?}");
        if let Some(changes) = inst.changes {
            for change in changes {
                println!("Change:");
                println!("{change:?}");
            }
        }
    }

    let effective = UnixNanos::from("2020-08-01");

    // Nautilus instrument definitions
    let resp = client
        .instruments(
            TardisExchange::Bitmex,
            Some("XBTUSD"),
            Some(&filter),
            None,
            None,
            None,
            Some(effective),
            None,
        )
        .await;

    for inst in resp.unwrap() {
        println!("{}", inst.id());
        println!("price_increment={}", inst.price_increment());
        println!("size_increment={}", inst.size_increment());
        println!("multiplier={}", inst.multiplier());
        println!("ts_event={}", inst.ts_event().to_rfc3339());
        println!("ts_init={}", inst.ts_init().to_rfc3339());
        println!("---------------------------");
    }
}
```


---

## Overview

This file is located at `crates/adapters/tardis/bin/example_http.rs` within the repository.

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

**Directory:** `crates/adapters/tardis/bin`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


