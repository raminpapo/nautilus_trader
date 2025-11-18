# Documentation: README.md

## File Metadata

- **Path**: `crates/adapters/hyperliquid/test_data/README.md`
- **Size**: 1,478 bytes
- **Lines**: 59
- **Language**: Markdown

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a Markdown documentation file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 30


**Identifiers**: `API`, `Account`, `BTC`, `Capturing`, `Data`, `DeserializeOwned`, `Existing`, `Failed`, `Files`, `HTTP`, `Hyperliquid`, `Keep`, `New`, `Order`, `PerpMetadata`, `Perpetuals`, `Policy`, `Public`, `Real`, `Required`, `Sample`, `Size`, `Spot`, `Test`, `Tests`, `This`, `Update`, `Usage`, `Use`, `WebSocket`

## Related Files

This file is located in `crates/adapters/hyperliquid/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/hyperliquid/test_data/README.md

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.128184Z*
