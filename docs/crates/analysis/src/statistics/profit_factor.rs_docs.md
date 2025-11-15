# Documentation: `crates/analysis/src/statistics/profit_factor.rs`
**Generated:** 2025-11-15T19:40:01.567063Z
**File Size:** 5910 bytes
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

- **Path:** `crates/analysis/src/statistics/profit_factor.rs`
- **Size:** 5,910 bytes
- **Lines:** 178
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 13

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


---

## Overview

This file is located at `crates/analysis/src/statistics/profit_factor.rs` within the repository.

**Classes defined:** ProfitFactor, Display, PortfolioStatistic

**Functions defined:** fmt, name, calculate_from_returns, calculate_from_realized_pnls, calculate_from_positions, create_returns, test_empty_returns, test_all_positive, test_all_negative, test_mixed_returns and 3 more


---

## Detailed Analysis

### Classes

#### `ProfitFactor`

**Type:** struct


#### `Display`

**Type:** impl


#### `PortfolioStatistic`

**Type:** impl


### Functions

#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `name(&self)`


#### `calculate_from_returns(&self, returns: &Returns)`


#### `calculate_from_realized_pnls(&self, _realized_pnls: &[f64])`


#### `calculate_from_positions(&self, _positions: &[Position])`


#### `create_returns(values: Vec<f64>)`


#### `test_empty_returns()`


#### `test_all_positive()`


#### `test_all_negative()`


#### `test_mixed_returns()`


#### `test_with_zero()`


#### `test_equal_positive_negative()`


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


