# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/src/websocket/error.rs`
- **Size**: 1,803 bytes
- **Lines**: 39
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Enums**: `CoinbaseIntxWsError`

## Related Files

This file is located in `crates/adapters/coinbase_intx/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.634597Z*
