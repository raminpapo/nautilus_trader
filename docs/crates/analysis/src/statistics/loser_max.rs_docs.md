# Documentation: loser_max.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/loser_max.rs`
- **Size**: 4,485 bytes
- **Lines**: 144
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
pub struct MaxLoser {}

impl Display for MaxLoser {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Max Loser")
    }
}

impl PortfolioStatistic for MaxLoser {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_realized_pnls(&self, realized_pnls: &[f64]) -> Option<Self::Item> {
        if realized_pnls.is_empty() {
            return Some(0.0);
        }

        let losers: Vec<f64> = realized_pnls
            .iter()
            .filter(|&&pnl| pnl < 0.0)
            .copied()
            .collect();

        if losers.is_empty() {
            return Some(0.0); // Match old Python behavior
        }

        losers
            .iter()
            .min_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal))
            .copied()
    }

    fn calculate_from_returns(&self, _returns: &Returns) -> Option<Self::Item> {
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
    use nautilus_core::approx_eq;
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_empty_pnls() {
        let max_loser = MaxLoser {};
        let result = max_loser.calculate_from_realized_pnls(&[]);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_positive() {
        let max_loser = MaxLoser {};
        let pnls = vec![10.0, 20.0, 30.0];
        let result = max_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        // Returns 0.0 when no losers (matches old Python behavior)
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_negative() {
        let max_loser = MaxLoser {};
        let pnls = vec![-10.0, -20.0, -30.0];
        let result = max_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -30.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_mixed_pnls() {
        let max_loser = MaxLoser {};
        let pnls = vec![10.0, -20.0, 30.0, -40.0];
        let result = max_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -40.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_with_zero() {
        let max_loser = MaxLoser {};
        let pnls = vec![10.0, 0.0, -20.0, -30.0];
        let result = max_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -30.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_single_value() {
        let max_loser = MaxLoser {};
        let pnls = vec![-10.0];
        let result = max_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -10.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let max_loser = MaxLoser {};
        assert_eq!(max_loser.name(), "Max Loser");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 12 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`test_empty_pnls()`**: Function defined in this file
- **`test_all_positive()`**: Function defined in this file
- **`test_all_negative()`**: Function defined in this file
- **`test_mixed_pnls()`**: Function defined in this file
- **`test_with_zero()`**: Function defined in this file
- **`test_single_value()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`MaxLoser`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `fmt`, `name`, `test_all_negative`, `test_all_positive`, `test_empty_pnls`, `test_mixed_pnls`, `test_name`, `test_single_value`, `test_with_zero`
**Impls**: `Display`, `PortfolioStatistic`
**Structs**: `MaxLoser`

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
*Generated on 2025-11-18T21:55:00.846204Z*
