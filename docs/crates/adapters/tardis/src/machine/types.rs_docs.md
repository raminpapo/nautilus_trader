# Documentation: types.rs

## File Metadata

- **Path**: `crates/adapters/tardis/src/machine/types.rs`
- **Size**: 6,023 bytes
- **Lines**: 154
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

use chrono::NaiveDate;
use nautilus_model::identifiers::InstrumentId;
use serde::{Deserialize, Serialize};
use ustr::Ustr;

use crate::enums::TardisExchange;
pub use crate::machine::client::TardisMachineClient;

/// Instrument definition information necessary for stream parsing.
#[derive(Clone, Debug, Serialize, Deserialize)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.adapters")
)]
pub struct TardisInstrumentMiniInfo {
    /// The instrument ID with optionally Nautilus normalized symbol.
    pub instrument_id: InstrumentId,
    /// The Tardis symbol.
    pub raw_symbol: Ustr,
    /// The Tardis exchange.
    pub exchange: TardisExchange,
    /// The price precision for the instrument.
    pub price_precision: u8,
    /// The size precision for the instrument.
    pub size_precision: u8,
}

impl TardisInstrumentMiniInfo {
    /// Creates a new [`TardisInstrumentMiniInfo`] instance.
    ///
    /// If `raw_instrument_id` is `None` then the `instrument_id` value will be assigned.
    #[must_use]
    pub fn new(
        instrument_id: InstrumentId,
        raw_symbol: Option<Ustr>,
        exchange: TardisExchange,
        price_precision: u8,
        size_precision: u8,
    ) -> Self {
        Self {
            instrument_id,
            raw_symbol: raw_symbol.unwrap_or(Ustr::from(instrument_id.symbol.as_str())),
            exchange,
            price_precision,
            size_precision,
        }
    }

    #[must_use]
    pub const fn as_tardis_instrument_key(&self) -> TardisInstrumentKey {
        TardisInstrumentKey::new(self.raw_symbol, self.exchange)
    }
}

/// Instrument definition information necessary for stream parsing.
#[derive(Clone, Debug, PartialEq, Eq, Hash, Serialize, Deserialize)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.adapters")
)]
pub struct TardisInstrumentKey {
    /// The Tardis raw symbol.
    pub raw_symbol: Ustr,
    /// The Tardis exchange.
    pub exchange: TardisExchange,
}

impl TardisInstrumentKey {
    /// Creates a new [`TardisInstrumentKey`] instance.
    #[must_use]
    pub const fn new(raw_symbol: Ustr, exchange: TardisExchange) -> Self {
        Self {
            raw_symbol,
            exchange,
        }
    }
}

/// The options that can be specified for calling Tardis Machine Server's replay-normalized.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.adapters")
)]
pub struct ReplayNormalizedRequestOptions {
    /// Requested [`TardisExchange`].
    pub exchange: TardisExchange,
    /// Optional symbols of requested historical data feed.
    /// Use /exchanges/:exchange HTTP API to get allowed symbols for requested exchange.
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(default)]
    pub symbols: Option<Vec<String>>,
    /// Replay period start date (UTC) in a ISO 8601 format, e.g., 2019-10-01.
    pub from: NaiveDate,
    /// Replay period start date (UTC) in a ISO 8601 format, e.g., 2019-10-02.
    pub to: NaiveDate,
    /// Array of normalized [data types](https://docs.tardis.dev/api/tardis-machine#normalized-data-types)
    /// for which real-time data will be provided.
    #[serde(alias = "data_types")]
    pub data_types: Vec<String>,
    /// When set to true, sends also disconnect messages that mark events when real-time WebSocket
    /// connection that was used to collect the historical data got disconnected.
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(default)]
    #[serde(alias = "with_disconnect_messages")]
    pub with_disconnect_messages: Option<bool>,
}

/// The options that can be specified for calling Tardis Machine Server's stream-normalized.
#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(rename_all = "camelCase")]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.adapters")
)]
pub struct StreamNormalizedRequestOptions {
    /// Requested [`TardisExchange`].
    pub exchange: TardisExchange,
    /// Optional symbols of requested real-time data feed.
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(default)]
    pub symbols: Option<Vec<String>>,
    /// Array of normalized [data types](https://docs.tardis.dev/api/tardis-machine#normalized-data-types)
    /// for which real-time data will be provided.
    #[serde(alias = "data_types")]
    pub data_types: Vec<String>,
    /// When set to true, sends disconnect messages anytime underlying exchange real-time WebSocket
    /// connection(s) gets disconnected.
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(default)]
    pub with_disconnect_messages: Option<bool>,
    /// Specifies time in milliseconds after which connection to real-time exchanges' WebSocket API
    /// is restarted if no message has been received.
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(default, rename = "timeoutIntervalMS")]
    pub timeout_interval_ms: Option<u64>,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s) and 4 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file
- **`as_tardis_instrument_key()`**: Function defined in this file
- **`new()`**: Function defined in this file

### Classes
- **`TardisInstrumentMiniInfo`**: Class defined in this file
- **`TardisInstrumentKey`**: Class defined in this file
- **`ReplayNormalizedRequestOptions`**: Class defined in this file
- **`StreamNormalizedRequestOptions`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 6


**Functions**: `as_tardis_instrument_key`, `new`
**Impls**: `TardisInstrumentKey`, `TardisInstrumentMiniInfo`
**Structs**: `ReplayNormalizedRequestOptions`, `StreamNormalizedRequestOptions`, `TardisInstrumentKey`, `TardisInstrumentMiniInfo`

## Related Files

This file is located in `crates/adapters/tardis/src/machine/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.718526Z*
