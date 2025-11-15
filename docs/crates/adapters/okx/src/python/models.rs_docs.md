# Documentation: `crates/adapters/okx/src/python/models.rs`
**Generated:** 2025-11-15T19:40:01.307552Z
**File Size:** 1215 bytes
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

- **Path:** `crates/adapters/okx/src/python/models.rs`
- **Size:** 1,215 bytes
- **Lines:** 36
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
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

use pyo3::prelude::*;

use crate::http::models::OKXBalanceDetail;

#[pymethods]
impl OKXBalanceDetail {
    #[getter]
    fn ccy(&self) -> String {
        self.ccy.to_string()
    }

    #[getter]
    fn cash_bal(&self) -> &str {
        &self.cash_bal
    }

    #[getter]
    fn liab(&self) -> &str {
        &self.liab
    }
}
```


---

## Overview

This file is located at `crates/adapters/okx/src/python/models.rs` within the repository.

**Classes defined:** OKXBalanceDetail

**Functions defined:** ccy, cash_bal, liab


---

## Detailed Analysis

### Classes

#### `OKXBalanceDetail`

**Type:** impl


### Functions

#### `ccy(&self)`


#### `cash_bal(&self)`


#### `liab(&self)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


