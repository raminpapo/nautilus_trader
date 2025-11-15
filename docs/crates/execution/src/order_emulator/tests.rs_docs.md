# Documentation: `crates/execution/src/order_emulator/tests.rs`
**Generated:** 2025-11-15T19:40:02.119018Z
**File Size:** 2143 bytes
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

- **Path:** `crates/execution/src/order_emulator/tests.rs`
- **Size:** 2,143 bytes
- **Lines:** 50
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

use nautilus_model::{
    instruments::{CryptoPerpetual, stubs::crypto_perpetual_ethusdt},
    types::Price,
};
use rstest::rstest;

use crate::matching_core::OrderMatchingCore;

#[rstest]
fn test_stop_limit_order_triggered_before_market_data_retains_command(
    crypto_perpetual_ethusdt: CryptoPerpetual,
) {
    // This test validates that the OrderMatchingCore correctly handles
    // quote ticks with None bid/ask prices
    let instrument_id = crypto_perpetual_ethusdt.id;
    let price_increment = crypto_perpetual_ethusdt.price_increment;

    // Create a matching core
    let mut matching_core =
        OrderMatchingCore::new(instrument_id, price_increment, None, None, None);

    // Verify matching core has no market data initially
    assert!(matching_core.bid.is_none());
    assert!(matching_core.ask.is_none());

    // Process a quote tick to provide market data
    matching_core.set_bid_raw(Price::from("5060.00"));
    matching_core.set_ask_raw(Price::from("5070.00"));

    // Verify market data is now available
    assert!(matching_core.bid.is_some());
    assert!(matching_core.ask.is_some());
    assert_eq!(matching_core.bid.unwrap(), Price::from("5060.00"));
    assert_eq!(matching_core.ask.unwrap(), Price::from("5070.00"));
}
```


---

## Overview

This file is located at `crates/execution/src/order_emulator/tests.rs` within the repository.

**Functions defined:** test_stop_limit_order_triggered_before_market_data_retains_command


---

## Detailed Analysis

### Functions

#### `test_stop_limit_order_triggered_before_market_data_retains_command(
    crypto_perpetual_ethusdt: CryptoPerpetual,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution/src/order_emulator`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


