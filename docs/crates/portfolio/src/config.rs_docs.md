# Documentation: config.rs

## File Metadata

- **Path**: `crates/portfolio/src/config.rs`
- **Size**: 2,852 bytes
- **Lines**: 65
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

use serde::{Deserialize, Serialize};

/// Configuration for `Portfolio` instances.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PortfolioConfig {
    /// The type of prices used for portfolio calculations, such as unrealized PnLs.
    /// If false (default), uses quote prices if available; otherwise, last trade prices
    /// (or falls back to bar prices if `bar_updates` is true).
    /// If true, uses mark prices.
    #[serde(default)]
    pub use_mark_prices: bool,
    /// The type of exchange rates used for portfolio calculations.
    /// If false (default), uses quote prices.
    /// If true, uses mark prices.
    #[serde(default)]
    pub use_mark_xrates: bool,
    /// If external bars should be considered for updating unrealized PnLs.
    #[serde(default = "default_true")]
    pub bar_updates: bool,
    /// If calculations should be converted into each account's base currency.
    /// This setting is only effective for accounts with a specified base currency.
    #[serde(default = "default_true")]
    pub convert_to_account_base_currency: bool,
    /// The minimum interval (milliseconds) between logging account state events for the same account.
    /// When set, account state updates will only be logged if this much time has passed since the last log.
    /// Useful for HFT deployments to prevent excessive logging when account states change rapidly.
    #[serde(default)]
    pub min_account_state_logging_interval_ms: Option<u64>,
    /// If debug mode is active (will provide extra debug logging).
    #[serde(default)]
    pub debug: bool,
}

const fn default_true() -> bool {
    true
}

impl Default for PortfolioConfig {
    fn default() -> Self {
        Self {
            use_mark_prices: false,
            use_mark_xrates: false,
            bar_updates: true,
            convert_to_account_base_currency: true,
            min_account_state_logging_interval_ms: None,
            debug: false,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`default_true()`**: Function defined in this file
- **`default()`**: Function defined in this file

### Classes
- **`PortfolioConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `default`, `default_true`
**Impls**: `Default`
**Structs**: `PortfolioConfig`

## Related Files

This file is located in `crates/portfolio/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.589411Z*
