# Documentation: paths.rs

## File Metadata

- **Path**: `crates/core/src/paths.rs`
- **Size**: 2,203 bytes
- **Lines**: 63
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

//! Utility functions for resolving project and workspace directory paths.

use std::path::PathBuf;

/// Returns the workspace root directory path.
///
/// # Panics
///
/// Panics if the `CARGO_MANIFEST_DIR` environment variable is not set or its parent directory cannot be determined.
#[must_use]
pub fn get_workspace_root_path() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("Failed to get project root")
        .to_path_buf()
}

/// Returns the project root directory path.
///
/// # Panics
///
/// Panics if the workspace root path cannot be determined or its parent directory is missing.
#[must_use]
pub fn get_project_root_path() -> PathBuf {
    get_workspace_root_path()
        .parent()
        .expect("Failed to get workspace root")
        .to_path_buf()
}

/// Returns the tests root directory path.
#[must_use]
pub fn get_tests_root_path() -> PathBuf {
    get_project_root_path().join("tests")
}

/// Returns the test data directory path.
#[must_use]
pub fn get_test_data_path() -> PathBuf {
    if let Ok(test_data_root_path) = std::env::var("TEST_DATA_ROOT_PATH") {
        get_project_root_path()
            .join(test_data_root_path)
            .join("test_data")
    } else {
        get_project_root_path().join("tests").join("test_data")
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s).

## Detailed Walkthrough

### Functions
- **`get_workspace_root_path()`**: Function defined in this file
- **`get_project_root_path()`**: Function defined in this file
- **`get_tests_root_path()`**: Function defined in this file
- **`get_test_data_path()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `get_project_root_path`, `get_test_data_path`, `get_tests_root_path`, `get_workspace_root_path`

## Related Files

This file is located in `crates/core/src/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

Tests for this file may be located in:
- `tests/` directory in the same folder
- Corresponding test module in the project

Run the full test suite to verify functionality.

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:01.415197Z*
