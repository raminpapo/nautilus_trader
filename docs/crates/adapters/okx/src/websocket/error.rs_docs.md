# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/okx/src/websocket/error.rs`
- **Size**: 2,162 bytes
- **Lines**: 55
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Enums**: `OKXWsError`
**Functions**: `from`
**Impls**: `From`

## Related Files

This file is located in `crates/adapters/okx/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.463456Z*
