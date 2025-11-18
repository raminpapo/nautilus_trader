# Documentation: ws_orderbook_snapshot.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_orderbook_snapshot.json`
- **Size**: 274 bytes
- **Lines**: 13
- **Language**: JSON

## Original Source

```json
{
  "topic": "orderbook.1.BTCUSDT",
  "type": "snapshot",
  "ts": 1709891679000,
  "data": {
    "s": "BTCUSDT",
    "b": [["27450.00", "0.500"], ["27449.50", "1.000"]],
    "a": [["27451.00", "0.750"], ["27451.50", "0.900"]],
    "u": 123456789,
    "seq": 987654321
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `BTCUSDT`

## Related Files

This file is located in `crates/adapters/bybit/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bybit/test_data/ws_orderbook_snapshot.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.532911Z*
