# Documentation: win_rate.rs

## File Metadata

- **Path**: `crates/analysis/src/statistics/win_rate.rs`
- **Size**: 4,397 bytes
- **Lines**: 130
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

/// Calculates the win rate of a trading strategy based on realized PnLs.
///
/// Win rate is the percentage of profitable trades out of total trades:
/// `Count(Trades with PnL > 0) / Total Trades`
///
/// Returns a value between 0.0 and 1.0, where 1.0 represents 100% winning trades.
///
/// Note: While a high win rate is desirable, it should be considered alongside
/// average win/loss sizes and profit factor for complete system evaluation.
///
/// # References
///
/// - Standard trading performance metric across the industry
/// - Tharp, V. K. (1998). *Trade Your Way to Financial Freedom*. McGraw-Hill.
/// - Kaufman, P. J. (2013). *Trading Systems and Methods* (5th ed.). Wiley.
#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct WinRate {}

impl Display for WinRate {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Win Rate")
    }
}

impl PortfolioStatistic for WinRate {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_realized_pnls(&self, realized_pnls: &[f64]) -> Option<Self::Item> {
        if realized_pnls.is_empty() {
            return Some(0.0);
        }

        let (winners, losers): (Vec<f64>, Vec<f64>) =
            realized_pnls.iter().partition(|&&pnl| pnl > 0.0);

        let total_trades = winners.len() + losers.len();
        Some(winners.len() as f64 / total_trades.max(1) as f64)
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
        let win_rate = WinRate {};
        let result = win_rate.calculate_from_realized_pnls(&[]);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_winning_trades() {
        let win_rate = WinRate {};
        let realized_pnls = vec![100.0, 50.0, 200.0];
        let result = win_rate.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 1.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_losing_trades() {
        let win_rate = WinRate {};
        let realized_pnls = vec![-100.0, -50.0, -200.0];
        let result = win_rate.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_mixed_trades() {
        let win_rate = WinRate {};
        let realized_pnls = vec![100.0, -50.0, 200.0, -100.0];
        let result = win_rate.calculate_from_realized_pnls(&realized_pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.5, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let win_rate = WinRate {};
        assert_eq!(win_rate.name(), "Win Rate");
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 10 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`name()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`test_empty_pnls()`**: Function defined in this file
- **`test_all_winning_trades()`**: Function defined in this file
- **`test_all_losing_trades()`**: Function defined in this file
- **`test_mixed_trades()`**: Function defined in this file
- **`test_name()`**: Function defined in this file

### Classes
- **`WinRate`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Functions**: `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `fmt`, `name`, `test_all_losing_trades`, `test_all_winning_trades`, `test_empty_pnls`, `test_mixed_trades`, `test_name`
**Impls**: `Display`, `PortfolioStatistic`
**Structs**: `WinRate`

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
*Generated on 2025-11-18T21:55:00.873267Z*
