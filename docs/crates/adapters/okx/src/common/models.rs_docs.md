# Documentation: `crates/adapters/okx/src/common/models.rs`
**Generated:** 2025-11-15T19:40:01.225975Z
**File Size:** 3843 bytes
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

- **Path:** `crates/adapters/okx/src/common/models.rs`
- **Size:** 3,843 bytes
- **Lines:** 91
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1

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

//! Data models representing OKX API payloads consumed by the adapter.

use serde::{Deserialize, Serialize};
use ustr::Ustr;

use super::enums::OKXOptionType;
use crate::common::{
    enums::{OKXContractType, OKXInstrumentStatus, OKXInstrumentType},
    parse::deserialize_optional_string_to_u64,
};

/// Represents an instrument on the OKX exchange.
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
pub struct OKXInstrument {
    /// Product type (SPOT, MARGIN, SWAP, FUTURES, OPTION).
    pub inst_type: OKXInstrumentType,
    /// Instrument ID, e.g. "BTC-USD-SWAP".
    pub inst_id: Ustr,
    /// Underlying of the instrument, e.g. "BTC-USD". Only applicable to FUTURES/SWAP/OPTION.
    pub uly: Ustr,
    /// Instrument family, e.g. "BTC-USD". Only applicable to FUTURES/SWAP/OPTION.
    pub inst_family: Ustr,
    /// Base currency, e.g. "BTC" in BTC-USDT. Applicable to SPOT/MARGIN.
    pub base_ccy: Ustr,
    /// Quote currency, e.g. "USDT" in BTC-USDT.
    pub quote_ccy: Ustr,
    /// Settlement currency, e.g. "BTC" for BTC-USD-SWAP.
    pub settle_ccy: Ustr,
    /// Contract value. Only applicable to FUTURES/SWAP/OPTION.
    pub ct_val: String,
    /// Contract multiplier. Only applicable to FUTURES/SWAP/OPTION.
    pub ct_mult: String,
    /// Contract value currency. Only applicable to FUTURES/SWAP/OPTION.
    pub ct_val_ccy: String,
    /// Option type, "C" for call options, "P" for put options. Only applicable to OPTION.
    pub opt_type: OKXOptionType,
    /// Strike price. Only applicable to OPTION.
    pub stk: String,
    /// Listing time, Unix timestamp format in milliseconds, e.g. "1597026383085".
    #[serde(deserialize_with = "deserialize_optional_string_to_u64")]
    pub list_time: Option<u64>,
    /// Expiry time, Unix timestamp format in milliseconds, e.g. "1597026383085".
    #[serde(deserialize_with = "deserialize_optional_string_to_u64")]
    pub exp_time: Option<u64>,
    /// Leverage. Not applicable to SPOT.
    pub lever: String,
    /// Tick size, e.g. "0.1".
    pub tick_sz: String,
    /// Lot size, e.g. "1".
    pub lot_sz: String,
    /// Minimum order size.
    pub min_sz: String,
    /// Contract type. linear: "linear", inverse: "inverse". Only applicable to FUTURES/SWAP.
    pub ct_type: OKXContractType,
    /// Instrument status.
    pub state: OKXInstrumentStatus,
    /// Rule type, e.g. "DynamicPL", "CT", etc.
    pub rule_type: String,
    /// Maximum limit order size.
    pub max_lmt_sz: String,
    /// Maximum market order size.
    pub max_mkt_sz: String,
    /// Maximum limit order amount.
    pub max_lmt_amt: String,
    /// Maximum market order amount.
    pub max_mkt_amt: String,
    /// Maximum TWAP order size.
    pub max_twap_sz: String,
    /// Maximum iceberg order size.
    pub max_iceberg_sz: String,
    /// Maximum trigger order size.
    pub max_trigger_sz: String,
    /// Maximum stop order size.
    pub max_stop_sz: String,
}
```


---

## Overview

This file is located at `crates/adapters/okx/src/common/models.rs` within the repository.

**Classes defined:** OKXInstrument


---

## Detailed Analysis

### Classes

#### `OKXInstrument`

**Type:** struct



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/src/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


