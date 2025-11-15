# Documentation: `crates/adapters/kraken/src/lib.rs`
**Generated:** 2025-11-15T19:40:01.147549Z
**File Size:** 2045 bytes
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

- **Path:** `crates/adapters/kraken/src/lib.rs`
- **Size:** 2,045 bytes
- **Lines:** 54
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

//! Kraken exchange adapter for NautilusTrader.
//!
//! This adapter provides integration with the Kraken cryptocurrency exchange,
//! supporting both Spot and Futures markets.
//!
//! # Features
//!
//! - REST API v2 client for market data and account operations
//! - WebSocket v2 client for real-time data feeds
//! - Support for Spot and Futures markets
//! - Comprehensive instrument, ticker, trade, orderbook, and OHLC data
//! - Prepared for execution support (orders, positions, balances)
//!
//! # API Documentation
//!
//! - [Kraken REST API](https://docs.kraken.com/api/)
//! - [Kraken WebSocket v2](https://docs.kraken.com/websockets-v2/)
//!
//! # Python Bindings
//!
//! Enable the `python` feature to use this adapter from Python:
//!
//! ```toml
//! nautilus-kraken = { version = "0.52.0", features = ["python"] }
//! ```

pub mod common;
pub mod config;
pub mod data;
pub mod execution;
pub mod http;
pub mod websocket;

#[cfg(feature = "python")]
pub mod python;

pub use config::{KrakenDataClientConfig, KrakenExecClientConfig};
pub use http::client::{KrakenHttpClient, KrakenRawHttpClient};
pub use websocket::client::KrakenWebSocketClient;
```


---

## Overview

This file is located at `crates/adapters/kraken/src/lib.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/kraken/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


