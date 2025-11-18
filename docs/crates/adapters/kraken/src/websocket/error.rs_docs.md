# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/websocket/error.rs`
- **Size**: 1,682 bytes
- **Lines**: 52
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

//! Error types for Kraken WebSocket client operations.

use thiserror::Error;

#[derive(Debug, Clone, Error)]
pub enum KrakenWsError {
    #[error("Connection error: {0}")]
    ConnectionError(String),

    #[error("Subscription error: {0}")]
    SubscriptionError(String),

    #[error("Authentication error: {0}")]
    AuthenticationError(String),

    #[error("Invalid message: {0}")]
    InvalidMessage(String),

    #[error("JSON error: {0}")]
    JsonError(String),

    #[error("Channel error: {0}")]
    ChannelError(String),

    #[error("Disconnected: {0}")]
    Disconnected(String),

    #[error("Timeout: {0}")]
    Timeout(String),
}

impl From<serde_json::Error> for KrakenWsError {
    fn from(error: serde_json::Error) -> Self {
        Self::JsonError(error.to_string())
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`from()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Enums**: `KrakenWsError`
**Functions**: `from`
**Impls**: `From`

## Related Files

This file is located in `crates/adapters/kraken/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.212620Z*
