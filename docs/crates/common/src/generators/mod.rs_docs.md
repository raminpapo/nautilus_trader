# Documentation: mod.rs

## File Metadata

- **Path**: `crates/common/src/generators/mod.rs`
- **Size**: 1,474 bytes
- **Lines**: 37
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

//! Provides generation of identifiers such as `ClientOrderId` and `PositionId`.

pub mod client_order_id;
pub mod order_list_id;
pub mod position_id;

use chrono::{DateTime, Datelike, Timelike};

fn get_datetime_tag(unix_ms: u64) -> String {
    let now_utc = DateTime::from_timestamp_millis(unix_ms as i64)
        .expect("Milliseconds timestamp should be within valid range");
    format!(
        "{}{:02}{:02}-{:02}{:02}{:02}",
        now_utc.year(),
        now_utc.month(),
        now_utc.day(),
        now_utc.hour(),
        now_utc.minute(),
        now_utc.second(),
    )
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`get_datetime_tag()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `get_datetime_tag`

## Related Files

This file is located in `crates/common/src/generators/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.122137Z*
