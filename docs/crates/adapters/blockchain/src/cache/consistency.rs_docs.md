# Documentation: consistency.rs

## File Metadata

- **Path**: `crates/adapters/blockchain/src/cache/consistency.rs`
- **Size**: 1,945 bytes
- **Lines**: 44
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

/// Represents the consistency status of cached blockchain blocks, tracking gaps in the block sequence.
///
/// This struct helps determine the optimal sync strategy by comparing the highest cached block
/// with the last continuous block number. When these values differ, it indicates gaps exist
/// in the cached data that require special handling during synchronization.
#[derive(Debug, Clone)]
pub struct CachedBlocksConsistencyStatus {
    /// The highest block number present in the cache
    pub max_block: u64,
    /// The highest block number in a continuous sequence from the beginning
    pub last_continuous_block: u64,
}

impl CachedBlocksConsistencyStatus {
    #[must_use]
    pub const fn new(max_block: u64, last_continuous_block: u64) -> Self {
        Self {
            max_block,
            last_continuous_block,
        }
    }

    /// Returns true if the cached blocks form a continuous sequence without gaps.
    #[must_use]
    pub const fn is_consistent(&self) -> bool {
        self.max_block == self.last_continuous_block
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`is_consistent()`**: Function defined in this file

### Classes
- **`helps`**: Class defined in this file
- **`CachedBlocksConsistencyStatus`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `is_consistent`, `new`
**Impls**: `CachedBlocksConsistencyStatus`
**Structs**: `CachedBlocksConsistencyStatus`, `helps`

## Related Files

This file is located in `crates/adapters/blockchain/src/cache/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.151976Z*
