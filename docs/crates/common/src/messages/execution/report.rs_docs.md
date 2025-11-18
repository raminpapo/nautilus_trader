# Documentation: report.rs

## File Metadata

- **Path**: `crates/common/src/messages/execution/report.rs`
- **Size**: 3,798 bytes
- **Lines**: 140
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

// Under development
#![allow(dead_code)]
#![allow(unused_variables)]

use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::identifiers::{ClientOrderId, InstrumentId};

#[derive(Debug)]
pub struct GenerateOrderStatusReport {
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub instrument_id: Option<InstrumentId>,
    pub client_order_id: Option<ClientOrderId>,
    pub venue_order_id: Option<ClientOrderId>,
}

impl GenerateOrderStatusReport {
    #[must_use]
    pub const fn new(
        command_id: UUID4,
        ts_init: UnixNanos,
        instrument_id: Option<InstrumentId>,
        client_order_id: Option<ClientOrderId>,
        venue_order_id: Option<ClientOrderId>,
    ) -> Self {
        Self {
            command_id,
            ts_init,
            instrument_id,
            client_order_id,
            venue_order_id,
        }
    }
}

#[derive(Debug)]
pub struct GenerateOrderStatusReports {
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub open_only: bool,
    pub instrument_id: Option<InstrumentId>,
    pub start: Option<UnixNanos>,
    pub end: Option<UnixNanos>,
}

impl GenerateOrderStatusReports {
    #[must_use]
    pub const fn new(
        command_id: UUID4,
        ts_init: UnixNanos,
        open_only: bool,
        instrument_id: Option<InstrumentId>,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) -> Self {
        Self {
            command_id,
            ts_init,
            open_only,
            instrument_id,
            start,
            end,
        }
    }
}

#[derive(Debug)]
pub struct GenerateFillReports {
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub instrument_id: Option<InstrumentId>,
    pub venue_order_id: Option<ClientOrderId>,
    pub start: Option<UnixNanos>,
    pub end: Option<UnixNanos>,
}

impl GenerateFillReports {
    #[must_use]
    pub const fn new(
        command_id: UUID4,
        ts_init: UnixNanos,
        instrument_id: Option<InstrumentId>,
        venue_order_id: Option<ClientOrderId>,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) -> Self {
        Self {
            command_id,
            ts_init,
            instrument_id,
            venue_order_id,
            start,
            end,
        }
    }
}

#[derive(Debug)]
pub struct GeneratePositionReports {
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub instrument_id: Option<InstrumentId>,
    pub start: Option<UnixNanos>,
    pub end: Option<UnixNanos>,
}

impl GeneratePositionReports {
    #[must_use]
    pub const fn new(
        command_id: UUID4,
        ts_init: UnixNanos,
        instrument_id: Option<InstrumentId>,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    ) -> Self {
        Self {
            command_id,
            ts_init,
            instrument_id,
            start,
            end,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 4 function(s) and 4 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file

### Classes
- **`GenerateOrderStatusReport`**: Class defined in this file
- **`GenerateOrderStatusReports`**: Class defined in this file
- **`GenerateFillReports`**: Class defined in this file
- **`GeneratePositionReports`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `new`
**Impls**: `GenerateFillReports`, `GenerateOrderStatusReport`, `GenerateOrderStatusReports`, `GeneratePositionReports`
**Structs**: `GenerateFillReports`, `GenerateOrderStatusReport`, `GenerateOrderStatusReports`, `GeneratePositionReports`

## Related Files

This file is located in `crates/common/src/messages/execution/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.203221Z*
