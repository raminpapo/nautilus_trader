# Documentation: `crates/analysis/src/statistics/loser_min.rs`
**Generated:** 2025-11-15T19:40:01.562946Z
**File Size:** 4653 bytes
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

- **Path:** `crates/analysis/src/statistics/loser_min.rs`
- **Size:** 4,653 bytes
- **Lines:** 145
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 12

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

#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct MinLoser {}

impl Display for MinLoser {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Min Loser")
    }
}

impl PortfolioStatistic for MinLoser {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_realized_pnls(&self, realized_pnls: &[f64]) -> Option<Self::Item> {
        if realized_pnls.is_empty() {
            return Some(0.0);
        }

        // Match old Python behavior: filters for x <= 0.0 (includes zero)
        let losers: Vec<f64> = realized_pnls
            .iter()
            .filter(|&&pnl| pnl <= 0.0)
            .copied()
            .collect();

        if losers.is_empty() {
            return Some(0.0); // Match old Python behavior
        }

        losers
            .iter()
            .max_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal))
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
        let min_loser = MinLoser {};
        let result = min_loser.calculate_from_realized_pnls(&[]);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_positive() {
        let min_loser = MinLoser {};
        let pnls = vec![10.0, 20.0, 30.0];
        let result = min_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        // Returns 0.0 when no losers (matches old Python behavior)
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_all_negative() {
        let min_loser = MinLoser {};
        let pnls = vec![-10.0, -20.0, -30.0];
        let result = min_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -10.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_mixed_pnls() {
        let min_loser = MinLoser {};
        let pnls = vec![10.0, -20.0, 30.0, -40.0];
        let result = min_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -20.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_with_zero() {
        let min_loser = MinLoser {};
        let pnls = vec![10.0, 0.0, -20.0, -30.0];
        let result = min_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        // Includes zero in losers (x <= 0.0), so max is 0.0 (matches old Python behavior)
        assert!(approx_eq!(f64, result.unwrap(), 0.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_single_negative() {
        let min_loser = MinLoser {};
        let pnls = vec![-10.0];
        let result = min_loser.calculate_from_realized_pnls(&pnls);
        assert!(result.is_some());
        assert!(approx_eq!(f64, result.unwrap(), -10.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let min_loser = MinLoser {};
        assert_eq!(min_loser.name(), "Min Loser");
    }
}
```


---

## Overview

This file is located at `crates/analysis/src/statistics/loser_min.rs` within the repository.

**Classes defined:** MinLoser, Display, PortfolioStatistic

**Functions defined:** fmt, name, calculate_from_realized_pnls, calculate_from_returns, calculate_from_positions, test_empty_pnls, test_all_positive, test_all_negative, test_mixed_pnls, test_with_zero and 2 more


---

## Detailed Analysis

### Classes

#### `MinLoser`

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


#### `test_all_positive()`


#### `test_all_negative()`


#### `test_mixed_pnls()`


#### `test_with_zero()`


#### `test_single_negative()`


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


