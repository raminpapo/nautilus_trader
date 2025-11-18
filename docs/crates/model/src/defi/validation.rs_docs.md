# Documentation: validation.rs

## File Metadata

- **Path**: `crates/model/src/defi/validation.rs`
- **Size**: 3,970 bytes
- **Lines**: 103
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

//! Validation utilities for blockchain data types.
//!
//! This module provides validation functions for ensuring the correctness and integrity
//! of blockchain-related data, particularly Ethereum addresses and other EVM-compatible
//! blockchain identifiers.

use std::str::FromStr;

use alloy_primitives::Address;

/// Validates an Ethereum address format, checksum, and returns the parsed address.
///
/// # Errors
///
/// This function returns an error if:
/// - The address does not start with the `0x` prefix.
/// - The address has invalid length (must be 42 characters including `0x`).
/// - The address contains invalid hexadecimal characters.
/// - The address has an incorrect checksum (for checksummed addresses).
pub fn validate_address(address: &str) -> anyhow::Result<Address> {
    // Check if the address starts with "0x"
    if !address.starts_with("0x") {
        anyhow::bail!("Ethereum address must start with '0x': {address}");
    }

    // Check if the address is valid
    let parsed_address = Address::from_str(address)
        .map_err(|e| anyhow::anyhow!("Blockchain address '{address}' is incorrect: {e}"))?;

    // Check if checksum is valid
    Address::parse_checksummed(address, None)
        .map_err(|_| anyhow::anyhow!("Blockchain address '{address}' has incorrect checksum"))?;

    Ok(parsed_address)
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_validate_address_invalid_prefix() {
        let invalid_address = "742d35Cc6634C0532925a3b844Bc454e4438f44e";
        let result = validate_address(invalid_address);
        assert!(result.is_err());
        assert_eq!(
            result.unwrap_err().to_string(),
            "Ethereum address must start with '0x': 742d35Cc6634C0532925a3b844Bc454e4438f44e"
        );
    }

    #[rstest]
    fn test_validate_invalid_address_format() {
        let invalid_length_address = "0x1233";
        let invalid_characters_address = "0xZZZd35Cc6634C0532925a3b844Bc454e4438f44e";

        assert_eq!(
            validate_address(invalid_length_address)
                .unwrap_err()
                .to_string(),
            "Blockchain address '0x1233' is incorrect: invalid string length"
        );
        assert_eq!(
            validate_address(invalid_characters_address)
                .unwrap_err()
                .to_string(),
            "Blockchain address '0xZZZd35Cc6634C0532925a3b844Bc454e4438f44e' is incorrect: invalid character 'Z' at position 0"
        );
    }

    #[rstest]
    fn test_validate_invalid_checksum() {
        let invalid_checksum_address = "0x742d35cc6634c0532925a3b844bc454e4438f44e";
        assert_eq!(
            validate_address(invalid_checksum_address)
                .unwrap_err()
                .to_string(),
            "Blockchain address '0x742d35cc6634c0532925a3b844bc454e4438f44e' has incorrect checksum"
        );
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`validate_address()`**: Function defined in this file
- **`test_validate_address_invalid_prefix()`**: Function defined in this file
- **`test_validate_invalid_address_format()`**: Function defined in this file
- **`test_validate_invalid_checksum()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `test_validate_address_invalid_prefix`, `test_validate_invalid_address_format`, `test_validate_invalid_checksum`, `validate_address`

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

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:02.435962Z*
