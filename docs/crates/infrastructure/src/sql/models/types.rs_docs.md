# Documentation: `crates/infrastructure/src/sql/models/types.rs`
**Generated:** 2025-11-15T19:40:02.358293Z
**File Size:** 3427 bytes
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

- **Path:** `crates/infrastructure/src/sql/models/types.rs`
- **Size:** 3,427 bytes
- **Lines:** 80
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 3
- **Functions:** 3

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


---

## Overview

This file is located at `crates/infrastructure/src/sql/models/types.rs` within the repository.

**Classes defined:** CurrencyModel, SignalModel, CustomDataModel

**Functions defined:** from_row, from_row, from_row


---

## Detailed Analysis

### Classes

#### `CurrencyModel`

**Type:** struct


#### `SignalModel`

**Type:** struct


#### `CustomDataModel`

**Type:** struct


### Functions

#### `from_row(row: &'r PgRow)`


#### `from_row(row: &'r PgRow)`


#### `from_row(row: &'r PgRow)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/infrastructure/src/sql/models`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


