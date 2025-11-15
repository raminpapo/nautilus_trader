# Documentation: `crates/common/src/python/xrate.rs`
**Generated:** 2025-11-15T19:40:01.833976Z
**File Size:** 2039 bytes
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

- **Path:** `crates/common/src/python/xrate.rs`
- **Size:** 2,039 bytes
- **Lines:** 53
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


---

## Overview

This file is located at `crates/common/src/python/xrate.rs` within the repository.

**Functions defined:** py_get_exchange_rate


---

## Detailed Analysis

### Functions

#### `py_get_exchange_rate(
    from_currency: &str,
    to_currency: &str,
    price_type: PriceType,
    quotes_bid: HashMap<String, f64>,
    quotes_ask: HashMap<String, f64>,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


