# Documentation: `crates/adapters/kraken/src/common/models.rs`
**Generated:** 2025-11-15T19:40:01.129061Z
**File Size:** 1564 bytes
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

- **Path:** `crates/adapters/kraken/src/common/models.rs`
- **Size:** 1,564 bytes
- **Lines:** 40
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
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

//! Common data structures shared across the Kraken adapter.

use serde::{Deserialize, Serialize};

/// Generic Kraken API response wrapper.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct KrakenResponse<T> {
    pub result: Option<T>,
    pub error: Option<Vec<String>>,
    #[serde(default)]
    pub success: bool,
}

impl<T> KrakenResponse<T> {
    pub fn is_success(&self) -> bool {
        self.success || (self.error.is_none() || self.error.as_ref().is_some_and(|e| e.is_empty()))
    }

    pub fn error_message(&self) -> Option<String> {
        self.error
            .as_ref()
            .filter(|e| !e.is_empty())
            .map(|e| e.join(", "))
    }
}
```


---

## Overview

This file is located at `crates/adapters/kraken/src/common/models.rs` within the repository.

**Classes defined:** KrakenResponse

**Functions defined:** is_success, error_message


---

## Detailed Analysis

### Classes

#### `KrakenResponse`

**Type:** struct


### Functions

#### `is_success(&self)`


#### `error_message(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


