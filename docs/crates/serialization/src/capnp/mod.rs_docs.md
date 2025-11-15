# Documentation: `crates/serialization/src/capnp/mod.rs`
**Generated:** 2025-11-15T19:40:03.738690Z
**File Size:** 3027 bytes
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

- **Path:** `crates/serialization/src/capnp/mod.rs`
- **Size:** 3,027 bytes
- **Lines:** 79
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 3

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

//! Cap'n Proto serialization for Nautilus types.
//!
//! This module provides Cap'n Proto serialization support for Nautilus domain types.
//! The generated schema modules are available at the crate root for proper cross-referencing.
//!
//! # Generated modules
//!
//! The following modules are generated from Cap'n Proto schemas:
//! - `crate::base_capnp` - Base types (UUID4, UnixNanos, StringMap)
//! - `crate::identifiers_capnp` - Identifier types
//! - `crate::types_capnp` - Value types (Price, Quantity, Money, etc.)
//! - `crate::enums_capnp` - Enumerations
//! - `crate::trading_capnp` - Trading commands
//! - `crate::data_capnp` - Data commands and responses
//! - `crate::order_capnp` - Order events
//! - `crate::position_capnp` - Position events
//! - `crate::account_capnp` - Account events
//! - `crate::market_capnp` - Market data types

#![cfg(feature = "capnp")]

pub mod conversions;

// Re-export generated modules for convenience.
// Re-export conversion functions for use by other crates
pub use conversions::order_side_to_capnp;

pub use crate::{
    account_capnp, base_capnp, data_capnp, enums_capnp, identifiers_capnp, market_capnp,
    order_capnp, position_capnp, trading_capnp, types_capnp,
};

/// Trait for converting Rust types to Cap'n Proto builders.
pub trait ToCapnp<'a> {
    /// The Cap'n Proto builder type for this Rust type.
    type Builder;

    /// Convert this Rust value to a Cap'n Proto builder.
    fn to_capnp(&self, builder: Self::Builder);
}

/// Trait for converting Cap'n Proto readers to Rust types.
pub trait FromCapnp<'a> {
    /// The Cap'n Proto reader type for this Rust type.
    type Reader;

    /// Convert a Cap'n Proto reader to this Rust type.
    ///
    /// # Errors
    ///
    /// Returns an error if the Cap'n Proto data is invalid or cannot be converted.
    fn from_capnp(reader: Self::Reader) -> Result<Self, Box<dyn std::error::Error>>
    where
        Self: Sized;
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_capnp_feature_enabled() {
        // This test ensures the capnp feature is properly configured
        assert!(cfg!(feature = "capnp"));
    }
}
```


---

## Overview

This file is located at `crates/serialization/src/capnp/mod.rs` within the repository.

**Functions defined:** to_capnp, from_capnp, test_capnp_feature_enabled


---

## Detailed Analysis

### Functions

#### `to_capnp(&self, builder: Self::Builder)`


#### `from_capnp(reader: Self::Reader)`


#### `test_capnp_feature_enabled()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/serialization/src/capnp`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


