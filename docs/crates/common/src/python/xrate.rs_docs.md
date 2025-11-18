# Documentation: xrate.rs

## File Metadata

- **Path**: `crates/common/src/python/xrate.rs`
- **Size**: 2,039 bytes
- **Lines**: 54
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

use std::collections::HashMap;

use ahash::AHashMap;
use nautilus_core::python::to_pyvalue_err;
use nautilus_model::enums::PriceType;
use pyo3::prelude::*;
use ustr::Ustr;

use crate::xrate::get_exchange_rate;

/// Calculates the exchange rate between two currencies using provided bid and ask quotes.
///
/// # Errors
///
/// Returns an error if:
/// - `price_type` is equal to `Last` or `Mark` (cannot calculate from quotes).
/// - `quotes_bid` or `quotes_ask` is empty.
/// - `quotes_bid` and `quotes_ask` lengths are not equal.
/// - The bid or ask side of a pair is missing.
#[pyfunction]
#[pyo3(name = "get_exchange_rate")]
#[pyo3(signature = (from_currency, to_currency, price_type, quotes_bid, quotes_ask))]
pub fn py_get_exchange_rate(
    from_currency: &str,
    to_currency: &str,
    price_type: PriceType,
    quotes_bid: HashMap<String, f64>,
    quotes_ask: HashMap<String, f64>,
) -> PyResult<Option<f64>> {
    get_exchange_rate(
        Ustr::from(from_currency),
        Ustr::from(to_currency),
        price_type,
        AHashMap::from_iter(quotes_bid),
        AHashMap::from_iter(quotes_ask),
    )
    .map_err(to_pyvalue_err)
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`py_get_exchange_rate()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `py_get_exchange_rate`

## Related Files

This file is located in `crates/common/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.291036Z*
