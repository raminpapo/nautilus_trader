# Documentation: `crates/adapters/tardis/src/tests/mod.rs`
**Generated:** 2025-11-15T19:40:01.512750Z
**File Size:** 1636 bytes
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

- **Path:** `crates/adapters/tardis/src/tests/mod.rs`
- **Size:** 1,636 bytes
- **Lines:** 46
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

#[cfg(test)]
/// Returns the path to the test data file.
///
/// # Panics
///
/// Panics if the file cannot be read.
#[must_use]
pub fn get_test_data_path(file_name: &str) -> std::path::PathBuf {
    use std::path::PathBuf;

    let path = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("src")
        .join("tests")
        .join("data")
        .join(file_name);

    assert!(path.exists(), "Test data file not found: {path:?}");
    path
}

#[cfg(test)]
/// Load the JSON data from `file_name`.
///
/// # Panics
///
/// Panics if the file cannot be read.
#[must_use]
pub fn load_test_json(file_name: &str) -> String {
    let path = get_test_data_path(file_name);
    std::fs::read_to_string(path).expect("Failed to read test JSON file")
}
```


---

## Overview

This file is located at `crates/adapters/tardis/src/tests/mod.rs` within the repository.

**Functions defined:** get_test_data_path, load_test_json


---

## Detailed Analysis

### Functions

#### `get_test_data_path(file_name: &str)`


#### `load_test_json(file_name: &str)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/src/tests`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


