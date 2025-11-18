# Documentation: returns_volatility.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/returns_volatility.rs`
- **Size**: 5,171 bytes
- **Lines**: 160
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 12 function(s) and 1 class(es).

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
- **`test_default_period()`**: Function defined in this file
- **`test_custom_period()`**: Function defined in this file
- **`test_volatility_calculation()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`ReturnsVolatility`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `create_returns`, `fmt`, `name`, `new`, `test_custom_period`, `test_default_period`, `test_empty_returns`, `test_name`, `test_volatility_calculation`
**Impls**: `Display`, `PortfolioStatistic`, `ReturnsVolatility`
**Structs**: `ReturnsVolatility`

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
*Generated on 2025-11-18T21:55:00.865625Z*
