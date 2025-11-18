# Documentation: models.rs

## File Metadata

- **Path**: `crates/adapters/dydx/src/common/models.rs`
- **Size**: 1,428 bytes
- **Lines**: 33
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

//! Common types and models for the dYdX adapter.

use serde::{Deserialize, Serialize};

/// dYdX account information.
///
/// Represents a Cosmos SDK account with its address, account number,
/// and current sequence (nonce) for transaction ordering.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct DydxAccount {
    /// Cosmos SDK address (dydx...).
    pub address: String,
    /// Account number from the blockchain.
    pub account_number: u64,
    /// Current sequence number (nonce) for transactions.
    pub sequence: u64,
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. 1 class(es).

## Detailed Walkthrough


### Classes
- **`DydxAccount`**: Class defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Structs**: `DydxAccount`

## Related Files

This file is located in `crates/adapters/dydx/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.785518Z*
