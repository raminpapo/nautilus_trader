# Documentation: `crates/core/src/python/version.rs`
**Generated:** 2025-11-15T19:40:01.935901Z
**File Size:** 3587 bytes
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

- **Path:** `crates/core/src/python/version.rs`
- **Size:** 3,587 bytes
- **Lines:** 88
- **Extension:** `.rs`
- **Type:** text
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

//! Functions for introspecting the running Python interpreter & installed packages.

#![allow(clippy::manual_let_else)]
use pyo3::{prelude::*, types::PyTuple};

/// Retrieves the Python interpreter version as a string.
///
/// # Panics
///
/// Panics if `version_info` cannot be downcast to a tuple or if tuple elements are missing.
#[must_use]
pub fn get_python_version() -> String {
    Python::attach(|py| {
        let sys = match py.import("sys") {
            Ok(mod_sys) => mod_sys,
            Err(_) => return "Unavailable (failed to import sys)".to_string(),
        };

        let version_info = match sys.getattr("version_info") {
            Ok(info) => info,
            Err(_) => return "Unavailable (version_info not found)".to_string(),
        };

        let version_tuple: &Bound<'_, PyTuple> = version_info
            .cast::<PyTuple>()
            .expect("Failed to extract version_info");

        let major = version_tuple
            .get_item(0)
            .expect("Failed to get major version")
            .extract::<i32>()
            .unwrap_or(-1);
        let minor = version_tuple
            .get_item(1)
            .expect("Failed to get minor version")
            .extract::<i32>()
            .unwrap_or(-1);
        let micro = version_tuple
            .get_item(2)
            .expect("Failed to get micro version")
            .extract::<i32>()
            .unwrap_or(-1);

        if major == -1 || minor == -1 || micro == -1 {
            "Unavailable (failed to extract version components)".to_string()
        } else {
            format!("{major}.{minor}.{micro}")
        }
    })
}

#[must_use]
/// Attempt to retrieve the `__version__` attribute of a *Python* package.
///
/// When the requested package cannot be imported, or when it does not define a `__version__`
/// attribute, the function returns a human-readable fallback string that starts with
/// `"Unavailable"` so that downstream code can distinguish *real* version strings from error
/// cases.
///
/// This helper is primarily intended for diagnostic/logging purposes inside the NautilusTrader
/// Python bindings.
pub fn get_python_package_version(package_name: &str) -> String {
    Python::attach(|py| match py.import(package_name) {
        Ok(package) => match package.getattr("__version__") {
            Ok(version_attr) => match version_attr.extract::<String>() {
                Ok(version) => version,
                Err(_) => "Unavailable (failed to extract version)".to_string(),
            },
            Err(_) => "Unavailable (__version__ attribute not found)".to_string(),
        },
        Err(_) => "Unavailable (failed to import package)".to_string(),
    })
}
```


---

## Overview

This file is located at `crates/core/src/python/version.rs` within the repository.

**Functions defined:** get_python_version, get_python_package_version


---

## Detailed Analysis

### Functions

#### `get_python_version()`


#### `get_python_package_version(package_name: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/src/python`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


