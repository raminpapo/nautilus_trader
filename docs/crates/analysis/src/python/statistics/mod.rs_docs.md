# Documentation: mod.rs

## File Metadata

- **Path**: `crates/analysis/src/python/statistics/mod.rs`
- **Size**: 1,628 bytes
- **Lines**: 49
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

//! Python bindings for trading performance statistics.

pub mod cagr;
pub mod calmar_ratio;
pub mod expectancy;
pub mod long_ratio;
pub mod loser_avg;
pub mod loser_max;
pub mod loser_min;
pub mod max_drawdown;
pub mod profit_factor;
pub mod returns_avg;
pub mod returns_avg_loss;
pub mod returns_avg_win;
pub mod returns_volatility;
pub mod risk_return_ratio;
pub mod sharpe_ratio;
pub mod sortino_ratio;
pub mod win_rate;
pub mod winner_avg;
pub mod winner_max;
pub mod winner_min;

use std::collections::BTreeMap;

use nautilus_core::UnixNanos;

fn transform_returns(raw_returns: BTreeMap<u64, f64>) -> BTreeMap<UnixNanos, f64> {
    raw_returns
        .keys()
        .map(|&k| (UnixNanos::from(k), raw_returns[&k]))
        .collect()
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`transform_returns()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `transform_returns`

## Related Files

This file is located in `crates/analysis/src/python/statistics/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.802934Z*
