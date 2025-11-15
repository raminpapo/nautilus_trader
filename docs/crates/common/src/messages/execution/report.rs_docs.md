# Documentation: `crates/common/src/messages/execution/report.rs`
**Generated:** 2025-11-15T19:40:01.776016Z
**File Size:** 3798 bytes
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

- **Path:** `crates/common/src/messages/execution/report.rs`
- **Size:** 3,798 bytes
- **Lines:** 139
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 8
- **Functions:** 4

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


---

## Overview

This file is located at `crates/common/src/messages/execution/report.rs` within the repository.

**Classes defined:** GenerateOrderStatusReport, GenerateOrderStatusReports, GenerateFillReports, GeneratePositionReports, GenerateOrderStatusReport, GenerateOrderStatusReports, GenerateFillReports, GeneratePositionReports

**Functions defined:** new, new, new, new


---

## Detailed Analysis

### Classes

#### `GenerateOrderStatusReport`

**Type:** struct


#### `GenerateOrderStatusReports`

**Type:** struct


#### `GenerateFillReports`

**Type:** struct


#### `GeneratePositionReports`

**Type:** struct


#### `GenerateOrderStatusReport`

**Type:** impl


#### `GenerateOrderStatusReports`

**Type:** impl


#### `GenerateFillReports`

**Type:** impl


#### `GeneratePositionReports`

**Type:** impl


### Functions

#### `new(
        command_id: UUID4,
        ts_init: UnixNanos,
        instrument_id: Option<InstrumentId>,
        client_order_id: Option<ClientOrderId>,
        venue_order_id: Option<ClientOrderId>,
    )`


#### `new(
        command_id: UUID4,
        ts_init: UnixNanos,
        open_only: bool,
        instrument_id: Option<InstrumentId>,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `new(
        command_id: UUID4,
        ts_init: UnixNanos,
        instrument_id: Option<InstrumentId>,
        venue_order_id: Option<ClientOrderId>,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`


#### `new(
        command_id: UUID4,
        ts_init: UnixNanos,
        instrument_id: Option<InstrumentId>,
        start: Option<UnixNanos>,
        end: Option<UnixNanos>,
    )`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/common/src/messages/execution`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


