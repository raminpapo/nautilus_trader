# Documentation: accounts.rs

## File Metadata

- **Path**: `crates/infrastructure/src/sql/models/accounts.rs`
- **Size**: 2,405 bytes
- **Lines**: 54
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

use std::str::FromStr;

use nautilus_core::{UUID4, UnixNanos};
use nautilus_model::{
    enums::AccountType, events::AccountState, identifiers::AccountId, types::Currency,
};
use sqlx::{FromRow, Row, postgres::PgRow};

#[derive(Debug)]
pub struct AccountEventModel(pub AccountState);

impl<'r> FromRow<'r, PgRow> for AccountEventModel {
    fn from_row(row: &'r PgRow) -> Result<Self, sqlx::Error> {
        let event_id = row.try_get::<&str, _>("id").map(UUID4::from)?;
        let account_id = row.try_get::<&str, _>("account_id").map(AccountId::from)?;
        let account_type = AccountType::from_str(row.try_get::<&str, _>("kind")?).unwrap();
        let is_reported = row.try_get::<bool, _>("is_reported")?;
        let ts_event = row.try_get::<&str, _>("ts_event").map(UnixNanos::from)?;
        let ts_init = row.try_get::<&str, _>("ts_init").map(UnixNanos::from)?;
        let base_currency = row
            .try_get::<Option<&str>, _>("base_currency")
            .map(|res| res.map(Currency::from))?;
        let balances: serde_json::Value = row.try_get("balances")?;
        let margins: serde_json::Value = row.try_get("margins")?;
        let account_event = AccountState::new(
            account_id,
            account_type,
            serde_json::from_value(balances).unwrap(),
            serde_json::from_value(margins).unwrap(),
            is_reported,
            event_id,
            ts_event,
            ts_init,
            base_currency,
        );
        Ok(Self(account_event))
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`from_row()`**: Function defined in this file

### Classes
- **`AccountEventModel`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `from_row`
**Impls**: `FromRow`
**Structs**: `AccountEventModel`

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

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:02.039085Z*
