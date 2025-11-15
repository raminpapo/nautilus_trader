# Documentation: `crates/core/src/message.rs`
**Generated:** 2025-11-15T19:40:01.905997Z
**File Size:** 2382 bytes
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

- **Path:** `crates/core/src/message.rs`
- **Size:** 2,382 bytes
- **Lines:** 62
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

//! Common message types.

use crate::{UUID4, UnixNanos};

/// Represents different types of messages in the system.
#[derive(Debug, Clone)]
pub enum Message {
    /// A command message with an identifier and initialization timestamp.
    Command {
        /// The unique identifier for this command.
        id: UUID4,
        /// The initialization timestamp.
        ts_init: UnixNanos,
    },
    /// A document message with an identifier and initialization timestamp.
    Document {
        /// The unique identifier for this document.
        id: UUID4,
        /// The initialization timestamp.
        ts_init: UnixNanos,
    },
    /// An event message with identifiers and timestamps.
    Event {
        /// The unique identifier for this event.
        id: UUID4,
        /// The initialization timestamp.
        ts_init: UnixNanos,
        /// The event timestamp.
        ts_event: UnixNanos,
    },
    /// A request message with an identifier and initialization timestamp.
    Request {
        /// The unique identifier for this request.
        id: UUID4,
        /// The initialization timestamp.
        ts_init: UnixNanos,
    },
    /// A response message with identifiers, timestamps, and correlation.
    Response {
        /// The unique identifier for this response.
        id: UUID4,
        /// The initialization timestamp.
        ts_init: UnixNanos,
        /// The correlation identifier linking this response to a request.
        correlation_id: UUID4,
    },
}
```


---

## Overview

This file is located at `crates/core/src/message.rs` within the repository.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/core/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


