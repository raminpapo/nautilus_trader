# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/dydx/src/http/error.rs`
- **Size**: 5,487 bytes
- **Lines**: 147
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

//! Error structures and enumerations for the dYdX integration.
//!
//! The dYdX v4 Indexer API error responses are typically returned with
//! appropriate HTTP status codes and error messages in the response body.

use serde::Deserialize;
use thiserror::Error;

/// Represents a build error for query parameter validation.
#[derive(Debug, Error)]
pub enum BuildError {
    /// Missing required address parameter.
    #[error("Missing required address parameter")]
    MissingAddress,
    /// Missing required market ticker parameter.
    #[error("Missing required market ticker parameter")]
    MissingTicker,
    /// Missing required subaccount number.
    #[error("Missing required subaccount number")]
    MissingSubaccountNumber,
    /// Both createdBeforeOrAt and createdBeforeOrAtHeight specified.
    #[error("Cannot specify both 'createdBeforeOrAt' and 'createdBeforeOrAtHeight' parameters")]
    BothCreatedBeforeParams,
    /// Both createdOnOrAfter and createdOnOrAfterHeight specified.
    #[error("Cannot specify both 'createdOnOrAfter' and 'createdOnOrAfterHeight' parameters")]
    BothCreatedAfterParams,
    /// Invalid time range.
    #[error("Invalid time range: from_iso must be before to_iso")]
    InvalidTimeRange,
    /// Limit exceeds maximum allowed value.
    #[error("Limit exceeds maximum allowed value")]
    LimitTooHigh,
    /// Invalid resolution parameter.
    #[error("Invalid resolution parameter: {0}")]
    InvalidResolution(String),
}

/// Represents the JSON structure of an error response returned by the dYdX Indexer API.
#[derive(Clone, Debug, Deserialize)]
pub struct DydxErrorResponse {
    /// HTTP status code.
    #[serde(default)]
    pub status: Option<u16>,
    /// Error message describing what went wrong.
    pub message: String,
    /// Additional error details if provided.
    #[serde(default)]
    pub details: Option<String>,
}

/// A typed error enumeration for the dYdX HTTP client.
#[derive(Debug, Error)]
pub enum DydxHttpError {
    /// Errors returned by the dYdX Indexer API with a specific HTTP status.
    #[error("dYdX API error {status}: {message}")]
    HttpStatus { status: u16, message: String },
    /// Failure during JSON serialization.
    #[error("Serialization error: {error}")]
    Serialization { error: String },
    /// Failure during JSON deserialization.
    #[error("Deserialization error: {error}, body: {body}")]
    Deserialization { error: String, body: String },
    /// Parameter validation error.
    #[error("Parameter validation error: {0}")]
    ValidationError(String),
    /// Request was canceled, typically due to shutdown or disconnect.
    #[error("Request canceled: {0}")]
    Canceled(String),
    /// Wrapping the underlying HttpClientError from the network crate.
    #[error("Network error: {0}")]
    HttpClientError(String),
    /// Any unknown HTTP status or unexpected response from dYdX.
    #[error("Unexpected HTTP status code {status}: {body}")]
    UnexpectedStatus { status: u16, body: String },
}

impl From<String> for DydxHttpError {
    fn from(error: String) -> Self {
        Self::ValidationError(error)
    }
}

impl From<BuildError> for DydxHttpError {
    fn from(error: BuildError) -> Self {
        Self::ValidationError(error.to_string())
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
    fn test_build_error_display() {
        let error = BuildError::MissingAddress;
        assert_eq!(error.to_string(), "Missing required address parameter");

        let error = BuildError::MissingTicker;
        assert_eq!(
            error.to_string(),
            "Missing required market ticker parameter"
        );
    }

    #[rstest]
    fn test_dydx_http_error_from_string() {
        let error: DydxHttpError = "Invalid parameter".to_string().into();
        match error {
            DydxHttpError::ValidationError(msg) => assert_eq!(msg, "Invalid parameter"),
            _ => panic!("Expected ValidationError"),
        }
    }

    #[rstest]
    fn test_dydx_http_error_from_build_error() {
        let build_error = BuildError::MissingSubaccountNumber;
        let http_error: DydxHttpError = build_error.into();
        match http_error {
            DydxHttpError::ValidationError(msg) => {
                assert_eq!(msg, "Missing required subaccount number");
            }
            _ => panic!("Expected ValidationError"),
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 5 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`test_build_error_display()`**: Function defined in this file
- **`test_dydx_http_error_from_string()`**: Function defined in this file
- **`test_dydx_http_error_from_build_error()`**: Function defined in this file

### Classes
- **`DydxErrorResponse`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 8


**Enums**: `BuildError`, `DydxHttpError`
**Functions**: `from`, `test_build_error_display`, `test_dydx_http_error_from_build_error`, `test_dydx_http_error_from_string`
**Impls**: `From`
**Structs**: `DydxErrorResponse`

## Related Files

This file is located in `crates/adapters/dydx/src/http/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.875841Z*
