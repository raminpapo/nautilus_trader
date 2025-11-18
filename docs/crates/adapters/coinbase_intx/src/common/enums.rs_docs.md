# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/src/common/enums.rs`
- **Size**: 8,973 bytes
- **Lines**: 424
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

use nautilus_model::enums::{AggressorSide, OrderSide, OrderType, TimeInForce};
use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumIter, EnumString};

/// Represents the type of book action.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CoinbaseIntxFeeTierType {
    Regular,
    LiquidityProgram,
}

/// Represents the type of book action.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "lowercase")]
pub enum CoinbaseIntxBookAction {
    /// Incremental update.
    Update,
    /// Full snapshot.
    Snapshot,
}

/// Represents the possible states of an order throughout its lifecycle.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
pub enum CoinbaseIntxCandleConfirm {
    /// K-line is "uncompleted".
    #[serde(rename = "0")]
    Partial,
    /// K-line is completed.
    #[serde(rename = "1")]
    Closed,
}

/// Represents the side of an order or trade (Buy/Sell).
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxSide {
    /// Buy side of a trade or order.
    Buy,
    /// Sell side of a trade or order.
    Sell,
}

impl From<OrderSide> for CoinbaseIntxSide {
    fn from(value: OrderSide) -> Self {
        match value {
            OrderSide::Buy => Self::Buy,
            OrderSide::Sell => Self::Sell,
            _ => panic!("Invalid `OrderSide`"),
        }
    }
}

impl From<AggressorSide> for CoinbaseIntxSide {
    fn from(value: AggressorSide) -> Self {
        match value {
            AggressorSide::Buyer => Self::Buy,
            AggressorSide::Seller => Self::Sell,
            _ => panic!("Invalid `AggressorSide`"),
        }
    }
}

impl From<CoinbaseIntxSide> for OrderSide {
    fn from(value: CoinbaseIntxSide) -> Self {
        match value {
            CoinbaseIntxSide::Buy => Self::Buy,
            CoinbaseIntxSide::Sell => Self::Sell,
        }
    }
}

impl From<CoinbaseIntxSide> for AggressorSide {
    fn from(value: CoinbaseIntxSide) -> Self {
        match value {
            CoinbaseIntxSide::Buy => Self::Buyer,
            CoinbaseIntxSide::Sell => Self::Seller,
        }
    }
}

/// Represents an order type.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CoinbaseIntxOrderType {
    Limit,
    Market,
    StopLimit,
    Stop,
    TakeProfitStopLoss,
}

impl From<CoinbaseIntxOrderType> for OrderType {
    fn from(value: CoinbaseIntxOrderType) -> Self {
        match value {
            CoinbaseIntxOrderType::Limit => Self::Limit,
            CoinbaseIntxOrderType::Market => Self::Market,
            CoinbaseIntxOrderType::StopLimit => Self::StopLimit,
            CoinbaseIntxOrderType::Stop => Self::StopMarket,
            CoinbaseIntxOrderType::TakeProfitStopLoss => Self::MarketIfTouched,
        }
    }
}

impl From<OrderType> for CoinbaseIntxOrderType {
    fn from(value: OrderType) -> Self {
        match value {
            OrderType::Limit => Self::Limit,
            OrderType::Market => Self::Market,
            OrderType::StopLimit => Self::StopLimit,
            OrderType::StopMarket => Self::Stop,
            OrderType::MarketIfTouched => Self::TakeProfitStopLoss,
            _ => panic!("Invalid `OrderType` cannot be represented on Coinbase International"),
        }
    }
}

/// Represents an overall order status.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxOrderStatus {
    Working,
    Done,
}

/// Represents an order time in force.
#[derive(
    Copy,
    Clone,
    Debug,
    Default,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxTimeInForce {
    #[default]
    Gtc, // Good Till Cancel
    Ioc, // Immediate or Cancel
    Gtt, // Good Till Time
    Fok, // Fill or Kill
}

impl From<TimeInForce> for CoinbaseIntxTimeInForce {
    fn from(time_in_force: TimeInForce) -> Self {
        match time_in_force {
            TimeInForce::Gtc => Self::Gtc,
            TimeInForce::Ioc => Self::Ioc,
            TimeInForce::Fok => Self::Fok,
            TimeInForce::Gtd => Self::Gtt,
            _ => panic!("Invalid `TimeInForce` cannot be represented on Coinbase International"),
        }
    }
}

impl From<CoinbaseIntxTimeInForce> for TimeInForce {
    fn from(coinbase_tif: CoinbaseIntxTimeInForce) -> Self {
        match coinbase_tif {
            CoinbaseIntxTimeInForce::Gtc => Self::Gtc,
            CoinbaseIntxTimeInForce::Ioc => Self::Ioc,
            CoinbaseIntxTimeInForce::Fok => Self::Fok,
            CoinbaseIntxTimeInForce::Gtt => Self::Gtd,
        }
    }
}

/// Represents a self trade protection (STP) mode.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxSTPMode {
    None,
    Aggressing,
    Resting,
    Both,
    DecrementAndCancel,
}

/// Represents an order event type.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxOrderEventType {
    New,
    Trade,
    Canceled,
    Replaced,
    PendingCancel,
    Rejected,
    PendingNew,
    Expired,
    PendingReplace,
    StopTriggered,
}

/// Represents an algo strategy.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxAlgoStrategy {
    Twap,
}

/// Represents the type of execution that generated a trade.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
pub enum CoinbaseIntxExecType {
    #[serde(rename = "T")]
    Taker,
    #[serde(rename = "M")]
    Maker,
    #[serde(rename = "")]
    None,
}

/// Represents instrument types on Coinbase International.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxInstrumentType {
    /// Spot products.
    Spot,
    /// Perpetual products.
    Perp,
    /// Index products.
    Index,
}

/// Represents an asset status on Coinbase International.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxAssetStatus {
    /// Asset is actively trading.
    Active,
}

/// Represents an instrument status on Coinbase International.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum CoinbaseIntxTradingState {
    /// Instrument is actively trading.
    Trading,
    /// Instrument trading is paused.
    Paused,
    /// Instrument trading is halted.
    Halt,
    /// Instrument has been delisted.
    Delisted,
    /// TBD.
    External,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file
- **`from()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Enums**: `CoinbaseIntxAlgoStrategy`, `CoinbaseIntxAssetStatus`, `CoinbaseIntxBookAction`, `CoinbaseIntxCandleConfirm`, `CoinbaseIntxExecType`, `CoinbaseIntxFeeTierType`, `CoinbaseIntxInstrumentType`, `CoinbaseIntxOrderEventType`, `CoinbaseIntxOrderStatus`, `CoinbaseIntxOrderType`, `CoinbaseIntxSTPMode`, `CoinbaseIntxSide`, `CoinbaseIntxTimeInForce`, `CoinbaseIntxTradingState`
**Functions**: `from`
**Impls**: `From`

## Related Files

This file is located in `crates/adapters/coinbase_intx/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.571806Z*
