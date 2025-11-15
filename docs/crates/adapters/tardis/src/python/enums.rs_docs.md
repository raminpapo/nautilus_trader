# Documentation: `crates/adapters/tardis/src/python/enums.rs`
**Generated:** 2025-11-15T19:40:01.488214Z
**File Size:** 1968 bytes
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

- **Path:** `crates/adapters/tardis/src/python/enums.rs`
- **Size:** 1,968 bytes
- **Lines:** 52
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 4

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


---

## Overview

This file is located at `crates/adapters/tardis/src/python/enums.rs` within the repository.

**Functions defined:** py_tardis_exchanges, py_tardis_exchange_from_venue_str, py_tardis_exchange_to_venue_str, py_tardis_exchange_is_option_exchange


---

## Detailed Analysis

### Functions

#### `py_tardis_exchanges()`


#### `py_tardis_exchange_from_venue_str(venue_str: &str)`


#### `py_tardis_exchange_to_venue_str(exchange_str: &str)`


#### `py_tardis_exchange_is_option_exchange(exchange_str: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


