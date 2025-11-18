# Documentation: types.rs

## File Metadata

- **Path**: `crates/network/src/socket/types.rs`
- **Size**: 1,480 bytes
- **Lines**: 38
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

//! Socket types and type aliases.

use std::sync::Arc;

use bytes::Bytes;
use tokio::io::{ReadHalf, WriteHalf};
use tokio_tungstenite::MaybeTlsStream;

use crate::net::TcpStream;

pub type TcpWriter = WriteHalf<MaybeTlsStream<TcpStream>>;
pub type TcpReader = ReadHalf<MaybeTlsStream<TcpStream>>;
pub type TcpMessageHandler = Arc<dyn Fn(&[u8]) + Send + Sync>;

/// Represents a command for the writer task.
#[derive(Debug)]
pub enum WriterCommand {
    /// Update the writer reference with a new one after reconnection.
    Update(TcpWriter),
    /// Send data to the server.
    Send(Bytes),
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Enums**: `WriterCommand`

## Related Files

This file is located in `crates/network/src/socket/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.428861Z*
