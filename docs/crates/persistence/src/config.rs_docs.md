# Documentation: config.rs

## File Metadata

- **Path**: `crates/persistence/src/config.rs`
- **Size**: 2,408 bytes
- **Lines**: 72
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

// Under development
#![allow(dead_code)]
#![allow(unused_variables)]

use crate::backend::feather::RotationConfig;

/// Configuration for streaming live or backtest runs to the catalog in feather format.
#[derive(Debug, Clone)]
pub struct StreamingConfig {
    /// The path to the data catalog.
    catalog_path: String,
    /// The `fsspec` filesystem protocol for the catalog.
    fst_protocol: String,
    /// The flush interval (milliseconds) for writing chunks.
    flush_interval_ms: u64,
    /// If any existing feather files should be replaced.
    replace_existing: bool,
    /// Rotation config
    rotation_config: RotationConfig,
}

impl StreamingConfig {
    /// Create a new streaming configuration.
    #[must_use]
    pub const fn new(
        catalog_path: String,
        fst_protocol: String,
        flush_interval_ms: u64,
        replace_existing: bool,
        rotation_config: RotationConfig,
    ) -> Self {
        Self {
            catalog_path,
            fst_protocol,
            flush_interval_ms,
            replace_existing,
            rotation_config,
        }
    }
}

/// Configuration for a data catalog.
pub struct DataCatalogConfig {
    /// The path to the data catalog.
    path: String,
    /// The fsspec file system protocol for the data catalog.
    fs_protocol: String,
}

impl DataCatalogConfig {
    /// Create a new data catalog configuration.
    #[must_use]
    pub const fn new(path: String, fs_protocol: String) -> Self {
        Self { path, fs_protocol }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file

### Classes
- **`StreamingConfig`**: Class defined in this file
- **`DataCatalogConfig`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `new`
**Impls**: `DataCatalogConfig`, `StreamingConfig`
**Structs**: `DataCatalogConfig`, `StreamingConfig`

## Related Files

This file is located in `crates/persistence/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:03.542152Z*
