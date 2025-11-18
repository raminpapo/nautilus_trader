# Documentation: ws_trade_update.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/ws_trade_update.json`
- **Size**: 495 bytes
- **Lines**: 25
- **Language**: JSON

## Original Source

```json
{
  "channel": "trade",
  "type": "update",
  "data": [
    {
      "symbol": "BTC/USD",
      "side": "buy",
      "price": 105944.20,
      "qty": 0.00027625,
      "ord_type": "limit",
      "trade_id": 10218208,
      "timestamp": "2023-10-06T17:35:55.440295Z"
    },
    {
      "symbol": "BTC/USD",
      "side": "sell",
      "price": 105910.50,
      "qty": 0.00012460,
      "ord_type": "market",
      "trade_id": 10218209,
      "timestamp": "2023-10-06T17:35:56.123456Z"
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


**Identifiers**: `BTC`, `USD`

## Related Files

This file is located in `crates/adapters/kraken/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/kraken/test_data/ws_trade_update.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.276617Z*
