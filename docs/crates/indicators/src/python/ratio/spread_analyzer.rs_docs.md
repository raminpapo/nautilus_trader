# Documentation: spread_analyzer.rs

## File Metadata

- **Path**: `crates/indicators/src/python/ratio/spread_analyzer.rs`
- **Size**: 2,210 bytes
- **Lines**: 77
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

use nautilus_model::{data::QuoteTick, identifiers::InstrumentId};
use pyo3::prelude::*;

use crate::{indicator::Indicator, ratio::spread_analyzer::SpreadAnalyzer};

#[pymethods]
impl SpreadAnalyzer {
    #[new]
    fn py_new(instrument_id: InstrumentId, capacity: usize) -> Self {
        Self::new(capacity, instrument_id)
    }

    fn __repr__(&self) -> String {
        format!("SpreadAnalyzer({})", self.capacity)
    }

    #[getter]
    #[pyo3(name = "name")]
    fn py_name(&self) -> String {
        self.name()
    }

    #[getter]
    #[pyo3(name = "capacity")]
    const fn py_capacity(&self) -> usize {
        self.capacity
    }

    #[getter]
    #[pyo3(name = "current")]
    const fn py_current(&self) -> f64 {
        self.current
    }

    #[getter]
    #[pyo3(name = "average")]
    const fn py_average(&self) -> f64 {
        self.average
    }

    #[getter]
    #[pyo3(name = "initialized")]
    const fn py_initialized(&self) -> bool {
        self.initialized
    }

    #[pyo3(name = "has_inputs")]
    fn py_has_inputs(&self) -> bool {
        self.has_inputs()
    }

    #[pyo3(name = "handle_quote_tick")]
    fn py_handle_quote_tick(&mut self, quote: &QuoteTick) {
        self.handle_quote(quote);
    }

    #[pyo3(name = "reset")]
    fn py_reset(&mut self) {
        self.reset();
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 10 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_name()`**: Function defined in this file
- **`py_capacity()`**: Function defined in this file
- **`py_current()`**: Function defined in this file
- **`py_average()`**: Function defined in this file
- **`py_initialized()`**: Function defined in this file
- **`py_has_inputs()`**: Function defined in this file
- **`py_handle_quote_tick()`**: Function defined in this file
- **`py_reset()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 11


**Functions**: `__repr__`, `py_average`, `py_capacity`, `py_current`, `py_handle_quote_tick`, `py_has_inputs`, `py_initialized`, `py_name`, `py_new`, `py_reset`
**Impls**: `SpreadAnalyzer`

## Related Files

This file is located in `crates/indicators/src/python/ratio/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.927407Z*
