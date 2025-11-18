# Documentation: types.rs

## File Metadata

- **Path**: `crates/infrastructure/src/sql/models/types.rs`
- **Size**: 3,427 bytes
- **Lines**: 81
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

use bytes::Bytes;
use indexmap::IndexMap;
use nautilus_common::{custom::CustomData, signal::Signal};
use nautilus_core::UnixNanos;
use nautilus_model::{data::DataType, types::Currency};
use sqlx::{FromRow, Row, postgres::PgRow};
use ustr::Ustr;

use crate::sql::models::enums::CurrencyTypeModel;

#[derive(Debug)]
pub struct CurrencyModel(pub Currency);

#[derive(Debug)]
pub struct SignalModel(pub Signal);

#[derive(Debug)]
pub struct CustomDataModel(pub CustomData);

impl<'r> FromRow<'r, PgRow> for CurrencyModel {
    fn from_row(row: &'r PgRow) -> Result<Self, sqlx::Error> {
        let id = row.try_get::<String, _>("id")?;
        let precision = row.try_get::<i32, _>("precision")?;
        let iso4217 = row.try_get::<i32, _>("iso4217")?;
        let name = row.try_get::<String, _>("name")?;
        let currency_type_model = row.try_get::<CurrencyTypeModel, _>("currency_type")?;
        let currency = Currency::new(
            id.as_str(),
            precision as u8,
            iso4217 as u16,
            name.as_str(),
            currency_type_model.0,
        );
        Ok(Self(currency))
    }
}

impl<'r> FromRow<'r, PgRow> for SignalModel {
    fn from_row(row: &'r PgRow) -> Result<Self, sqlx::Error> {
        let name = row.try_get::<&str, _>("name").map(Ustr::from)?;
        let value = row.try_get::<String, _>("value")?;
        let ts_event = row.try_get::<&str, _>("ts_event").map(UnixNanos::from)?;
        let ts_init = row.try_get::<&str, _>("ts_init").map(UnixNanos::from)?;
        let signal = Signal::new(name, value, ts_event, ts_init);
        Ok(Self(signal))
    }
}

impl<'r> FromRow<'r, PgRow> for CustomDataModel {
    fn from_row(row: &'r PgRow) -> Result<Self, sqlx::Error> {
        let type_name = row.try_get::<&str, _>("data_type")?;
        let metadata_json: Option<serde_json::Value> =
            row.try_get::<Option<serde_json::Value>, _>("metadata")?;
        let metadata: Option<IndexMap<String, String>> = match metadata_json {
            Some(json_value) => serde_json::from_value(json_value).unwrap_or(None), // Handle deserialization
            None => None,
        };
        let data_type = DataType::new(type_name, metadata);
        let value = row.try_get::<Vec<u8>, _>("value").map(Bytes::from)?;
        let ts_event = row.try_get::<&str, _>("ts_event").map(UnixNanos::from)?;
        let ts_init = row.try_get::<&str, _>("ts_init").map(UnixNanos::from)?;
        let custom = CustomData::new(data_type, value, ts_event, ts_init);
        Ok(Self(custom))
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
- **`CurrencyModel`**: Class defined in this file
- **`SignalModel`**: Class defined in this file
- **`CustomDataModel`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 5


**Functions**: `from_row`
**Impls**: `FromRow`
**Structs**: `CurrencyModel`, `CustomDataModel`, `SignalModel`

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
*Generated on 2025-11-18T21:55:02.064873Z*
