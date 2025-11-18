# Documentation: bit_math.rs

## File Metadata

- **Path**: `crates/model/src/defi/tick_map/bit_math.rs`
- **Size**: 2,354 bytes
- **Lines**: 71
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

use alloy_primitives::U256;

/// Returns the position of the most significant bit (highest set bit) in a U256 number.
pub fn most_significant_bit(x: U256) -> i32 {
    if x.is_zero() {
        return 0;
    }

    255 - x.leading_zeros() as i32
}

/// Returns the position of the least significant bit (lowest set bit) in a U256 number.
pub fn least_significant_bit(x: U256) -> i32 {
    if x.is_zero() {
        return 0;
    }
    x.trailing_zeros() as i32
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_most_significant_bit() {
        for i in 0..=255 {
            let x = U256::ONE << i;
            assert_eq!(most_significant_bit(x), i);
        }
        for i in 1..=255 {
            let x = (U256::ONE << i) - U256::ONE;
            assert_eq!(most_significant_bit(x), i - 1);
        }
        assert_eq!(most_significant_bit(U256::MAX), 255);
    }

    #[rstest]
    fn test_least_significant_bit() {
        for i in 0..=255 {
            let x = U256::ONE << i;
            assert_eq!(least_significant_bit(x), i);
        }
        for i in 1..=255 {
            let x = (U256::ONE << i) - U256::ONE;
            assert_eq!(least_significant_bit(x), 0);
        }
        assert_eq!(least_significant_bit(U256::MAX), 0);
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`most_significant_bit()`**: Function defined in this file
- **`least_significant_bit()`**: Function defined in this file
- **`test_most_significant_bit()`**: Function defined in this file
- **`test_least_significant_bit()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `least_significant_bit`, `most_significant_bit`, `test_least_significant_bit`, `test_most_significant_bit`

## Related Files

This file is located in `crates/model/src/defi/tick_map/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.390722Z*
