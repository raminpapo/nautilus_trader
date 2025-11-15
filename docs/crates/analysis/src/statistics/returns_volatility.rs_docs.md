# Documentation: `crates/analysis/src/statistics/returns_volatility.rs`
**Generated:** 2025-11-15T19:40:01.572795Z
**File Size:** 5171 bytes
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

- **Path:** `crates/analysis/src/statistics/returns_volatility.rs`
- **Size:** 5,171 bytes
- **Lines:** 159
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 12

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

use std::fmt::Display;

use nautilus_model::position::Position;

use crate::{Returns, statistic::PortfolioStatistic};

/// Calculates the annualized volatility (standard deviation) of portfolio returns.
///
/// Volatility is calculated as the standard deviation of returns, annualized by
/// multiplying the daily standard deviation by the square root of the period:
/// `Standard Deviation * sqrt(period)`
///
/// Uses Bessel's correction (ddof=1) for sample standard deviation.
/// This provides a measure of the portfolio's risk or uncertainty of returns.
///
/// # References
///
/// - CFA Institute Level I Curriculum: Quantitative Methods
/// - Hull, J. C. (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
/// - Fabozzi, F. J., et al. (2002). *The Handbook of Financial Instruments*. Wiley.
#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct ReturnsVolatility {
    /// The annualization period (default: 252 for daily data).
    period: usize,
}

impl ReturnsVolatility {
    /// Creates a new [`ReturnsVolatility`] instance.
    #[must_use]
    pub fn new(period: Option<usize>) -> Self {
        Self {
            period: period.unwrap_or(252),
        }
    }
}

impl Display for ReturnsVolatility {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Returns Volatility ({} days)", self.period)
    }
}

impl PortfolioStatistic for ReturnsVolatility {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_returns(&self, raw_returns: &Returns) -> Option<Self::Item> {
        if !self.check_valid_returns(raw_returns) {
            return Some(f64::NAN);
        }

        let returns = self.downsample_to_daily_bins(raw_returns);
        let daily_std = self.calculate_std(&returns);
        let annualized_std = daily_std * (self.period as f64).sqrt();
        Some(annualized_std)
    }
    fn calculate_from_realized_pnls(&self, _realized_pnls: &[f64]) -> Option<Self::Item> {
        None
    }

    fn calculate_from_positions(&self, _positions: &[Position]) -> Option<Self::Item> {
        None
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use std::collections::BTreeMap;

    use nautilus_core::{UnixNanos, approx_eq};
    use rstest::rstest;

    use super::*;

    fn create_returns(values: Vec<f64>) -> BTreeMap<UnixNanos, f64> {
        let mut new_return = BTreeMap::new();
        let one_day_in_nanos = 86_400_000_000_000;
        let start_time = 1_600_000_000_000_000_000;

        for (i, &value) in values.iter().enumerate() {
            let timestamp = start_time + i as u64 * one_day_in_nanos;
            new_return.insert(UnixNanos::from(timestamp), value);
        }

        new_return
    }

    #[rstest]
    fn test_empty_returns() {
        let volatility = ReturnsVolatility::new(None);
        let returns = create_returns(vec![]);
        let result = volatility.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_default_period() {
        let volatility = ReturnsVolatility::new(None);
        assert_eq!(volatility.period, 252);
    }

    #[rstest]
    fn test_custom_period() {
        let volatility = ReturnsVolatility::new(Some(365));
        assert_eq!(volatility.period, 365);
    }

    #[rstest]
    fn test_volatility_calculation() {
        let volatility = ReturnsVolatility::new(None);

        let returns = create_returns(vec![
            0.01, -0.02, 0.03, -0.01, 0.02, 0.04, -0.03, 0.05, -0.04, 0.02,
        ]);
        let result = volatility.calculate_from_returns(&returns);
        assert!(result.is_some());

        assert!(approx_eq!(
            f64,
            result.unwrap(),
            0.48526281538976396,
            epsilon = 1e-9
        ));
    }

    #[rstest]
    fn test_name() {
        let volatility = ReturnsVolatility::new(None);
        assert_eq!(volatility.name(), "Returns Volatility (252 days)");
    }
}
```


---

## Overview

This file is located at `crates/analysis/src/statistics/returns_volatility.rs` within the repository.

**Classes defined:** ReturnsVolatility, ReturnsVolatility, Display, PortfolioStatistic

**Functions defined:** new, fmt, name, calculate_from_returns, calculate_from_realized_pnls, calculate_from_positions, create_returns, test_empty_returns, test_default_period, test_custom_period and 2 more


---

## Detailed Analysis

### Classes

#### `ReturnsVolatility`

**Type:** struct


#### `ReturnsVolatility`

**Type:** impl


#### `Display`

**Type:** impl


#### `PortfolioStatistic`

**Type:** impl


### Functions

#### `new(period: Option<usize>)`


#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `name(&self)`


#### `calculate_from_returns(&self, raw_returns: &Returns)`


#### `calculate_from_realized_pnls(&self, _realized_pnls: &[f64])`


#### `calculate_from_positions(&self, _positions: &[Position])`


#### `create_returns(values: Vec<f64>)`


#### `test_empty_returns()`


#### `test_default_period()`


#### `test_custom_period()`


#### `test_volatility_calculation()`


#### `test_name()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/analysis/src/statistics`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


