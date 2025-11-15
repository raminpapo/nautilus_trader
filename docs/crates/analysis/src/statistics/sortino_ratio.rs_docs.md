# Documentation: `crates/analysis/src/statistics/sortino_ratio.rs`
**Generated:** 2025-11-15T19:40:01.577314Z
**File Size:** 5417 bytes
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

- **Path:** `crates/analysis/src/statistics/sortino_ratio.rs`
- **Size:** 5,417 bytes
- **Lines:** 169
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 11

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

/// Calculates the Sortino ratio for portfolio returns.
///
/// The Sortino ratio is a variation of the Sharpe ratio that only penalizes downside
/// volatility, making it more appropriate for strategies with asymmetric return distributions.
///
/// Formula: `Mean Return / Downside Deviation * sqrt(period)`
///
/// Where downside deviation is calculated as:
/// `sqrt(sum(negative_returns^2) / total_observations)`
///
/// Note: Uses total observations count (not just negative returns) as per Sortino's methodology.
///
/// # References
///
/// - Sortino, F. A., & van der Meer, R. (1991). "Downside Risk". *Journal of Portfolio Management*, 17(4), 27-31.
/// - Sortino, F. A., & Price, L. N. (1994). "Performance Measurement in a Downside Risk Framework".
///   *Journal of Investing*, 3(3), 59-64.
#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct SortinoRatio {
    period: usize,
}

impl SortinoRatio {
    /// Creates a new [`SortinoRatio`] instance.
    #[must_use]
    pub fn new(period: Option<usize>) -> Self {
        Self {
            period: period.unwrap_or(252),
        }
    }
}

impl Display for SortinoRatio {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Sortino Ratio ({} days)", self.period)
    }
}

impl PortfolioStatistic for SortinoRatio {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_returns(&self, raw_returns: &Returns) -> Option<Self::Item> {
        if !self.check_valid_returns(raw_returns) {
            return Some(f64::NAN);
        }

        let returns = self.downsample_to_daily_bins(raw_returns);
        let total_n = returns.len() as f64;
        let mean = returns.values().sum::<f64>() / total_n;

        let downside = (returns
            .values()
            .filter(|&&x| x < 0.0)
            .map(|x| x.powi(2))
            .sum::<f64>()
            / total_n)
            .sqrt();

        if downside < f64::EPSILON {
            return Some(f64::NAN);
        }

        let annualized_ratio = (mean / downside) * (self.period as f64).sqrt();

        Some(annualized_ratio)
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
        let ratio = SortinoRatio::new(None);
        let returns = create_returns(vec![]);
        let result = ratio.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_zero_downside_deviation() {
        let ratio = SortinoRatio::new(None);
        let returns = create_returns(vec![0.02, 0.03, 0.01]);
        let result = ratio.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_valid_sortino_ratio() {
        let ratio = SortinoRatio::new(Some(252));
        let returns = create_returns(vec![-0.01, 0.02, -0.015, 0.005, -0.02]);
        let result = ratio.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(approx_eq!(
            f64,
            result.unwrap(),
            -5.273224492824493,
            epsilon = 1e-9
        ));
    }

    #[rstest]
    fn test_name() {
        let ratio = SortinoRatio::new(None);
        assert_eq!(ratio.name(), "Sortino Ratio (252 days)");
    }
}
```


---

## Overview

This file is located at `crates/analysis/src/statistics/sortino_ratio.rs` within the repository.

**Classes defined:** SortinoRatio, SortinoRatio, Display, PortfolioStatistic

**Functions defined:** new, fmt, name, calculate_from_returns, calculate_from_realized_pnls, calculate_from_positions, create_returns, test_empty_returns, test_zero_downside_deviation, test_valid_sortino_ratio and 1 more


---

## Detailed Analysis

### Classes

#### `SortinoRatio`

**Type:** struct


#### `SortinoRatio`

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


#### `test_zero_downside_deviation()`


#### `test_valid_sortino_ratio()`


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


