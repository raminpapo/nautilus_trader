# Documentation: urls.rs

## File Metadata

- **Path**: `crates/adapters/bybit/src/common/urls.rs`
- **Size**: 5,262 bytes
- **Lines**: 152
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

//! Helpers for resolving Bybit REST and WebSocket base URLs at runtime.

use super::enums::{BybitEnvironment, BybitProductType};

const STREAM_MAINNET: &str = "stream";
const STREAM_TESTNET: &str = "stream-testnet";
const STREAM_DEMO: &str = "stream-demo";

/// Returns the base HTTP endpoint for the given environment.
#[must_use]
pub const fn bybit_http_base_url(environment: BybitEnvironment) -> &'static str {
    match environment {
        BybitEnvironment::Mainnet => "https://api.bybit.com",
        BybitEnvironment::Demo => "https://api-demo.bybit.com",
        BybitEnvironment::Testnet => "https://api-testnet.bybit.com",
    }
}

fn ws_public_subdomain(environment: BybitEnvironment) -> &'static str {
    match environment {
        BybitEnvironment::Mainnet => STREAM_MAINNET,
        BybitEnvironment::Demo => STREAM_DEMO,
        BybitEnvironment::Testnet => STREAM_TESTNET,
    }
}

/// Builds the public WebSocket endpoint for the given product/environment pair.
#[must_use]
pub fn bybit_ws_public_url(
    product_type: BybitProductType,
    environment: BybitEnvironment,
) -> String {
    let subdomain = ws_public_subdomain(environment);
    format!(
        "wss://{subdomain}.bybit.com/v5/public/{}",
        product_type.as_str()
    )
}

/// Returns the private WebSocket endpoint for the given environment.
///
/// # Notes
///
/// Bybit only exposes dedicated demo endpoints for public market data streams.
/// Private and trade channels share the main/testnet hosts.
#[must_use]
pub const fn bybit_ws_private_url(environment: BybitEnvironment) -> &'static str {
    match environment {
        BybitEnvironment::Testnet => "wss://stream-testnet.bybit.com/v5/private",
        BybitEnvironment::Mainnet | BybitEnvironment::Demo => "wss://stream.bybit.com/v5/private",
    }
}

/// Returns the trade WebSocket endpoint for order operations.
#[must_use]
pub const fn bybit_ws_trade_url(environment: BybitEnvironment) -> &'static str {
    match environment {
        BybitEnvironment::Testnet => "wss://stream-testnet.bybit.com/v5/trade",
        BybitEnvironment::Mainnet | BybitEnvironment::Demo => "wss://stream.bybit.com/v5/trade",
    }
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn resolves_public_urls() {
        assert_eq!(
            bybit_ws_public_url(BybitProductType::Linear, BybitEnvironment::Mainnet),
            "wss://stream.bybit.com/v5/public/linear"
        );
        assert_eq!(
            bybit_ws_public_url(BybitProductType::Option, BybitEnvironment::Demo),
            "wss://stream-demo.bybit.com/v5/public/option"
        );
        assert_eq!(
            bybit_ws_public_url(BybitProductType::Inverse, BybitEnvironment::Testnet),
            "wss://stream-testnet.bybit.com/v5/public/inverse"
        );
    }

    #[rstest]
    fn resolves_private_urls() {
        assert_eq!(
            bybit_ws_private_url(BybitEnvironment::Mainnet),
            "wss://stream.bybit.com/v5/private"
        );
        assert_eq!(
            bybit_ws_private_url(BybitEnvironment::Demo),
            "wss://stream.bybit.com/v5/private"
        );
        assert_eq!(
            bybit_ws_private_url(BybitEnvironment::Testnet),
            "wss://stream-testnet.bybit.com/v5/private"
        );
    }

    #[rstest]
    fn resolves_trade_urls() {
        assert_eq!(
            bybit_ws_trade_url(BybitEnvironment::Mainnet),
            "wss://stream.bybit.com/v5/trade"
        );
        assert_eq!(
            bybit_ws_trade_url(BybitEnvironment::Demo),
            "wss://stream.bybit.com/v5/trade"
        );
        assert_eq!(
            bybit_ws_trade_url(BybitEnvironment::Testnet),
            "wss://stream-testnet.bybit.com/v5/trade"
        );
    }

    #[rstest]
    fn resolves_http_urls() {
        assert_eq!(
            bybit_http_base_url(BybitEnvironment::Mainnet),
            "https://api.bybit.com"
        );
        assert_eq!(
            bybit_http_base_url(BybitEnvironment::Demo),
            "https://api-demo.bybit.com"
        );
        assert_eq!(
            bybit_http_base_url(BybitEnvironment::Testnet),
            "https://api-testnet.bybit.com"
        );
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 9 function(s).

## Detailed Walkthrough

### Functions
- **`bybit_http_base_url()`**: Function defined in this file
- **`ws_public_subdomain()`**: Function defined in this file
- **`bybit_ws_public_url()`**: Function defined in this file
- **`bybit_ws_private_url()`**: Function defined in this file
- **`bybit_ws_trade_url()`**: Function defined in this file
- **`resolves_public_urls()`**: Function defined in this file
- **`resolves_private_urls()`**: Function defined in this file
- **`resolves_trade_urls()`**: Function defined in this file
- **`resolves_http_urls()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `bybit_http_base_url`, `bybit_ws_private_url`, `bybit_ws_public_url`, `bybit_ws_trade_url`, `resolves_http_urls`, `resolves_private_urls`, `resolves_public_urls`, `resolves_trade_urls`, `ws_public_subdomain`

## Related Files

This file is located in `crates/adapters/bybit/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:54:59.379136Z*
