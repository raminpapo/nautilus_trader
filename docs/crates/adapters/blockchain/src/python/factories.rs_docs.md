# Documentation: `crates/adapters/blockchain/src/python/factories.rs`
**Generated:** 2025-11-15T19:40:00.570773Z
**File Size:** 1593 bytes
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

- **Path:** `crates/adapters/blockchain/src/python/factories.rs`
- **Size:** 1,593 bytes
- **Lines:** 44
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 4

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

//! Python bindings for blockchain factories.

use pyo3::prelude::*;

use crate::factories::BlockchainDataClientFactory;

#[pymethods]
impl BlockchainDataClientFactory {
    /// Creates a new `BlockchainDataClientFactory` instance.
    #[new]
    const fn py_new() -> Self {
        Self::new()
    }

    /// Returns the factory name.
    const fn name(&self) -> &'static str {
        "BLOCKCHAIN"
    }

    /// Returns the configuration type.
    const fn config_type(&self) -> &'static str {
        "BlockchainDataClientConfig"
    }

    /// Returns a string representation of the factory.
    fn __repr__(&self) -> String {
        format!("BlockchainDataClientFactory(name={})", self.name())
    }
}
```


---

## Overview

This file is located at `crates/adapters/blockchain/src/python/factories.rs` within the repository.

**Classes defined:** BlockchainDataClientFactory

**Functions defined:** py_new, name, config_type, __repr__


---

## Detailed Analysis

### Classes

#### `BlockchainDataClientFactory`

**Type:** impl


### Functions

#### `py_new()`


#### `name(&self)`


#### `config_type(&self)`


#### `__repr__(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/blockchain/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


