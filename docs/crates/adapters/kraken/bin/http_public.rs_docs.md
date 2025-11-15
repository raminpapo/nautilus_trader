# Documentation: `crates/adapters/kraken/bin/http_public.rs`
**Generated:** 2025-11-15T19:40:01.118188Z
**File Size:** 1529 bytes
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

- **Path:** `crates/adapters/kraken/bin/http_public.rs`
- **Size:** 1,529 bytes
- **Lines:** 35
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

use nautilus_kraken::http::client::KrakenHttpClient;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    tracing::subscriber::set_global_default(
        tracing_subscriber::fmt()
            .with_max_level(tracing::Level::INFO)
            .finish(),
    )?;

    tracing::info!("Kraken HTTP client example (public data methods)");

    let _client = KrakenHttpClient::default();

    tracing::info!("Client created successfully");
    tracing::info!("TODO: Implement request_instruments, request_bars, request_trades methods");
    tracing::info!("These methods will parse Kraken responses into Nautilus domain types");

    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/kraken/bin/http_public.rs` within the repository.

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

**Directory:** `crates/adapters/kraken/bin`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


