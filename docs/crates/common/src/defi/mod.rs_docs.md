# Documentation: mod.rs

## File Metadata

- **Path**: `crates/common/src/defi/mod.rs`
- **Size**: 1,558 bytes
- **Lines**: 40
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

//! DeFi (Decentralized Finance) integration for NautilusTrader.
//!
//! This module provides centralized access to DeFi functionality throughout the common crate.
//! DeFi support includes:
//!
//! # Feature Flag
//!
//! All DeFi functionality requires the `defi` feature flag to be enabled:
//! ```toml
//! nautilus-common = { version = "0.x", features = ["defi"] }
//! ```

pub mod cache;
pub mod data_actor;
pub mod switchboard;

// Re-exports
// Re-exports
pub use switchboard::{
    get_defi_blocks_topic, get_defi_collect_topic, get_defi_flash_topic, get_defi_liquidity_topic,
    get_defi_pool_swaps_topic, get_defi_pool_topic,
};

pub use crate::messages::defi::*;

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/common/src/defi/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.094174Z*
