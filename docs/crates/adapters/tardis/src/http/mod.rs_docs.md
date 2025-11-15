# Documentation: `crates/adapters/tardis/src/http/mod.rs`
**Generated:** 2025-11-15T19:40:01.459699Z
**File Size:** 1094 bytes
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

- **Path:** `crates/adapters/tardis/src/http/mod.rs`
- **Size:** 1,094 bytes
- **Lines:** 25
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

pub mod client;
pub mod error;
pub mod instruments;
pub mod models;
pub mod parse;
pub mod query;

pub use crate::http::client::TardisHttpClient;

pub const TARDIS_BASE_URL: &str = "https://api.tardis.dev/v1";
```


---

## Overview

This file is located at `crates/adapters/tardis/src/http/mod.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/src/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


