# Documentation: ws_public_trade.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_public_trade.json`
- **Size**: 290 bytes
- **Lines**: 17
- **Language**: JSON

## Original Source

```json
{
  "topic": "trade.linear.BTCUSDT",
  "type": "snapshot",
  "ts": 1709891679005,
  "data": [
    {
      "T": 1709891679000,
      "s": "BTCUSDT",
      "S": "Buy",
      "v": "0.010",
      "p": "27451.00",
      "i": "9dc75fca-4bdd-4773-9f78-6f5d7ab2a110",
      "BT": false
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `BTCUSDT`, `Buy`

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
pytest crates/adapters/bybit/test_data/ws_public_trade.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.534097Z*
