# Documentation: error.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/http/error.rs`
- **Size**: 1,861 bytes
- **Lines**: 48
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

//! Error types for Kraken HTTP client operations.

use std::fmt;

#[derive(Debug, Clone)]
pub enum KrakenHttpError {
    NetworkError(String),
    ApiError(Vec<String>),
    ParseError(String),
    AuthenticationError(String),
    MissingCredentials,
}

impl fmt::Display for KrakenHttpError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::NetworkError(msg) => write!(f, "Network error: {msg}"),
            Self::ApiError(errors) => write!(f, "API error: {}", errors.join(", ")),
            Self::ParseError(msg) => write!(f, "Parse error: {msg}"),
            Self::AuthenticationError(msg) => write!(f, "Authentication error: {msg}"),
            Self::MissingCredentials => write!(f, "Missing credentials"),
        }
    }
}

impl std::error::Error for KrakenHttpError {}

impl From<anyhow::Error> for KrakenHttpError {
    fn from(err: anyhow::Error) -> Self {
        Self::NetworkError(err.to_string())
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s).

## Detailed Walkthrough

### Functions
- **`fmt()`**: Function defined in this file
- **`from()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Enums**: `KrakenHttpError`
**Functions**: `fmt`, `from`
**Impls**: `From`, `fmt`, `std`

## Related Files

This file is located in `crates/adapters/kraken/src/http/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.182025Z*
