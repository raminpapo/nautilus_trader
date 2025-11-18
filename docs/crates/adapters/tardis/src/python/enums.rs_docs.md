# Documentation: enums.rs

## File Metadata

- **Path**: `crates/adapters/tardis/src/python/enums.rs`
- **Size**: 1,968 bytes
- **Lines**: 53
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

use pyo3::prelude::*;
use strum::IntoEnumIterator;

use crate::enums::TardisExchange;

#[must_use]
#[pyfunction(name = "tardis_exchanges")]
pub fn py_tardis_exchanges() -> Vec<String> {
    TardisExchange::iter().map(|e| e.to_string()).collect()
}

#[must_use]
#[pyfunction(name = "tardis_exchange_from_venue_str")]
pub fn py_tardis_exchange_from_venue_str(venue_str: &str) -> Vec<String> {
    TardisExchange::from_venue_str(venue_str)
        .iter()
        .map(ToString::to_string)
        .collect()
}

#[must_use]
#[pyfunction(name = "tardis_exchange_to_venue_str")]
pub fn py_tardis_exchange_to_venue_str(exchange_str: &str) -> String {
    match exchange_str.parse::<TardisExchange>() {
        Ok(exchange) => exchange.as_venue_str().to_string(),
        Err(_) => String::new(),
    }
}

#[must_use]
#[pyfunction(name = "tardis_exchange_is_option_exchange")]
pub fn py_tardis_exchange_is_option_exchange(exchange_str: &str) -> bool {
    match exchange_str.parse::<TardisExchange>() {
        Ok(exchange) => exchange.is_option_exchange(),
        Err(_) => false,
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`py_tardis_exchanges()`**: Function defined in this file
- **`py_tardis_exchange_from_venue_str()`**: Function defined in this file
- **`py_tardis_exchange_to_venue_str()`**: Function defined in this file
- **`py_tardis_exchange_is_option_exchange()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `py_tardis_exchange_from_venue_str`, `py_tardis_exchange_is_option_exchange`, `py_tardis_exchange_to_venue_str`, `py_tardis_exchanges`

## Related Files

This file is located in `crates/adapters/tardis/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.729583Z*
