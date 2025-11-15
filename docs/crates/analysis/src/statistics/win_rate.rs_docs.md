# Documentation: `crates/analysis/src/statistics/win_rate.rs`
**Generated:** 2025-11-15T19:40:01.578819Z
**File Size:** 4397 bytes
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

- **Path:** `crates/analysis/src/statistics/win_rate.rs`
- **Size:** 4,397 bytes
- **Lines:** 129
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 10

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


---

## Overview

This file is located at `crates/analysis/src/statistics/win_rate.rs` within the repository.

**Classes defined:** WinRate, Display, PortfolioStatistic

**Functions defined:** fmt, name, calculate_from_realized_pnls, calculate_from_returns, calculate_from_positions, test_empty_pnls, test_all_winning_trades, test_all_losing_trades, test_mixed_trades, test_name


---

## Detailed Analysis

### Classes

#### `WinRate`

**Type:** struct


#### `Display`

**Type:** impl


#### `PortfolioStatistic`

**Type:** impl


### Functions

#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `name(&self)`


#### `calculate_from_realized_pnls(&self, realized_pnls: &[f64])`


#### `calculate_from_returns(&self, _returns: &Returns)`


#### `calculate_from_positions(&self, _positions: &[Position])`


#### `test_empty_pnls()`


#### `test_all_winning_trades()`


#### `test_all_losing_trades()`


#### `test_mixed_trades()`


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


