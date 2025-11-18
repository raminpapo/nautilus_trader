# Documentation: http_private.rs

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/bin/http_private.rs`
- **Size**: 2,445 bytes
- **Lines**: 59
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

use nautilus_coinbase_intx::http::client::CoinbaseIntxHttpClient;
use nautilus_core::env::get_env_var;
use nautilus_model::identifiers::{AccountId, Symbol};
use tracing::level_filters::LevelFilter;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    tracing_subscriber::fmt()
        .with_max_level(LevelFilter::TRACE)
        .init();

    let mut client = CoinbaseIntxHttpClient::from_env().unwrap();

    // The direct Coinbase REST API can be accessed through the inner client,
    // these methods are prefixed with "http_" for clarity that a HTTP request is
    // about to be initiated, as well as avoiding naming conflicts with API endpoints
    // vs the method names which Nautilus needs ("cancel_order", etc).
    // match client.inner.http_list_fee_rate_tiers().await {
    //     Ok(resp) => {
    //         tracing::info!("Received {resp:?}");
    //     }
    //     Err(e) => tracing::error!("{e:?}"),
    // }

    let symbol = Symbol::from("BTC-PERP");
    let instrument = client.request_instrument(&symbol).await?;
    client.add_instrument(instrument);

    // Otherwise, the client can return Nautilus domain objects
    let portfolio_id = get_env_var("COINBASE_INTX_PORTFOLIO_ID")?;
    let account_id = AccountId::from(format!("COINBASE_INTX-{portfolio_id}"));
    let reports = client
        .request_order_status_reports(account_id, symbol)
        .await?;

    tracing::info!("Received {} reports", reports.len());

    for report in reports {
        tracing::info!("{report:?}");
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

This file is located in `crates/adapters/coinbase_intx/bin/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.563224Z*
