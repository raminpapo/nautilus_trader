# Documentation: `crates/adapters/bybit/src/http/parse.rs`
**Generated:** 2025-11-15T19:40:00.654351Z
**File Size:** 7862 bytes
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

- **Path:** `crates/adapters/bybit/src/http/parse.rs`
- **Size:** 7,862 bytes
- **Lines:** 234
- **Extension:** `.rs`
- **Type:** text
- **Functions:** 17

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

//! Parsing functions for Bybit HTTP API responses.

use super::models::{
    BybitInstrumentInverseResponse, BybitInstrumentLinearResponse, BybitInstrumentOptionResponse,
    BybitInstrumentSpotResponse, BybitKlinesResponse, BybitServerTimeResponse,
    BybitTickersLinearResponse, BybitTickersOptionResponse, BybitTickersSpotResponse,
    BybitTradesResponse,
};
use crate::common::models::BybitResponse;

/// Parses a Bybit server time response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_server_time_response(data: &[u8]) -> anyhow::Result<BybitServerTimeResponse> {
    let response = serde_json::from_slice::<BybitServerTimeResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit spot instruments response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_instruments_spot_response(data: &[u8]) -> anyhow::Result<BybitInstrumentSpotResponse> {
    let response = serde_json::from_slice::<BybitInstrumentSpotResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit linear instruments response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_instruments_linear_response(
    data: &[u8],
) -> anyhow::Result<BybitInstrumentLinearResponse> {
    let response = serde_json::from_slice::<BybitInstrumentLinearResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit inverse instruments response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_instruments_inverse_response(
    data: &[u8],
) -> anyhow::Result<BybitInstrumentInverseResponse> {
    let response = serde_json::from_slice::<BybitInstrumentInverseResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit option instruments response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_instruments_option_response(
    data: &[u8],
) -> anyhow::Result<BybitInstrumentOptionResponse> {
    let response = serde_json::from_slice::<BybitInstrumentOptionResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit spot tickers response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_tickers_spot_response(data: &[u8]) -> anyhow::Result<BybitTickersSpotResponse> {
    let response = serde_json::from_slice::<BybitTickersSpotResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit linear tickers response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_tickers_linear_response(data: &[u8]) -> anyhow::Result<BybitTickersLinearResponse> {
    let response = serde_json::from_slice::<BybitTickersLinearResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit option tickers response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_tickers_option_response(data: &[u8]) -> anyhow::Result<BybitTickersOptionResponse> {
    let response = serde_json::from_slice::<BybitTickersOptionResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit klines response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_klines_response(data: &[u8]) -> anyhow::Result<BybitKlinesResponse> {
    let response = serde_json::from_slice::<BybitKlinesResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Parses a Bybit trades response from raw JSON bytes.
///
/// # Errors
///
/// Returns an error if deserialization fails.
pub fn parse_trades_response(data: &[u8]) -> anyhow::Result<BybitTradesResponse> {
    let response = serde_json::from_slice::<BybitTradesResponse>(data)?;
    validate_response(&response)?;
    Ok(response)
}

/// Validates that a Bybit response has a successful return code.
///
/// # Errors
///
/// Returns an error if the response indicates a failure.
fn validate_response<T>(response: &BybitResponse<T>) -> anyhow::Result<()> {
    if response.ret_code != 0 {
        anyhow::bail!(
            "Bybit API error {}: {}",
            response.ret_code,
            response.ret_msg
        );
    }
    Ok(())
}

////////////////////////////////////////////////////////////////////////////////
// Tests
////////////////////////////////////////////////////////////////////////////////

#[cfg(test)]
mod tests {
    use rstest::rstest;

    use super::*;
    use crate::common::testing::load_test_json;

    #[rstest]
    fn test_parse_instruments_linear_response() {
        let json = load_test_json("http_get_instruments_linear.json");
        let result = parse_instruments_linear_response(json.as_bytes());
        assert!(result.is_ok());

        let response = result.unwrap();
        assert_eq!(response.ret_code, 0);
        assert!(!response.result.list.is_empty());
    }

    #[rstest]
    fn test_parse_instruments_spot_response() {
        let json = load_test_json("http_get_instruments_spot.json");
        let result = parse_instruments_spot_response(json.as_bytes());
        assert!(result.is_ok());

        let response = result.unwrap();
        assert_eq!(response.ret_code, 0);
        assert!(!response.result.list.is_empty());
    }

    #[rstest]
    fn test_parse_instruments_inverse_response() {
        let json = load_test_json("http_get_instruments_inverse.json");
        let result = parse_instruments_inverse_response(json.as_bytes());
        assert!(result.is_ok());

        let response = result.unwrap();
        assert_eq!(response.ret_code, 0);
        assert!(!response.result.list.is_empty());
    }

    #[rstest]
    fn test_parse_instruments_option_response() {
        let json = load_test_json("http_get_instruments_option.json");
        let result = parse_instruments_option_response(json.as_bytes());
        assert!(result.is_ok());

        let response = result.unwrap();
        assert_eq!(response.ret_code, 0);
        assert!(!response.result.list.is_empty());
    }

    #[rstest]
    fn test_parse_klines_response() {
        let json = load_test_json("http_get_klines_linear.json");
        let result = parse_klines_response(json.as_bytes());
        assert!(result.is_ok());

        let response = result.unwrap();
        assert_eq!(response.ret_code, 0);
        assert!(!response.result.list.is_empty());
    }

    #[rstest]
    fn test_parse_trades_response() {
        let json = load_test_json("http_get_trades_recent.json");
        let result = parse_trades_response(json.as_bytes());
        assert!(result.is_ok());

        let response = result.unwrap();
        assert_eq!(response.ret_code, 0);
        assert!(!response.result.list.is_empty());
    }
}
```


---

## Overview

This file is located at `crates/adapters/bybit/src/http/parse.rs` within the repository.

**Functions defined:** parse_server_time_response, parse_instruments_spot_response, parse_instruments_linear_response, parse_instruments_inverse_response, parse_instruments_option_response, parse_tickers_spot_response, parse_tickers_linear_response, parse_tickers_option_response, parse_klines_response, parse_trades_response and 7 more


---

## Detailed Analysis

### Functions

#### `parse_server_time_response(data: &[u8])`


#### `parse_instruments_spot_response(data: &[u8])`


#### `parse_instruments_linear_response(
    data: &[u8],
)`


#### `parse_instruments_inverse_response(
    data: &[u8],
)`


#### `parse_instruments_option_response(
    data: &[u8],
)`


#### `parse_tickers_spot_response(data: &[u8])`


#### `parse_tickers_linear_response(data: &[u8])`


#### `parse_tickers_option_response(data: &[u8])`


#### `parse_klines_response(data: &[u8])`


#### `parse_trades_response(data: &[u8])`


#### `validate_response(response: &BybitResponse<T>)`


#### `test_parse_instruments_linear_response()`


#### `test_parse_instruments_spot_response()`


#### `test_parse_instruments_inverse_response()`


#### `test_parse_instruments_option_response()`


#### `test_parse_klines_response()`


#### `test_parse_trades_response()`



---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/src/http`

See [folder index](./index.md) for related files.


---

## Notes

*No special notes for this file.*


