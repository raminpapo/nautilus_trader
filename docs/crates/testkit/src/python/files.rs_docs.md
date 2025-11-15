# Documentation: `crates/testkit/src/python/files.rs`
**Generated:** 2025-11-15T19:40:03.786411Z
**File Size:** 1940 bytes
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

- **Path:** `crates/testkit/src/python/files.rs`
- **Size:** 1,940 bytes
- **Lines:** 45
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

use std::path::Path;

use nautilus_core::python::to_pyruntime_err;
use pyo3::prelude::*;

use crate::files::ensure_file_exists_or_download_http;

/// Python wrapper for `ensure_file_exists_or_download_http`.
///
/// Ensures that a file exists at the specified path by downloading it if necessary.
///
/// # Errors
///
/// Returns an error if:
/// - The HTTP request fails or returns a non-success status code: `PyErr`.
/// - Any I/O operation fails during file creation, reading, or writing: `PyErr`.
/// - Checksum verification or JSON parsing fails: `PyErr`.
#[pyfunction(name = "ensure_file_exists_or_download_http")]
#[pyo3(signature = (filepath, url, checksums=None, timeout_secs=30))]
pub fn py_ensure_file_exists_or_download_http(
    filepath: &str,
    url: &str,
    checksums: Option<&str>,
    timeout_secs: Option<u64>,
) -> PyResult<()> {
    let filepath = Path::new(filepath);
    let checksums = checksums.map(Path::new);
    ensure_file_exists_or_download_http(filepath, url, checksums, timeout_secs)
        .map_err(to_pyruntime_err)
}
```


---

## Overview

This file is located at `crates/testkit/src/python/files.rs` within the repository.

**Functions defined:** py_ensure_file_exists_or_download_http


---

## Detailed Analysis

### Functions

#### `py_ensure_file_exists_or_download_http(
    filepath: &str,
    url: &str,
    checksums: Option<&str>,
    timeout_secs: Option<u64>,
)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/testkit/src/python`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


