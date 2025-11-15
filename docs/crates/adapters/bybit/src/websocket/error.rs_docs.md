# Documentation: `crates/adapters/bybit/src/websocket/error.rs`
**Generated:** 2025-11-15T19:40:00.683229Z
**File Size:** 2504 bytes
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

- **Path:** `crates/adapters/bybit/src/websocket/error.rs`
- **Size:** 2,504 bytes
- **Lines:** 74
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 4

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

//! Error types for Bybit WebSocket client operations.

use nautilus_network::error::SendError;
use thiserror::Error;

/// Result alias for Bybit WebSocket operations.
pub type BybitWsResult<T> = Result<T, BybitWsError>;

/// Error type for Bybit WebSocket client failures.
#[derive(Clone, Debug, Error)]
pub enum BybitWsError {
    /// The WebSocket client is not currently connected.
    #[error("WebSocket not connected")]
    NotConnected,

    /// Failed to send a message over the WebSocket connection.
    #[error("WebSocket send error: {0}")]
    Send(String),

    /// Underlying transport error from the WebSocket implementation.
    #[error("WebSocket transport error: {0}")]
    Transport(String),

    /// Failed to parse or serialize JSON payloads.
    #[error("JSON error: {0}")]
    Json(String),

    /// Authentication handshake failed or timed out.
    #[error("Authentication error: {0}")]
    Authentication(String),

    /// Client-side validation or logic error.
    #[error("Client error: {0}")]
    ClientError(String),
}

impl From<SendError> for BybitWsError {
    fn from(error: SendError) -> Self {
        Self::Send(error.to_string())
    }
}

impl From<tokio_tungstenite::tungstenite::Error> for BybitWsError {
    fn from(error: tokio_tungstenite::tungstenite::Error) -> Self {
        Self::Transport(error.to_string())
    }
}

impl From<serde_json::Error> for BybitWsError {
    fn from(error: serde_json::Error) -> Self {
        Self::Json(error.to_string())
    }
}

impl From<String> for BybitWsError {
    fn from(msg: String) -> Self {
        Self::Authentication(msg)
    }
}
```


---

## Overview

This file is located at `crates/adapters/bybit/src/websocket/error.rs` within the repository.

**Classes defined:** From, From, From, From

**Functions defined:** from, from, from, from


---

## Detailed Analysis

### Classes

#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


### Functions

#### `from(error: SendError)`


#### `from(error: tokio_tungstenite::tungstenite::Error)`


#### `from(error: serde_json::Error)`


#### `from(msg: String)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


