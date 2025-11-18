# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/rpc/error.rs`
- **Size**: 2,028 bytes
- **Lines**: 43
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

/// Represents errors that can occur when interacting with a blockchain RPC client.
#[derive(Debug, Error)]
pub enum BlockchainRpcClientError {
    /// Occurs when the RPC client encounters a client-level error, such as connection failures.
    #[error("Client error: {0}")]
    ClientError(String),
    /// Occurs when input parameters to an RPC call are invalid.
    #[error("Invalid RPC parameters: {0}")]
    InvalidParameters(String),
    /// Occurs when decoding contract ABI data fails.
    #[error("Decoding error: {0}")]
    AbiDecodingError(String),
    /// Occurs when parsing an RPC message fails.
    #[error("Parsing error: {0}")]
    MessageParsingError(String),
    /// Occurs when receiving an unsupported RPC response type.
    #[error("Unsupported rpc response type of message {0}")]
    UnsupportedRpcResponseType(String),
    /// Occurs when an internal RPC client error is encountered.
    #[error("Internal Rpc client error: {0}")]
    InternalRpcClientError(String),
    /// Indicates that no message was received from the RPC channel.
    #[error("No message received")]
    NoMessageReceived,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Enums**: `BlockchainRpcClientError`

## Related Files

This file is located in `crates/adapters/blockchain/src/rpc/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.332474Z*
