# Documentation: `crates/common/src/cache/config.rs`
**Generated:** 2025-11-15T19:40:01.662650Z
**File Size:** 3802 bytes
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

- **Path:** `crates/common/src/cache/config.rs`
- **Size:** 3,802 bytes
- **Lines:** 102
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 2

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

use serde::{Deserialize, Serialize};

use crate::{enums::SerializationEncoding, msgbus::database::DatabaseConfig};

/// Configuration for `Cache` instances.
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.common")
)]
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(default)]
pub struct CacheConfig {
    /// The configuration for the cache backing database.
    pub database: Option<DatabaseConfig>,
    /// The encoding for database operations, controls the type of serializer used.
    pub encoding: SerializationEncoding,
    /// If timestamps should be persisted as ISO 8601 strings.
    pub timestamps_as_iso8601: bool,
    /// The buffer interval (milliseconds) between pipelined/batched transactions.
    pub buffer_interval_ms: Option<usize>,
    /// If a 'trader-' prefix is used for keys.
    pub use_trader_prefix: bool,
    /// If the trader's instance ID is used for keys.
    pub use_instance_id: bool,
    /// If the database should be flushed on start.
    pub flush_on_start: bool,
    /// If instrument data should be dropped from the cache's memory on reset.
    pub drop_instruments_on_reset: bool,
    /// The maximum length for internal tick deques.
    pub tick_capacity: usize,
    /// The maximum length for internal bar deques.
    pub bar_capacity: usize,
    /// If market data should be persisted to disk.
    pub save_market_data: bool,
}

impl Default for CacheConfig {
    /// Creates a new default [`CacheConfig`] instance.
    fn default() -> Self {
        Self {
            database: None,
            encoding: SerializationEncoding::MsgPack,
            timestamps_as_iso8601: false,
            buffer_interval_ms: None,
            use_trader_prefix: true,
            use_instance_id: false,
            flush_on_start: false,
            drop_instruments_on_reset: true,
            tick_capacity: 10_000,
            bar_capacity: 10_000,
            save_market_data: false,
        }
    }
}

impl CacheConfig {
    /// Creates a new [`CacheConfig`] instance.
    #[allow(clippy::too_many_arguments)]
    #[must_use]
    pub const fn new(
        database: Option<DatabaseConfig>,
        encoding: SerializationEncoding,
        timestamps_as_iso8601: bool,
        buffer_interval_ms: Option<usize>,
        use_trader_prefix: bool,
        use_instance_id: bool,
        flush_on_start: bool,
        drop_instruments_on_reset: bool,
        tick_capacity: usize,
        bar_capacity: usize,
        save_market_data: bool,
    ) -> Self {
        Self {
            database,
            encoding,
            timestamps_as_iso8601,
            buffer_interval_ms,
            use_trader_prefix,
            use_instance_id,
            flush_on_start,
            drop_instruments_on_reset,
            tick_capacity,
            bar_capacity,
            save_market_data,
        }
    }
}
```


---

## Overview

This file is located at `crates/common/src/cache/config.rs` within the repository.

**Classes defined:** CacheConfig, Default, CacheConfig

**Functions defined:** default, new


---

## Detailed Analysis

### Classes

#### `CacheConfig`

**Type:** struct


#### `Default`

**Type:** impl


#### `CacheConfig`

**Type:** impl


### Functions

#### `default()`


#### `new(
        database: Option<DatabaseConfig>,
        encoding: SerializationEncoding,
        timestamps_as_iso8601: bool,
        buffer_interval_ms: Option<usize>,
        use_trader_prefix: bool,
        use_instance_id: bool,
        flush_on_start: bool,
        drop_instruments_on_reset: bool,
        tick_capacity: usize,
        bar_capacity: usize,
        save_market_data: bool,
    )`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/cache`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


