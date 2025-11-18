# Documentation: sandbox.rs

## File Metadata

- **Path**: `crates/adapters/databento/bin/sandbox.rs`
- **Size**: 2,206 bytes
- **Lines**: 68
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

use std::env;

use databento::{
    LiveClient,
    dbn::{Dataset::GlbxMdp3, MboMsg, SType, Schema, TradeMsg},
    live::Subscription,
};
use nautilus_core::consts::NAUTILUS_USER_AGENT;
use time::OffsetDateTime;

#[tokio::main]
async fn main() {
    let mut client = LiveClient::builder()
        .user_agent_extension(NAUTILUS_USER_AGENT.into())
        .key(env::var("DATABENTO_API_KEY").unwrap())
        .unwrap()
        .dataset(GlbxMdp3)
        .build()
        .await
        .unwrap();

    client
        .subscribe(
            Subscription::builder()
                .schema(Schema::Mbo)
                .stype_in(SType::RawSymbol)
                .symbols("ESM4")
                .start(OffsetDateTime::from_unix_timestamp_nanos(0).unwrap())
                .build(),
        )
        .await
        .unwrap();

    client.start().await.unwrap();

    let mut count = 0;

    while let Some(record) = client.next_record().await.unwrap() {
        if let Some(msg) = record.get::<TradeMsg>() {
            println!("{msg:#?}");
        }
        if let Some(msg) = record.get::<MboMsg>() {
            println!(
                "Received delta: {} {} flags={}",
                count,
                msg.hd.ts_event,
                msg.flags.raw(),
            );
            count += 1;
        }
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

This file is located in `crates/adapters/databento/bin/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.675854Z*
