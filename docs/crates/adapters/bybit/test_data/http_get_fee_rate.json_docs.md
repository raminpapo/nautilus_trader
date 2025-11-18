# Documentation: http_get_fee_rate.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_fee_rate.json`
- **Size**: 533 bytes
- **Lines**: 29
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "takerFeeRate": "0.0006",
        "makerFeeRate": "0.0001",
        "baseCoin": ""
      },
      {
        "symbol": "ETHUSDT",
        "takerFeeRate": "0.0006",
        "makerFeeRate": "0.0001",
        "baseCoin": ""
      },
      {
        "symbol": "SOLUSDT",
        "takerFeeRate": "0.00075",
        "makerFeeRate": "0.00025",
        "baseCoin": ""
      }
    ]
  },
  "retExtInfo": {},
  "time": 1697673900000
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`

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
pytest crates/adapters/bybit/test_data/http_get_fee_rate.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.494637Z*
