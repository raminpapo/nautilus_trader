# Documentation: `crates/adapters/dydx/src/websocket/mod.rs`
**Generated:** 2025-11-15T19:40:00.971668Z
**File Size:** 2611 bytes
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

- **Path:** `crates/adapters/dydx/src/websocket/mod.rs`
- **Size:** 2,611 bytes
- **Lines:** 55
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

//! WebSocket client implementation for the dYdX v4 API.
//!
//! This module provides real-time streaming connectivity to dYdX WebSocket endpoints,
//! supporting:
//!
//! - **Market data streaming**: Trades, order books, candles (bars), and market updates (oracle prices).
//! - **Private data streaming**: Subaccount updates, orders, fills, and positions.
//! - **Channel subscription management**: Subscribe and unsubscribe to public and private channels.
//! - **Automatic reconnection**: Reconnection with state restoration and resubscription.
//! - **Message parsing**: Fast conversion of WebSocket messages to Nautilus domain objects.
//!
//! # Architecture
//!
//! The WebSocket client follows a two-layer architecture:
//!
//! - **Outer client** ([`client::DydxWebSocketClient`]): Orchestrates connection lifecycle, manages
//!   subscriptions, and maintains state accessible to Python via `Arc<DashMap>`.
//! - **Inner handler** ([`handler::FeedHandler`]): Runs in a dedicated Tokio task as the I/O boundary,
//!   processing commands and parsing raw WebSocket messages into Nautilus types.
//!
//! Communication between layers uses lock-free channels:
//! - Commands flow from client to handler via `mpsc` channel.
//! - Parsed domain events flow from handler to client via `mpsc` channel.
//!
//! # References
//!
//! - dYdX v4 WebSocket API: <https://docs.dydx.trade/developers/indexer/websockets>

pub mod client;
pub mod enums;
pub mod error;
pub mod handler;
pub mod messages;
pub mod types;

// Re-exports
pub use client::DydxWebSocketClient;
pub use enums::{DydxWsChannel, DydxWsOperation};
pub use error::{DydxWebSocketError, DydxWsError, DydxWsResult};
pub use messages::{DydxWsMessage, NautilusWsMessage};
```


---

## Overview

This file is located at `crates/adapters/dydx/src/websocket/mod.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/dydx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


