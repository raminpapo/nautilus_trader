# Documentation: ws_candles.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/ws_candles.json`
- **Size**: 333 bytes
- **Lines**: 18
- **Language**: JSON

## Original Source

```json
{
  "channel": "CANDLES_ONE_MINUTE",
  "type": "SNAPSHOT",
  "product_id": "ETH-PERP",
  "sequence": 0,
  "granularity": "ONE_MINUTE",
  "candles": [
    {
      "start": "2025-03-14T23:14:00Z",
      "open": "1921.71",
      "high": "1921.71",
      "low": "1919.87",
      "close": "1919.87",
      "volume": "11.2803"
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `CANDLES_ONE_MINUTE`, `ETH`, `ONE_MINUTE`, `PERP`, `SNAPSHOT`

## Related Files

This file is located in `crates/adapters/coinbase_intx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/coinbase_intx/test_data/ws_candles.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.665671Z*
