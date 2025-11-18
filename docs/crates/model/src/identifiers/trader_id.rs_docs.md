# Documentation: trader_id.rs

## File Metadata

- **Path**: `crates/model/src/identifiers/trader_id.rs`
- **Size**: 4,255 bytes
- **Lines**: 129
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

//! Represents a valid trader ID.

use std::fmt::{Debug, Display, Formatter};

use nautilus_core::correctness::{FAILED, check_string_contains, check_valid_string_ascii};
use ustr::Ustr;

/// Represents a valid trader ID.
#[repr(C)]
#[derive(Clone, Copy, Hash, PartialEq, Eq, PartialOrd, Ord)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.model")
)]
pub struct TraderId(Ustr);

impl TraderId {
    /// Creates a new [`TraderId`] instance.
    ///
    /// Must be correctly formatted with two valid strings either side of a hyphen.
    /// It is expected a trader ID is the abbreviated name of the trader
    /// with an order ID tag number separated by a hyphen.
    ///
    /// Example: "TESTER-001".
    ///
    /// The reason for the numerical component of the ID is so that order and position IDs
    /// do not collide with those from another node instance.
    ///
    /// # Errors
    ///
    /// Returns an error if `value` is not a valid string, or does not contain a hyphen '-' separator.
    ///
    /// # Notes
    ///
    /// PyO3 requires a `Result` type for proper error handling and stacktrace printing in Python.
    pub fn new_checked<T: AsRef<str>>(value: T) -> anyhow::Result<Self> {
        let value = value.as_ref();
        check_valid_string_ascii(value, stringify!(value))?;
        check_string_contains(value, "-", stringify!(value))?;
        Ok(Self(Ustr::from(value)))
    }

    /// Creates a new [`TraderId`] instance.
    ///
    /// # Panics
    ///
    /// Panics if `value` is not a valid string, or does not contain a hyphen '-' separator.
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

    /// Returns the inner identifier value as a string slice.
    #[must_use]
    pub fn as_str(&self) -> &str {
        self.0.as_str()
    }

    /// Returns the numerical tag portion of the trader ID.
    ///
    /// # Panics
    ///
    /// Panics if the internal ID string does not contain a '-' separator.
    #[must_use]
    pub fn get_tag(&self) -> &str {
        // SAFETY: Unwrap safe as value previously validated
        self.0.split('-').next_back().unwrap()
    }
}

impl Debug for TraderId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self.0)
    }
}

impl Display for TraderId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use rstest::rstest;

    use crate::identifiers::{stubs::*, trader_id::TraderId};

    #[rstest]
    fn test_string_reprs(trader_id: TraderId) {
        assert_eq!(trader_id.as_str(), "TRADER-001");
        assert_eq!(format!("{trader_id}"), "TRADER-001");
    }

    #[rstest]
    fn test_get_tag(trader_id: TraderId) {
        assert_eq!(trader_id.get_tag(), "001");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 10 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new_checked()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`set_inner()`**: Function defined in this file
- **`inner()`**: Function defined in this file
- **`as_str()`**: Function defined in this file
- **`get_tag()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`test_string_reprs()`**: Function defined in this file
- **`test_get_tag()`**: Function defined in this file

### Classes
- **`TraderId`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 12


**Functions**: `as_str`, `fmt`, `get_tag`, `inner`, `new`, `new_checked`, `set_inner`, `test_get_tag`, `test_string_reprs`
**Impls**: `Debug`, `Display`, `TraderId`
**Structs**: `TraderId`

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
*Generated on 2025-11-18T21:55:02.672596Z*
