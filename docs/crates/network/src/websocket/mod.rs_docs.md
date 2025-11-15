# Documentation: `crates/network/src/websocket/mod.rs`
**Generated:** 2025-11-15T19:40:03.279499Z
**File Size:** 1444 bytes
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

- **Path:** `crates/network/src/websocket/mod.rs`
- **Size:** 1,444 bytes
- **Lines:** 31
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

//! WebSocket client implementation with automatic reconnection and subscription tracking.

pub mod auth;
pub mod client;
pub mod config;
pub mod consts;
pub mod subscription;
pub mod types;

// Re-export main types for convenience
pub use auth::AuthTracker;
pub use client::{WebSocketClient, WebSocketClientInner};
pub use config::WebSocketConfig;
pub use consts::{AUTHENTICATION_TIMEOUT_SECS, TEXT_PING, TEXT_PONG};
pub use subscription::{SubscriptionState, split_topic};
pub use types::{MessageHandler, MessageReader, PingHandler, channel_message_handler};
```


---

## Overview

This file is located at `crates/network/src/websocket/mod.rs` within the repository.


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


