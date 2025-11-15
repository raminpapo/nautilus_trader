# Documentation: `crates/execution/src/models/latency.rs`
**Generated:** 2025-11-15T19:40:02.107444Z
**File Size:** 1981 bytes
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

- **Path:** `crates/execution/src/models/latency.rs`
- **Size:** 1,981 bytes
- **Lines:** 54
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


---

## Overview

This file is located at `crates/execution/src/models/latency.rs` within the repository.

**Classes defined:** LatencyModel, LatencyModel, Display

**Functions defined:** new, fmt


---

## Detailed Analysis

### Classes

#### `LatencyModel`

**Type:** struct


#### `LatencyModel`

**Type:** impl


#### `Display`

**Type:** impl


### Functions

#### `new(
        base_latency_nanos: UnixNanos,
        insert_latency_nanos: UnixNanos,
        update_latency_nanos: UnixNanos,
        delete_latency_nanos: UnixNanos,
    )`


#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/execution/src/models`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


