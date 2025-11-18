# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/hyperliquid/src/python/mod.rs`
- **Size**: 2,364 bytes
- **Lines**: 57
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

//! Python bindings from `pyo3`.

pub mod enums;
pub mod http;
pub mod urls;
pub mod websocket;

use nautilus_core::python::to_pyvalue_err;
use pyo3::prelude::*;

/// Extract product type from a Hyperliquid symbol.
///
/// # Errors
///
/// Returns an error if the symbol does not contain a valid Hyperliquid product type suffix.
#[pyfunction]
#[pyo3(name = "hyperliquid_product_type_from_symbol")]
fn py_hyperliquid_product_type_from_symbol(
    symbol: &str,
) -> PyResult<crate::common::HyperliquidProductType> {
    crate::common::HyperliquidProductType::from_symbol(symbol).map_err(to_pyvalue_err)
}

/// Loaded as `nautilus_pyo3.hyperliquid`.
#[pymodule]
pub fn hyperliquid(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<crate::http::HyperliquidHttpClient>()?;
    m.add_class::<crate::websocket::HyperliquidWebSocketClient>()?;
    m.add_class::<crate::common::enums::HyperliquidProductType>()?;
    m.add_class::<crate::common::enums::HyperliquidTpSl>()?;
    m.add_class::<crate::common::enums::HyperliquidTriggerPriceType>()?;
    m.add_class::<crate::common::enums::HyperliquidConditionalOrderType>()?;
    m.add_class::<crate::common::enums::HyperliquidTrailingOffsetType>()?;
    m.add_function(wrap_pyfunction!(urls::py_get_hyperliquid_http_base_url, m)?)?;
    m.add_function(wrap_pyfunction!(urls::py_get_hyperliquid_ws_url, m)?)?;
    m.add_function(wrap_pyfunction!(
        py_hyperliquid_product_type_from_symbol,
        m
    )?)?;
    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`py_hyperliquid_product_type_from_symbol()`**: Function defined in this file
- **`hyperliquid()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `hyperliquid`, `py_hyperliquid_product_type_from_symbol`

## Related Files

This file is located in `crates/adapters/hyperliquid/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.064597Z*
