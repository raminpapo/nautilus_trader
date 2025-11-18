# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/src/http/error.rs`
- **Size**: 3,193 bytes
- **Lines**: 71
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

//! Defines the error structures and enumerations for the Coinbase International integration.
//!
//! This module includes data types for deserializing exchange errors from Coinbase International
//! (`CoinbaseIntxErrorResponse`, `CoinbaseIntxErrorMessage`), as well as a higher-level typed
//! error enum (`CoinbaseIntxHttpError`) that represents the various failure states in
//! the client (e.g., missing credentials, network errors, unexpected status
//! codes, etc.).

use nautilus_network::http::HttpClientError;
use reqwest::StatusCode;
use serde::Deserialize;
use thiserror::Error;

/// Represents the JSON structure of an error response returned by the Coinbase API.
#[derive(Clone, Debug, Deserialize)]
pub struct CoinbaseIntxErrorResponse {
    /// The top-level error object included in the Coinbase error response.
    pub error: CoinbaseIntxErrorMessage,
}

/// Contains the specific error details provided by the Coinbase API.
#[derive(Clone, Debug, Deserialize)]
pub struct CoinbaseIntxErrorMessage {
    /// A human-readable explanation of the error condition.
    pub message: String,
    /// A short identifier or category for the error, as returned by Coinbase.
    pub name: String,
}

#[derive(Deserialize)]
pub(crate) struct ErrorBody {
    pub title: Option<String>,
    pub error: Option<String>,
}

/// A typed error enumeration for the Coinbase HTTP client.
#[derive(Debug, Error)]
pub enum CoinbaseIntxHttpError {
    /// Error variant when credentials are missing but the request is authenticated.
    #[error("Missing credentials for authenticated request")]
    MissingCredentials,
    /// Errors returned directly by Coinbase (non-zero code).
    #[error("{error_code}: {message}")]
    CoinbaseError { error_code: String, message: String },
    /// Failure during URL parameter encoding or JSON serialization/deserialization.
    /// Covers errors from `serde_urlencoded` and `serde_json`.
    #[error("Serialization error: {0}")]
    JsonError(String),
    /// Underlying network or HTTP client error.
    #[error("Network error: {0}")]
    HttpClientError(#[from] HttpClientError),
    /// Any unknown HTTP status or unexpected response from Coinbase.
    #[error("Unexpected HTTP status code {status}: {body}")]
    UnexpectedStatus { status: StatusCode, body: String },
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. 3 class(es).

## Detailed Walkthrough


### Classes
- **`CoinbaseIntxErrorResponse`**: Class defined in this file
- **`CoinbaseIntxErrorMessage`**: Class defined in this file
- **`ErrorBody`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Enums**: `CoinbaseIntxHttpError`
**Structs**: `CoinbaseIntxErrorMessage`, `CoinbaseIntxErrorResponse`, `ErrorBody`

## Related Files

This file is located in `crates/adapters/coinbase_intx/src/http/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.598071Z*
