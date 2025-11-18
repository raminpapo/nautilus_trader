# Documentation: profiler.rs

## File Metadata

- **Path**: `crates/model/src/python/defi/profiler.rs`
- **Size**: 6,237 bytes
- **Lines**: 202
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

//! Python bindings for DeFi pool profiler.

use std::str::FromStr;

use alloy_primitives::{U160, U256};
use nautilus_core::python::to_pyvalue_err;
use pyo3::prelude::*;

use crate::{
    defi::{
        Pool,
        pool_analysis::{PoolProfiler, quote::SwapQuote, size_estimator::SizeForImpactResult},
    },
    identifiers::InstrumentId,
};

#[pymethods]
impl PoolProfiler {
    #[getter]
    #[pyo3(name = "pool")]
    fn py_pool(&self) -> Pool {
        self.pool.as_ref().clone()
    }

    #[getter]
    #[pyo3(name = "instrument_id")]
    fn py_instrument_id(&self) -> InstrumentId {
        self.pool.instrument_id
    }

    #[getter]
    #[pyo3(name = "is_initialized")]
    fn py_is_initialized(&self) -> bool {
        self.is_initialized
    }

    #[getter]
    #[pyo3(name = "current_tick")]
    fn py_current_tick(&self) -> i32 {
        self.state.current_tick
    }

    #[getter]
    #[pyo3(name = "price_sqrt_ratio_x96")]
    fn py_price_sqrt_ratio_x96(&self) -> String {
        self.state.price_sqrt_ratio_x96.to_string()
    }

    #[getter]
    #[pyo3(name = "total_amount0_deposited")]
    fn py_total_amount0_deposited(&self) -> String {
        self.analytics.total_amount0_deposited.to_string()
    }

    #[getter]
    #[pyo3(name = "total_amount1_deposited")]
    fn py_total_amount1_deposited(&self) -> String {
        self.analytics.total_amount1_deposited.to_string()
    }

    #[getter]
    #[pyo3(name = "total_amount0_collected")]
    fn py_total_amount0_collected(&self) -> String {
        self.analytics.total_amount0_collected.to_string()
    }

    #[getter]
    #[pyo3(name = "total_amount1_collected")]
    fn py_total_amount1_collected(&self) -> String {
        self.analytics.total_amount1_collected.to_string()
    }

    #[getter]
    #[pyo3(name = "protocol_fees_token0")]
    fn py_protocol_fees_token0(&self) -> String {
        self.state.protocol_fees_token0.to_string()
    }

    #[getter]
    #[pyo3(name = "protocol_fees_token1")]
    fn py_protocol_fees_token1(&self) -> String {
        self.state.protocol_fees_token1.to_string()
    }

    #[getter]
    #[pyo3(name = "fee_protocol")]
    fn py_fee_protocol(&self) -> u8 {
        self.state.fee_protocol
    }

    #[pyo3(name = "get_active_liquidity")]
    fn py_get_active_liquidity(&self) -> u128 {
        self.get_active_liquidity()
    }

    #[pyo3(name = "get_active_tick_count")]
    fn py_get_active_tick_count(&self) -> usize {
        self.get_active_tick_count()
    }

    #[pyo3(name = "get_total_tick_count")]
    fn py_get_total_tick_count(&self) -> usize {
        self.get_total_tick_count()
    }

    #[pyo3(name = "get_total_active_positions")]
    fn py_get_total_active_positions(&self) -> usize {
        self.get_total_active_positions()
    }

    #[pyo3(name = "get_total_inactive_positions")]
    fn py_get_total_inactive_positions(&self) -> usize {
        self.get_total_inactive_positions()
    }

    #[pyo3(name = "estimate_balance_of_token0")]
    fn py_estimate_balance_of_token0(&self) -> String {
        self.estimate_balance_of_token0().to_string()
    }

    #[pyo3(name = "estimate_balance_of_token1")]
    fn py_estimate_balance_of_token1(&self) -> String {
        self.estimate_balance_of_token1().to_string()
    }

    #[pyo3(name = "get_total_liquidity")]
    fn py_get_total_liquidity_all_positions(&self) -> String {
        self.get_total_liquidity().to_string()
    }

    #[pyo3(name = "liquidity_utilization_rate")]
    fn py_liquidity_utilization_rate(&self) -> f64 {
        self.liquidity_utilization_rate()
    }

    #[pyo3(name = "swap_exact_in")]
    fn py_swap_exact_in(
        &self,
        amount_in: &str,
        zero_for_one: bool,
        sqrt_price_limit_x96: Option<&str>,
    ) -> PyResult<SwapQuote> {
        let amount_in = U256::from_str(amount_in).map_err(to_pyvalue_err)?;
        let sqrt_price_limit = match sqrt_price_limit_x96 {
            Some(limit_str) => Some(U160::from_str(limit_str).map_err(to_pyvalue_err)?),
            None => None,
        };

        self.swap_exact_in(amount_in, zero_for_one, sqrt_price_limit)
            .map_err(to_pyvalue_err)
    }

    #[pyo3(name = "swap_exact_out")]
    fn py_swap_exact_out(
        &self,
        amount_out: &str,
        zero_for_one: bool,
        sqrt_price_limit_x96: Option<&str>,
    ) -> PyResult<SwapQuote> {
        let amount_out = U256::from_str(amount_out).map_err(to_pyvalue_err)?;
        let sqrt_price_limit = match sqrt_price_limit_x96 {
            Some(limit_str) => Some(U160::from_str(limit_str).map_err(to_pyvalue_err)?),
            None => None,
        };

        self.swap_exact_out(amount_out, zero_for_one, sqrt_price_limit)
            .map_err(to_pyvalue_err)
    }

    #[pyo3(name = "size_for_impact_bps")]
    fn py_size_for_impact_bps(&self, impact_bps: u32, zero_for_one: bool) -> PyResult<String> {
        self.size_for_impact_bps(impact_bps, zero_for_one)
            .map(|size| size.to_string())
            .map_err(to_pyvalue_err)
    }

    #[pyo3(name = "size_for_impact_bps_detailed")]
    fn py_size_for_impact_bps_detailed(
        &self,
        impact_bps: u32,
        zero_for_one: bool,
    ) -> PyResult<SizeForImpactResult> {
        self.size_for_impact_bps_detailed(impact_bps, zero_for_one)
            .map_err(to_pyvalue_err)
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 25 function(s).

## Detailed Walkthrough

### Functions
- **`py_pool()`**: Function defined in this file
- **`py_instrument_id()`**: Function defined in this file
- **`py_is_initialized()`**: Function defined in this file
- **`py_current_tick()`**: Function defined in this file
- **`py_price_sqrt_ratio_x96()`**: Function defined in this file
- **`py_total_amount0_deposited()`**: Function defined in this file
- **`py_total_amount1_deposited()`**: Function defined in this file
- **`py_total_amount0_collected()`**: Function defined in this file
- **`py_total_amount1_collected()`**: Function defined in this file
- **`py_protocol_fees_token0()`**: Function defined in this file
- **`py_protocol_fees_token1()`**: Function defined in this file
- **`py_fee_protocol()`**: Function defined in this file
- **`py_get_active_liquidity()`**: Function defined in this file
- **`py_get_active_tick_count()`**: Function defined in this file
- **`py_get_total_tick_count()`**: Function defined in this file
- **`py_get_total_active_positions()`**: Function defined in this file
- **`py_get_total_inactive_positions()`**: Function defined in this file
- **`py_estimate_balance_of_token0()`**: Function defined in this file
- **`py_estimate_balance_of_token1()`**: Function defined in this file
- **`py_get_total_liquidity_all_positions()`**: Function defined in this file

*...and 5 more functions*


## Keywords and Identifiers

Total unique keywords extracted: 26


**Functions**: `py_current_tick`, `py_estimate_balance_of_token0`, `py_estimate_balance_of_token1`, `py_fee_protocol`, `py_get_active_liquidity`, `py_get_active_tick_count`, `py_get_total_active_positions`, `py_get_total_inactive_positions`, `py_get_total_liquidity_all_positions`, `py_get_total_tick_count`, `py_instrument_id`, `py_is_initialized`, `py_liquidity_utilization_rate`, `py_pool`, `py_price_sqrt_ratio_x96`, `py_protocol_fees_token0`, `py_protocol_fees_token1`, `py_size_for_impact_bps`, `py_size_for_impact_bps_detailed`, `py_swap_exact_in`, `py_swap_exact_out`, `py_total_amount0_collected`, `py_total_amount0_deposited`, `py_total_amount1_collected`, `py_total_amount1_deposited`
**Impls**: `PoolProfiler`

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
*Generated on 2025-11-18T21:55:03.012083Z*
