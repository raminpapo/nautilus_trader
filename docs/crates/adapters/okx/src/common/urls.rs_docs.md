# Documentation: urls.rs

## File Metadata

- **Path**: `crates/adapters/okx/src/common/urls.rs`
- **Size**: 5,305 bytes
- **Lines**: 158
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

//! URL helpers and endpoint metadata for OKX services.

use nautilus_core::env::get_env_var;

/// OKX endpoint types for determining URL and authentication requirements.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
#[cfg_attr(feature = "python", pyo3::pyclass)]
pub enum OKXEndpointType {
    Public,
    Private,
    Business,
}

/// Checks if endpoint requires authentication.
pub fn requires_authentication(endpoint_type: OKXEndpointType) -> bool {
    matches!(
        endpoint_type,
        OKXEndpointType::Private | OKXEndpointType::Business
    )
}

/// Gets the HTTP base URL.
pub fn get_http_base_url() -> String {
    get_env_var("OKX_BASE_URL_HTTP").unwrap_or_else(|_| "https://www.okx.com".to_string())
}

/// Gets the WebSocket base URL for public data (market data).
pub fn get_ws_base_url_public(is_demo: bool) -> String {
    if is_demo {
        get_env_var("OKX_DEMO_BASE_URL_WS_PUBLIC")
            .unwrap_or_else(|_| "wss://wspap.okx.com:8443/ws/v5/public".to_string())
    } else {
        get_env_var("OKX_BASE_URL_WS_PUBLIC")
            .unwrap_or_else(|_| "wss://ws.okx.com:8443/ws/v5/public".to_string())
    }
}

/// Gets the WebSocket base URL for private data (account/order management).
pub fn get_ws_base_url_private(is_demo: bool) -> String {
    if is_demo {
        get_env_var("OKX_DEMO_BASE_URL_WS_PRIVATE")
            .unwrap_or_else(|_| "wss://wspap.okx.com:8443/ws/v5/private".to_string())
    } else {
        get_env_var("OKX_BASE_URL_WS_PRIVATE")
            .unwrap_or_else(|_| "wss://ws.okx.com:8443/ws/v5/private".to_string())
    }
}

/// Gets the WebSocket base URL for business data (bars/candlesticks).
pub fn get_ws_base_url_business(is_demo: bool) -> String {
    if is_demo {
        get_env_var("OKX_DEMO_BASE_URL_WS_BUSINESS")
            .unwrap_or_else(|_| "wss://wspap.okx.com:8443/ws/v5/business".to_string())
    } else {
        get_env_var("OKX_BASE_URL_WS_BUSINESS")
            .unwrap_or_else(|_| "wss://ws.okx.com:8443/ws/v5/business".to_string())
    }
}

/// Gets WebSocket URL by endpoint type.
pub fn get_ws_url(endpoint_type: OKXEndpointType, is_demo: bool) -> String {
    match endpoint_type {
        OKXEndpointType::Public => get_ws_base_url_public(is_demo),
        OKXEndpointType::Private => get_ws_base_url_private(is_demo),
        OKXEndpointType::Business => get_ws_base_url_business(is_demo),
    }
}

/// Gets the WebSocket base URL (backward compatibility - defaults to private).
///
/// .. deprecated::
///     Use get_ws_base_url_public() or get_ws_base_url_private() instead.
pub fn get_ws_base_url(is_demo: bool) -> String {
    get_ws_base_url_private(is_demo)
}

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;

    #[rstest]
    fn test_endpoint_authentication() {
        assert!(!requires_authentication(OKXEndpointType::Public));
        assert!(requires_authentication(OKXEndpointType::Private));
        assert!(requires_authentication(OKXEndpointType::Business));
    }

    #[rstest]
    fn test_http_base_url() {
        assert_eq!(get_http_base_url(), "https://www.okx.com");
    }

    #[rstest]
    fn test_ws_urls_production() {
        assert_eq!(
            get_ws_base_url_public(false),
            "wss://ws.okx.com:8443/ws/v5/public"
        );
        assert_eq!(
            get_ws_base_url_private(false),
            "wss://ws.okx.com:8443/ws/v5/private"
        );
        assert_eq!(
            get_ws_base_url_business(false),
            "wss://ws.okx.com:8443/ws/v5/business"
        );
    }

    #[rstest]
    fn test_ws_urls_demo() {
        assert_eq!(
            get_ws_base_url_public(true),
            "wss://wspap.okx.com:8443/ws/v5/public"
        );
        assert_eq!(
            get_ws_base_url_private(true),
            "wss://wspap.okx.com:8443/ws/v5/private"
        );
        assert_eq!(
            get_ws_base_url_business(true),
            "wss://wspap.okx.com:8443/ws/v5/business"
        );
    }

    #[rstest]
    fn test_get_ws_url_by_type() {
        assert_eq!(
            get_ws_url(OKXEndpointType::Public, false),
            get_ws_base_url_public(false)
        );
        assert_eq!(
            get_ws_url(OKXEndpointType::Private, false),
            get_ws_base_url_private(false)
        );
        assert_eq!(
            get_ws_url(OKXEndpointType::Business, false),
            get_ws_base_url_business(false)
        );
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 12 function(s).

## Detailed Walkthrough

### Functions
- **`requires_authentication()`**: Function defined in this file
- **`get_http_base_url()`**: Function defined in this file
- **`get_ws_base_url_public()`**: Function defined in this file
- **`get_ws_base_url_private()`**: Function defined in this file
- **`get_ws_base_url_business()`**: Function defined in this file
- **`get_ws_url()`**: Function defined in this file
- **`get_ws_base_url()`**: Function defined in this file
- **`test_endpoint_authentication()`**: Function defined in this file
- **`test_http_base_url()`**: Function defined in this file
- **`test_ws_urls_production()`**: Function defined in this file
- **`test_ws_urls_demo()`**: Function defined in this file
- **`test_get_ws_url_by_type()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 13


**Enums**: `OKXEndpointType`
**Functions**: `get_http_base_url`, `get_ws_base_url`, `get_ws_base_url_business`, `get_ws_base_url_private`, `get_ws_base_url_public`, `get_ws_url`, `requires_authentication`, `test_endpoint_authentication`, `test_get_ws_url_by_type`, `test_http_base_url`, `test_ws_urls_demo`, `test_ws_urls_production`

## Related Files

This file is located in `crates/adapters/okx/src/common/`. Related files may include:
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
*Generated on 2025-11-18T21:55:00.355979Z*
