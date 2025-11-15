# Documentation: `crates/adapters/dydx/src/common/mod.rs`
**Generated:** 2025-11-15T19:40:00.902146Z
**File Size:** 1779 bytes
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

- **Path:** `crates/adapters/dydx/src/common/mod.rs`
- **Size:** 1,779 bytes
- **Lines:** 37
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

//! Common functionality shared across the dYdX adapter.
//!
//! This module provides core utilities, constants, and data structures used throughout
//! the dYdX integration, including:
//!
//! - **Authentication**: Wallet credential storage and message signing for dYdX v4.
//! - **Common enumerations**: dYdX-specific enums mirrored from REST/WebSocket payloads.
//! - **Constants**: Venue identifiers, broker IDs, and scaling factors.
//! - **Parsing utilities**: Helpers for converting dYdX data to Nautilus types.
//! - **URL management**: Environment-aware base URL resolvers for testnet and mainnet.
//! - **Common models**: Shared data structures used across HTTP and WebSocket layers.
//! - **Testing helpers**: Fixtures and utilities for unit tests.

pub mod consts;
pub mod credential;
pub mod enums;
pub mod models;
pub mod parse;
pub mod urls;

#[cfg(test)]
pub(crate) mod testing;
```


---

## Overview

This file is located at `crates/adapters/dydx/src/common/mod.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src/common`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: credential, auth. Ensure proper handling of secrets.


