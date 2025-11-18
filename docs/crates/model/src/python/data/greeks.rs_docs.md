# Documentation: greeks.rs

## File Metadata

- **Path**: `crates/model/src/python/data/greeks.rs`
- **Size**: 4,428 bytes
- **Lines**: 191
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

use crate::data::greeks::{
    BlackScholesGreeksResult, ImplyVolAndGreeksResult, black_scholes_greeks, imply_vol,
    imply_vol_and_greeks,
};

#[pymethods]
impl ImplyVolAndGreeksResult {
    /// Creates a new [`ImplyVolAndGreeksResult`] instance.
    #[new]
    fn py_new(vol: f64, price: f64, delta: f64, gamma: f64, theta: f64, vega: f64) -> Self {
        Self {
            vol,
            price,
            delta,
            gamma,
            theta,
            vega,
        }
    }

    #[getter]
    #[pyo3(name = "vol")]
    fn py_vol(&self) -> f64 {
        self.vol
    }

    #[getter]
    #[pyo3(name = "price")]
    fn py_price(&self) -> f64 {
        self.price
    }

    #[getter]
    #[pyo3(name = "delta")]
    fn py_delta(&self) -> f64 {
        self.delta
    }

    #[getter]
    #[pyo3(name = "gamma")]
    fn py_gamma(&self) -> f64 {
        self.gamma
    }

    #[getter]
    #[pyo3(name = "vega")]
    fn py_vega(&self) -> f64 {
        self.vega
    }

    #[getter]
    #[pyo3(name = "theta")]
    fn py_theta(&self) -> f64 {
        self.theta
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }
}

#[pymethods]
impl BlackScholesGreeksResult {
    /// Creates a new [`BlackScholesGreeksResult`] instance.
    #[new]
    fn py_new(price: f64, delta: f64, gamma: f64, theta: f64, vega: f64) -> Self {
        Self {
            price,
            delta,
            gamma,
            theta,
            vega,
        }
    }

    #[getter]
    #[pyo3(name = "price")]
    fn py_price(&self) -> f64 {
        self.price
    }

    #[getter]
    #[pyo3(name = "delta")]
    fn py_delta(&self) -> f64 {
        self.delta
    }

    #[getter]
    #[pyo3(name = "gamma")]
    fn py_gamma(&self) -> f64 {
        self.gamma
    }

    #[getter]
    #[pyo3(name = "vega")]
    fn py_vega(&self) -> f64 {
        self.vega
    }

    #[getter]
    #[pyo3(name = "theta")]
    fn py_theta(&self) -> f64 {
        self.theta
    }

    fn __repr__(&self) -> String {
        format!("{self:?}")
    }
}

/// Computes Black-Scholes greeks for given parameters.
///
/// # Errors
///
/// Returns a `PyErr` if the greeks calculation fails.
#[pyfunction]
#[pyo3(name = "black_scholes_greeks")]
#[allow(clippy::too_many_arguments)]
pub fn py_black_scholes_greeks(
    s: f64,
    r: f64,
    b: f64,
    sigma: f64,
    is_call: bool,
    k: f64,
    t: f64,
    multiplier: f64,
) -> PyResult<BlackScholesGreeksResult> {
    let result = black_scholes_greeks(s, r, b, sigma, is_call, k, t, multiplier);
    Ok(result)
}

/// Computes the implied volatility for an option given its parameters and market price.
///
/// # Errors
///
/// Returns a `PyErr` if implied volatility calculation fails.
#[pyfunction]
#[pyo3(name = "imply_vol")]
pub fn py_imply_vol(
    s: f64,
    r: f64,
    b: f64,
    is_call: bool,
    k: f64,
    t: f64,
    price: f64,
) -> PyResult<f64> {
    let vol = imply_vol(s, r, b, is_call, k, t, price);
    Ok(vol)
}

/// Computes implied volatility and option greeks for given parameters and market price.
///
/// # Errors
///
/// Returns a `PyErr` if calculation fails.
#[pyfunction]
#[pyo3(name = "imply_vol_and_greeks")]
#[allow(clippy::too_many_arguments)]
pub fn py_imply_vol_and_greeks(
    s: f64,
    r: f64,
    b: f64,
    is_call: bool,
    k: f64,
    t: f64,
    price: f64,
    multiplier: f64,
) -> PyResult<ImplyVolAndGreeksResult> {
    let result = imply_vol_and_greeks(s, r, b, is_call, k, t, price, multiplier);
    Ok(result)
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 18 function(s).

## Detailed Walkthrough

### Functions
- **`py_new()`**: Function defined in this file
- **`py_vol()`**: Function defined in this file
- **`py_price()`**: Function defined in this file
- **`py_delta()`**: Function defined in this file
- **`py_gamma()`**: Function defined in this file
- **`py_vega()`**: Function defined in this file
- **`py_theta()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_new()`**: Function defined in this file
- **`py_price()`**: Function defined in this file
- **`py_delta()`**: Function defined in this file
- **`py_gamma()`**: Function defined in this file
- **`py_vega()`**: Function defined in this file
- **`py_theta()`**: Function defined in this file
- **`__repr__()`**: Function defined in this file
- **`py_black_scholes_greeks()`**: Function defined in this file
- **`py_imply_vol()`**: Function defined in this file
- **`py_imply_vol_and_greeks()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Functions**: `__repr__`, `py_black_scholes_greeks`, `py_delta`, `py_gamma`, `py_imply_vol`, `py_imply_vol_and_greeks`, `py_new`, `py_price`, `py_theta`, `py_vega`, `py_vol`
**Impls**: `BlackScholesGreeksResult`, `ImplyVolAndGreeksResult`

## Related Files

This file is located in `crates/model/src/python/data/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.979927Z*
