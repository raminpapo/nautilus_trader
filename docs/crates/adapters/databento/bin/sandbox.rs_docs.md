# Documentation: `crates/adapters/databento/bin/sandbox.rs`
**Generated:** 2025-11-15T19:40:00.841963Z
**File Size:** 2206 bytes
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

- **Path:** `crates/adapters/databento/bin/sandbox.rs`
- **Size:** 2,206 bytes
- **Lines:** 67
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


---

## Overview

This file is located at `crates/adapters/databento/bin/sandbox.rs` within the repository.

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

**Directory:** `crates/adapters/databento/bin`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: api_key. Ensure proper handling of secrets.


