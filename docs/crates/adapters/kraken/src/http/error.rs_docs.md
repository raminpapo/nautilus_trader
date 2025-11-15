# Documentation: `crates/adapters/kraken/src/http/error.rs`
**Generated:** 2025-11-15T19:40:01.141472Z
**File Size:** 1861 bytes
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

- **Path:** `crates/adapters/kraken/src/http/error.rs`
- **Size:** 1,861 bytes
- **Lines:** 47
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 2

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


---

## Overview

This file is located at `crates/adapters/kraken/src/http/error.rs` within the repository.

**Classes defined:** fmt, std, From

**Functions defined:** fmt, from


---

## Detailed Analysis

### Classes

#### `fmt`

**Type:** impl


#### `std`

**Type:** impl


#### `From`

**Type:** impl


### Functions

#### `fmt(&self, f: &mut fmt::Formatter<'_>)`


#### `from(err: anyhow::Error)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/http`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: credential, auth. Ensure proper handling of secrets.


