# Documentation: mod.rs

## File Metadata

- **Path**: `crates/persistence/src/python/mod.rs`
- **Size**: 1,805 bytes
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

//! Python bindings from [PyO3](https://pyo3.rs).

pub mod backend;
pub mod catalog;
pub mod wranglers;

use pyo3::prelude::*;

/// Loaded as `nautilus_pyo3.persistence`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn persistence(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<crate::backend::session::DataBackendSession>()?;
    m.add_class::<crate::backend::session::DataQueryResult>()?;
    m.add_class::<backend::session::NautilusDataType>()?;
    m.add_class::<catalog::ParquetDataCatalogV2>()?;
    m.add_class::<wranglers::bar::BarDataWrangler>()?;
    m.add_class::<wranglers::delta::OrderBookDeltaDataWrangler>()?;
    m.add_class::<wranglers::depth::OrderBookDepth10DataWrangler>()?;
    m.add_class::<wranglers::quote::QuoteTickDataWrangler>()?;
    m.add_class::<wranglers::trade::TradeTickDataWrangler>()?;
    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`persistence()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `persistence`

## Related Files

This file is located in `crates/persistence/src/python/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.562979Z*
