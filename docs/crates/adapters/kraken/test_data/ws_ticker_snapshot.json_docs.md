# Documentation: ws_ticker_snapshot.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/ws_ticker_snapshot.json`
- **Size**: 377 bytes
- **Lines**: 21
- **Language**: JSON

## Original Source

```json
{
  "channel": "ticker",
  "type": "snapshot",
  "data": [
    {
      "symbol": "BTC/USD",
      "bid": 105944.20,
      "bid_qty": 2.5,
      "ask": 105944.30,
      "ask_qty": 3.2,
      "last": 105899.40,
      "volume": 163.28908096,
      "vwap": 105904.39279,
      "low": 104711.00,
      "high": 106613.10,
      "change": 250.00,
      "change_pct": 0.24
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
pytest crates/adapters/kraken/test_data/ws_ticker_snapshot.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.275218Z*
