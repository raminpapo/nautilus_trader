# Documentation: rpc.rs

## File Metadata

- **Path**: `crates/model/src/defi/rpc.rs`
- **Size**: 2,490 bytes
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

use serde::{Deserialize, de::DeserializeOwned};

/// A response structure received from a WebSocket JSON-RPC blockchain node subscription.
#[derive(Debug, Deserialize)]
pub struct RpcNodeWssResponse<T>
where
    T: DeserializeOwned,
{
    /// JSON-RPC version identifier.
    pub jsonrpc: String,
    /// Name of the RPC method that was called.
    pub method: String,
    /// Parameters containing subscription information and the deserialized result.
    #[serde(bound(deserialize = ""))]
    pub params: RpcNodeSubscriptionResponse<T>,
}

/// Container for subscription data within an RPC response, holding the subscription ID and the deserialized result.
#[derive(Debug, Deserialize)]
pub struct RpcNodeSubscriptionResponse<T>
where
    T: DeserializeOwned,
{
    /// ID of the subscription associated with the RPC response.
    pub subscription: String,
    /// Deserialized result.
    #[serde(bound(deserialize = ""))]
    pub result: T,
}

/// A response structure received from an HTTP JSON-RPC blockchain node request.
#[derive(Debug, Deserialize)]
pub struct RpcNodeHttpResponse<T>
where
    T: DeserializeOwned,
{
    /// JSON-RPC version identifier.
    pub jsonrpc: String,
    /// Request identifier returned by the server.
    pub id: u64,
    /// Deserialized result.
    #[serde(bound(deserialize = ""))]
    pub result: Option<T>,
    /// Error information if the request failed.
    pub error: Option<RpcError>,
}

/// JSON-RPC error structure.
#[derive(Debug, Deserialize)]
pub struct RpcError {
    /// Error code.
    pub code: i32,
    /// Error message.
    pub message: String,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. 4 class(es).

## Detailed Walkthrough


### Classes
- **`RpcNodeWssResponse`**: Class defined in this file
- **`RpcNodeSubscriptionResponse`**: Class defined in this file
- **`RpcNodeHttpResponse`**: Class defined in this file
- **`RpcError`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Structs**: `RpcError`, `RpcNodeHttpResponse`, `RpcNodeSubscriptionResponse`, `RpcNodeWssResponse`

## Related Files

This file is located in `crates/model/src/defi/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.386989Z*
