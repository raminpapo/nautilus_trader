# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/dydx/src/error.rs`
- **Size**: 2,805 bytes
- **Lines**: 89
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

//! Error handling for the dYdX adapter.
//!
//! This module provides error types for all dYdX operations, including
//! HTTP, WebSocket, and gRPC errors.

use thiserror::Error;

/// Result type for dYdX operations.
pub type DydxResult<T> = Result<T, DydxError>;

/// The main error type for all dYdX adapter operations.
#[derive(Debug, Error)]
pub enum DydxError {
    /// HTTP client errors.
    #[error("HTTP error: {0}")]
    Http(String),

    /// WebSocket connection errors.
    #[error("WebSocket error: {0}")]
    WebSocket(String),

    /// gRPC errors from Cosmos SDK node.
    #[error("gRPC error: {0}")]
    Grpc(#[from] tonic::Status),

    /// Transaction signing errors.
    #[error("Signing error: {0}")]
    Signing(String),

    /// Protocol buffer encoding errors.
    #[error("Encoding error: {0}")]
    Encoding(#[from] prost::EncodeError),

    /// Protocol buffer decoding errors.
    #[error("Decoding error: {0}")]
    Decoding(#[from] prost::DecodeError),

    /// JSON serialization/deserialization errors.
    #[error("JSON error: {message}")]
    Json {
        message: String,
        /// The raw JSON that failed to parse, if available.
        raw: Option<String>,
    },

    /// Configuration errors.
    #[error("Configuration error: {0}")]
    Config(String),

    /// Invalid data errors.
    #[error("Invalid data: {0}")]
    InvalidData(String),

    /// Invalid order side error.
    #[error("Invalid order side: {0}")]
    InvalidOrderSide(String),

    /// Unsupported order type error.
    #[error("Unsupported order type: {0}")]
    UnsupportedOrderType(String),

    /// Feature not yet implemented.
    #[error("Not implemented: {0}")]
    NotImplemented(String),

    /// Order construction and submission errors.
    #[error("Order error: {0}")]
    Order(String),

    /// Nautilus core errors.
    #[error("Nautilus error: {0}")]
    Nautilus(#[from] anyhow::Error),
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Enums**: `DydxError`

## Related Files

This file is located in `crates/adapters/dydx/src/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.826702Z*
