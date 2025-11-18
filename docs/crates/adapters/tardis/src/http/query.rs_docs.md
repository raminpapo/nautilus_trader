# Documentation: query.rs

## File Metadata

- **Path**: `crates/adapters/tardis/src/http/query.rs`
- **Size**: 2,611 bytes
- **Lines**: 68
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

use chrono::{DateTime, Utc};
use derive_builder::Builder;
use serde::Serialize;

mod datetime_format {
    use chrono::{DateTime, Utc};
    use serde::{self, Serializer};

    pub fn serialize<S>(date: &Option<DateTime<Utc>>, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        match date {
            Some(dt) => {
                serializer.serialize_str(&dt.to_rfc3339_opts(chrono::SecondsFormat::Millis, true))
            }
            None => serializer.serialize_none(),
        }
    }
}

/// Provides an instrument metadata API filter object.
///
/// See <https://docs.tardis.dev/api/instruments-metadata-api>.
#[derive(Debug, Default, Serialize, Builder)]
#[serde(rename_all = "camelCase")]
pub struct InstrumentFilter {
    #[serde(skip_serializing_if = "Option::is_none")]
    #[builder(default)]
    pub base_currency: Option<Vec<String>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    #[builder(default)]
    pub quote_currency: Option<Vec<String>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(rename = "type")]
    #[builder(default)]
    pub instrument_type: Option<Vec<String>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    #[builder(default)]
    pub contract_type: Option<Vec<String>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    #[builder(default)]
    pub active: Option<bool>,
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(with = "datetime_format")]
    #[builder(default)]
    pub available_since: Option<DateTime<Utc>>,
    #[serde(skip_serializing_if = "Option::is_none")]
    #[serde(with = "datetime_format")]
    #[builder(default)]
    pub available_to: Option<DateTime<Utc>>,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`serialize()`**: Function defined in this file

### Classes
- **`InstrumentFilter`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `serialize`
**Structs**: `InstrumentFilter`

## Related Files

This file is located in `crates/adapters/tardis/src/http/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.699203Z*
