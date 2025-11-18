# Documentation: http_get_instruments_spot.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_instruments_spot.json`
- **Size**: 648 bytes
- **Lines**: 31
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "nextPageCursor": "",
    "list": [
      {
        "symbol": "BTCUSDT",
        "baseCoin": "BTC",
        "quoteCoin": "USDT",
        "innovation": "0",
        "status": "Trading",
        "marginTrading": "utaOnly",
        "lotSizeFilter": {
          "basePrecision": "0.0001",
          "quotePrecision": "0.01",
          "minOrderQty": "0.001",
          "maxOrderQty": "100.0",
          "minOrderAmt": "10",
          "maxOrderAmt": "1000000"
        },
        "priceFilter": {
          "tickSize": "0.1"
        }
      }
    ]
  },
  "retExtInfo": {},
  "time": 1700000000000
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BTC`, `BTCUSDT`, `Trading`, `USDT`

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
pytest crates/adapters/bybit/test_data/http_get_instruments_spot.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.499563Z*
