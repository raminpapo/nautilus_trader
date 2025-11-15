# Documentation: `crates/adapters/coinbase_intx/src/websocket/error.rs`
**Generated:** 2025-11-15T19:40:00.808887Z
**File Size:** 1803 bytes
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

- **Path:** `crates/adapters/coinbase_intx/src/websocket/error.rs`
- **Size:** 1,803 bytes
- **Lines:** 38
- **Extension:** `.rs`
- **Type:** text

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

use thiserror::Error;
use tokio_tungstenite::tungstenite;

/// A typed error enumeration for the Coinbase WebSocket client.
#[derive(Debug, Error)]
pub enum CoinbaseIntxWsError {
    #[error("Parsing error: {0}")]
    ParsingError(String),
    /// Errors returned directly by Coinbase (non-zero code).
    #[error("Coinbase error {code}: {message}")]
    CoinbaseError { code: String, message: String },
    /// Failure during JSON serialization/deserialization.
    #[error("JSON error: {0}")]
    JsonError(String),
    #[error("Client error: {0}")]
    ClientError(String),
    /// Wrapping the underlying `HttpClientError` from the network crate.
    // #[error("Network error: {0}")]
    // WebSocketClientError(WebSocketClientError),  // TODO: Implement Debug
    /// Any unknown HTTP status or unexpected response from Coinbase.
    #[error("Tungstenite error: {0}")]
    TungsteniteError(tungstenite::Error),
}
```


---

## Overview

This file is located at `crates/adapters/coinbase_intx/src/websocket/error.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/coinbase_intx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


