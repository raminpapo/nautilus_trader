# Documentation: `crates/adapters/dydx/src/error.rs`
**Generated:** 2025-11-15T19:40:00.912860Z
**File Size:** 2377 bytes
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

- **Path:** `crates/adapters/dydx/src/error.rs`
- **Size:** 2,377 bytes
- **Lines:** 72
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

    /// Nautilus core errors.
    #[error("Nautilus error: {0}")]
    Nautilus(#[from] anyhow::Error),
}
```


---

## Overview

This file is located at `crates/adapters/dydx/src/error.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


