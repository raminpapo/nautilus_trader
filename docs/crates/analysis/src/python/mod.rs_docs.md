# Documentation: `crates/analysis/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:01.524622Z
**File Size:** 2814 bytes
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

- **Path:** `crates/analysis/src/python/mod.rs`
- **Size:** 2,814 bytes
- **Lines:** 61
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

pub mod analyzer;
pub mod statistics;

use pyo3::{prelude::*, pymodule};

/// Initializes the Python `analysis` module.
///
/// Adds the `PortfolioAnalyzer` class and all portfolio statistics.
///
/// # Errors
///
/// Returns a Python exception if adding any class fails.
#[pymodule]
pub fn analysis(_: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<crate::analyzer::PortfolioAnalyzer>()?;

    // Statistics - Returns-based
    m.add_class::<crate::statistics::cagr::CAGR>()?;
    m.add_class::<crate::statistics::calmar_ratio::CalmarRatio>()?;
    m.add_class::<crate::statistics::max_drawdown::MaxDrawdown>()?;
    m.add_class::<crate::statistics::profit_factor::ProfitFactor>()?;
    m.add_class::<crate::statistics::returns_avg::ReturnsAverage>()?;
    m.add_class::<crate::statistics::returns_avg_loss::ReturnsAverageLoss>()?;
    m.add_class::<crate::statistics::returns_avg_win::ReturnsAverageWin>()?;
    m.add_class::<crate::statistics::returns_volatility::ReturnsVolatility>()?;
    m.add_class::<crate::statistics::risk_return_ratio::RiskReturnRatio>()?;
    m.add_class::<crate::statistics::sharpe_ratio::SharpeRatio>()?;
    m.add_class::<crate::statistics::sortino_ratio::SortinoRatio>()?;

    // Statistics - PnL-based
    m.add_class::<crate::statistics::expectancy::Expectancy>()?;
    m.add_class::<crate::statistics::loser_avg::AvgLoser>()?;
    m.add_class::<crate::statistics::loser_max::MaxLoser>()?;
    m.add_class::<crate::statistics::loser_min::MinLoser>()?;
    m.add_class::<crate::statistics::win_rate::WinRate>()?;
    m.add_class::<crate::statistics::winner_avg::AvgWinner>()?;
    m.add_class::<crate::statistics::winner_max::MaxWinner>()?;
    m.add_class::<crate::statistics::winner_min::MinWinner>()?;

    // Statistics - Position-based
    m.add_class::<crate::statistics::long_ratio::LongRatio>()?;

    Ok(())
}
```


---

## Overview

This file is located at `crates/analysis/src/python/mod.rs` within the repository.

**Functions defined:** analysis


---

## Detailed Analysis

### Functions

#### `analysis(_: Python<'_>, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/analysis/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


