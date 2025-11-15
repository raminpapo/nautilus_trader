# Documentation: `crates/core/src/consts.rs`
**Generated:** 2025-11-15T19:40:01.869415Z
**File Size:** 1336 bytes
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

- **Path:** `crates/core/src/consts.rs`
- **Size:** 1,336 bytes
- **Lines:** 27
- **Extension:** `.rs`
- **Type:** text

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

//! Core constants.

use std::env;

/// The NautilusTrader string constant.
pub static NAUTILUS_TRADER: &str = "NautilusTrader";

/// The NautilusTrader version string read from the top-level `pyproject.toml` at compile time.
pub static NAUTILUS_VERSION: &str = env!("NAUTILUS_VERSION");

/// The NautilusTrader common User-Agent string including the current version at compile time.
pub static NAUTILUS_USER_AGENT: &str = env!("NAUTILUS_USER_AGENT");
```


---

## Overview

This file is located at `crates/core/src/consts.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


