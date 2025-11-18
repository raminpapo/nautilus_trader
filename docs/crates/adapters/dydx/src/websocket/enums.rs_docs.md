# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/dydx/src/websocket/enums.rs`
- **Size**: 3,083 bytes
- **Lines**: 110
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

//! Enums for dYdX WebSocket operations and channels.

use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumString, FromRepr};

/// WebSocket operation types for dYdX.
#[derive(
    Clone,
    Copy,
    Debug,
    PartialEq,
    Eq,
    Hash,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "snake_case")]
#[strum(serialize_all = "snake_case")]
pub enum DydxWsOperation {
    /// Subscribe to a channel.
    Subscribe,
    /// Unsubscribe from a channel.
    Unsubscribe,
    /// Ping keepalive message.
    Ping,
    /// Pong response to ping.
    Pong,
}

/// dYdX WebSocket channel identifiers.
///
/// # References
///
/// <https://docs.dydx.trade/developers/indexer/websockets>
#[derive(
    Clone,
    Copy,
    Debug,
    PartialEq,
    Eq,
    Hash,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "snake_case")]
#[strum(serialize_all = "snake_case")]
pub enum DydxWsChannel {
    /// Market data for all markets.
    #[serde(rename = "v4_markets")]
    #[strum(serialize = "v4_markets")]
    Markets,
    /// Trade stream for specific market.
    #[serde(rename = "v4_trades")]
    #[strum(serialize = "v4_trades")]
    Trades,
    /// Order book snapshots and updates.
    #[serde(rename = "v4_orderbook")]
    #[strum(serialize = "v4_orderbook")]
    Orderbook,
    /// Candlestick/kline data.
    #[serde(rename = "v4_candles")]
    #[strum(serialize = "v4_candles")]
    Candles,
    /// Subaccount updates (orders, fills, positions).
    #[serde(rename = "v4_subaccounts")]
    #[strum(serialize = "v4_subaccounts")]
    Subaccounts,
    /// Block height updates from chain.
    #[serde(rename = "v4_block_height")]
    #[strum(serialize = "v4_block_height")]
    BlockHeight,
}

impl DydxWsChannel {
    /// Returns `true` if this is a private channel requiring authentication.
    #[must_use]
    pub const fn is_private(&self) -> bool {
        matches!(self, Self::Subaccounts)
    }

    /// Returns `true` if this is a public channel.
    #[must_use]
    pub const fn is_public(&self) -> bool {
        !self.is_private()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`is_private()`**: Function defined in this file
- **`is_public()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Enums**: `DydxWsChannel`, `DydxWsOperation`
**Functions**: `is_private`, `is_public`
**Impls**: `DydxWsChannel`

## Related Files

This file is located in `crates/adapters/dydx/src/websocket/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.917870Z*
