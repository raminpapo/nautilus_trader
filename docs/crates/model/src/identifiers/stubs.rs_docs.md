# Documentation: stubs.rs

## File Metadata

- **Path**: `crates/model/src/identifiers/stubs.rs`
- **Size**: 3,474 bytes
- **Lines**: 160
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

//! Default implementations and fixture functions to provide stub identifiers for testing.

use nautilus_core::UUID4;
use rstest::fixture;

use crate::identifiers::{
    AccountId, ClientId, ClientOrderId, ComponentId, ExecAlgorithmId, InstrumentId, OrderListId,
    PositionId, StrategyId, Symbol, TradeId, TraderId, Venue, VenueOrderId,
};

// ---- AccountId ----

#[fixture]
pub fn account_id() -> AccountId {
    AccountId::from("SIM-001")
}

#[fixture]
pub fn account_ib() -> AccountId {
    AccountId::from("IB-1234567890")
}

// ---- ClientId ----

#[fixture]
pub fn client_id_binance() -> ClientId {
    ClientId::from("BINANCE")
}

#[fixture]
pub fn client_id_dydx() -> ClientId {
    ClientId::from("COINBASE")
}

// ---- ClientOrderId ----

#[fixture]
pub fn client_order_id() -> ClientOrderId {
    ClientOrderId::from("O-19700101-000000-001-001-1")
}

// ---- ComponentId ----

#[fixture]
pub fn component_risk_engine() -> ComponentId {
    ComponentId::from("RiskEngine")
}

// ---- ExecAlgorithmId ----

#[fixture]
pub fn exec_algorithm_id() -> ExecAlgorithmId {
    ExecAlgorithmId::from("001")
}

// ---- InstrumentId ----

#[fixture]
pub fn instrument_id_eth_usdt_binance() -> InstrumentId {
    InstrumentId::from("ETHUSDT.BINANCE")
}

#[fixture]
pub fn instrument_id_btc_usdt() -> InstrumentId {
    InstrumentId::from("BTCUSDT.COINBASE")
}

#[fixture]
pub fn instrument_id_aud_usd_sim() -> InstrumentId {
    InstrumentId::from("AUDUSD.SIM")
}

// ---- OrderListId ----

#[fixture]
pub fn order_list_id_test() -> OrderListId {
    OrderListId::from("001")
}

// ---- PositionId ----

#[fixture]
pub fn position_id_test() -> PositionId {
    PositionId::from("P-123456789")
}

// ---- StrategyId ----

#[fixture]
pub fn strategy_id_ema_cross() -> StrategyId {
    StrategyId::from("EMACross-001")
}

// ---- Symbol ----

#[fixture]
pub fn symbol_eth_perp() -> Symbol {
    Symbol::from("ETH-PERP")
}

#[fixture]
pub fn symbol_aud_usd() -> Symbol {
    Symbol::from("AUDUSD")
}

// ---- TradeId ----

#[fixture]
pub fn trade_id() -> TradeId {
    TradeId::from("1234567890")
}

// ---- TraderId ----

#[fixture]
pub fn trader_id() -> TraderId {
    TraderId::from("TRADER-001")
}

// ---- Venue ----

#[fixture]
pub fn venue_binance() -> Venue {
    Venue::from("BINANCE")
}

#[fixture]
pub fn venue_sim() -> Venue {
    Venue::from("SIM")
}

// ---- VenueOrderId ----

#[fixture]
pub fn venue_order_id() -> VenueOrderId {
    VenueOrderId::from("001")
}

// ---- UUID4 ----

#[fixture]
pub fn uuid4() -> UUID4 {
    UUID4::from("16578139-a945-4b65-b46c-bc131a15d8e7")
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 21 function(s).

## Detailed Walkthrough

### Functions
- **`account_id()`**: Function defined in this file
- **`account_ib()`**: Function defined in this file
- **`client_id_binance()`**: Function defined in this file
- **`client_id_dydx()`**: Function defined in this file
- **`client_order_id()`**: Function defined in this file
- **`component_risk_engine()`**: Function defined in this file
- **`exec_algorithm_id()`**: Function defined in this file
- **`instrument_id_eth_usdt_binance()`**: Function defined in this file
- **`instrument_id_btc_usdt()`**: Function defined in this file
- **`instrument_id_aud_usd_sim()`**: Function defined in this file
- **`order_list_id_test()`**: Function defined in this file
- **`position_id_test()`**: Function defined in this file
- **`strategy_id_ema_cross()`**: Function defined in this file
- **`symbol_eth_perp()`**: Function defined in this file
- **`symbol_aud_usd()`**: Function defined in this file
- **`trade_id()`**: Function defined in this file
- **`trader_id()`**: Function defined in this file
- **`venue_binance()`**: Function defined in this file
- **`venue_sim()`**: Function defined in this file
- **`venue_order_id()`**: Function defined in this file

*...and 1 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 21


**Functions**: `account_ib`, `account_id`, `client_id_binance`, `client_id_dydx`, `client_order_id`, `component_risk_engine`, `exec_algorithm_id`, `instrument_id_aud_usd_sim`, `instrument_id_btc_usdt`, `instrument_id_eth_usdt_binance`, `order_list_id_test`, `position_id_test`, `strategy_id_ema_cross`, `symbol_aud_usd`, `symbol_eth_perp`, `trade_id`, `trader_id`, `uuid4`, `venue_binance`, `venue_order_id`, `venue_sim`

## Related Files

This file is located in `crates/model/src/identifiers/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.665273Z*
