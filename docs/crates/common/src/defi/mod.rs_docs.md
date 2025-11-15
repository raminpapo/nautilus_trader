# Documentation: `crates/common/src/defi/mod.rs`
**Generated:** 2025-11-15T19:40:01.712225Z
**File Size:** 1558 bytes
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

- **Path:** `crates/common/src/defi/mod.rs`
- **Size:** 1,558 bytes
- **Lines:** 39
- **Extension:** `.rs`
- **Type:** text

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


---

## Overview

This file is located at `crates/common/src/defi/mod.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/defi`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


