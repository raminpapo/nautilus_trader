# Documentation: mod.rs

## File Metadata

- **Path**: `crates/model/src/events/mod.rs`
- **Size**: 1,832 bytes
- **Lines**: 39
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

//! Events for the trading domain model.

pub mod account;
pub mod order;
pub mod position;

// Re-exports
pub use crate::events::{
    account::state::AccountState,
    order::{
        OrderEvent, OrderEventType, accepted::OrderAccepted, any::OrderEventAny,
        cancel_rejected::OrderCancelRejected, canceled::OrderCanceled, denied::OrderDenied,
        emulated::OrderEmulated, expired::OrderExpired, filled::OrderFilled,
        initialized::OrderInitialized, modify_rejected::OrderModifyRejected,
        pending_cancel::OrderPendingCancel, pending_update::OrderPendingUpdate,
        rejected::OrderRejected, released::OrderReleased, snapshot::OrderSnapshot,
        submitted::OrderSubmitted, triggered::OrderTriggered, updated::OrderUpdated,
    },
    position::{
        PositionEvent, adjusted::PositionAdjusted, changed::PositionChanged,
        closed::PositionClosed, opened::PositionOpened, snapshot::PositionSnapshot,
    },
};

```

## High-Level Overview

This file is part of the NautilusTrader repository. This file contains code and configuration.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

## Related Files

This file is located in `crates/model/src/events/`. Related files may include:
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
*Generated on 2025-11-18T21:55:02.456429Z*
