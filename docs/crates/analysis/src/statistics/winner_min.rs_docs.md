# Documentation: winner_min.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/winner_min.rs`
- **Size**: 4,382 bytes
- **Lines**: 135
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
pub struct MinWinner {}

impl Display for MinWinner {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Min Winner")
    }
}

impl PortfolioStatistic for MinWinner {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_realized_pnls(&self, realized_pnls: &[f64]) -> Option<Self::Item> {
        if realized_pnls.is_empty() {
            return Some(0.0);
        }

        let winners: Vec<f64> = realized_pnls
            .iter()
            .filter(|&&pnl| pnl > 0.0)
            .copied()
            .collect();

        if winners.is_empty() {
            return Some(0.0); // Match old Python behavior
        }

        winners
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
        let min_winner = MinWinner {};
        let result = min_winner.calculate_from_realized_pnls(&[]);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_no_winning_trades() {
        let min_winner = MinWinner {};
        let realized_pnls = vec![-100.0, -50.0, -200.0];
        let result = min_winner.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        // Returns 0.0 when no winners (matches old Python behavior)
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_winning_trades() {
        let min_winner = MinWinner {};
        let realized_pnls = vec![100.0, 50.0, 200.0];
        let result = min_winner.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 50.0, epsilon = 1e-9)); // Minimum of 100.0, 50.0, and 200.0 is 50.0
    }

    #[rstest]
    fn test_mixed_trades() {
        let min_winner = MinWinner {};
        let realized_pnls = vec![100.0, -50.0, 200.0, -100.0];
        let result = min_winner.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 100.0, epsilon = 1e-9)); // Minimum of 100.0 and 200.0 is 100.0
    }

    #[rstest]
    fn test_single_winning_trade() {
        let min_winner = MinWinner {};
        let realized_pnls = vec![50.0];
        let result = min_winner.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 50.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let min_winner = MinWinner {};
        assert_eq!(min_winner.name(), "Min Winner");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 11 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`test_empty_pnls()`**: Function defined in this file
- **`test_no_winning_trades()`**: Function defined in this file
- **`test_all_winning_trades()`**: Function defined in this file
- **`test_mixed_trades()`**: Function defined in this file
- **`test_single_winning_trade()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`MinWinner`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 14


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `fmt`, `name`, `test_all_winning_trades`, `test_empty_pnls`, `test_mixed_trades`, `test_name`, `test_no_winning_trades`, `test_single_winning_trade`
**Impls**: `Display`, `PortfolioStatistic`
**Structs**: `MinWinner`

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
*Generated on 2025-11-18T21:55:00.879021Z*
