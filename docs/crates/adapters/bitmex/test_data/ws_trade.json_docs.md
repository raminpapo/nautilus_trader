# Documentation: ws_trade.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_trade.json`
- **Size**: 338 bytes
- **Lines**: 13
- **Language**: JSON

## Original Source

```json
{
    "timestamp": "2024-11-24T08:15:38.704Z",
    "symbol": "XBTUSD",
    "side": "Sell",
    "size": 100,
    "price": 98570.9,
    "tickDirection": "ZeroPlusTick",
    "trdMatchID": "00000000-006d-1000-0000-000e8737d536",
    "grossValue": 101450,
    "homeNotional": 0.0010145,
    "foreignNotional": 100.0,
    "trdType": "Regular"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `Regular`, `Sell`, `XBTUSD`, `ZeroPlusTick`

## Related Files

This file is located in `crates/adapters/bitmex/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bitmex/test_data/ws_trade.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.123707Z*
