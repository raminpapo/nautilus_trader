# Documentation: `crates/adapters/bitmex/src/http/mod.rs`
**Generated:** 2025-11-15T19:40:00.340281Z
**File Size:** 1535 bytes
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

- **Path:** `crates/adapters/bitmex/src/http/mod.rs`
- **Size:** 1,535 bytes
- **Lines:** 35
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

//! HTTP REST API client implementation for BitMEX.
//!
//! This module provides an HTTP client for interacting with the BitMEX REST API.
//! It handles:
//! - Request signing and authentication.
//! - Rate limiting and retry logic.
//! - Request/response models.
//! - Parsing BitMEX data into Nautilus domain models.
//!
//! The client supports all major BitMEX REST endpoints including:
//! - Market data (instruments, trades, order books).
//! - Account data (wallet, positions, margins).
//! - Order management (place, modify, cancel orders).
//! - Execution history.

pub mod client;
pub mod error;
pub mod models;
pub mod parse;
pub mod query;
```


---

## Overview

This file is located at `crates/adapters/bitmex/src/http/mod.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/src/http`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


