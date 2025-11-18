# Documentation: latency.rs

## File Metadata

- **Path**: `crates/execution/src/models/latency.rs`
- **Size**: 1,981 bytes
- **Lines**: 55
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

use std::fmt::Display;

use nautilus_core::UnixNanos;

/// Provides latency modeling for order processing operations.
///
/// Models the latency for different order operations including base network latency
/// and specific operation latencies for insert, update, and delete operations.
#[derive(Debug)]
pub struct LatencyModel {
    pub base_latency_nanos: UnixNanos,
    pub insert_latency_nanos: UnixNanos,
    pub update_latency_nanos: UnixNanos,
    pub delete_latency_nanos: UnixNanos,
}

impl LatencyModel {
    /// Creates a new [`LatencyModel`] instance.
    #[must_use]
    pub const fn new(
        base_latency_nanos: UnixNanos,
        insert_latency_nanos: UnixNanos,
        update_latency_nanos: UnixNanos,
        delete_latency_nanos: UnixNanos,
    ) -> Self {
        Self {
            base_latency_nanos,
            insert_latency_nanos,
            update_latency_nanos,
            delete_latency_nanos,
        }
    }
}

impl Display for LatencyModel {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "LatencyModel()")
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`fmt()`**: Function defined in this file

### Classes
- **`LatencyModel`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `fmt`, `new`
**Impls**: `Display`, `LatencyModel`
**Structs**: `LatencyModel`

## Related Files

This file is located in `crates/execution/src/models/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.710932Z*
