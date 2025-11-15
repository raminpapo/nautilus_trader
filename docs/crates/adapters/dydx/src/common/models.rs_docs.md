# Documentation: `crates/adapters/dydx/src/common/models.rs`
**Generated:** 2025-11-15T19:40:00.903371Z
**File Size:** 1428 bytes
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

- **Path:** `crates/adapters/dydx/src/common/models.rs`
- **Size:** 1,428 bytes
- **Lines:** 32
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1

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

//! Common types and models for the dYdX adapter.

use serde::{Deserialize, Serialize};

/// dYdX account information.
///
/// Represents a Cosmos SDK account with its address, account number,
/// and current sequence (nonce) for transaction ordering.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxAccount {
    /// Cosmos SDK address (dydx...).
    pub address: String,
    /// Account number from the blockchain.
    pub account_number: u64,
    /// Current sequence number (nonce) for transactions.
    pub sequence: u64,
}
```


---

## Overview

This file is located at `crates/adapters/dydx/src/common/models.rs` within the repository.

**Classes defined:** DydxAccount


---

## Detailed Analysis

### Classes

#### `DydxAccount`

**Type:** struct



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src/common`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


