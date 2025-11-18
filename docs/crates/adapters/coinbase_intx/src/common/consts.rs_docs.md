# Documentation: consts.rs

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/src/common/consts.rs`
- **Size**: 1,584 bytes
- **Lines**: 31
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

use std::sync::LazyLock;

use nautilus_model::identifiers::Venue;
use ustr::Ustr;

pub const COINBASE_INTX: &str = "COINBASE_INTX";
pub static COINBASE_INTX_VENUE: LazyLock<Venue> =
    LazyLock::new(|| Venue::new(Ustr::from(COINBASE_INTX)));

// Coinbase International Exchange constants
pub const COINBASE_INTX_REST_URL: &str = "https://api.international.coinbase.com";
pub const COINBASE_INTX_REST_SANDBOX_URL: &str = "https://api-n5e1.coinbase.com";
pub const COINBASE_INTX_WS_URL: &str = "wss://ws-md.international.coinbase.com";
pub const COINBASE_INTX_WS_SANDBOX_URL: &str = "wss://ws-md.n5e2.coinbase.com";
pub const COINBASE_INTX_FIX_DROP_COPY: &str = "fix.international.coinbase.com:6130";

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/adapters/coinbase_intx/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.567141Z*
