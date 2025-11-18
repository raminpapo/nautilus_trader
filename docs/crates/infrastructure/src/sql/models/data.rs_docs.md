# Documentation: data.rs

## File Metadata

- **Path**: `crates/infrastructure/src/sql/models/data.rs`
- **Size**: 4,834 bytes
- **Lines**: 120
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

use nautilus_core::UnixNanos;
use nautilus_model::{
    data::{Bar, BarSpecification, BarType, QuoteTick, TradeTick},
    identifiers::{InstrumentId, TradeId},
    types::{Price, Quantity},
};
use sqlx::{Error, FromRow, Row, postgres::PgRow};

use crate::sql::models::enums::{
    AggregationSourceModel, AggressorSideModel, BarAggregationModel, PriceTypeModel,
};

#[derive(Debug)]
pub struct QuoteTickModel(pub QuoteTick);

#[derive(Debug)]
pub struct TradeTickModel(pub TradeTick);

#[derive(Debug)]
pub struct BarModel(pub Bar);

impl<'r> FromRow<'r, PgRow> for QuoteTickModel {
    fn from_row(row: &'r PgRow) -> Result<Self, Error> {
        let instrument_id = row
            .try_get::<&str, _>("instrument_id")
            .map(InstrumentId::from)?;
        let bid_price = row.try_get::<&str, _>("bid_price").map(Price::from)?;
        let ask_price = row.try_get::<&str, _>("ask_price").map(Price::from)?;
        let bid_size = row.try_get::<&str, _>("bid_size").map(Quantity::from)?;
        let ask_size = row.try_get::<&str, _>("ask_size").map(Quantity::from)?;
        let ts_event = row.try_get::<&str, _>("ts_event").map(UnixNanos::from)?;
        let ts_init = row.try_get::<&str, _>("ts_init").map(UnixNanos::from)?;
        let quote = QuoteTick::new(
            instrument_id,
            bid_price,
            ask_price,
            bid_size,
            ask_size,
            ts_event,
            ts_init,
        );
        Ok(Self(quote))
    }
}

impl<'r> FromRow<'r, PgRow> for TradeTickModel {
    fn from_row(row: &'r PgRow) -> Result<Self, Error> {
        let instrument_id = row
            .try_get::<&str, _>("instrument_id")
            .map(InstrumentId::from)?;
        let price = row.try_get::<&str, _>("price").map(Price::from)?;
        let size = row.try_get::<&str, _>("quantity").map(Quantity::from)?;
        let aggressor_side = row
            .try_get::<AggressorSideModel, _>("aggressor_side")
            .map(|x| x.0)?;
        let trade_id = row
            .try_get::<&str, _>("venue_trade_id")
            .map(TradeId::from)?;
        let ts_event = row.try_get::<&str, _>("ts_event").map(UnixNanos::from)?;
        let ts_init = row.try_get::<&str, _>("ts_init").map(UnixNanos::from)?;
        let trade = TradeTick::new(
            instrument_id,
            price,
            size,
            aggressor_side,
            trade_id,
            ts_event,
            ts_init,
        );
        Ok(Self(trade))
    }
}

impl<'r> FromRow<'r, PgRow> for BarModel {
    fn from_row(row: &'r PgRow) -> Result<Self, Error> {
        let instrument_id = row
            .try_get::<&str, _>("instrument_id")
            .map(InstrumentId::from)?;
        let step = row.try_get::<i32, _>("step")?;
        let price_type = row
            .try_get::<PriceTypeModel, _>("price_type")
            .map(|x| x.0)?;
        let bar_aggregation = row
            .try_get::<BarAggregationModel, _>("bar_aggregation")
            .map(|x| x.0)?;
        let aggregation_source = row
            .try_get::<AggregationSourceModel, _>("aggregation_source")
            .map(|x| x.0)?;
        let bar_type = BarType::new(
            instrument_id,
            BarSpecification::new(step as usize, bar_aggregation, price_type),
            aggregation_source,
        );
        let open = row.try_get::<&str, _>("open").map(Price::from)?;
        let high = row.try_get::<&str, _>("high").map(Price::from)?;
        let low = row.try_get::<&str, _>("low").map(Price::from)?;
        let close = row.try_get::<&str, _>("close").map(Price::from)?;
        let volume = row.try_get::<&str, _>("volume").map(Quantity::from)?;
        let ts_event = row.try_get::<&str, _>("ts_event").map(UnixNanos::from)?;
        let ts_init = row.try_get::<&str, _>("ts_init").map(UnixNanos::from)?;
        let bar = Bar::new(bar_type, open, high, low, close, volume, ts_event, ts_init);
        Ok(Self(bar))
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 3 function(s) and 3 class(es).

## Detailed Walkthrough

### Functions
- **`from_row()`**: Function defined in this file
- **`from_row()`**: Function defined in this file
- **`from_row()`**: Function defined in this file

### Classes
- **`QuoteTickModel`**: Class defined in this file
- **`TradeTickModel`**: Class defined in this file
- **`BarModel`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `from_row`
**Impls**: `FromRow`
**Structs**: `BarModel`, `QuoteTickModel`, `TradeTickModel`

## Related Files

This file is located in `crates/infrastructure/src/sql/models/`. Related files may include:
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

⚠️ **Security**: This file may perform database operations. Use parameterized queries to prevent SQL injection.

---
*Generated on 2025-11-18T21:55:02.042076Z*
