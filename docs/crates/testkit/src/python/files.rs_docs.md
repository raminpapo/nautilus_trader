# Documentation: files.rs

## File Metadata

- **Path**: `crates/testkit/src/python/files.rs`
- **Size**: 1,940 bytes
- **Lines**: 46
- **Language**: Rust

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`py_ensure_file_exists_or_download_http()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `py_ensure_file_exists_or_download_http`

## Related Files

This file is located in `crates/testkit/src/python/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/testkit/src/python/files.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.187058Z*
