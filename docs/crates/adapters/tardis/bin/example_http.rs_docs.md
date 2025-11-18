# Documentation: example_http.rs

## File Metadata

- **Path**: `crates/adapters/tardis/bin/example_http.rs`
- **Size**: 3,101 bytes
- **Lines**: 92
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`main()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `main`

## Related Files

This file is located in `crates/adapters/tardis/bin/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.641051Z*
