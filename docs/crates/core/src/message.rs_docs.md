# Documentation: message.rs

## File Metadata

- **Path**: `crates/core/src/message.rs`
- **Size**: 2,382 bytes
- **Lines**: 63
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

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Enums**: `Message`

## Related Files

This file is located in `crates/core/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.396463Z*
