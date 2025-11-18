# Documentation: common.rs

## File Metadata

- **Path**: `crates/testkit/src/common.rs`
- **Size**: 4,109 bytes
- **Lines**: 116
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

use std::path::PathBuf;

use nautilus_core::paths::get_test_data_path;

use crate::files::ensure_file_exists_or_download_http;

/// Returns the full path to the test data file at the specified relative `path` within the standard test data directory.
///
/// # Panics
///
/// Panics if the computed path cannot be represented as a valid UTF-8 string.
#[must_use]
pub fn get_test_data_file_path(path: &str) -> String {
    get_test_data_path()
        .join(path)
        .to_str()
        .unwrap()
        .to_string()
}

/// Returns the full path to the Nautilus-specific test data file given by `filename`, within the configured precision directory ("64-bit" or "128-bit").
///
/// # Panics
///
/// Panics if the computed path cannot be represented as a valid UTF-8 string.
#[must_use]
#[allow(unused_mut)]
pub fn get_nautilus_test_data_file_path(filename: &str) -> String {
    let mut path = get_test_data_path().join("nautilus");

    #[cfg(feature = "high-precision")]
    {
        path = path.join("128-bit");
    }
    #[cfg(not(feature = "high-precision"))]
    {
        path = path.join("64-bit");
    }

    path.join(filename).to_str().unwrap().to_string()
}

/// Returns the path to the checksums file for large test data files.
#[must_use]
pub fn get_test_data_large_checksums_filepath() -> PathBuf {
    get_test_data_path().join("large").join("checksums.json")
}

/// Ensures that the specified test data file exists locally by downloading it if necessary, using the provided `url`.
///
/// # Panics
///
/// Panics if the download or checksum verification fails, or if the resulting path cannot be represented as a valid UTF-8 string.
#[must_use]
pub fn ensure_test_data_exists(filename: &str, url: &str) -> PathBuf {
    let filepath = get_test_data_path().join("large").join(filename);
    let checksums_filepath = get_test_data_large_checksums_filepath();
    ensure_file_exists_or_download_http(&filepath, url, Some(&checksums_filepath), None).unwrap();
    filepath
}

/// Returns the path to the Tardis Deribit incremental book L2 test data.
#[must_use]
pub fn get_tardis_deribit_book_l2_path() -> PathBuf {
    get_test_data_path()
        .join("tardis")
        .join("deribit_incremental_book_L2_BTC-PERPETUAL.csv")
}

/// Returns the path to the Tardis Binance Futures book snapshot (depth 5) test data.
#[must_use]
pub fn get_tardis_binance_snapshot5_path() -> PathBuf {
    get_test_data_path()
        .join("tardis")
        .join("binance-futures_book_snapshot_5_BTCUSDT.csv")
}

/// Returns the path to the Tardis Binance Futures book snapshot (depth 25) test data.
#[must_use]
pub fn get_tardis_binance_snapshot25_path() -> PathBuf {
    get_test_data_path()
        .join("tardis")
        .join("binance-futures_book_snapshot_25_BTCUSDT.csv")
}

/// Returns the path to the Tardis Huobi quotes test data.
#[must_use]
pub fn get_tardis_huobi_quotes_path() -> PathBuf {
    get_test_data_path()
        .join("tardis")
        .join("huobi-dm-swap_quotes_BTC-USD.csv")
}

/// Returns the path to the Tardis Bitmex trades test data.
#[must_use]
pub fn get_tardis_bitmex_trades_path() -> PathBuf {
    get_test_data_path()
        .join("tardis")
        .join("bitmex_trades_XBTUSD.csv")
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 9 function(s).

## Detailed Walkthrough

### Functions
- **`get_test_data_file_path()`**: Function defined in this file
- **`get_nautilus_test_data_file_path()`**: Function defined in this file
- **`get_test_data_large_checksums_filepath()`**: Function defined in this file
- **`ensure_test_data_exists()`**: Function defined in this file
- **`get_tardis_deribit_book_l2_path()`**: Function defined in this file
- **`get_tardis_binance_snapshot5_path()`**: Function defined in this file
- **`get_tardis_binance_snapshot25_path()`**: Function defined in this file
- **`get_tardis_huobi_quotes_path()`**: Function defined in this file
- **`get_tardis_bitmex_trades_path()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 9


**Functions**: `ensure_test_data_exists`, `get_nautilus_test_data_file_path`, `get_tardis_binance_snapshot25_path`, `get_tardis_binance_snapshot5_path`, `get_tardis_bitmex_trades_path`, `get_tardis_deribit_book_l2_path`, `get_tardis_huobi_quotes_path`, `get_test_data_file_path`, `get_test_data_large_checksums_filepath`

## Related Files

This file is located in `crates/testkit/src/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/testkit/src/common.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:04.179651Z*
