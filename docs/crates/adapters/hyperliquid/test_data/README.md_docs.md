# Documentation: `crates/adapters/hyperliquid/test_data/README.md`
**Generated:** 2025-11-15T19:40:01.104253Z
**File Size:** 1478 bytes
**Extension:** .md
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

- **Path:** `crates/adapters/hyperliquid/test_data/README.md`
- **Size:** 1,478 bytes
- **Lines:** 58
- **Extension:** `.md`
- **Type:** text

---

## Source Code

```markdown
# Hyperliquid Test Data

This directory contains real API response samples for testing.

## Files

### HTTP Public Data (No Account Required)

- `http_meta_perp_sample.json` - Perpetuals market metadata (sample of 3 markets)
- `http_meta_spot_sample.json` - Spot market metadata (sample of 3 markets)
- `http_l2_book_btc.json` - BTC order book snapshot (5 levels each side)
- `http_l2_book_snapshot.json` - Existing order book test data

### WebSocket Public Data (No Account Required)

- `ws_trades_sample.json` - Real-time trade message sample
- `ws_l2_book_sample.json` - Order book update message sample
- `ws_book_data.json` - Existing book data test sample

## Capturing New Test Data

### HTTP Data

```bash
cargo run --bin capture-test-data
```

### WebSocket Data

```bash
cargo run --bin capture-ws-test-data
```

## Usage in Tests

```rust
fn load_test_data<T>(filename: &str) -> T
where
    T: serde::de::DeserializeOwned,
{
    let path = format!("test_data/{}", filename);
    let content = std::fs::read_to_string(path).expect("Failed to read test data");
    serde_json::from_str(&content).expect("Failed to parse test data")
}

#[rstest]
fn test_parse_perpetuals_metadata() {
    let meta: PerpMetadata = load_test_data("http_meta_perp_sample.json");
    // assertions...
}
```

## Data Size Policy

- Keep files small (< 50KB each)
- Sample only 3-5 items from large arrays
- Use real mainnet data when possible
- Update files when API response format changes
```


---

## Overview

This file is located at `crates/adapters/hyperliquid/test_data/README.md` within the repository.

This is a Markdown documentation file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/hyperliquid/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


