# Documentation: returns_avg_win.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/returns_avg_win.rs`
- **Size**: 4,297 bytes
- **Lines**: 133
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

#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct ReturnsAverageWin {}

impl Display for ReturnsAverageWin {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Average Win (Return)")
    }
}

impl PortfolioStatistic for ReturnsAverageWin {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_returns(&self, returns: &Returns) -> Option<Self::Item> {
        if !self.check_valid_returns(returns) {
            return Some(f64::NAN);
        }

        let negative_returns: Vec<f64> = returns.values().copied().filter(|&x| x > 0.0).collect();

        if negative_returns.is_empty() {
            return Some(f64::NAN);
        }

        let sum: f64 = negative_returns.iter().sum();
        let count = negative_returns.len() as f64;

        Some(sum / count)
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

    fn create_returns(values: Vec<f64>) -> Returns {
        let mut new_return = BTreeMap::new();
        for (i, value) in values.iter().enumerate() {
            new_return.insert(UnixNanos::from(i as u64), *value);
        }
        new_return
    }

    #[rstest]
    fn test_empty_returns() {
        let avg_win = ReturnsAverageWin {};
        let returns = create_returns(vec![]);
        let result = avg_win.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_all_negative() {
        let avg_win = ReturnsAverageWin {};
        let returns = create_returns(vec![-10.0, -20.0, -30.0]);
        let result = avg_win.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_all_positive() {
        let avg_win = ReturnsAverageWin {};
        let returns = create_returns(vec![10.0, 20.0, 30.0]);
        let result = avg_win.calculate_from_returns(&returns);
        assert!(result.is_some());
        // Average of [10.0, 20.0, 30.0] = (10 + 20 + 30) / 3 = 20.0
        assert!(approx_eq!(f64, result.unwrap(), 20.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_mixed_returns() {
        let avg_win = ReturnsAverageWin {};
        let returns = create_returns(vec![10.0, -20.0, 30.0, -40.0]);
        let result = avg_win.calculate_from_returns(&returns);
        assert!(result.is_some());
        // Average of [10.0, 30.0] = (10 + 30) / 2 = 20.0
        assert!(approx_eq!(f64, result.unwrap(), 20.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let avg_win = ReturnsAverageWin {};
        assert_eq!(avg_win.name(), "Average Win (Return)");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`create_returns()`**: Function defined in this file
- **`test_empty_returns()`**: Function defined in this file
- **`test_all_negative()`**: Function defined in this file
- **`test_all_positive()`**: Function defined in this file
- **`test_mixed_returns()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`ReturnsAverageWin`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `create_returns`, `fmt`, `name`, `test_all_negative`, `test_all_positive`, `test_empty_returns`, `test_mixed_returns`, `test_name`
**Impls**: `Display`, `PortfolioStatistic`
**Structs**: `ReturnsAverageWin`

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
*Generated on 2025-11-18T21:55:00.863059Z*
