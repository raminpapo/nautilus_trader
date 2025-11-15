# Documentation: `crates/network/src/websocket/consts.rs`
**Generated:** 2025-11-15T19:40:03.278340Z
**File Size:** 1598 bytes
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

- **Path:** `crates/network/src/websocket/consts.rs`
- **Size:** 1,598 bytes
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

//! Constants for WebSocket protocol handling.

/// Standard text ping message.
pub const TEXT_PING: &str = "ping";

/// Standard text pong message.
pub const TEXT_PONG: &str = "pong";

/// Default authentication timeout in seconds.
pub const AUTHENTICATION_TIMEOUT_SECS: u64 = 10;

/// Connection state check interval in milliseconds.
pub(crate) const CONNECTION_STATE_CHECK_INTERVAL_MS: u64 = 10;

/// Send operation check interval in milliseconds.
pub(crate) const SEND_OPERATION_CHECK_INTERVAL_MS: u64 = 1;

/// Graceful shutdown delay in milliseconds.
pub(crate) const GRACEFUL_SHUTDOWN_DELAY_MS: u64 = 100;

/// Graceful shutdown timeout in seconds.
pub(crate) const GRACEFUL_SHUTDOWN_TIMEOUT_SECS: u64 = 5;
```


---

## Overview

This file is located at `crates/network/src/websocket/consts.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/network/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


