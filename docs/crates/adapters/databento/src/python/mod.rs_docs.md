# Documentation: `crates/adapters/databento/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:00.885382Z
**File Size:** 2024 bytes
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

- **Path:** `crates/adapters/databento/src/python/mod.rs`
- **Size:** 2,024 bytes
- **Lines:** 50
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

//! Python bindings from [PyO3](https://pyo3.rs).

pub mod enums;
pub mod historical;
pub mod loader;
pub mod types;

#[cfg(feature = "live")]
pub mod live;

use pyo3::prelude::*;

/// Databento Python module.
///
/// The module is exposed under different paths depending on the build configuration:
/// - With `cython-compat` feature: `nautilus_trader.core.nautilus_pyo3.databento`
/// - Without `cython-compat`: `nautilus_trader.databento` (via re-export)
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn databento(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<super::enums::DatabentoStatisticType>()?;
    m.add_class::<super::enums::DatabentoStatisticUpdateAction>()?;
    m.add_class::<super::types::DatabentoPublisher>()?;
    m.add_class::<super::types::DatabentoStatistics>()?;
    m.add_class::<super::types::DatabentoImbalance>()?;
    m.add_class::<super::loader::DatabentoDataLoader>()?;
    m.add_class::<historical::DatabentoHistoricalClient>()?;

    #[cfg(feature = "live")]
    m.add_class::<live::DatabentoLiveClient>()?;
    Ok(())
}
```


---

## Overview

This file is located at `crates/adapters/databento/src/python/mod.rs` within the repository.

**Functions defined:** databento


---

## Detailed Analysis

### Functions

#### `databento(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


