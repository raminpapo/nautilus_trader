# Documentation: tests.rs

## File Metadata

- **Path**: `crates/execution/src/order_emulator/tests.rs`
- **Size**: 2,143 bytes
- **Lines**: 51
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`test_stop_limit_order_triggered_before_market_data_retains_command()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `test_stop_limit_order_triggered_before_market_data_retains_command`

## Related Files

This file is located in `crates/execution/src/order_emulator/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/execution/src/order_emulator/tests.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:01.729942Z*
