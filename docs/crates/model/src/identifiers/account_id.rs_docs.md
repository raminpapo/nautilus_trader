# Documentation: account_id.rs

## File Metadata

- **Path**: `crates/model/src/identifiers/account_id.rs`
- **Size**: 5,072 bytes
- **Lines**: 168
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

//! Represents a valid account ID.

use std::{
    fmt::{Debug, Display, Formatter},
    hash::Hash,
};

use nautilus_core::correctness::{FAILED, check_string_contains, check_valid_string_ascii};
use ustr::Ustr;

use super::Venue;

/// Represents a valid account ID.
#[repr(C)]
#[derive(Clone, Copy, Hash, PartialEq, Eq, PartialOrd, Ord)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.model")
)]
pub struct AccountId(Ustr);

impl AccountId {
    /// Creates a new [`AccountId`] instance with correctness checking.
    ///
    /// Must be correctly formatted with two valid strings either side of a hyphen '-'.
    ///
    /// It is expected an account ID is the name of the issuer with an account number
    /// separated by a hyphen.
    ///
    /// # Errors
    ///
    /// Returns an error if:
    /// - `value` is not a valid string.
    /// - `value` length is greater than 36.
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

    /// Creates a new [`AccountId`] instance.
    ///
    /// # Panics
    ///
    /// Panics if `value` is not a valid string, or value length is greater than 36.
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

    /// Returns the account issuer for this identifier.
    ///
    /// # Panics
    ///
    /// Panics if the internal ID does not contain a hyphen separator.
    #[must_use]
    pub fn get_issuer(&self) -> Venue {
        // SAFETY: Account ID is guaranteed to have chars either side of a hyphen
        Venue::from_str_unchecked(self.0.split_once('-').unwrap().0)
    }

    /// Returns the account ID assigned by the issuer.
    ///
    /// # Panics
    ///
    /// Panics if the internal ID does not contain a hyphen separator.
    #[must_use]
    pub fn get_issuers_id(&self) -> &str {
        // SAFETY: Account ID is guaranteed to have chars either side of a hyphen
        self.0.split_once('-').unwrap().1
    }
}

impl Debug for AccountId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self.0)
    }
}

impl Display for AccountId {
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

    use super::*;
    use crate::identifiers::stubs::*;

    #[rstest]
    #[should_panic]
    fn test_account_id_new_invalid_string() {
        AccountId::new("");
    }

    #[rstest]
    #[should_panic]
    fn test_account_id_new_missing_hyphen() {
        AccountId::new("123456789");
    }

    #[rstest]
    fn test_account_id_fmt() {
        let s = "IB-U123456789";
        let account_id = AccountId::new(s);
        let formatted = format!("{account_id}");
        assert_eq!(formatted, s);
    }

    #[rstest]
    fn test_string_reprs(account_ib: AccountId) {
        assert_eq!(account_ib.as_str(), "IB-1234567890");
    }

    #[rstest]
    fn test_get_issuer(account_ib: AccountId) {
        assert_eq!(account_ib.get_issuer(), Venue::new("IB"));
    }

    #[rstest]
    fn test_get_issuers_id(account_ib: AccountId) {
        assert_eq!(account_ib.get_issuers_id(), "1234567890");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 15 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new_checked()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`set_inner()`**: Function defined in this file
- **`inner()`**: Function defined in this file
- **`as_str()`**: Function defined in this file
- **`get_issuer()`**: Function defined in this file
- **`get_issuers_id()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`test_account_id_new_invalid_string()`**: Function defined in this file
- **`test_account_id_new_missing_hyphen()`**: Function defined in this file
- **`test_account_id_fmt()`**: Function defined in this file
- **`test_string_reprs()`**: Function defined in this file
- **`test_get_issuer()`**: Function defined in this file
- **`test_get_issuers_id()`**: Function defined in this file

### Classes
- **`AccountId`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 17


**Functions**: `as_str`, `fmt`, `get_issuer`, `get_issuers_id`, `inner`, `new`, `new_checked`, `set_inner`, `test_account_id_fmt`, `test_account_id_new_invalid_string`, `test_account_id_new_missing_hyphen`, `test_get_issuer`, `test_get_issuers_id`, `test_string_reprs`
**Impls**: `AccountId`, `Debug`, `Display`
**Structs**: `AccountId`

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
*Generated on 2025-11-18T21:55:02.636133Z*
