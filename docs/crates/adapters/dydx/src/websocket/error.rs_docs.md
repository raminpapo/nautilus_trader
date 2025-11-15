# Documentation: `crates/adapters/dydx/src/websocket/error.rs`
**Generated:** 2025-11-15T19:40:00.964280Z
**File Size:** 4698 bytes
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

- **Path:** `crates/adapters/dydx/src/websocket/error.rs`
- **Size:** 4,698 bytes
- **Lines:** 151
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 8
- **Functions:** 7

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

//! Error types for dYdX WebSocket operations.

use std::fmt::{self, Display};

use nautilus_network::error::SendError;
use serde::{Deserialize, Serialize};
use serde_json::Value;
use thiserror::Error;

use super::enums::DydxWsChannel;
use crate::schemas::ws::DydxWsMessageType;

/// Result type for dYdX WebSocket operations.
pub type DydxWsResult<T> = Result<T, DydxWsError>;

/// Errors that can occur during dYdX WebSocket operations.
#[derive(Debug, Error)]
pub enum DydxWsError {
    /// WebSocket client is not connected.
    #[error("WebSocket client not connected")]
    NotConnected,

    /// Failed to send a message over the WebSocket connection.
    #[error("WebSocket send error: {0}")]
    Send(String),

    /// Underlying transport error from the WebSocket implementation.
    #[error("WebSocket transport error: {0}")]
    Transport(String),

    /// Error during JSON serialization/deserialization.
    #[error("JSON error: {0}")]
    Json(String),

    /// Failed to parse venue message.
    #[error("Failed to parse message: {0}")]
    Parse(String),

    /// Authentication failed.
    #[error("Authentication error: {0}")]
    Authentication(String),

    /// Generic client error.
    #[error("Client error: {0}")]
    ClientError(String),

    /// Subscription operation failed.
    #[error("Subscription error: {0}")]
    Subscription(String),

    /// Error from the dYdX venue.
    #[error("dYdX error: {0}")]
    Venue(#[from] DydxWebSocketError),
}

impl From<SendError> for DydxWsError {
    fn from(error: SendError) -> Self {
        Self::Send(error.to_string())
    }
}

impl From<tokio_tungstenite::tungstenite::Error> for DydxWsError {
    fn from(error: tokio_tungstenite::tungstenite::Error) -> Self {
        Self::Transport(error.to_string())
    }
}

impl From<serde_json::Error> for DydxWsError {
    fn from(error: serde_json::Error) -> Self {
        Self::Json(error.to_string())
    }
}

impl From<anyhow::Error> for DydxWsError {
    fn from(e: anyhow::Error) -> Self {
        Self::ClientError(e.to_string())
    }
}

/// Error message received from the dYdX WebSocket API.
///
/// # References
///
/// <https://docs.dydx.trade/developers/indexer/websockets>
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxWebSocketError {
    /// The type field (typically "error").
    #[serde(rename = "type")]
    pub msg_type: DydxWsMessageType,
    /// The error message from the venue.
    pub message: String,
    /// The connection ID.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub connection_id: Option<String>,
    /// The message ID.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub message_id: Option<u64>,
    /// The channel name.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub channel: Option<DydxWsChannel>,
    /// The channel-specific ID.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
}

impl DydxWebSocketError {
    /// Creates a new [`DydxWebSocketError`] from a message.
    #[must_use]
    pub fn from_message(message: String) -> Self {
        Self {
            msg_type: DydxWsMessageType::Error,
            message,
            connection_id: None,
            message_id: None,
            channel: None,
            id: None,
        }
    }

    /// Creates a new [`DydxWebSocketError`] from a raw JSON value.
    pub fn from_value(value: &Value) -> Option<Self> {
        serde_json::from_value(value.clone()).ok()
    }
}

impl Display for DydxWebSocketError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{} (channel: {:?}, id: {:?})",
            self.message, self.channel, self.id
        )
    }
}

impl std::error::Error for DydxWebSocketError {}
```


---

## Overview

This file is located at `crates/adapters/dydx/src/websocket/error.rs` within the repository.

**Classes defined:** DydxWebSocketError, From, From, From, From, DydxWebSocketError, Display, std

**Functions defined:** from, from, from, from, from_message, from_value, fmt


---

## Detailed Analysis

### Classes

#### `DydxWebSocketError`

**Type:** struct


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


#### `DydxWebSocketError`

**Type:** impl


#### `Display`

**Type:** impl


#### `std`

**Type:** impl


### Functions

#### `from(error: SendError)`


#### `from(error: tokio_tungstenite::tungstenite::Error)`


#### `from(error: serde_json::Error)`


#### `from(e: anyhow::Error)`


#### `from_message(message: String)`


#### `from_value(value: &Value)`


#### `fmt(&self, f: &mut fmt::Formatter<'_>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


