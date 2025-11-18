# Documentation: stubs.rs

## File Metadata

- **Path**: `crates/model/src/types/stubs.rs`
- **Size**: 1,416 bytes
- **Lines**: 37
- **Language**: Rust

## Original Source

```rust
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

use rstest::fixture;

use crate::{
    identifiers::stubs::instrument_id_btc_usdt,
    types::{AccountBalance, MarginBalance, Money},
};

#[fixture]
pub fn stub_account_balance() -> AccountBalance {
    let total = Money::from("1525000 USD");
    let locked = Money::from("25000 USD");
    let free = Money::from("1500000 USD");
    AccountBalance::new(total, locked, free)
}

#[fixture]
pub fn stub_margin_balance() -> MarginBalance {
    let initial = Money::from("5000 USD");
    let maintenance = Money::from("20000 USD");
    let instrument = instrument_id_btc_usdt();
    MarginBalance::new(initial, maintenance, instrument)
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`stub_account_balance()`**: Function defined in this file
- **`stub_margin_balance()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `stub_account_balance`, `stub_margin_balance`

## Related Files

This file is located in `crates/model/src/types/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.309184Z*
