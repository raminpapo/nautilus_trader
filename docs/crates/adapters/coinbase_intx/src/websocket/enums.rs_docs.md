# Documentation: `crates/adapters/coinbase_intx/src/websocket/enums.rs`
**Generated:** 2025-11-15T19:40:00.807139Z
**File Size:** 2738 bytes
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

- **Path:** `crates/adapters/coinbase_intx/src/websocket/enums.rs`
- **Size:** 2,738 bytes
- **Lines:** 120
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

use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display, EnumIter, EnumString};

/// Error types that can be returned by the WebSocket API.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "camelCase")]
pub enum WsErrorType {
    /// General error.
    Error,
    /// Error during subscription.
    SubscriptionError,
    /// Error during unsubscription.
    UnsubscriptionError,
    /// Authentication failure.
    AuthenticationError,
    /// Rate limit exceeded.
    RateLimit,
}

/// Operation type for WebSocket commands.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum WsOperation {
    /// Subscribe to one or more topics.
    Subscribe,
    /// Unsubscribe from one or more topics.
    Unsubscribe,
}

/// Operation type for WebSocket commands.
#[derive(
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "UPPERCASE")]
pub enum WsMessageType {
    /// Snapshot message type.
    Snapshot,
    /// Update message type.
    Update,
}

/// Coinbase International WebSocket feed channel.
#[derive(
    Copy,
    Clone,
    Debug,
    Display,
    PartialEq,
    Eq,
    Hash,
    AsRefStr,
    EnumIter,
    EnumString,
    Serialize,
    Deserialize,
)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum CoinbaseIntxWsChannel {
    Subscriptions,
    Instruments,
    Match,
    Funding,
    Risk,
    Level1,
    Level2,
    CandlesOneMinute,
    CandlesFiveMinute,
    CandlesThirtyMinute,
    CandlesTwoHour,
    CandlesOneDay,
}
```


---

## Overview

This file is located at `crates/adapters/coinbase_intx/src/websocket/enums.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/coinbase_intx/src/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Security:** This file may contain sensitive patterns: auth. Ensure proper handling of secrets.


