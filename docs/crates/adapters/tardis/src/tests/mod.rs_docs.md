# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/mod.rs`
- **Size**: 1,636 bytes
- **Lines**: 47
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

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`get_test_data_path()`**: Function defined in this file
- **`load_test_json()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `get_test_data_path`, `load_test_json`

## Related Files

This file is located in `crates/adapters/tardis/src/tests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/tardis/src/tests/mod.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.771505Z*
