# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/hyperliquid/src/common/mod.rs`
- **Size**: 1,960 bytes
- **Lines**: 42
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

pub mod consts;
pub mod converters;
pub mod credential;
pub mod enums;
pub mod models;
pub mod parse;
pub mod types;

pub use converters::{
    determine_tpsl_type, hyperliquid_conditional_to_nautilus, hyperliquid_order_type_to_nautilus,
    hyperliquid_time_in_force_to_nautilus, nautilus_order_type_to_hyperliquid,
    nautilus_time_in_force_to_hyperliquid, nautilus_to_hyperliquid_conditional,
};
pub use enums::{
    HyperliquidOrderStatus, HyperliquidProductType, hyperliquid_status_to_order_status,
};
pub use models::{
    ConversionError, HyperliquidAccountEvent, HyperliquidAccountState, HyperliquidBalance,
    HyperliquidDataConverter, HyperliquidInstrumentCache, HyperliquidInstrumentInfo,
    HyperliquidPositionData, HyperliquidTradeKey, LatencyModel, parse_position_status_report,
};
pub use parse::{
    deserialize_decimal_from_str, deserialize_optional_decimal_from_str, ensure_min_notional,
    normalize_order, normalize_price, normalize_quantity, round_down_to_step, round_down_to_tick,
    serialize_decimal_as_str, serialize_optional_decimal_as_str,
};

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/adapters/hyperliquid/src/common/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:54:59.979009Z*
