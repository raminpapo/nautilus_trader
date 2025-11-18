# Documentation: consts.rs

## File Metadata

- **Path**: `crates/adapters/bitmex/src/common/consts.rs`
- **Size**: 1,513 bytes
- **Lines**: 33
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

//! BitMEX adapter constants including base URLs and the venue identifier.

use std::sync::LazyLock;

use nautilus_model::identifiers::Venue;
use ustr::Ustr;

pub const BITMEX: &str = "BITMEX";

pub const BITMEX_WS_URL: &str = "wss://ws.bitmex.com/realtime";
pub const BITMEX_WS_TESTNET_URL: &str = "wss://ws.testnet.bitmex.com/realtime";
pub const BITMEX_HTTP_URL: &str = "https://www.bitmex.com/api/v1";
pub const BITMEX_HTTP_TESTNET_URL: &str = "https://testnet.bitmex.com/api/v1";

pub const BITMEX_WS_TOPIC_DELIMITER: char = ':';

pub static BITMEX_VENUE: LazyLock<Venue> = LazyLock::new(|| Venue::new(Ustr::from(BITMEX)));

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/adapters/bitmex/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:54:58.936886Z*
