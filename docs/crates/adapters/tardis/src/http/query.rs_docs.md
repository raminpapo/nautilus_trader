# Documentation: `crates/adapters/tardis/src/http/query.rs`
**Generated:** 2025-11-15T19:40:01.466632Z
**File Size:** 2611 bytes
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

- **Path:** `crates/adapters/tardis/src/http/query.rs`
- **Size:** 2,611 bytes
- **Lines:** 67
- **Extension:** `.rs`
- **Type:** text
- **Classes:** 1
- **Functions:** 1

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


---

## Overview

This file is located at `crates/adapters/tardis/src/http/query.rs` within the repository.

**Classes defined:** InstrumentFilter

**Functions defined:** serialize


---

## Detailed Analysis

### Classes

#### `InstrumentFilter`

**Type:** struct


### Functions

#### `serialize(date: &Option<DateTime<Utc>>, serializer: S)`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/tardis/src/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


