# Documentation: `crates/adapters/kraken/src/websocket/error.rs`
**Generated:** 2025-11-15T19:40:01.164099Z
**File Size:** 1682 bytes
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

- **Path:** `crates/adapters/kraken/src/websocket/error.rs`
- **Size:** 1,682 bytes
- **Lines:** 51
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
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

//! Error types for Kraken WebSocket client operations.

use thiserror::Error;

#[derive(Debug, Clone, Error)]
pub enum KrakenWsError {
    #[error("Connection error: {0}")]
    ConnectionError(String),

    #[error("Subscription error: {0}")]
    SubscriptionError(String),

    #[error("Authentication error: {0}")]
    AuthenticationError(String),

    #[error("Invalid message: {0}")]
    InvalidMessage(String),

    #[error("JSON error: {0}")]
    JsonError(String),

    #[error("Channel error: {0}")]
    ChannelError(String),

    #[error("Disconnected: {0}")]
    Disconnected(String),

    #[error("Timeout: {0}")]
    Timeout(String),
}

impl From<serde_json::Error> for KrakenWsError {
    fn from(error: serde_json::Error) -> Self {
        Self::JsonError(error.to_string())
    }
}
```


---

## Overview

This file is located at `crates/adapters/kraken/src/websocket/error.rs` within the repository.

**Classes defined:** From

**Functions defined:** from


---

## Detailed Analysis

### Classes

#### `From`

**Type:** impl


### Functions

#### `from(error: serde_json::Error)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


