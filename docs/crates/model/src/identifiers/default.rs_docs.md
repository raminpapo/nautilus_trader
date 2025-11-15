# Documentation: `crates/model/src/identifiers/default.rs`
**Generated:** 2025-11-15T19:40:02.758951Z
**File Size:** 2635 bytes
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

- **Path:** `crates/model/src/identifiers/default.rs`
- **Size:** 2,635 bytes
- **Lines:** 88
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 10
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

use crate::identifiers::{
    AccountId, ClientId, ClientOrderId, PositionId, StrategyId, Symbol, TradeId, TraderId, Venue,
    VenueOrderId,
};

impl Default for AccountId {
    /// Creates a new default [`AccountId`] instance for testing.
    fn default() -> Self {
        Self::from("SIM-001")
    }
}

impl Default for ClientId {
    /// Creates a new default [`ClientId`] instance for testing.
    fn default() -> Self {
        Self::from("SIM")
    }
}

impl Default for ClientOrderId {
    /// Creates a new default [`ClientOrderId`] instance for testing.
    fn default() -> Self {
        Self::from("O-19700101-000000-001-001-1")
    }
}

impl Default for PositionId {
    /// Creates a new default [`PositionId`] instance for testing.
    fn default() -> Self {
        Self::from("P-001")
    }
}

impl Default for StrategyId {
    /// Creates a new default [`StrategyId`] instance for testing.
    fn default() -> Self {
        Self::from("S-001")
    }
}

impl Default for TradeId {
    /// Creates a new default [`TradeId`] instance for testing.
    fn default() -> Self {
        Self::from("1")
    }
}

impl Default for TraderId {
    /// Creates a new default [`TraderId`] instance for testing.
    fn default() -> Self {
        Self::from("TRADER-001")
    }
}
impl Default for Symbol {
    /// Creates a new default [`Symbol`] instance for testing.
    fn default() -> Self {
        Self::from("AUD/USD")
    }
}

impl Default for Venue {
    /// Creates a new default [`Venue`] instance for testing.
    fn default() -> Self {
        Self::from("SIM")
    }
}

impl Default for VenueOrderId {
    /// Creates a new default [`VenueOrderId`] instance for testing.
    fn default() -> Self {
        Self::from("001")
    }
}
```


---

## Overview

This file is located at `crates/model/src/identifiers/default.rs` within the repository.

**Classes defined:** Default, Default, Default, Default, Default, Default, Default, Default, Default, Default

**Functions defined:** default, default, default, default, default, default, default, default, default, default


---

## Detailed Analysis

### Classes

#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


#### `Default`

**Type:** impl


### Functions

#### `default()`


#### `default()`


#### `default()`


#### `default()`


#### `default()`


#### `default()`


#### `default()`


#### `default()`


#### `default()`


#### `default()`



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


