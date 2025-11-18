# Documentation: testing.rs

## File Metadata

- **Path**: `crates/indicators/src/testing.rs`
- **Size**: 1,563 bytes
- **Lines**: 42
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

//! Common test related helper functions.

/// Checks if two floating-point numbers are approximately equal within the
/// margin of floating-point precision.
///
/// - `a`: The first floating-point number.
/// - `b`: The second floating-point number.
///
/// # Returns
///
/// Returns `true` if the absolute difference between `a` and `b` is less than
/// `f64::EPSILON`, indicating that they are approximately equal.
///
/// # Example
///
/// ```
/// use nautilus_indicators::testing::approx_equal;
///
/// let a = 0.1 + 0.2;
/// let b = 0.3;
/// assert!(approx_equal(a, b));
/// ```
#[must_use]
pub fn approx_equal(a: f64, b: f64) -> bool {
    (a - b).abs() < f64::EPSILON
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`approx_equal()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `approx_equal`

## Related Files

This file is located in `crates/indicators/src/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/indicators/src/testing.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:01.957631Z*
