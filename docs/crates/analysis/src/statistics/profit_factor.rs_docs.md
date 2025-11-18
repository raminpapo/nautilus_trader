# Documentation: profit_factor.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/profit_factor.rs`
- **Size**: 5,910 bytes
- **Lines**: 179
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

/// Calculates the profit factor based on portfolio returns.
///
/// Profit factor is defined as the ratio of gross profits to gross losses:
/// `Sum(Positive Returns) / Abs(Sum(Negative Returns))`
///
/// A profit factor greater than 1.0 indicates a profitable strategy, while
/// a factor less than 1.0 indicates losses exceed gains.
///
/// Generally:
/// - 1.0-1.5: Modest profitability
/// - 1.5-2.0: Good profitability
/// - > 2.0: Excellent profitability
///
/// # References
///
/// - Tharp, V. K. (1998). *Trade Your Way to Financial Freedom*. McGraw-Hill.
/// - Kaufman, P. J. (2013). *Trading Systems and Methods* (5th ed.). Wiley.
#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct ProfitFactor {}

impl Display for ProfitFactor {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Profit Factor")
    }
}

impl PortfolioStatistic for ProfitFactor {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_returns(&self, returns: &Returns) -> Option<Self::Item> {
        if !self.check_valid_returns(returns) {
            return Some(f64::NAN);
        }

        let (positive_returns_sum, negative_returns_sum) =
            returns
                .values()
                .fold((0.0, 0.0), |(pos_sum, neg_sum), &pnl| {
                    if pnl >= 0.0 {
                        (pos_sum + pnl, neg_sum)
                    } else {
                        (pos_sum, neg_sum + pnl)
                    }
                });

        if negative_returns_sum == 0.0 {
            return Some(f64::NAN);
        }
        Some((positive_returns_sum / negative_returns_sum).abs())
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
mod profit_factor_tests {
    use std::collections::BTreeMap;

    use nautilus_core::{UnixNanos, approx_eq};
    use rstest::rstest;

    use super::*;

    fn create_returns(values: Vec<f64>) -> Returns {
        let mut new_return = BTreeMap::new();
        for (i, value) in values.iter().enumerate() {
            new_return.insert(UnixNanos::from(i as u64), *value);
        }

        new_return
    }

    #[rstest]
    fn test_empty_returns() {
        let profit_factor = ProfitFactor {};
        let returns = create_returns(vec![]);
        let result = profit_factor.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_all_positive() {
        let profit_factor = ProfitFactor {};
        let returns = create_returns(vec![10.0, 20.0, 30.0]);
        let result = profit_factor.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_all_negative() {
        let profit_factor = ProfitFactor {};
        let returns = create_returns(vec![-10.0, -20.0, -30.0]);
        let result = profit_factor.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_mixed_returns() {
        let profit_factor = ProfitFactor {};
        let returns = create_returns(vec![10.0, -20.0, 30.0, -40.0]);
        let result = profit_factor.calculate_from_returns(&returns);
        assert!(result.is_some());
        // (10.0 + 30.0) / |-20.0 + -40.0| = 40 / 60 = 0.666...
        assert!(approx_eq!(
            f64,
            result.unwrap(),
            0.6666666666666666,
            epsilon = 1e-9
        ));
    }

    #[rstest]
    fn test_with_zero() {
        let profit_factor = ProfitFactor {};
        let returns = create_returns(vec![10.0, 0.0, -20.0, -30.0]);
        let result = profit_factor.calculate_from_returns(&returns);
        assert!(result.is_some());
        // (10.0 + 0.0) / |-20.0 + -30.0| = 10 / 50 = 0.2
        assert!(approx_eq!(f64, result.unwrap(), 0.2, epsilon = 1e-9));
    }

    #[rstest]
    fn test_equal_positive_negative() {
        let profit_factor = ProfitFactor {};
        let returns = create_returns(vec![20.0, -20.0]);
        let result = profit_factor.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 1.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let profit_factor = ProfitFactor {};
        assert_eq!(profit_factor.name(), "Profit Factor");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 13 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`create_returns()`**: Function defined in this file
- **`test_empty_returns()`**: Function defined in this file
- **`test_all_positive()`**: Function defined in this file
- **`test_all_negative()`**: Function defined in this file
- **`test_mixed_returns()`**: Function defined in this file
- **`test_with_zero()`**: Function defined in this file
- **`test_equal_positive_negative()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`ProfitFactor`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 16


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `create_returns`, `fmt`, `name`, `test_all_negative`, `test_all_positive`, `test_empty_returns`, `test_equal_positive_negative`, `test_mixed_returns`, `test_name`, `test_with_zero`
**Impls**: `Display`, `PortfolioStatistic`
**Structs**: `ProfitFactor`

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
*Generated on 2025-11-18T21:55:00.856737Z*
