# Documentation: `crates/model/src/identifiers/account_id.rs`
**Generated:** 2025-11-15T19:40:02.751305Z
**File Size:** 5072 bytes
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

- **Path:** `crates/model/src/identifiers/account_id.rs`
- **Size:** 5,072 bytes
- **Lines:** 167
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 13

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


---

## Overview

This file is located at `crates/model/src/identifiers/account_id.rs` within the repository.

**Classes defined:** AccountId, AccountId, Debug, Display

**Functions defined:** set_inner, inner, as_str, get_issuer, get_issuers_id, fmt, fmt, test_account_id_new_invalid_string, test_account_id_new_missing_hyphen, test_account_id_fmt and 3 more


---

## Detailed Analysis

### Classes

#### `AccountId`

**Type:** struct


#### `AccountId`

**Type:** impl


#### `Debug`

**Type:** impl


#### `Display`

**Type:** impl


### Functions

#### `set_inner(&mut self, value: &str)`


#### `inner(&self)`


#### `as_str(&self)`


#### `get_issuer(&self)`


#### `get_issuers_id(&self)`


#### `fmt(&self, f: &mut Formatter<'_>)`


#### `fmt(&self, f: &mut Formatter<'_>)`


#### `test_account_id_new_invalid_string()`


#### `test_account_id_new_missing_hyphen()`


#### `test_account_id_fmt()`


#### `test_string_reprs(account_ib: AccountId)`


#### `test_get_issuer(account_ib: AccountId)`


#### `test_get_issuers_id(account_ib: AccountId)`



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


