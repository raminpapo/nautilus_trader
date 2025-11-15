# Documentation: `crates/indicators/src/testing.rs`
**Generated:** 2025-11-15T19:40:02.279804Z
**File Size:** 1563 bytes
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

- **Path:** `crates/indicators/src/testing.rs`
- **Size:** 1,563 bytes
- **Lines:** 41
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

//! Common test related helper functions.

/// Checks if two floating-point numbers are approximately equal within the
/// margin of floating-point precision.
///
/// - `a`: The first floating-point number.
/// - `b`: The second floating-point number.
///
/// # Returns
///
/// Returns `true` if the absolute difference between `a` and `b` is less than
/// `f64::EPSILON`, indicating that they are approximately equal.
///
/// # Example
///
/// ```
/// use nautilus_indicators::testing::approx_equal;
///
/// let a = 0.1 + 0.2;
/// let b = 0.3;
/// assert!(approx_equal(a, b));
/// ```
#[must_use]
pub fn approx_equal(a: f64, b: f64) -> bool {
    (a - b).abs() < f64::EPSILON
}
```


---

## Overview

This file is located at `crates/indicators/src/testing.rs` within the repository.

**Functions defined:** approx_equal


---

## Detailed Analysis

### Functions

#### `approx_equal(a: f64, b: f64)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/indicators/src`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


