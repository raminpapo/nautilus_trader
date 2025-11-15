# Documentation: `crates/cryptography/src/python/mod.rs`
**Generated:** 2025-11-15T19:40:01.956719Z
**File Size:** 1467 bytes
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

- **Path:** `crates/cryptography/src/python/mod.rs`
- **Size:** 1,467 bytes
- **Lines:** 35
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 1

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

//! Python bindings from [PyO3](https://pyo3.rs).

pub mod signing;

use pyo3::prelude::*;

use crate::python;

/// Loaded as `nautilus_pyo3.cryptography`.
///
/// # Errors
///
/// Returns a `PyErr` if registering any module components fails.
#[pymodule]
pub fn cryptography(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(python::signing::py_hmac_signature, m)?)?;
    m.add_function(wrap_pyfunction!(python::signing::py_rsa_signature, m)?)?;
    m.add_function(wrap_pyfunction!(python::signing::py_ed25519_signature, m)?)?;
    Ok(())
}
```


---

## Overview

This file is located at `crates/cryptography/src/python/mod.rs` within the repository.

**Functions defined:** cryptography


---

## Detailed Analysis

### Functions

#### `cryptography(_py: Python, m: &Bound<'_, PyModule>)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/cryptography/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


