# Documentation: `crates/model/src/identifiers/venue.rs`
**Generated:** 2025-11-15T19:40:02.779429Z
**File Size:** 11761 bytes
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

- **Path:** `crates/model/src/identifiers/venue.rs`
- **Size:** 11,761 bytes
- **Lines:** 371
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 23

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

//! Represents a valid trading venue ID.

use std::{
    fmt::{Debug, Display, Formatter},
    hash::Hash,
};

use nautilus_core::correctness::{FAILED, check_valid_string_ascii};
use ustr::Ustr;

#[cfg(feature = "defi")]
use crate::defi::{Blockchain, Chain, DexType};
use crate::venues::VENUE_MAP;

pub const SYNTHETIC_VENUE: &str = "SYNTH";

/// Represents a valid trading venue ID.
#[repr(C)]
#[derive(Clone, Copy, Hash, PartialEq, Eq, PartialOrd, Ord)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.model")
)]
pub struct Venue(Ustr);

impl Venue {
    /// Creates a new [`Venue`] instance with correctness checking.
    ///
    /// # Errors
    ///
    /// Returns an error if `value` is not a valid string.
    ///
    /// # Notes
    ///
    /// PyO3 requires a `Result` type for proper error handling and stacktrace printing in Python.
    pub fn new_checked<T: AsRef<str>>(value: T) -> anyhow::Result<Self> {
        let value = value.as_ref();
        check_valid_string_ascii(value, stringify!(value))?;

        #[cfg(feature = "defi")]
        if value.contains(':')
            && let Err(e) = validate_blockchain_venue(value)
        {
            anyhow::bail!("Error creating `Venue` from '{value}': {e}");
        }

        Ok(Self(Ustr::from(value)))
    }

    /// Creates a new [`Venue`] instance.
    ///
    /// # Panics
    ///
    /// Panics if `value` is not a valid string.
    pub fn new<T: AsRef<str>>(value: T) -> Self {
        Self::new_checked(value).expect(FAILED)
    }

    /// Sets the inner identifier value.
    #[cfg_attr(not(feature = "python"), allow(dead_code))]
    pub(crate) fn set_inner(&mut self, value: &str) {
        self.0 = Ustr::from(value);
    }

    /// Returns the inner identifier value.
    #[must_use]
    pub fn inner(&self) -> Ustr {
        self.0
    }

    /// Returns the inner value as a string slice.
    #[must_use]
    pub fn as_str(&self) -> &str {
        self.0.as_str()
    }

    #[must_use]
    pub fn from_str_unchecked<T: AsRef<str>>(s: T) -> Self {
        Self(Ustr::from(s.as_ref()))
    }

    #[must_use]
    pub const fn from_ustr_unchecked(s: Ustr) -> Self {
        Self(s)
    }

    /// # Errors
    ///
    /// Returns an error if the venue code is unknown or lock on venue map fails.
    pub fn from_code(code: &str) -> anyhow::Result<Self> {
        let map_guard = VENUE_MAP
            .lock()
            .map_err(|e| anyhow::anyhow!("Error acquiring lock on `VENUE_MAP`: {e}"))?;
        map_guard
            .get(code)
            .copied()
            .ok_or_else(|| anyhow::anyhow!("Unknown venue code: {code}"))
    }

    #[must_use]
    pub fn synthetic() -> Self {
        // SAFETY: Unwrap safe as using known synthetic venue constant
        Self::new(SYNTHETIC_VENUE)
    }

    #[must_use]
    pub fn is_synthetic(&self) -> bool {
        self.0.as_str() == SYNTHETIC_VENUE
    }

    /// Returns true if the venue represents a decentralized exchange (contains ':').
    #[cfg(feature = "defi")]
    #[must_use]
    pub fn is_dex(&self) -> bool {
        self.0.as_str().contains(':')
    }

    #[cfg(feature = "defi")]
    /// Parses a venue string to extract blockchain and DEX type information.
    ///
    /// # Errors
    ///
    /// Returns an error if:
    /// - The venue string is not in the format "chain:dex"
    /// - The chain name is not recognized
    /// - The DEX name is not recognized
    pub fn parse_dex(&self) -> anyhow::Result<(Blockchain, DexType)> {
        let venue_str = self.as_str();

        if let Some((chain_name, dex_id)) = venue_str.split_once(':') {
            // Get the chain reference and extract the Blockchain enum
            let chain = Chain::from_chain_name(chain_name).ok_or_else(|| {
                anyhow::anyhow!("Invalid chain '{}' in venue '{}'", chain_name, venue_str)
            })?;

            // Get the DexType enum
            let dex_type = DexType::from_dex_name(dex_id).ok_or_else(|| {
                anyhow::anyhow!("Invalid DEX '{}' in venue '{}'", dex_id, venue_str)
            })?;

            Ok((chain.name, dex_type))
        } else {
            anyhow::bail!(
                "Venue '{}' is not a DEX venue (expected format 'Chain:DexId')",
                venue_str
            )
        }
    }
}

impl Debug for Venue {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self.0)
    }
}

impl Display for Venue {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}

/// Validates blockchain venue format "Chain:DexId".
///
/// # Errors
///
/// Returns an error if:
/// - Format is not "Chain:DexId" (missing colon or empty parts)
/// - Chain or Dex is not recognized
#[cfg(feature = "defi")]
pub fn validate_blockchain_venue(venue_part: &str) -> anyhow::Result<()> {
    if let Some((chain_name, dex_id)) = venue_part.split_once(':') {
        if chain_name.is_empty() || dex_id.is_empty() {
            anyhow::bail!(
                "invalid blockchain venue '{}': expected format 'Chain:DexId'",
                venue_part
            );
        }
        if Chain::from_chain_name(chain_name).is_none() {
            anyhow::bail!(
                "invalid blockchain venue '{}': chain '{}' not recognized",
                venue_part,
                chain_name
            );
        }
        if DexType::from_dex_name(dex_id).is_none() {
            anyhow::bail!(
                "invalid blockchain venue '{}': dex '{}' not recognized",
                venue_part,
                dex_id
            );
        }
        Ok(())
    } else {
        anyhow::bail!(
            "invalid blockchain venue '{}': expected format 'Chain:DexId'",
            venue_part
        );
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use rstest::rstest;

    #[cfg(feature = "defi")]
    use crate::defi::{Blockchain, DexType};
    use crate::identifiers::{Venue, stubs::*};

    #[rstest]
    fn test_string_reprs(venue_binance: Venue) {
        assert_eq!(venue_binance.as_str(), "BINANCE");
        assert_eq!(format!("{venue_binance}"), "BINANCE");
    }

    #[cfg(feature = "defi")]
    #[rstest]
    fn test_blockchain_venue_valid_dex_names() {
        // Test various valid DEX names
        let valid_dexes = vec![
            "UniswapV3",
            "UniswapV2",
            "UniswapV4",
            "SushiSwapV2",
            "SushiSwapV3",
            "PancakeSwapV3",
            "CamelotV3",
            "CurveFinance",
            "FluidDEX",
            "MaverickV1",
            "MaverickV2",
            "BaseX",
            "BaseSwapV2",
            "AerodromeV1",
            "AerodromeSlipstream",
            "BalancerV2",
            "BalancerV3",
        ];

        for dex_name in valid_dexes {
            let venue_str = format!("Arbitrum:{dex_name}");
            let venue = Venue::new(&venue_str);
            assert_eq!(venue.to_string(), venue_str);
        }
    }
    #[cfg(feature = "defi")]
    #[rstest]
    #[should_panic(
        expected = "Error creating `Venue` from 'InvalidChain:UniswapV3': invalid blockchain venue 'InvalidChain:UniswapV3': chain 'InvalidChain' not recognized"
    )]
    fn test_blockchain_venue_invalid_chain() {
        let _ = Venue::new("InvalidChain:UniswapV3");
    }

    #[cfg(feature = "defi")]
    #[rstest]
    #[should_panic(
        expected = "Error creating `Venue` from 'Arbitrum:': invalid blockchain venue 'Arbitrum:': expected format 'Chain:DexId'"
    )]
    fn test_blockchain_venue_empty_dex() {
        let _ = Venue::new("Arbitrum:");
    }

    #[cfg(feature = "defi")]
    #[rstest]
    fn test_regular_venue_with_blockchain_like_name_but_without_dex() {
        // Should work fine since it doesn't contain ':'
        let venue = Venue::new("Ethereum");
        assert_eq!(venue.to_string(), "Ethereum");
    }

    #[cfg(feature = "defi")]
    #[rstest]
    #[should_panic(
        expected = "Error creating `Venue` from 'Arbitrum:InvalidDex': invalid blockchain venue 'Arbitrum:InvalidDex': dex 'InvalidDex' not recognized"
    )]
    fn test_blockchain_venue_invalid_dex() {
        let _ = Venue::new("Arbitrum:InvalidDex");
    }

    #[cfg(feature = "defi")]
    #[rstest]
    #[should_panic(
        expected = "Error creating `Venue` from 'Arbitrum:uniswapv3': invalid blockchain venue 'Arbitrum:uniswapv3': dex 'uniswapv3' not recognized"
    )]
    fn test_blockchain_venue_dex_case_sensitive() {
        // DEX names should be case sensitive
        let _ = Venue::new("Arbitrum:uniswapv3");
    }

    #[cfg(feature = "defi")]
    #[rstest]
    fn test_blockchain_venue_various_chain_dex_combinations() {
        // Test various valid chain:dex combinations
        let valid_combinations = vec![
            ("Ethereum", "UniswapV2"),
            ("Ethereum", "BalancerV2"),
            ("Arbitrum", "CamelotV3"),
            ("Base", "AerodromeV1"),
            ("Polygon", "SushiSwapV3"),
        ];

        for (chain, dex) in valid_combinations {
            let venue_str = format!("{chain}:{dex}");
            let venue = Venue::new(&venue_str);
            assert_eq!(venue.to_string(), venue_str);
        }
    }

    #[cfg(feature = "defi")]
    #[rstest]
    #[case("Ethereum:UniswapV3", Blockchain::Ethereum, DexType::UniswapV3)]
    #[case("Arbitrum:CamelotV3", Blockchain::Arbitrum, DexType::CamelotV3)]
    #[case("Base:AerodromeV1", Blockchain::Base, DexType::AerodromeV1)]
    #[case("Polygon:SushiSwapV2", Blockchain::Polygon, DexType::SushiSwapV2)]
    fn test_parse_dex_valid(
        #[case] venue_str: &str,
        #[case] expected_chain: Blockchain,
        #[case] expected_dex: DexType,
    ) {
        let venue = Venue::new(venue_str);
        let (blockchain, dex_type) = venue.parse_dex().unwrap();

        assert_eq!(blockchain, expected_chain);
        assert_eq!(dex_type, expected_dex);
    }

    #[cfg(feature = "defi")]
    #[rstest]
    fn test_parse_dex_non_dex_venue() {
        let venue = Venue::new("BINANCE");
        let result = venue.parse_dex();
        assert!(result.is_err());
        assert!(
            result
                .unwrap_err()
                .to_string()
                .contains("is not a DEX venue")
        );
    }

    #[cfg(feature = "defi")]
    #[rstest]
    fn test_parse_dex_invalid_components() {
        // Test invalid chain
        let venue = Venue::from_str_unchecked("InvalidChain:UniswapV3");
        assert!(venue.parse_dex().is_err());

        // Test invalid DEX
        let venue = Venue::from_str_unchecked("Ethereum:InvalidDex");
        assert!(venue.parse_dex().is_err());
    }
}
```


---

## Overview

This file is located at `crates/model/src/identifiers/venue.rs` within the repository.

**Classes defined:** Venue, Venue, Debug, Display

**Functions defined:** set_inner, inner, as_str, from_ustr_unchecked, from_code, synthetic, is_synthetic, is_dex, parse_dex, fmt and 13 more


---

## Detailed Analysis

### Classes

#### `Venue`

**Type:** struct


#### `Venue`

**Type:** impl


#### `Debug`

**Type:** impl


#### `Display`

**Type:** impl


### Functions

#### `set_inner(&mut self, value: &str)`


#### `inner(&self)`


#### `as_str(&self)`


#### `from_ustr_unchecked(s: Ustr)`


#### `from_code(code: &str)`


#### `synthetic()`


#### `is_synthetic(&self)`


#### `is_dex(&self)`


#### `parse_dex(&self)`


#### `fmt(&self, f: &mut Formatter<'_>)`


#### `fmt(&self, f: &mut Formatter<'_>)`


#### `validate_blockchain_venue(venue_part: &str)`


#### `test_string_reprs(venue_binance: Venue)`


#### `test_blockchain_venue_valid_dex_names()`


#### `test_blockchain_venue_invalid_chain()`


#### `test_blockchain_venue_empty_dex()`


#### `test_regular_venue_with_blockchain_like_name_but_without_dex()`


#### `test_blockchain_venue_invalid_dex()`


#### `test_blockchain_venue_dex_case_sensitive()`


#### `test_blockchain_venue_various_chain_dex_combinations()`


#### `test_parse_dex_valid(
        #[case] venue_str: &str,
        #[case] expected_chain: Blockchain,
        #[case] expected_dex: DexType,
    )`


#### `test_parse_dex_non_dex_venue()`


#### `test_parse_dex_invalid_components()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/identifiers`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


