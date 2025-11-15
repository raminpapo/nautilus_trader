# Documentation: `crates/adapters/dydx/src/websocket/messages.rs`
**Generated:** 2025-11-15T19:40:00.970064Z
**File Size:** 11852 bytes
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

- **Path:** `crates/adapters/dydx/src/websocket/messages.rs`
- **Size:** 11,852 bytes
- **Lines:** 353
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 15
- **Functions:** 6

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

//! WebSocket message types for dYdX public and private channels.

use std::collections::HashMap;

use nautilus_model::{
    data::{Data, OrderBookDeltas},
    events::AccountState,
    reports::{FillReport, OrderStatusReport, PositionStatusReport},
};
use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::{
    schemas::ws::DydxWsMessageType,
    websocket::{
        enums::{DydxWsChannel, DydxWsOperation},
        error::DydxWebSocketError,
    },
};

/// dYdX WebSocket subscription message.
///
/// # References
///
/// <https://docs.dydx.trade/developers/indexer/websockets>
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxSubscription {
    /// The operation type (subscribe/unsubscribe).
    #[serde(rename = "type")]
    pub op: DydxWsOperation,
    /// The channel to subscribe to.
    pub channel: DydxWsChannel,
    /// Optional channel-specific identifier (e.g., market symbol).
    #[serde(skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
}

/// High level message emitted by the dYdX WebSocket client.
#[derive(Debug, Clone)]
pub enum DydxWsMessage {
    /// Subscription acknowledgement.
    Subscribed(DydxWsSubscriptionMsg),
    /// Unsubscription acknowledgement.
    Unsubscribed(DydxWsSubscriptionMsg),
    /// Connected acknowledgement with connection_id.
    Connected(DydxWsConnectedMsg),
    /// Channel data update.
    ChannelData(DydxWsChannelDataMsg),
    /// Batch of channel data updates.
    ChannelBatchData(DydxWsChannelBatchDataMsg),
    /// Error received from the venue or client lifecycle.
    Error(DydxWebSocketError),
    /// Raw message payload that does not yet have a typed representation.
    Raw(Value),
    /// Notification that the underlying connection reconnected.
    Reconnected,
    /// Explicit pong event (text-based heartbeat acknowledgement).
    Pong,
}

/// Nautilus domain message emitted after parsing dYdX WebSocket events.
///
/// This enum contains fully-parsed Nautilus domain objects ready for consumption
/// by the Python layer without additional processing.
#[derive(Debug, Clone)]
pub enum NautilusWsMessage {
    /// Market data (trades, quotes, bars).
    Data(Vec<Data>),
    /// Order book deltas.
    Deltas(Box<OrderBookDeltas>),
    /// Order status reports from subaccount stream.
    Order(Box<OrderStatusReport>),
    /// Fill reports from subaccount stream.
    Fill(Box<FillReport>),
    /// Position status reports from subaccount stream.
    Position(Box<PositionStatusReport>),
    /// Account state updates from subaccount stream.
    AccountState(Box<AccountState>),
    /// Error message.
    Error(DydxWebSocketError),
    /// Reconnection notification.
    Reconnected,
}

/// Generic subscription/unsubscription confirmation message.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxWsSubscriptionMsg {
    /// The message type ("subscribed" or "unsubscribed").
    #[serde(rename = "type")]
    pub msg_type: DydxWsMessageType,
    /// The connection ID.
    pub connection_id: String,
    /// The message sequence number.
    pub message_id: u64,
    /// The channel name.
    pub channel: DydxWsChannel,
    /// Optional channel-specific identifier.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
}

/// Connection established message.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxWsConnectedMsg {
    /// The message type ("connected").
    #[serde(rename = "type")]
    pub msg_type: DydxWsMessageType,
    /// The connection ID assigned by the server.
    pub connection_id: String,
    /// The message sequence number.
    pub message_id: u64,
}

/// Single channel data update message.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxWsChannelDataMsg {
    /// The message type ("channel_data").
    #[serde(rename = "type")]
    pub msg_type: DydxWsMessageType,
    /// The connection ID.
    pub connection_id: String,
    /// The message sequence number.
    pub message_id: u64,
    /// The channel name.
    pub channel: DydxWsChannel,
    /// Optional channel-specific identifier.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    /// The payload data (format depends on channel).
    pub contents: Value,
    /// API version.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub version: Option<String>,
}

/// Batch channel data update message (multiple updates in one message).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxWsChannelBatchDataMsg {
    /// The message type ("channel_batch_data").
    #[serde(rename = "type")]
    pub msg_type: DydxWsMessageType,
    /// The connection ID.
    pub connection_id: String,
    /// The message sequence number.
    pub message_id: u64,
    /// The channel name.
    pub channel: DydxWsChannel,
    /// Optional channel-specific identifier.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    /// Array of payload data.
    pub contents: Value,
    /// API version.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub version: Option<String>,
}

/// Generic message structure for initial classification.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxWsGenericMsg {
    /// The message type.
    #[serde(rename = "type")]
    pub msg_type: DydxWsMessageType,
    /// Optional connection ID.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub connection_id: Option<String>,
    /// Optional message sequence number.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub message_id: Option<u64>,
    /// Optional channel name.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub channel: Option<DydxWsChannel>,
    /// Optional channel-specific identifier.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    /// Optional error message.
    #[serde(default, skip_serializing_if = "Option::is_none")]
    pub message: Option<String>,
}

impl DydxWsGenericMsg {
    /// Returns `true` if this message is an error.
    #[must_use]
    pub fn is_error(&self) -> bool {
        self.msg_type == DydxWsMessageType::Error
    }

    /// Returns `true` if this message is a subscription confirmation.
    #[must_use]
    pub fn is_subscribed(&self) -> bool {
        self.msg_type == DydxWsMessageType::Subscribed
    }

    /// Returns `true` if this message is an unsubscription confirmation.
    #[must_use]
    pub fn is_unsubscribed(&self) -> bool {
        self.msg_type == DydxWsMessageType::Unsubscribed
    }

    /// Returns `true` if this message is a connection notification.
    #[must_use]
    pub fn is_connected(&self) -> bool {
        self.msg_type == DydxWsMessageType::Connected
    }

    /// Returns `true` if this message is channel data.
    #[must_use]
    pub fn is_channel_data(&self) -> bool {
        self.msg_type == DydxWsMessageType::ChannelData
    }

    /// Returns `true` if this message is batch channel data.
    #[must_use]
    pub fn is_channel_batch_data(&self) -> bool {
        self.msg_type == DydxWsMessageType::ChannelBatchData
    }
}

// ================================================================================================
// Channel content types
// ================================================================================================

use chrono::{DateTime, Utc};
use nautilus_model::enums::OrderSide;

/// Trade message from v4_trades channel.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct DydxTrade {
    /// Trade ID.
    pub id: String,
    /// Order side (BUY/SELL).
    pub side: OrderSide,
    /// Trade size.
    pub size: String,
    /// Trade price.
    pub price: String,
    /// Trade timestamp.
    pub created_at: DateTime<Utc>,
    /// Order type.
    #[serde(rename = "type")]
    pub order_type: String,
    /// Block height (optional).
    #[serde(skip_serializing_if = "Option::is_none")]
    pub created_at_height: Option<String>,
}

/// Contents of v4_trades channel_data message.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxTradeContents {
    /// Array of trades.
    pub trades: Vec<DydxTrade>,
}

/// Candle/bar data from v4_candles channel.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct DydxCandle {
    /// Base token volume.
    pub base_token_volume: String,
    /// Close price.
    pub close: String,
    /// High price.
    pub high: String,
    /// Low price.
    pub low: String,
    /// Open price.
    pub open: String,
    /// Resolution/timeframe.
    pub resolution: String,
    /// Start time.
    pub started_at: DateTime<Utc>,
    /// Starting open interest.
    pub starting_open_interest: String,
    /// Market ticker.
    pub ticker: String,
    /// Number of trades.
    pub trades: i64,
    /// USD volume.
    pub usd_volume: String,
    /// Orderbook mid price at close (optional).
    #[serde(skip_serializing_if = "Option::is_none")]
    pub orderbook_mid_price_close: Option<String>,
    /// Orderbook mid price at open (optional).
    #[serde(skip_serializing_if = "Option::is_none")]
    pub orderbook_mid_price_open: Option<String>,
}

/// Order book price level (price, size tuple).
pub type PriceLevel = (String, String);

/// Contents of v4_orderbook channel_data/channel_batch_data messages.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxOrderbookContents {
    /// Bid price levels.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub bids: Option<Vec<PriceLevel>>,
    /// Ask price levels.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub asks: Option<Vec<PriceLevel>>,
}

/// Price level for orderbook snapshot (structured format).
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxPriceLevel {
    /// Price.
    pub price: String,
    /// Size.
    pub size: String,
}

/// Contents of v4_orderbook subscribed (snapshot) message.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxOrderbookSnapshotContents {
    /// Bid price levels.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub bids: Option<Vec<DydxPriceLevel>>,
    /// Ask price levels.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub asks: Option<Vec<DydxPriceLevel>>,
}

/// Oracle price data for a market.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct DydxOraclePriceMarket {
    /// Oracle price.
    pub oracle_price: String,
}

/// Contents of v4_markets channel_data message.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct DydxMarketsContents {
    /// Oracle prices by market symbol.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub oracle_prices: Option<HashMap<String, DydxOraclePriceMarket>>,
}
```


---

## Overview

This file is located at `crates/adapters/dydx/src/websocket/messages.rs` within the repository.

**Classes defined:** DydxSubscription, DydxWsSubscriptionMsg, DydxWsConnectedMsg, DydxWsChannelDataMsg, DydxWsChannelBatchDataMsg, DydxWsGenericMsg, DydxTrade, DydxTradeContents, DydxCandle, DydxOrderbookContents and 5 more

**Functions defined:** is_error, is_subscribed, is_unsubscribed, is_connected, is_channel_data, is_channel_batch_data


---

## Detailed Analysis

### Classes

#### `DydxSubscription`

**Type:** struct


#### `DydxWsSubscriptionMsg`

**Type:** struct


#### `DydxWsConnectedMsg`

**Type:** struct


#### `DydxWsChannelDataMsg`

**Type:** struct


#### `DydxWsChannelBatchDataMsg`

**Type:** struct


#### `DydxWsGenericMsg`

**Type:** struct


#### `DydxTrade`

**Type:** struct


#### `DydxTradeContents`

**Type:** struct


#### `DydxCandle`

**Type:** struct


#### `DydxOrderbookContents`

**Type:** struct


#### `DydxPriceLevel`

**Type:** struct


#### `DydxOrderbookSnapshotContents`

**Type:** struct


#### `DydxOraclePriceMarket`

**Type:** struct


#### `DydxMarketsContents`

**Type:** struct


#### `DydxWsGenericMsg`

**Type:** impl


### Functions

#### `is_error(&self)`


#### `is_subscribed(&self)`


#### `is_unsubscribed(&self)`


#### `is_connected(&self)`


#### `is_channel_data(&self)`


#### `is_channel_batch_data(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: token. Ensure proper handling of secrets.


