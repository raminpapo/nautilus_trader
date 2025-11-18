# Documentation: unsubscribe.rs

## File Metadata

- **Path**: `crates/common/src/messages/defi/unsubscribe.rs`
- **Size**: 5,657 bytes
- **Lines**: 200
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
use nautilus_model::{
    defi::chain::Blockchain,
    identifiers::{ClientId, InstrumentId},
};

#[derive(Debug, Clone)]
pub struct UnsubscribeBlocks {
    pub chain: Blockchain,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeBlocks {
    /// Creates a new [`UnsubscribeBlocks`] instance.
    #[must_use]
    pub const fn new(
        chain: Blockchain,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            chain,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from definition updates for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePool {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePool {
    /// Creates a new [`UnsubscribePool`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Debug, Clone)]
pub struct UnsubscribePoolSwaps {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolSwaps {
    /// Creates a new [`UnsubscribePoolSwaps`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from liquidity updates for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePoolLiquidityUpdates {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolLiquidityUpdates {
    /// Creates a new [`UnsubscribePoolLiquidityUpdates`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from fee-collect events for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePoolFeeCollects {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolFeeCollects {
    /// Creates a new [`UnsubscribePoolFeeCollects`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

/// Represents a command to unsubscribe from flash-loan events for a specific AMM pool.
#[derive(Debug, Clone)]
pub struct UnsubscribePoolFlashEvents {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribePoolFlashEvents {
    /// Creates a new [`UnsubscribePoolFlashEvents`] instance.
    #[must_use]
    pub const fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            instrument_id,
            client_id,
            command_id,
            ts_init,
            params,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 6 function(s) and 6 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file

### Classes
- **`UnsubscribeBlocks`**: Class defined in this file
- **`UnsubscribePool`**: Class defined in this file
- **`UnsubscribePoolSwaps`**: Class defined in this file
- **`UnsubscribePoolLiquidityUpdates`**: Class defined in this file
- **`UnsubscribePoolFeeCollects`**: Class defined in this file
- **`UnsubscribePoolFlashEvents`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 7


**Functions**: `new`
**Impls**: `UnsubscribeBlocks`, `UnsubscribePool`, `UnsubscribePoolFeeCollects`, `UnsubscribePoolFlashEvents`, `UnsubscribePoolLiquidityUpdates`, `UnsubscribePoolSwaps`
**Structs**: `UnsubscribeBlocks`, `UnsubscribePool`, `UnsubscribePoolFeeCollects`, `UnsubscribePoolFlashEvents`, `UnsubscribePoolLiquidityUpdates`, `UnsubscribePoolSwaps`

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
*Generated on 2025-11-18T21:55:01.192448Z*
