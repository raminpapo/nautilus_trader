# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/common/enums.rs`
- **Size**: 6,824 bytes
- **Lines**: 315
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

//! Enumerations that model Kraken string/int enums across HTTP and WebSocket payloads.

use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumString, FromRepr};

#[derive(
    Clone,
    Copy,
    Debug,
    Default,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenEnvironment {
    #[default]
    Mainnet,
    Testnet,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Default,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenProductType {
    #[default]
    Spot,
    Futures,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenOrderType {
    Market,
    Limit,
    #[serde(rename = "stop-loss")]
    #[strum(serialize = "stop-loss")]
    StopLoss,
    #[serde(rename = "take-profit")]
    #[strum(serialize = "take-profit")]
    TakeProfit,
    #[serde(rename = "stop-loss-limit")]
    #[strum(serialize = "stop-loss-limit")]
    StopLossLimit,
    #[serde(rename = "take-profit-limit")]
    #[strum(serialize = "take-profit-limit")]
    TakeProfitLimit,
    #[serde(rename = "settle-position")]
    #[strum(serialize = "settle-position")]
    SettlePosition,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenOrderSide {
    Buy,
    Sell,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "UPPERCASE")]
#[strum(ascii_case_insensitive, serialize_all = "UPPERCASE")]
pub enum KrakenTimeInForce {
    #[serde(rename = "GTC")]
    #[strum(serialize = "GTC")]
    GoodTilCancelled,
    #[serde(rename = "IOC")]
    #[strum(serialize = "IOC")]
    ImmediateOrCancel,
    #[serde(rename = "GTD")]
    #[strum(serialize = "GTD")]
    GoodTilDate,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenOrderStatus {
    Pending,
    Open,
    Closed,
    Canceled,
    Expired,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenPositionSide {
    Long,
    Short,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "snake_case")]
#[strum(ascii_case_insensitive, serialize_all = "snake_case")]
pub enum KrakenPairStatus {
    Online,
    #[serde(rename = "cancel_only")]
    #[strum(serialize = "cancel_only")]
    CancelOnly,
    #[serde(rename = "post_only")]
    #[strum(serialize = "post_only")]
    PostOnly,
    #[serde(rename = "limit_only")]
    #[strum(serialize = "limit_only")]
    LimitOnly,
    #[serde(rename = "reduce_only")]
    #[strum(serialize = "reduce_only")]
    ReduceOnly,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenSystemStatus {
    Online,
    Maintenance,
    #[serde(rename = "cancel_only")]
    #[strum(serialize = "cancel_only")]
    CancelOnly,
    #[serde(rename = "post_only")]
    #[strum(serialize = "post_only")]
    PostOnly,
}

#[derive(
    Clone,
    Copy,
    Debug,
    Display,
    AsRefStr,
    EnumString,
    FromRepr,
    PartialEq,
    Eq,
    Hash,
    Serialize,
    Deserialize,
)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.kraken", eq, eq_int)
)]
#[serde(rename_all = "lowercase")]
#[strum(ascii_case_insensitive, serialize_all = "lowercase")]
pub enum KrakenAssetClass {
    Currency,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 10


**Enums**: `KrakenAssetClass`, `KrakenEnvironment`, `KrakenOrderSide`, `KrakenOrderStatus`, `KrakenOrderType`, `KrakenPairStatus`, `KrakenPositionSide`, `KrakenProductType`, `KrakenSystemStatus`, `KrakenTimeInForce`

## Related Files

This file is located in `crates/adapters/kraken/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.157013Z*
