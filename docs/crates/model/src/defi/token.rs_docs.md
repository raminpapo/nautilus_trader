# Documentation: token.rs

## File Metadata

- **Path**: `crates/model/src/defi/token.rs`
- **Size**: 5,979 bytes
- **Lines**: 190
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

use std::{
    fmt::{Display, Formatter},
    sync::Arc,
};

use alloy_primitives::Address;
use serde::{Deserialize, Serialize};

use crate::defi::chain::SharedChain;

/// Represents a cryptocurrency token on a blockchain network.
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.model")
)]
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
pub struct Token {
    /// The blockchain network where this token exists.
    pub chain: SharedChain,
    /// The blockchain address of the token contract.
    pub address: Address,
    /// The full name of the token.
    pub name: String,
    /// The token's ticker symbol.
    pub symbol: String,
    /// The number of decimal places used to represent fractional token amounts.
    pub decimals: u8,
}

/// A thread-safe shared pointer to a `Token`, enabling efficient reuse across multiple components.
pub type SharedToken = Arc<Token>;

impl Token {
    /// Creates a new [`Token`] instance with the specified properties.
    #[must_use]
    pub fn new(
        chain: SharedChain,
        address: Address,
        name: String,
        symbol: String,
        decimals: u8,
    ) -> Self {
        Self {
            chain,
            address,
            name,
            symbol,
            decimals,
        }
    }

    /// Returns true if this token is a stablecoin.
    ///
    /// Checks against common stablecoin symbols including USD-pegged tokens,
    /// Euro-pegged tokens, and other algorithmic/collateralized stablecoins.
    pub fn is_stablecoin(&self) -> bool {
        matches!(
            self.symbol.as_str(),
            "USDC"
                | "USDT"
                | "DAI"
                | "BUSD"
                | "FRAX"
                | "LUSD"
                | "TUSD"
                | "USDP"
                | "GUSD"
                | "SUSD"
                | "UST"
                | "USDD"
                | "CUSD"
                | "EUROC"
                | "EURT"
                | "EURS"
                | "AGEUR"
                | "MIM"
                | "FEI"
                | "OUSD"
                | "USDB"
        )
    }

    /// Returns true if this token is a native blockchain currency wrapper.
    ///
    /// Identifies wrapped versions of native currencies like WETH (Wrapped ETH),
    /// WMATIC (Wrapped MATIC), WBNB (Wrapped BNB), etc.
    pub fn is_native_currency(&self) -> bool {
        matches!(
            self.symbol.as_str(),
            "WETH"
                | "ETH"
                | "WMATIC"
                | "MATIC"
                | "WBNB"
                | "BNB"
                | "WAVAX"
                | "AVAX"
                | "WFTM"
                | "FTM"
        )
    }

    /// Returns the priority of this token for base/quote determination.
    ///
    /// Lower numbers indicate higher priority to become the quote token (pricing currency).
    /// This follows market conventions where trades are quoted in the most liquid/stable assets.
    ///
    /// # Priority Levels
    /// - **1**: Stablecoins (USDC, USDT, DAI, etc.) - Highest priority to be quote
    /// - **2**: Native currencies (WETH, WMATIC, WBNB, etc.) - Medium priority
    /// - **3**: Other tokens - Lowest priority (typically become base tokens)
    pub fn get_token_priority(&self) -> u8 {
        if self.is_stablecoin() {
            1
        } else if self.is_native_currency() {
            2
        } else {
            3
        }
    }
}

impl Display for Token {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "Token(symbol={}, name={})", self.symbol, self.name)
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use std::sync::Arc;

    use rstest::rstest;

    use super::*;
    use crate::defi::{chain::chains, stubs::weth};

    #[rstest]
    fn test_token_constructor(weth: Token) {
        assert_eq!(weth.chain.chain_id, chains::ARBITRUM.chain_id);
        assert_eq!(weth.name, "Wrapped Ether");
        assert_eq!(weth.symbol, "WETH");
        assert_eq!(weth.decimals, 18);
        assert!(weth.is_native_currency());
    }

    #[rstest]
    fn test_token_display_with_special_characters() {
        // Test edge case where token names/symbols contain formatting characters
        let chain = Arc::new(chains::ETHEREUM.clone());
        let token = Token::new(
            chain,
            "0xA0b86a33E6441b936662bb6B5d1F8Fb0E2b57A5D"
                .parse()
                .unwrap(),
            "Test Token (with parentheses)".to_string(),
            "TEST-1".to_string(),
            18,
        );

        let display = token.to_string();
        assert_eq!(
            display,
            "Token(symbol=TEST-1, name=Test Token (with parentheses))"
        );
        assert!(!token.is_native_currency());
        assert!(!token.is_stablecoin());
        assert_eq!(token.get_token_priority(), 3);
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 7 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`is_stablecoin()`**: Function defined in this file
- **`is_native_currency()`**: Function defined in this file
- **`get_token_priority()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`test_token_constructor()`**: Function defined in this file
- **`test_token_display_with_special_characters()`**: Function defined in this file

### Classes
- **`Token`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `fmt`, `get_token_priority`, `is_native_currency`, `is_stablecoin`, `new`, `test_token_constructor`, `test_token_display_with_special_characters`
**Impls**: `Display`, `Token`
**Structs**: `Token`

## Related Files

This file is located in `crates/model/src/defi/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:55:02.422293Z*
