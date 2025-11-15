# Documentation: `crates/adapters/okx/src/websocket/error.rs`
**Generated:** 2025-11-15T19:40:01.329871Z
**File Size:** 2162 bytes
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

- **Path:** `crates/adapters/okx/src/websocket/error.rs`
- **Size:** 2,162 bytes
- **Lines:** 54
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 2

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

//! Error types produced by the OKX WebSocket client implementation.

use thiserror::Error;
use tokio_tungstenite::tungstenite;

/// A typed error enumeration for the OKX WebSocket client.
#[derive(Debug, Clone, Error)]
pub enum OKXWsError {
    #[error("Parsing error: {0}")]
    ParsingError(String),
    /// Errors returned directly by OKX (non-zero code).
    #[error("OKX error {error_code}: {message}")]
    OkxError { error_code: String, message: String },
    /// Failure during JSON serialization/deserialization.
    #[error("JSON error: {0}")]
    JsonError(String),
    #[error("Client error: {0}")]
    ClientError(String),
    #[error("Authentication error: {0}")]
    AuthenticationError(String),
    /// Wrapping the underlying HttpClientError from the network crate.
    // #[error("Network error: {0}")]
    // WebSocketClientError(WebSocketClientError),  // TODO: Implement Debug
    /// WebSocket transport error.
    #[error("Tungstenite error: {0}")]
    TungsteniteError(String),
}

impl From<tungstenite::Error> for OKXWsError {
    fn from(error: tungstenite::Error) -> Self {
        Self::TungsteniteError(error.to_string())
    }
}

impl From<String> for OKXWsError {
    fn from(msg: String) -> Self {
        Self::AuthenticationError(msg)
    }
}
```


---

## Overview

This file is located at `crates/adapters/okx/src/websocket/error.rs` within the repository.

**Classes defined:** From, From

**Functions defined:** from, from


---

## Detailed Analysis

### Classes

#### `From`

**Type:** impl


#### `From`

**Type:** impl


### Functions

#### `from(error: tungstenite::Error)`


#### `from(msg: String)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


