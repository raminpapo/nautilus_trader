# Documentation: size_estimator.rs

## File Metadata

- **Path**: `crates/model/src/python/defi/size_estimator.rs`
- **Size**: 2,984 bytes
- **Lines**: 109
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

//! Python bindings for size estimation.

use pyo3::prelude::*;

use crate::defi::pool_analysis::size_estimator::SizeForImpactResult;

#[pymethods]
impl SizeForImpactResult {
    #[getter]
    #[pyo3(name = "target_impact_bps")]
    fn py_target_impact_bps(&self) -> u32 {
        self.target_impact_bps
    }

    #[getter]
    #[pyo3(name = "size")]
    fn py_size(&self) -> String {
        self.size.to_string()
    }

    #[getter]
    #[pyo3(name = "actual_impact_bps")]
    fn py_actual_impact_bps(&self) -> u32 {
        self.actual_impact_bps
    }

    #[getter]
    #[pyo3(name = "zero_for_one")]
    fn py_zero_for_one(&self) -> bool {
        self.zero_for_one
    }

    #[getter]
    #[pyo3(name = "iterations")]
    fn py_iterations(&self) -> u32 {
        self.iterations
    }

    #[getter]
    #[pyo3(name = "converged")]
    fn py_converged(&self) -> bool {
        self.converged
    }

    #[getter]
    #[pyo3(name = "expansion_count")]
    fn py_expansion_count(&self) -> u32 {
        self.expansion_count
    }

    #[getter]
    #[pyo3(name = "initial_high")]
    fn py_initial_high(&self) -> String {
        self.initial_high.to_string()
    }

    #[getter]
    #[pyo3(name = "final_low")]
    fn py_final_low(&self) -> String {
        self.final_low.to_string()
    }

    #[getter]
    #[pyo3(name = "final_high")]
    fn py_final_high(&self) -> String {
        self.final_high.to_string()
    }

    #[pyo3(name = "within_tolerance")]
    fn py_within_tolerance(&self, tolerance_bps: u32) -> bool {
        self.within_tolerance(tolerance_bps)
    }

    #[pyo3(name = "accuracy_percent")]
    fn py_accuracy_percent(&self) -> f64 {
        self.accuracy_percent()
    }

    fn __str__(&self) -> String {
        format!(
            "SizeForImpactResult(target={}bps, actual={}bps, size={}, converged={}, iterations={})",
            self.target_impact_bps,
            self.actual_impact_bps,
            self.size,
            self.converged,
            self.iterations,
        )
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 14 function(s).

## Detailed Walkthrough

### Functions
- **`py_target_impact_bps()`**: Function defined in this file
- **`py_size()`**: Function defined in this file
- **`py_actual_impact_bps()`**: Function defined in this file
- **`py_zero_for_one()`**: Function defined in this file
- **`py_iterations()`**: Function defined in this file
- **`py_converged()`**: Function defined in this file
- **`py_expansion_count()`**: Function defined in this file
- **`py_initial_high()`**: Function defined in this file
- **`py_final_low()`**: Function defined in this file
- **`py_final_high()`**: Function defined in this file
- **`py_within_tolerance()`**: Function defined in this file
- **`py_accuracy_percent()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Functions**: `__repr__`, `__str__`, `py_accuracy_percent`, `py_actual_impact_bps`, `py_converged`, `py_expansion_count`, `py_final_high`, `py_final_low`, `py_initial_high`, `py_iterations`, `py_size`, `py_target_impact_bps`, `py_within_tolerance`, `py_zero_for_one`
**Impls**: `SizeForImpactResult`

## Related Files

This file is located in `crates/model/src/python/defi/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.016843Z*
