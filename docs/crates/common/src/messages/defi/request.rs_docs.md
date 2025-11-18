# Documentation: request.rs

## File Metadata

- **Path**: `crates/common/src/messages/defi/request.rs`
- **Size**: 1,781 bytes
- **Lines**: 49
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

use indexmap::IndexMap;
use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::identifiers::{ClientId, InstrumentId};

/// Represents a request for a pool snapshot from a specific AMM pool.
#[derive(Clone, Debug)]
pub struct RequestPoolSnapshot {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub request_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl RequestPoolSnapshot {
    /// Creates a new [`RequestPoolSnapshot`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        request_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            request_id,
            ts_init,
            params,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file

### Classes
- **`RequestPoolSnapshot`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `new`
**Impls**: `RequestPoolSnapshot`
**Structs**: `RequestPoolSnapshot`

## Related Files

This file is located in `crates/common/src/messages/defi/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.187140Z*
