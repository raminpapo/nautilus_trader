# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/bybit/src/websocket/enums.rs`
- **Size**: 2,643 bytes
- **Lines**: 109
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

//! Enumerations for Bybit WebSocket operations and channels.

use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumIter, EnumString};

/// WebSocket operation type.
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
#[serde(rename_all = "lowercase")]
#[strum(serialize_all = "lowercase")]
pub enum BybitWsOperation {
    /// Subscribe to topics.
    Subscribe,
    /// Unsubscribe from topics.
    Unsubscribe,
    /// Authenticate connection.
    Auth,
    /// Ping message.
    Ping,
    /// Pong message.
    Pong,
}

/// Private authenticated channel types.
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
#[serde(rename_all = "lowercase")]
#[strum(serialize_all = "lowercase")]
pub enum BybitWsPrivateChannel {
    /// Order updates.
    Order,
    /// Execution/fill updates.
    Execution,
    /// Position updates.
    Position,
    /// Wallet/balance updates.
    Wallet,
}

/// Public channel types.
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
#[serde(rename_all = "lowercase")]
#[strum(serialize_all = "lowercase")]
pub enum BybitWsPublicChannel {
    /// Order book updates.
    #[serde(rename = "orderbook")]
    #[strum(serialize = "orderbook")]
    OrderBook,
    /// Public trades.
    #[serde(rename = "publicTrade")]
    #[strum(serialize = "publicTrade")]
    PublicTrade,
    /// Trade updates.
    Trade,
    /// Kline/candlestick updates.
    Kline,
    /// Ticker updates.
    Tickers,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Enums**: `BybitWsOperation`, `BybitWsPrivateChannel`, `BybitWsPublicChannel`

## Related Files

This file is located in `crates/adapters/bybit/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.463302Z*
