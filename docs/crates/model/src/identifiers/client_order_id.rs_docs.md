# Documentation: `crates/model/src/identifiers/client_order_id.rs`
**Generated:** 2025-11-15T19:40:02.755971Z
**File Size:** 5251 bytes
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

- **Path:** `crates/model/src/identifiers/client_order_id.rs`
- **Size:** 5,251 bytes
- **Lines:** 163
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 10

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

//! Represents a valid client order ID (assigned by the Nautilus system).

use std::{
    fmt::{Debug, Display, Formatter},
    hash::Hash,
};

use nautilus_core::correctness::{FAILED, check_valid_string_ascii};
use ustr::Ustr;

/// Represents a valid client order ID (assigned by the Nautilus system).
#[repr(C)]
#[derive(Clone, Copy, Hash, PartialEq, Eq, PartialOrd, Ord)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.model")
)]
pub struct ClientOrderId(Ustr);

impl ClientOrderId {
    /// Creates a new [`ClientOrderId`] instance with correctness checking.
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
        Ok(Self(Ustr::from(value)))
    }

    /// Creates a new [`ClientOrderId`] instance.
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

    /// Returns the inner identifier value as a string slice.
    #[must_use]
    pub fn as_str(&self) -> &str {
        self.0.as_str()
    }
}

impl Debug for ClientOrderId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{:?}", self.0)
    }
}

impl Display for ClientOrderId {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}

#[must_use]
pub fn optional_ustr_to_vec_client_order_ids(s: Option<Ustr>) -> Option<Vec<ClientOrderId>> {
    s.map(|ustr| {
        let s_str = ustr.to_string();
        s_str
            .split(',')
            .map(ClientOrderId::new)
            .collect::<Vec<ClientOrderId>>()
    })
}

#[must_use]
pub fn optional_vec_client_order_ids_to_ustr(vec: Option<Vec<ClientOrderId>>) -> Option<Ustr> {
    vec.map(|client_order_ids| {
        let s: String = client_order_ids
            .into_iter()
            .map(|id| id.to_string())
            .collect::<Vec<String>>()
            .join(",");
        Ustr::from(&s)
    })
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use rstest::rstest;
    use ustr::Ustr;

    use super::ClientOrderId;
    use crate::identifiers::{
        client_order_id::{
            optional_ustr_to_vec_client_order_ids, optional_vec_client_order_ids_to_ustr,
        },
        stubs::*,
    };

    #[rstest]
    fn test_string_reprs(client_order_id: ClientOrderId) {
        assert_eq!(client_order_id.as_str(), "O-19700101-000000-001-001-1");
        assert_eq!(format!("{client_order_id}"), "O-19700101-000000-001-001-1");
    }

    #[rstest]
    fn test_optional_ustr_to_vec_client_order_ids() {
        // Test with None
        assert_eq!(optional_ustr_to_vec_client_order_ids(None), None);

        // Test with Some
        let ustr = Ustr::from("id1,id2,id3");
        let client_order_ids = optional_ustr_to_vec_client_order_ids(Some(ustr)).unwrap();
        assert_eq!(client_order_ids[0].as_str(), "id1");
        assert_eq!(client_order_ids[1].as_str(), "id2");
        assert_eq!(client_order_ids[2].as_str(), "id3");
    }

    #[rstest]
    fn test_optional_vec_client_order_ids_to_ustr() {
        // Test with None
        assert_eq!(optional_vec_client_order_ids_to_ustr(None), None);

        // Test with Some
        let client_order_ids = vec![
            ClientOrderId::from("id1"),
            ClientOrderId::from("id2"),
            ClientOrderId::from("id3"),
        ];
        let ustr = optional_vec_client_order_ids_to_ustr(Some(client_order_ids)).unwrap();
        assert_eq!(ustr.to_string(), "id1,id2,id3");
    }
}
```


---

## Overview

This file is located at `crates/model/src/identifiers/client_order_id.rs` within the repository.

**Classes defined:** ClientOrderId, ClientOrderId, Debug, Display

**Functions defined:** set_inner, inner, as_str, fmt, fmt, optional_ustr_to_vec_client_order_ids, optional_vec_client_order_ids_to_ustr, test_string_reprs, test_optional_ustr_to_vec_client_order_ids, test_optional_vec_client_order_ids_to_ustr


---

## Detailed Analysis

### Classes

#### `ClientOrderId`

**Type:** struct


#### `ClientOrderId`

**Type:** impl


#### `Debug`

**Type:** impl


#### `Display`

**Type:** impl


### Functions

#### `set_inner(&mut self, value: &str)`


#### `inner(&self)`


#### `as_str(&self)`


#### `fmt(&self, f: &mut Formatter<'_>)`


#### `fmt(&self, f: &mut Formatter<'_>)`


#### `optional_ustr_to_vec_client_order_ids(s: Option<Ustr>)`


#### `optional_vec_client_order_ids_to_ustr(vec: Option<Vec<ClientOrderId>>)`


#### `test_string_reprs(client_order_id: ClientOrderId)`


#### `test_optional_ustr_to_vec_client_order_ids()`


#### `test_optional_vec_client_order_ids_to_ustr()`



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


