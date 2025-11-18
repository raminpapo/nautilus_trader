# Documentation: models.rs

## File Metadata

- **Path**: `crates/adapters/kraken/src/common/models.rs`
- **Size**: 1,564 bytes
- **Lines**: 41
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

//! Common data structures shared across the Kraken adapter.

use serde::{Deserialize, Serialize};

/// Generic Kraken API response wrapper.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct KrakenResponse<T> {
    pub result: Option<T>,
    pub error: Option<Vec<String>>,
    #[serde(default)]
    pub success: bool,
}

impl<T> KrakenResponse<T> {
    pub fn is_success(&self) -> bool {
        self.success || (self.error.is_none() || self.error.as_ref().is_some_and(|e| e.is_empty()))
    }

    pub fn error_message(&self) -> Option<String> {
        self.error
            .as_ref()
            .filter(|e| !e.is_empty())
            .map(|e| e.join(", "))
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 2 function(s) and 1 class(es).

## Detailed Walkthrough

### Functions
- **`is_success()`**: Function defined in this file
- **`error_message()`**: Function defined in this file

### Classes
- **`KrakenResponse`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Functions**: `error_message`, `is_success`
**Impls**: `KrakenResponse`
**Structs**: `KrakenResponse`

## Related Files

This file is located in `crates/adapters/kraken/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.160933Z*
