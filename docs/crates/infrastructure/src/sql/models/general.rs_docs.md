# Documentation: general.rs

## File Metadata

- **Path**: `crates/infrastructure/src/sql/models/general.rs`
- **Size**: 1,725 bytes
- **Lines**: 47
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

use nautilus_model::identifiers::{ClientId, ClientOrderId};
use sqlx::{Error, FromRow, Row, postgres::PgRow};

#[derive(Debug, sqlx::FromRow)]
pub struct GeneralRow {
    pub id: String,
    pub value: Vec<u8>,
}

#[derive(Debug)]
pub struct OrderEventOrderClientIdCombination {
    pub client_order_id: ClientOrderId,
    pub client_id: ClientId,
}

impl<'r> FromRow<'r, PgRow> for OrderEventOrderClientIdCombination {
    fn from_row(row: &'r PgRow) -> Result<Self, Error> {
        let client_order_id = row
            .try_get::<&str, _>("client_order_id")
            .map(ClientOrderId::from)
            .unwrap();
        let client_id = row
            .try_get::<&str, _>("client_id")
            .map(ClientId::from)
            .unwrap();
        Ok(Self {
            client_order_id,
            client_id,
        })
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 2 class(es).

## Detailed Walkthrough

### Functions
- **`from_row()`**: Function defined in this file

### Classes
- **`GeneralRow`**: Class defined in this file
- **`OrderEventOrderClientIdCombination`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 4


**Functions**: `from_row`
**Impls**: `FromRow`
**Structs**: `GeneralRow`, `OrderEventOrderClientIdCombination`

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
*Generated on 2025-11-18T21:55:02.047444Z*
