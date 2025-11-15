# Documentation: `crates/adapters/hyperliquid/src/signing/types.rs`
**Generated:** 2025-11-15T19:40:01.072353Z
**File Size:** 1795 bytes
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

- **Path:** `crates/adapters/hyperliquid/src/signing/types.rs`
- **Size:** 1,795 bytes
- **Lines:** 49
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 4
- **Functions:** 3

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

use serde::{Deserialize, Serialize};

/// Unique identifier for a signer (API wallet or user address).
#[derive(Debug, Clone, Hash, PartialEq, Eq, Serialize, Deserialize)]
pub struct SignerId(pub String);

impl Display for SignerId {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.0)
    }
}

impl From<String> for SignerId {
    fn from(value: String) -> Self {
        Self(value)
    }
}

impl From<&str> for SignerId {
    fn from(value: &str) -> Self {
        Self(value.to_string())
    }
}

/// Hyperliquid action types for different signing schemes.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum HyperliquidActionType {
    /// L1 actions (agent deposits, withdrawals) - signed with L1 scheme.
    L1,
    /// User actions (trading) - signed with user-signed scheme.
    UserSigned,
}
```


---

## Overview

This file is located at `crates/adapters/hyperliquid/src/signing/types.rs` within the repository.

**Classes defined:** SignerId, Display, From, From

**Functions defined:** fmt, from, from


---

## Detailed Analysis

### Classes

#### `SignerId`

**Type:** struct


#### `Display`

**Type:** impl


#### `From`

**Type:** impl


#### `From`

**Type:** impl


### Functions

#### `fmt(&self, f: &mut std::fmt::Formatter<'_>)`


#### `from(value: String)`


#### `from(value: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/hyperliquid/src/signing`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


