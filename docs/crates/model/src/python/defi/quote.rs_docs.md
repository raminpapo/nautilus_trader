# Documentation: quote.rs

## File Metadata

- **Path**: `crates/model/src/python/defi/quote.rs`
- **Size**: 3,405 bytes
- **Lines**: 124
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

use crate::defi::pool_analysis::quote::SwapQuote;

#[pymethods]
impl SwapQuote {
    #[getter]
    #[pyo3(name = "amount0")]
    fn py_amount0(&self) -> String {
        self.amount0.to_string()
    }

    #[getter]
    #[pyo3(name = "amount1")]
    fn py_amount1(&self) -> String {
        self.amount1.to_string()
    }

    #[getter]
    #[pyo3(name = "sqrt_price_before_x96")]
    fn py_sqrt_price_before_x96(&self) -> String {
        self.sqrt_price_before_x96.to_string()
    }

    #[getter]
    #[pyo3(name = "sqrt_price_after_x96")]
    fn py_sqrt_price_after_x96(&self) -> String {
        self.sqrt_price_after_x96.to_string()
    }

    #[getter]
    #[pyo3(name = "tick_before")]
    fn py_tick_before(&self) -> i32 {
        self.tick_before
    }

    #[getter]
    #[pyo3(name = "tick_after")]
    fn py_tick_after(&self) -> i32 {
        self.tick_after
    }

    #[getter]
    #[pyo3(name = "liquidity_after")]
    fn py_liquidity_after(&self) -> u128 {
        self.liquidity_after
    }

    #[getter]
    #[pyo3(name = "fee_growth_global_after")]
    fn py_fee_growth_global_after(&self) -> String {
        self.fee_growth_global_after.to_string()
    }

    #[getter]
    #[pyo3(name = "lp_fee")]
    fn py_lp_fee(&self) -> String {
        self.lp_fee.to_string()
    }

    #[getter]
    #[pyo3(name = "protocol_fee")]
    fn py_protocol_fee(&self) -> String {
        self.protocol_fee.to_string()
    }

    #[getter]
    #[pyo3(name = "crossed_ticks_count")]
    fn py_crossed_ticks_count(&self) -> usize {
        self.crossed_ticks.len()
    }

    #[pyo3(name = "zero_for_one")]
    fn py_zero_for_one(&self) -> bool {
        self.zero_for_one()
    }

    #[pyo3(name = "total_fee")]
    fn py_total_fee(&self) -> String {
        self.total_fee().to_string()
    }

    #[pyo3(name = "total_crossed_ticks")]
    fn py_total_crossed_ticks(&self) -> u32 {
        self.total_crossed_ticks()
    }

    #[pyo3(name = "get_output_amount")]
    fn py_get_output_amount(&self) -> String {
        self.get_output_amount().to_string()
    }

    fn __str__(&self) -> String {
        format!(
            "SwapQuote(amount0={}, amount1={}, tick_before={}, tick_after={}, liquidity_after={}, total_fee={})",
            self.amount0,
            self.amount1,
            self.tick_before,
            self.tick_after,
            self.liquidity_after,
            self.total_fee()
        )
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 17 function(s).

## Detailed Walkthrough

### Functions
- **`py_amount0()`**: Function defined in this file
- **`py_amount1()`**: Function defined in this file
- **`py_sqrt_price_before_x96()`**: Function defined in this file
- **`py_sqrt_price_after_x96()`**: Function defined in this file
- **`py_tick_before()`**: Function defined in this file
- **`py_tick_after()`**: Function defined in this file
- **`py_liquidity_after()`**: Function defined in this file
- **`py_fee_growth_global_after()`**: Function defined in this file
- **`py_lp_fee()`**: Function defined in this file
- **`py_protocol_fee()`**: Function defined in this file
- **`py_crossed_ticks_count()`**: Function defined in this file
- **`py_zero_for_one()`**: Function defined in this file
- **`py_total_fee()`**: Function defined in this file
- **`py_total_crossed_ticks()`**: Function defined in this file
- **`py_get_output_amount()`**: Function defined in this file
- **`__str__()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 18


**Functions**: `__repr__`, `__str__`, `py_amount0`, `py_amount1`, `py_crossed_ticks_count`, `py_fee_growth_global_after`, `py_get_output_amount`, `py_liquidity_after`, `py_lp_fee`, `py_protocol_fee`, `py_sqrt_price_after_x96`, `py_sqrt_price_before_x96`, `py_tick_after`, `py_tick_before`, `py_total_crossed_ticks`, `py_total_fee`, `py_zero_for_one`
**Impls**: `SwapQuote`

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
*Generated on 2025-11-18T21:55:03.014234Z*
