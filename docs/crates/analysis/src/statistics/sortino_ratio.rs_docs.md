# Documentation: sortino_ratio.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/sortino_ratio.rs`
- **Size**: 5,417 bytes
- **Lines**: 170
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`create_returns()`**: Function defined in this file
- **`test_empty_returns()`**: Function defined in this file
- **`test_zero_downside_deviation()`**: Function defined in this file
- **`test_valid_sortino_ratio()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`SortinoRatio`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `create_returns`, `fmt`, `name`, `new`, `test_empty_returns`, `test_name`, `test_valid_sortino_ratio`, `test_zero_downside_deviation`
**Impls**: `Display`, `PortfolioStatistic`, `SortinoRatio`
**Structs**: `SortinoRatio`

## Related Files

This file is located in `crates/analysis/src/statistics/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.871586Z*
