# Documentation: any.rs

## File Metadata

- **Path**: `crates/model/src/instruments/any.rs`
- **Size**: 3,333 bytes
- **Lines**: 74
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

use enum_dispatch::enum_dispatch;
use serde::{Deserialize, Serialize};

use super::{
    Instrument, betting::BettingInstrument, binary_option::BinaryOption,
    crypto_future::CryptoFuture, crypto_option::CryptoOption, crypto_perpetual::CryptoPerpetual,
    currency_pair::CurrencyPair, equity::Equity, futures_contract::FuturesContract,
    futures_spread::FuturesSpread, option_contract::OptionContract, option_spread::OptionSpread,
};
use crate::types::{Price, Quantity};

#[derive(Clone, Debug, Serialize, Deserialize)]
#[enum_dispatch(Instrument)]
pub enum InstrumentAny {
    Betting(BettingInstrument),
    BinaryOption(BinaryOption),
    CryptoFuture(CryptoFuture),
    CryptoOption(CryptoOption),
    CryptoPerpetual(CryptoPerpetual),
    CurrencyPair(CurrencyPair),
    Equity(Equity),
    FuturesContract(FuturesContract),
    FuturesSpread(FuturesSpread),
    OptionContract(OptionContract),
    OptionSpread(OptionSpread),
}

// TODO: Probably move this to the `Instrument` trait too
impl InstrumentAny {
    #[must_use]
    pub fn get_base_quantity(&self, quantity: Quantity, last_px: Price) -> Quantity {
        match self {
            Self::Betting(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::BinaryOption(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::CryptoFuture(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::CryptoOption(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::CryptoPerpetual(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::CurrencyPair(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::Equity(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::FuturesContract(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::FuturesSpread(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::OptionContract(inst) => inst.calculate_base_quantity(quantity, last_px),
            Self::OptionSpread(inst) => inst.calculate_base_quantity(quantity, last_px),
        }
    }

    /// Returns true if the instrument is a spread instrument.
    #[must_use]
    pub fn is_spread(&self) -> bool {
        matches!(self, Self::FuturesSpread(_) | Self::OptionSpread(_))
    }
}

impl PartialEq for InstrumentAny {
    fn eq(&self, other: &Self) -> bool {
        self.id() == other.id()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s).

## Detailed Walkthrough

### Functions
- **`get_base_quantity()`**: Function defined in this file
- **`is_spread()`**: Function defined in this file
- **`eq()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Enums**: `InstrumentAny`
**Functions**: `eq`, `get_base_quantity`, `is_spread`
**Impls**: `InstrumentAny`, `PartialEq`
**Traits**: `too`

## Related Files

This file is located in `crates/model/src/instruments/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.680159Z*
