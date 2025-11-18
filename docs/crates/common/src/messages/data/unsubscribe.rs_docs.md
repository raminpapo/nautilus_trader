# Documentation: unsubscribe.rs

## File Metadata

- **Path**: `crates/common/src/messages/data/unsubscribe.rs`
- **Size**: 12,835 bytes
- **Lines**: 479
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
    data::{BarType, DataType},
    identifiers::{ClientId, InstrumentId, Venue},
};

use super::check_client_id_or_venue;

#[derive(Clone, Debug)]
pub struct UnsubscribeCustomData {
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub data_type: DataType,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeCustomData {
    /// Creates a new [`UnsubscribeCustomData`] instance.
    pub fn new(
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        data_type: DataType,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            client_id,
            venue,
            data_type,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeInstrument {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeInstrument {
    /// Creates a new [`UnsubscribeInstrument`] instance.
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeInstruments {
    pub client_id: Option<ClientId>,
    pub venue: Venue,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeInstruments {
    /// Creates a new [`UnsubscribeInstruments`] instance.
    pub fn new(
        client_id: Option<ClientId>,
        venue: Venue,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        Self {
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeBookDeltas {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeBookDeltas {
    /// Creates a new [`UnsubscribeBookDeltas`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeBookDepth10 {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeBookDepth10 {
    /// Creates a new [`UnsubscribeBookDepth10`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeBookSnapshots {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeBookSnapshots {
    /// Creates a new [`UnsubscribeBookSnapshots`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeQuotes {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeQuotes {
    /// Creates a new [`UnsubscribeQuotes`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeTrades {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeTrades {
    /// Creates a new [`UnsubscribeTrades`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeBars {
    pub bar_type: BarType,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeBars {
    /// Creates a new [`UnsubscribeBars`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        bar_type: BarType,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            bar_type,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeMarkPrices {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeMarkPrices {
    /// Creates a new [`UnsubscribeMarkPrices`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeIndexPrices {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeIndexPrices {
    /// Creates a new [`UnsubscribeIndexPrices`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeFundingRates {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeFundingRates {
    /// Creates a new [`UnsubscribeFundingRates`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeInstrumentStatus {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeInstrumentStatus {
    /// Creates a new [`UnsubscribeInstrumentStatus`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

#[derive(Clone, Debug)]
pub struct UnsubscribeInstrumentClose {
    pub instrument_id: InstrumentId,
    pub client_id: Option<ClientId>,
    pub venue: Option<Venue>,
    pub command_id: UUID4,
    pub ts_init: UnixNanos,
    pub params: Option<IndexMap<String, String>>,
}

impl UnsubscribeInstrumentClose {
    /// Creates a new [`UnsubscribeInstrumentClose`] instance.
    #[allow(clippy::too_many_arguments)]
    pub fn new(
        instrument_id: InstrumentId,
        client_id: Option<ClientId>,
        venue: Option<Venue>,
        command_id: UUID4,
        ts_init: UnixNanos,
        params: Option<IndexMap<String, String>>,
    ) -> Self {
        check_client_id_or_venue(&client_id, &venue);
        Self {
            instrument_id,
            client_id,
            venue,
            command_id,
            ts_init,
            params,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 14 function(s) and 14 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file
- **`new()`**: Function defined in this file

### Classes
- **`UnsubscribeCustomData`**: Class defined in this file
- **`UnsubscribeInstrument`**: Class defined in this file
- **`UnsubscribeInstruments`**: Class defined in this file
- **`UnsubscribeBookDeltas`**: Class defined in this file
- **`UnsubscribeBookDepth10`**: Class defined in this file
- **`UnsubscribeBookSnapshots`**: Class defined in this file
- **`UnsubscribeQuotes`**: Class defined in this file
- **`UnsubscribeTrades`**: Class defined in this file
- **`UnsubscribeBars`**: Class defined in this file
- **`UnsubscribeMarkPrices`**: Class defined in this file
- **`UnsubscribeIndexPrices`**: Class defined in this file
- **`UnsubscribeFundingRates`**: Class defined in this file
- **`UnsubscribeInstrumentStatus`**: Class defined in this file
- **`UnsubscribeInstrumentClose`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 15


**Functions**: `new`
**Impls**: `UnsubscribeBars`, `UnsubscribeBookDeltas`, `UnsubscribeBookDepth10`, `UnsubscribeBookSnapshots`, `UnsubscribeCustomData`, `UnsubscribeFundingRates`, `UnsubscribeIndexPrices`, `UnsubscribeInstrument`, `UnsubscribeInstrumentClose`, `UnsubscribeInstrumentStatus`, `UnsubscribeInstruments`, `UnsubscribeMarkPrices`, `UnsubscribeQuotes`, `UnsubscribeTrades`
**Structs**: `UnsubscribeBars`, `UnsubscribeBookDeltas`, `UnsubscribeBookDepth10`, `UnsubscribeBookSnapshots`, `UnsubscribeCustomData`, `UnsubscribeFundingRates`, `UnsubscribeIndexPrices`, `UnsubscribeInstrument`, `UnsubscribeInstrumentClose`, `UnsubscribeInstrumentStatus`, `UnsubscribeInstruments`, `UnsubscribeMarkPrices`, `UnsubscribeQuotes`, `UnsubscribeTrades`

## Related Files

This file is located in `crates/common/src/messages/data/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.182011Z*
