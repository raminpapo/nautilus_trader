# Documentation: `crates/adapters/bitmex/src/websocket/mod.rs`
**Generated:** 2025-11-15T19:40:00.390310Z
**File Size:** 1687 bytes
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

- **Path:** `crates/adapters/bitmex/src/websocket/mod.rs`
- **Size:** 1,687 bytes
- **Lines:** 36
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

//! WebSocket client implementation for BitMEX real-time data feeds.
//!
//! This module provides a WebSocket client for subscribing to BitMEX's real-time data streams.
//! It supports:
//! - Public market data subscriptions (trades, quotes, order book updates).
//! - Private account data subscriptions (orders, positions, executions).
//! - Authentication for private channels.
//! - Automatic reconnection and subscription management.
//! - Message parsing into Nautilus domain models.
//!
//! The WebSocket client maintains internal caches for order book reconstruction
//! and provides efficient parsing of BitMEX's table-based update format.

pub mod client;
pub mod enums;
pub mod error;
pub mod handler;
pub mod messages;
pub mod parse;

pub use crate::websocket::client::BitmexWebSocketClient;
```


---

## Overview

This file is located at `crates/adapters/bitmex/src/websocket/mod.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


