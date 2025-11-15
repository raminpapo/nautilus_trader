# Documentation: `crates/core/src/python/parsing.rs`
**Generated:** 2025-11-15T19:40:01.929624Z
**File Size:** 5185 bytes
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

- **Path:** `crates/core/src/python/parsing.rs`
- **Size:** 5,185 bytes
- **Lines:** 153
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 6

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

//! JSON / string parsing helpers for Python inputs.

use pyo3::{
    exceptions::PyKeyError,
    prelude::*,
    types::{PyDict, PyList},
};

/// Helper function to get a required string value from a Python dictionary.
///
/// # Returns
///
/// Returns the extracted string value or a `PyErr` if the key is missing or extraction fails.
///
/// # Errors
///
/// Returns `PyErr` if the key is missing or value extraction fails.
pub fn get_required_string(dict: &Bound<'_, PyDict>, key: &str) -> PyResult<String> {
    dict.get_item(key)?
        .ok_or_else(|| PyKeyError::new_err(format!("Missing required key: {key}")))?
        .extract()
}

/// Helper function to get a required value from a Python dictionary and extract it.
///
/// # Returns
///
/// Returns the extracted value or a `PyErr` if the key is missing or extraction fails.
///
/// # Errors
///
/// Returns `PyErr` if the key is missing or value extraction fails.
pub fn get_required<T>(dict: &Bound<'_, PyDict>, key: &str) -> PyResult<T>
where
    T: for<'a, 'py> FromPyObject<'a, 'py>,
    for<'a, 'py> PyErr: From<<T as FromPyObject<'a, 'py>>::Error>,
{
    dict.get_item(key)?
        .ok_or_else(|| PyKeyError::new_err(format!("Missing required key: {key}")))?
        .extract()
        .map_err(PyErr::from)
}

/// Helper function to get an optional value from a Python dictionary.
///
/// # Returns
///
/// Returns Some(value) if the key exists and extraction succeeds, None if the key is missing
/// or if the value is Python None, or a `PyErr` if extraction fails.
///
/// # Errors
///
/// Returns `PyErr` if value extraction fails (but not if the key is missing or value is None).
pub fn get_optional<T>(dict: &Bound<'_, PyDict>, key: &str) -> PyResult<Option<T>>
where
    T: for<'a, 'py> FromPyObject<'a, 'py>,
    for<'a, 'py> PyErr: From<<T as FromPyObject<'a, 'py>>::Error>,
{
    match dict.get_item(key)? {
        Some(value) => {
            if value.is_none() {
                Ok(None)
            } else {
                value.extract().map(Some).map_err(PyErr::from)
            }
        }
        None => Ok(None),
    }
}

/// Helper function to get a required value, parse it with a closure, and handle parse errors.
///
/// # Returns
///
/// Returns the parsed value or a `PyErr` if the key is missing, extraction fails, or parsing fails.
///
/// # Errors
///
/// Returns `PyErr` if the key is missing, value extraction fails, or parsing fails.
pub fn get_required_parsed<T, F>(dict: &Bound<'_, PyDict>, key: &str, parser: F) -> PyResult<T>
where
    F: FnOnce(String) -> Result<T, String>,
{
    let value_str = get_required_string(dict, key)?;
    parser(value_str).map_err(|e| PyKeyError::new_err(format!("Failed to parse {key}: {e}")))
}

/// Helper function to get an optional value, parse it with a closure, and handle parse errors.
///
/// # Returns
///
/// Returns `Some(parsed_value)` if the key exists and parsing succeeds, None if the key is missing
/// or if the value is Python None, or a `PyErr` if extraction or parsing fails.
///
/// # Errors
///
/// Returns `PyErr` if value extraction or parsing fails (but not if the key is missing or value is None).
pub fn get_optional_parsed<T, F>(
    dict: &Bound<'_, PyDict>,
    key: &str,
    parser: F,
) -> PyResult<Option<T>>
where
    F: FnOnce(String) -> Result<T, String>,
{
    match dict.get_item(key)? {
        Some(value) => {
            if value.is_none() {
                Ok(None)
            } else {
                let value_str: String = value.extract()?;
                parser(value_str)
                    .map(Some)
                    .map_err(|e| PyKeyError::new_err(format!("Failed to parse {key}: {e}")))
            }
        }
        None => Ok(None),
    }
}

/// Helper function to get a required `PyList` from a Python dictionary.
///
/// # Returns
///
/// Returns the extracted `PyList` or a `PyErr` if the key is missing or extraction fails.
///
/// # Errors
///
/// Returns `PyErr` if the key is missing or value extraction fails.
pub fn get_required_list<'py>(
    dict: &Bound<'py, PyDict>,
    key: &str,
) -> PyResult<Bound<'py, PyList>> {
    dict.get_item(key)?
        .ok_or_else(|| PyKeyError::new_err(format!("Missing required key: {key}")))?
        .downcast_into()
        .map_err(Into::into)
}
```


---

## Overview

This file is located at `crates/core/src/python/parsing.rs` within the repository.

**Functions defined:** get_required_string, get_required, get_optional, get_required_parsed, get_optional_parsed, get_required_list


---

## Detailed Analysis

### Functions

#### `get_required_string(dict: &Bound<'_, PyDict>, key: &str)`


#### `get_required(dict: &Bound<'_, PyDict>, key: &str)`


#### `get_optional(dict: &Bound<'_, PyDict>, key: &str)`


#### `get_required_parsed(dict: &Bound<'_, PyDict>, key: &str, parser: F)`


#### `get_optional_parsed(
    dict: &Bound<'_, PyDict>,
    key: &str,
    parser: F,
)`


#### `get_required_list(
    dict: &Bound<'py, PyDict>,
    key: &str,
)`



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


