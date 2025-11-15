# Documentation: `crates/adapters/databento/src/enums.rs`
**Generated:** 2025-11-15T19:40:00.857084Z
**File Size:** 3498 bytes
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

- **Path:** `crates/adapters/databento/src/enums.rs`
- **Size:** 3,498 bytes
- **Lines:** 123
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 2

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

//! Enumerations for the Databento integration.

use std::str::FromStr;

use nautilus_model::{enum_strum_serde, enums::FromU8};
use serde::{Deserialize, Deserializer, Serialize, Serializer};
use strum::{AsRefStr, Display, EnumIter, EnumString, FromRepr};

/// Represents a Databento statistic type.
#[repr(C)]
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    Hash,
    PartialEq,
    Eq,
    PartialOrd,
    Ord,
    AsRefStr,
    FromRepr,
    EnumIter,
    EnumString,
)]
#[strum(ascii_case_insensitive)]
#[strum(serialize_all = "SCREAMING_SNAKE_CASE")]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(eq, eq_int, module = "nautilus_trader.core.nautilus_pyo3.databento")
)]
pub enum DatabentoStatisticType {
    OpeningPrice = 1,
    IndicativeOpeningPrice = 2,
    SettlementPrice = 3,
    TradingSessionLowPrice = 4,
    TradingSessionHighPrice = 5,
    ClearedVolume = 6,
    LowestOffer = 7,
    HighestBid = 8,
    OpenInterest = 9,
    FixingPrice = 10,
    ClosePrice = 11,
    NetChange = 12,
    Vwap = 13,
}

impl FromU8 for DatabentoStatisticType {
    fn from_u8(value: u8) -> Option<Self> {
        match value {
            1 => Some(Self::OpeningPrice),
            2 => Some(Self::IndicativeOpeningPrice),
            3 => Some(Self::SettlementPrice),
            4 => Some(Self::TradingSessionLowPrice),
            5 => Some(Self::TradingSessionHighPrice),
            6 => Some(Self::ClearedVolume),
            7 => Some(Self::LowestOffer),
            8 => Some(Self::HighestBid),
            9 => Some(Self::OpenInterest),
            10 => Some(Self::FixingPrice),
            11 => Some(Self::ClosePrice),
            12 => Some(Self::NetChange),
            13 => Some(Self::Vwap),
            _ => None,
        }
    }
}

/// Represents a Databento statistic update action.
#[repr(C)]
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    Hash,
    PartialEq,
    Eq,
    PartialOrd,
    Ord,
    AsRefStr,
    FromRepr,
    EnumIter,
    EnumString,
)]
#[strum(ascii_case_insensitive)]
#[strum(serialize_all = "SCREAMING_SNAKE_CASE")]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(eq, eq_int, module = "nautilus_trader.core.nautilus_pyo3.databento")
)]
pub enum DatabentoStatisticUpdateAction {
    Added = 1,
    Deleted = 2,
}

impl FromU8 for DatabentoStatisticUpdateAction {
    fn from_u8(value: u8) -> Option<Self> {
        match value {
            1 => Some(Self::Added),
            2 => Some(Self::Deleted),
            _ => None,
        }
    }
}

enum_strum_serde!(DatabentoStatisticType);
enum_strum_serde!(DatabentoStatisticUpdateAction);
```


---

## Overview

This file is located at `crates/adapters/databento/src/enums.rs` within the repository.

**Classes defined:** FromU8, FromU8

**Functions defined:** from_u8, from_u8


---

## Detailed Analysis

### Classes

#### `FromU8`

**Type:** impl


#### `FromU8`

**Type:** impl


### Functions

#### `from_u8(value: u8)`


#### `from_u8(value: u8)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento/src`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: session. Ensure proper handling of secrets.


