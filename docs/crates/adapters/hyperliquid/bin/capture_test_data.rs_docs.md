# Documentation: capture_test_data.rs

## File Metadata

- **Path**: `crates/adapters/hyperliquid/bin/capture_test_data.rs`
- **Size**: 2,493 bytes
- **Lines**: 65
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

// Simple script to capture real API responses for test fixtures

use std::fs;

use nautilus_hyperliquid::http::client::HyperliquidHttpClient;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("Capturing Hyperliquid test data...");

    let client = HyperliquidHttpClient::new(false, Some(60), None)?;

    // Capture perpetuals metadata (first 3 markets to keep file small)
    println!("Fetching perpetuals metadata...");
    let meta = client.info_meta().await?;
    let sample_meta = serde_json::json!({
        "universe": meta.universe.iter().take(3).collect::<Vec<_>>()
    });
    fs::write(
        "test_data/http_meta_perp_sample.json",
        serde_json::to_string_pretty(&sample_meta)?,
    )?;
    println!("Saved http_meta_perp_sample.json (3 markets)");

    // Note: Spot metadata endpoint not yet implemented in client

    // Capture BTC order book
    println!("Fetching BTC order book...");
    let book = client.info_l2_book("BTC").await?;
    // Keep only top 5 levels each side
    let sample_book = serde_json::json!({
        "coin": book.coin,
        "levels": vec![
            book.levels.first().unwrap().iter().take(5).collect::<Vec<_>>(),
            book.levels[1].iter().take(5).collect::<Vec<_>>()
        ],
        "time": book.time
    });
    fs::write(
        "test_data/http_l2_book_btc.json",
        serde_json::to_string_pretty(&sample_book)?,
    )?;
    println!("Saved http_l2_book_btc.json (5 levels each side)");

    println!("\nTest data capture complete!");
    println!("Files saved in test_data/");

    Ok(())
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. It defines 1 function(s).

## Detailed Walkthrough

### Functions
- **`main()`**: Function defined in this file


## Keywords and Identifiers

Total unique keywords extracted: 1


**Functions**: `main`

## Related Files

This file is located in `crates/adapters/hyperliquid/bin/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/hyperliquid/bin/capture_test_data.rs

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.948816Z*
