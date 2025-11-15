# Documentation: `crates/analysis/src/statistics/returns_avg.rs`
**Generated:** 2025-11-15T19:40:01.568455Z
**File Size:** 3863 bytes
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

- **Path:** `crates/analysis/src/statistics/returns_avg.rs`
- **Size:** 3,863 bytes
- **Lines:** 122
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

#[repr(C)]
#[derive(Debug, Clone)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.analysis")
)]
pub struct ReturnsAverage {}

impl Display for ReturnsAverage {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Average (Return)")
    }
}

impl PortfolioStatistic for ReturnsAverage {
    type Item = f64;

    fn name(&self) -> String {
        self.to_string()
    }

    fn calculate_from_returns(&self, returns: &Returns) -> Option<Self::Item> {
        if !self.check_valid_returns(returns) {
            return Some(f64::NAN);
        }

        let negative_returns: Vec<f64> = returns.values().copied().filter(|&x| x != 0.0).collect();

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
        let avg = ReturnsAverage {};
        let returns = create_returns(vec![]);
        let result = avg.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_all_zero() {
        let avg = ReturnsAverage {};
        let returns = create_returns(vec![0.0, 0.0, 0.0]);
        let result = avg.calculate_from_returns(&returns);
        assert!(result.is_some());
        assert!(result.unwrap().is_nan());
    }

    #[rstest]
    fn test_mixed_non_zero() {
        let avg = ReturnsAverage {};
        let returns = create_returns(vec![10.0, -20.0, 0.0, 30.0, -40.0]);
        let result = avg.calculate_from_returns(&returns);
        assert!(result.is_some());
        // Average of [10.0, -20.0, 30.0, -40.0] = (-20 + -40 + 10 + 30) / 4 = -5.0
        assert!(approx_eq!(f64, result.unwrap(), -5.0, epsilon = 1e-9));
    }

    #[rstest]
    fn test_name() {
        let avg = ReturnsAverage {};
        assert_eq!(avg.name(), "Average (Return)");
    }
}
```


---

## Overview

This file is located at `crates/analysis/src/statistics/returns_avg.rs` within the repository.

**Classes defined:** ReturnsAverage, Display, PortfolioStatistic

**Functions defined:** fmt, name, calculate_from_returns, calculate_from_realized_pnls, calculate_from_positions, create_returns, test_empty_returns, test_all_zero, test_mixed_non_zero, test_name


---

## Detailed Analysis

### Classes

#### `ReturnsAverage`

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


#### `test_all_zero()`


#### `test_mixed_non_zero()`


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


