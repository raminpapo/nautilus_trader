# Documentation: `crates/common/src/ffi/enums.rs`
**Generated:** 2025-11-15T19:40:01.721734Z
**File Size:** 3550 bytes
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

- **Path:** `crates/common/src/ffi/enums.rs`
- **Size:** 3,550 bytes
- **Lines:** 104
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 8

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

use std::{ffi::c_char, str::FromStr};

use nautilus_core::ffi::string::{cstr_as_str, str_to_cstr};

use crate::enums::{ComponentState, ComponentTrigger, LogColor, LogLevel};

#[unsafe(no_mangle)]
pub extern "C" fn component_state_to_cstr(value: ComponentState) -> *const c_char {
    str_to_cstr(&value.to_string())
}

/// Returns an enum from a Python string.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
///
/// # Panics
///
/// Panics if the input C string does not match a valid enum variant.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn component_state_from_cstr(ptr: *const c_char) -> ComponentState {
    let value = unsafe { cstr_as_str(ptr) };
    ComponentState::from_str(value)
        .unwrap_or_else(|_| panic!("invalid `ComponentState` enum string value, was '{value}'"))
}

#[unsafe(no_mangle)]
pub extern "C" fn component_trigger_to_cstr(value: ComponentTrigger) -> *const c_char {
    str_to_cstr(&value.to_string())
}

/// Returns an enum from a Python string.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
///
/// # Panics
///
/// Panics if the input C string does not match a valid enum variant.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn component_trigger_from_cstr(ptr: *const c_char) -> ComponentTrigger {
    let value = unsafe { cstr_as_str(ptr) };
    ComponentTrigger::from_str(value)
        .unwrap_or_else(|_| panic!("invalid `ComponentTrigger` enum string value, was '{value}'"))
}

#[unsafe(no_mangle)]
pub extern "C" fn log_level_to_cstr(value: LogLevel) -> *const c_char {
    str_to_cstr(&value.to_string())
}

/// Returns an enum from a Python string.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
///
/// # Panics
///
/// Panics if the input C string does not match a valid enum variant.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn log_level_from_cstr(ptr: *const c_char) -> LogLevel {
    let value = unsafe { cstr_as_str(ptr) };
    LogLevel::from_str(value)
        .unwrap_or_else(|_| panic!("invalid `LogLevel` enum string value, was '{value}'"))
}

#[unsafe(no_mangle)]
pub extern "C" fn log_color_to_cstr(value: LogColor) -> *const c_char {
    str_to_cstr(&value.to_string())
}

/// Returns an enum from a Python string.
///
/// # Safety
///
/// Assumes `ptr` is a valid C string pointer.
///
/// # Panics
///
/// Panics if the input C string does not match a valid enum variant.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn log_color_from_cstr(ptr: *const c_char) -> LogColor {
    let value = unsafe { cstr_as_str(ptr) };
    LogColor::from_str(value)
        .unwrap_or_else(|_| panic!("invalid `LogColor` enum string value, was '{value}'"))
}
```


---

## Overview

This file is located at `crates/common/src/ffi/enums.rs` within the repository.

**Functions defined:** component_state_to_cstr, component_state_from_cstr, component_trigger_to_cstr, component_trigger_from_cstr, log_level_to_cstr, log_level_from_cstr, log_color_to_cstr, log_color_from_cstr


---

## Detailed Analysis

### Functions

#### `component_state_to_cstr(value: ComponentState)`


#### `component_state_from_cstr(ptr: *const c_char)`


#### `component_trigger_to_cstr(value: ComponentTrigger)`


#### `component_trigger_from_cstr(ptr: *const c_char)`


#### `log_level_to_cstr(value: LogLevel)`


#### `log_level_from_cstr(ptr: *const c_char)`


#### `log_color_to_cstr(value: LogColor)`


#### `log_color_from_cstr(ptr: *const c_char)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/ffi`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


