# Documentation: mod.rs

## File Metadata

- **Path**: `crates/adapters/bitmex/src/common/mod.rs`
- **Size**: 1,424 bytes
- **Lines**: 33
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

//! Common types and utilities shared across the BitMEX adapter.
//!
//! This module provides reusable components that are used by both the HTTP and WebSocket
//! clients, including:
//! - Constants for BitMEX URLs and venue identifier.
//! - Credential management for API authentication.
//! - Enumerations for order types, sides, and statuses.
//! - Parsing utilities for currency codes and other data transformations.

pub mod consts;
pub mod credential;
pub mod enums;
pub mod parse;
pub mod urls;

#[cfg(test)]
pub(crate) mod testing;

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/adapters/bitmex/src/common/`. Related files may include:
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

⚠️ **Security**: This file may handle sensitive data. Ensure proper encryption and access controls.

---
*Generated on 2025-11-18T21:54:58.946110Z*
