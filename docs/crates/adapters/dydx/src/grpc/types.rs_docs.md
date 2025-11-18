# Documentation: types.rs

## File Metadata

- **Path**: `crates/adapters/dydx/src/grpc/types.rs`
- **Size**: 1,747 bytes
- **Lines**: 45
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

//! Type definitions for dYdX v4 gRPC operations.

use cosmrs::tendermint::{Error, chain::Id};
use serde::{Deserialize, Serialize};
use strum::{AsRefStr, Display};

/// [Chain ID](https://docs.dydx.xyz/nodes/network-constants#chain-id)
/// serves as a unique chain identifier to prevent replay attacks.
///
/// See also [Cosmos ecosystem](https://cosmos.directory/).
#[derive(Debug, Eq, PartialEq, Clone, Display, AsRefStr, Deserialize, Serialize)]
pub enum ChainId {
    /// Testnet.
    #[strum(serialize = "dydx-testnet-4")]
    #[serde(rename = "dydx-testnet-4")]
    Testnet4,
    /// Mainnet.
    #[strum(serialize = "dydx-mainnet-1")]
    #[serde(rename = "dydx-mainnet-1")]
    Mainnet1,
}

impl TryFrom<ChainId> for Id {
    type Error = Error;

    fn try_from(chain_id: ChainId) -> Result<Self, Self::Error> {
        chain_id.as_ref().parse()
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`try_from()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 3


**Enums**: `ChainId`
**Functions**: `try_from`
**Impls**: `TryFrom`

## Related Files

This file is located in `crates/adapters/dydx/src/grpc/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.861206Z*
