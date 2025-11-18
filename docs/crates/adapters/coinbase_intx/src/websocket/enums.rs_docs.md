# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/src/websocket/enums.rs`
- **Size**: 2,738 bytes
- **Lines**: 121
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

use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumIter, EnumString};

/// Error types that can be returned by the WebSocket API.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "camelCase")]
pub enum WsErrorType {
    /// General error.
    Error,
    /// Error during subscription.
    SubscriptionError,
    /// Error during unsubscription.
    UnsubscriptionError,
    /// Authentication failure.
    AuthenticationError,
    /// Rate limit exceeded.
    RateLimit,
}

/// Operation type for WebSocket commands.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum WsOperation {
    /// Subscribe to one or more topics.
    Subscribe,
    /// Unsubscribe from one or more topics.
    Unsubscribe,
}

/// Operation type for WebSocket commands.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum WsMessageType {
    /// Snapshot message type.
    Snapshot,
    /// Update message type.
    Update,
}

/// Coinbase International WebSocket feed channel.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CoinbaseIntxWsChannel {
    Subscriptions,
    Instruments,
    Match,
    Funding,
    Risk,
    Level1,
    Level2,
    CandlesOneMinute,
    CandlesFiveMinute,
    CandlesThirtyMinute,
    CandlesTwoHour,
    CandlesOneDay,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Enums**: `CoinbaseIntxWsChannel`, `WsErrorType`, `WsMessageType`, `WsOperation`

## Related Files

This file is located in `crates/adapters/coinbase_intx/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.632960Z*
