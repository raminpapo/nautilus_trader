# Documentation: `crates/adapters/bitmex/src/websocket/error.rs`
**Generated:** 2025-11-15T19:40:00.380956Z
**File Size:** 4396 bytes
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

- **Path:** `crates/adapters/bitmex/src/websocket/error.rs`
- **Size:** 4,396 bytes
- **Lines:** 117
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 5

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

//! Error definitions for the BitMEX WebSocket client.

use thiserror::Error;
use tokio_tungstenite::tungstenite;

/// A typed error enumeration for the BitMEX WebSocket client.
#[derive(Debug, Error)]
pub enum BitmexWsError {
    /// Parsing error.
    #[error("Parsing error: {0}")]
    ParsingError(String),
    /// Errors returned directly by BitMEX (non-zero code).
    #[error("BitMEX error {error_name}: {message}")]
    BitmexError { error_name: String, message: String },
    /// Failure during JSON serialization/deserialization.
    #[error("JSON error: {0}")]
    JsonError(String),
    /// Client error.
    #[error("Client error: {0}")]
    ClientError(String),
    /// Authentication error.
    #[error("Authentication error: {0}")]
    AuthenticationError(String),
    /// Subscription error.
    #[error("Subscription error: {0}")]
    SubscriptionError(String),
    /// WebSocket transport error.
    #[error("Tungstenite error: {0}")]
    TungsteniteError(#[from] tungstenite::Error),
    /// Missing credentials for authenticated operation.
    #[error("Missing credentials: API authentication required for this operation")]
    MissingCredentials,
}

impl From<serde_json::Error> for BitmexWsError {
    fn from(error: serde_json::Error) -> Self {
        Self::JsonError(error.to_string())
    }
}

impl From<String> for BitmexWsError {
    fn from(msg: String) -> Self {
        Self::AuthenticationError(msg)
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_bitmex_ws_error_display() {
        let error = BitmexWsError::ParsingError("Invalid message format".to_string());
        assert_eq!(error.to_string(), "Parsing error: Invalid message format");

        let error = BitmexWsError::BitmexError {
            error_name: "InvalidTopic".to_string(),
            message: "Unknown subscription topic".to_string(),
        };
        assert_eq!(
            error.to_string(),
            "BitMEX error InvalidTopic: Unknown subscription topic"
        );

        let error = BitmexWsError::ClientError("Connection lost".to_string());
        assert_eq!(error.to_string(), "Client error: Connection lost");

        let error = BitmexWsError::AuthenticationError("Invalid API key".to_string());
        assert_eq!(error.to_string(), "Authentication error: Invalid API key");

        let error = BitmexWsError::SubscriptionError("Topic not available".to_string());
        assert_eq!(error.to_string(), "Subscription error: Topic not available");

        let error = BitmexWsError::MissingCredentials;
        assert_eq!(
            error.to_string(),
            "Missing credentials: API authentication required for this operation"
        );
    }

    #[rstest]
    fn test_bitmex_ws_error_from_json_error() {
        let json_err = serde_json::from_str::<serde_json::Value>("invalid json").unwrap_err();
        let ws_error: BitmexWsError = json_err.into();
        assert!(ws_error.to_string().contains("JSON error"));
    }

    #[rstest]
    fn test_bitmex_ws_error_from_tungstenite() {
        use tokio_tungstenite::tungstenite::Error as WsError;

        let tungstenite_err = WsError::ConnectionClosed;
        let ws_error: BitmexWsError = tungstenite_err.into();
        assert!(ws_error.to_string().contains("Tungstenite error"));
    }
}
```


---

## Overview

This file is located at `crates/adapters/bitmex/src/websocket/error.rs` within the repository.

**Classes defined:** From, From

**Functions defined:** from, from, test_bitmex_ws_error_display, test_bitmex_ws_error_from_json_error, test_bitmex_ws_error_from_tungstenite


---

## Detailed Analysis

### Classes

#### `From`

**Type:** impl


#### `From`

**Type:** impl


### Functions

#### `from(error: serde_json::Error)`


#### `from(msg: String)`


#### `test_bitmex_ws_error_display()`


#### `test_bitmex_ws_error_from_json_error()`


#### `test_bitmex_ws_error_from_tungstenite()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: credential, auth. Ensure proper handling of secrets.


