# Documentation: custom.rs

## File Metadata

- **Path**: `crates/common/src/custom.rs`
- **Size**: 1,715 bytes
- **Lines**: 53
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

//! A user custom data type.

use bytes::Bytes;
use nautilus_core::UnixNanos;
use nautilus_model::data::DataType;
use serde::{Deserialize, Serialize};

/// Represents a custom data.
#[repr(C)]
#[derive(Clone, Debug, PartialEq, Eq, Serialize, Deserialize)]
#[cfg_attr(
    feature = "python",
    pyo3::pyclass(module = "nautilus_trader.core.nautilus_pyo3.common")
)]
pub struct CustomData {
    pub data_type: DataType,
    pub value: Bytes,
    pub ts_event: UnixNanos,
    pub ts_init: UnixNanos,
}

impl CustomData {
    /// Creates a new [`CustomData`] instance.
    pub const fn new(
        data_type: DataType,
        value: Bytes,
        ts_event: UnixNanos,
        ts_init: UnixNanos,
    ) -> Self {
        Self {
            data_type,
            value,
            ts_event,
            ts_init,
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`new()`**: Function defined in this file

### Classes
- **`CustomData`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 2


**Functions**: `new`
**Impls**: `CustomData`
**Structs**: `CustomData`

## Related Files

This file is located in `crates/common/src/`. Related files may include:
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
*Generated on 2025-11-18T21:55:01.086164Z*
