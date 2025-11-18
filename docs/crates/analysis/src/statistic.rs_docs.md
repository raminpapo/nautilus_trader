# Documentation: statistic.rs

## File Metadata

- **Path**: `crates/analysis/src/statistic.rs`
- **Size**: 4,236 bytes
- **Lines**: 111
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

use std::{collections::BTreeMap, fmt::Debug};

use nautilus_model::{orders::Order, position::Position};

use crate::Returns;

const IMPL_ERR: &str = "is not implemented for";

/// Trait for portfolio performance statistics that can be calculated from different data sources.
///
/// This trait provides a flexible framework for implementing various financial performance
/// metrics that can operate on returns, realized PnLs, orders, or positions data.
/// Each statistic implementation should override the relevant calculation methods.
#[allow(unused_variables)]
pub trait PortfolioStatistic: Debug {
    type Item;

    /// Returns the name of this statistic for display and identification purposes.
    fn name(&self) -> String;

    /// Calculates the statistic from time-indexed returns data.
    ///
    /// # Panics
    ///
    /// Panics if this method is not implemented for the specific statistic.
    fn calculate_from_returns(&self, returns: &Returns) -> Option<Self::Item> {
        panic!("`calculate_from_returns` {IMPL_ERR} `{}`", self.name());
    }

    /// Calculates the statistic from realized profit and loss values.
    ///
    /// # Panics
    ///
    /// Panics if this method is not implemented for the specific statistic.
    fn calculate_from_realized_pnls(&self, realized_pnls: &[f64]) -> Option<Self::Item> {
        panic!(
            "`calculate_from_realized_pnls` {IMPL_ERR} `{}`",
            self.name()
        );
    }

    /// Calculates the statistic from order data.
    ///
    /// # Panics
    ///
    /// Panics if this method is not implemented for the specific statistic.
    #[allow(dead_code)]
    fn calculate_from_orders(&self, orders: Vec<Box<dyn Order>>) -> Option<Self::Item> {
        panic!("`calculate_from_orders` {IMPL_ERR} `{}`", self.name());
    }

    /// Calculates the statistic from position data.
    ///
    /// # Panics
    ///
    /// Panics if this method is not implemented for the specific statistic.
    fn calculate_from_positions(&self, positions: &[Position]) -> Option<Self::Item> {
        panic!("`calculate_from_positions` {IMPL_ERR} `{}`", self.name());
    }

    /// Validates that returns data is not empty.
    fn check_valid_returns(&self, returns: &Returns) -> bool {
        !returns.is_empty()
    }

    /// Downsamples high-frequency returns to daily bins for daily statistics calculation.
    fn downsample_to_daily_bins(&self, returns: &Returns) -> Returns {
        let nanos_per_day = 86_400_000_000_000; // Number of nanoseconds in a day
        let mut daily_bins = BTreeMap::new();

        for (&timestamp, &value) in returns {
            // Calculate the start of the day in nanoseconds for the given timestamp
            let day_start = timestamp - (timestamp.as_u64() % nanos_per_day);

            // Sum returns for each day
            *daily_bins.entry(day_start).or_insert(0.0) += value;
        }

        daily_bins
    }

    /// Calculates the standard deviation of returns with Bessel's correction.
    fn calculate_std(&self, returns: &Returns) -> f64 {
        let n = returns.len() as f64;
        if n < 2.0 {
            return f64::NAN;
        }

        let mean = returns.values().sum::<f64>() / n;

        let variance = returns.values().map(|x| (x - mean).powi(2)).sum::<f64>() / (n - 1.0);

        variance.sqrt()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 8 function(s).

## Detailed Walkthrough

### Functions
- **`name()`**: Function defined in this file
- **`calculate_from_returns()`**: Function defined in this file
- **`calculate_from_realized_pnls()`**: Function defined in this file
- **`calculate_from_orders()`**: Function defined in this file
- **`calculate_from_positions()`**: Function defined in this file
- **`check_valid_returns()`**: Function defined in this file
- **`downsample_to_daily_bins()`**: Function defined in this file
- **`calculate_std()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 10


**Functions**: `calculate_from_orders`, `calculate_from_positions`, `calculate_from_realized_pnls`, `calculate_from_returns`, `calculate_std`, `check_valid_returns`, `downsample_to_daily_bins`, `name`
**Traits**: `PortfolioStatistic`, `provides`

## Related Files

This file is located in `crates/analysis/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.830193Z*
