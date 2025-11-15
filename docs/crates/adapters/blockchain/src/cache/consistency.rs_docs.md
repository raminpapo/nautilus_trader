# Documentation: `crates/adapters/blockchain/src/cache/consistency.rs`
**Generated:** 2025-11-15T19:40:00.438963Z
**File Size:** 1945 bytes
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

- **Path:** `crates/adapters/blockchain/src/cache/consistency.rs`
- **Size:** 1,945 bytes
- **Lines:** 43
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


---

## Overview

This file is located at `crates/adapters/blockchain/src/cache/consistency.rs` within the repository.

**Classes defined:** helps, CachedBlocksConsistencyStatus, CachedBlocksConsistencyStatus

**Functions defined:** new, is_consistent


---

## Detailed Analysis

### Classes

#### `helps`

**Type:** struct


#### `CachedBlocksConsistencyStatus`

**Type:** struct


#### `CachedBlocksConsistencyStatus`

**Type:** impl


### Functions

#### `new(max_block: u64, last_continuous_block: u64)`


#### `is_consistent(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/cache`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


