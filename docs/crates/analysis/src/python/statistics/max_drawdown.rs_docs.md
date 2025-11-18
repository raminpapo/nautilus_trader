# Documentation: max_drawdown.rs

## File Metadata

- **Path**: `crates/analysis/src/python/statistics/max_drawdown.rs`
- **Size**: 1,554 bytes
- **Lines**: 45
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

use std::collections::BTreeMap;

use pyo3::prelude::*;

use super::transform_returns;
use crate::{statistic::PortfolioStatistic, statistics::max_drawdown::MaxDrawdown};

#[pymethods]
impl MaxDrawdown {
    #[new]
    fn py_new() -> Self {
        Self::new()
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[pyo3(name = "calculate_from_returns")]
    fn py_calculate_from_returns(&self, raw_returns: BTreeMap<u64, f64>) -> Option<f64> {
        self.calculate_from_returns(&transform_returns(raw_returns))
    }

    fn __repr__(&self) -> String {
        format!("MaxDrawdown({})", self.name())
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_calculate_from_returns()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `__repr__`, `py_calculate_from_returns`, `py_name`, `py_new`
**Impls**: `MaxDrawdown`

## Related Files

This file is located in `crates/analysis/src/python/statistics/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.801043Z*
