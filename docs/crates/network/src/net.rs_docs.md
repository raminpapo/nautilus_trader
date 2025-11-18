# Documentation: net.rs

## File Metadata

- **Path**: `crates/network/src/net.rs`
- **Size**: 2,661 bytes
- **Lines**: 63
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

//! Network abstractions for dependency injection and testing.
//!
//! This module provides traits and types that allow our networking components
//! to work with both real networking (`tokio::net`) and simulated networking (`turmoil::net`)
//! through dependency injection.
//!
//! ## Conditional Compilation
//!
//! The module re-exports TCP types that are swapped at compile time:
//! - Default builds: `tokio::net::{TcpStream, TcpListener}`
//! - Builds with `--features turmoil`: `turmoil::net::{TcpStream, TcpListener}`
//!
//! This allows production code to be tested with turmoil's network simulation
//! without runtime overhead or code changes when the feature flag is enabled.

use std::{future::Future, io::Result};

use tokio::io::{AsyncRead, AsyncWrite};
// Re-export TCP types based on build configuration
// Production: use tokio networking
#[cfg(not(feature = "turmoil"))]
pub use tokio::net::{TcpListener, TcpStream};
// Testing with turmoil: use turmoil's simulated networking
#[cfg(feature = "turmoil")]
pub use turmoil::net::{TcpListener, TcpStream};

/// Trait for network types that can establish TCP connections.
pub trait TcpConnector: Send + Sync {
    type Stream: AsyncRead + AsyncWrite + Send + Unpin + 'static;

    /// Connect to the specified address.
    fn connect(&self, addr: &str) -> impl Future<Output = Result<Self::Stream>> + Send;
}

/// Production TCP connector.
///
/// Uses `tokio::net::TcpStream` in production, `turmoil::net::TcpStream` in turmoil tests.
#[derive(Default, Clone, Debug)]
pub struct RealTcpConnector;

impl TcpConnector for RealTcpConnector {
    type Stream = TcpStream;

    fn connect(&self, addr: &str) -> impl Future<Output = Result<Self::Stream>> + Send {
        TcpStream::connect(addr.to_string())
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`connect()`**: Function defined in this file
- **`connect()`**: Function defined in this file

### Classes
- **`RealTcpConnector`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `connect`
**Impls**: `Future`, `TcpConnector`
**Structs**: `RealTcpConnector`
**Traits**: `TcpConnector`

## Related Files

This file is located in `crates/network/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.359856Z*
