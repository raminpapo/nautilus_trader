# Documentation: `crates/adapters/databento/src/common.rs`
**Generated:** 2025-11-15T19:40:00.844647Z
**File Size:** 2369 bytes
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

- **Path:** `crates/adapters/databento/src/common.rs`
- **Size:** 2,369 bytes
- **Lines:** 59
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 2

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

//! Common functions to support Databento adapter operations.

use databento::historical::DateTimeRange;
use nautilus_core::UnixNanos;
use time::OffsetDateTime;

pub const DATABENTO: &str = "DATABENTO";
pub const ALL_SYMBOLS: &str = "ALL_SYMBOLS";

/// # Errors
///
/// Returns an error if converting `start` or `end` to `OffsetDateTime` fails.
pub fn get_date_time_range(start: UnixNanos, end: UnixNanos) -> anyhow::Result<DateTimeRange> {
    Ok(DateTimeRange::from((
        OffsetDateTime::from_unix_timestamp_nanos(i128::from(start.as_u64()))?,
        OffsetDateTime::from_unix_timestamp_nanos(i128::from(end.as_u64()))?,
    )))
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////
#[cfg(test)]
mod tests {
    use rstest::*;

    use super::*;

    #[rstest]
    #[case(
        UnixNanos::default(),
        UnixNanos::default(),
        "DateTimeRange { start: 1970-01-01 0:00:00.0 +00:00:00, end: 1970-01-01 0:00:00.0 +00:00:00 }"
    )]
    #[case(UnixNanos::default(), 1_000_000_000.into(), "DateTimeRange { start: 1970-01-01 0:00:00.0 +00:00:00, end: 1970-01-01 0:00:01.0 +00:00:00 }")]
    fn test_get_date_time_range(
        #[case] start: UnixNanos,
        #[case] end: UnixNanos,
        #[case] range_str: &str,
    ) {
        let range = get_date_time_range(start, end).unwrap();
        assert_eq!(format!("{range:?}"), range_str);
    }
}
```


---

## Overview

This file is located at `crates/adapters/databento/src/common.rs` within the repository.

**Functions defined:** get_date_time_range, test_get_date_time_range


---

## Detailed Analysis

### Functions

#### `get_date_time_range(start: UnixNanos, end: UnixNanos)`


#### `test_get_date_time_range(
        #[case] start: UnixNanos,
        #[case] end: UnixNanos,
        #[case] range_str: &str,
    )`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/databento/src`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


