# Documentation: `crates/model/src/python/data/greeks.rs`
**Generated:** 2025-11-15T19:40:02.962218Z
**File Size:** 4428 bytes
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

- **Path:** `crates/model/src/python/data/greeks.rs`
- **Size:** 4,428 bytes
- **Lines:** 190
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 2
- **Functions:** 18

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


---

## Overview

This file is located at `crates/model/src/python/data/greeks.rs` within the repository.

**Classes defined:** ImplyVolAndGreeksResult, BlackScholesGreeksResult

**Functions defined:** py_new, py_vol, py_price, py_delta, py_gamma, py_vega, py_theta, __repr__, py_new, py_price and 8 more


---

## Detailed Analysis

### Classes

#### `ImplyVolAndGreeksResult`

**Type:** impl


#### `BlackScholesGreeksResult`

**Type:** impl


### Functions

#### `py_new(vol: f64, price: f64, delta: f64, gamma: f64, theta: f64, vega: f64)`


#### `py_vol(&self)`


#### `py_price(&self)`


#### `py_delta(&self)`


#### `py_gamma(&self)`


#### `py_vega(&self)`


#### `py_theta(&self)`


#### `__repr__(&self)`


#### `py_new(price: f64, delta: f64, gamma: f64, theta: f64, vega: f64)`


#### `py_price(&self)`


#### `py_delta(&self)`


#### `py_gamma(&self)`


#### `py_vega(&self)`


#### `py_theta(&self)`


#### `__repr__(&self)`


#### `py_black_scholes_greeks(
    s: f64,
    r: f64,
    b: f64,
    sigma: f64,
    is_call: bool,
    k: f64,
    t: f64,
    multiplier: f64,
)`


#### `py_imply_vol(
    s: f64,
    r: f64,
    b: f64,
    is_call: bool,
    k: f64,
    t: f64,
    price: f64,
)`


#### `py_imply_vol_and_greeks(
    s: f64,
    r: f64,
    b: f64,
    is_call: bool,
    k: f64,
    t: f64,
    price: f64,
    multiplier: f64,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/model/src/python/data`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


