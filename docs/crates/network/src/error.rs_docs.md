# Documentation: error.rs

## File Metadata

- **Path**: `crates/network/src/error.rs`
- **Size**: 1,429 bytes
- **Lines**: 33
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

//! Network error types.

use thiserror::Error;

/// Error type for send operations in network clients.
#[derive(Error, Debug)]
pub enum SendError {
    /// The client has been closed or is disconnecting.
    #[error("send failed: client closed or disconnecting")]
    Closed,
    /// Timed out waiting for the client to become active.
    #[error("send failed: timeout waiting for active state")]
    Timeout,
    /// Failed to send because the writer channel is closed.
    #[error("send failed: broken pipe ({0})")]
    BrokenPipe(String),
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Enums**: `SendError`

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
*Generated on 2025-11-18T21:55:03.341457Z*
