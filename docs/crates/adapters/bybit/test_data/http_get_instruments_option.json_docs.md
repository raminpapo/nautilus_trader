# Documentation: http_get_instruments_option.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_instruments_option.json`
- **Size**: 715 bytes
- **Lines**: 33
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "nextPageCursor": null,
    "list": [
      {
        "symbol": "ETH-26JUN26-16000-P",
        "status": "Trading",
        "baseCoin": "ETH",
        "quoteCoin": "USDC",
        "settleCoin": "USDC",
        "optionsType": "Put",
        "launchTime": "1700005000000",
        "deliveryTime": "1780005000000",
        "deliveryFeeRate": "0.0002",
        "priceFilter": {
          "minPrice": "0.1",
          "maxPrice": "5000",
          "tickSize": "0.1"
        },
        "lotSizeFilter": {
          "maxOrderQty": "100",
          "minOrderQty": "1",
          "qtyStep": "1"
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


**Identifiers**: `ETH`, `Put`, `Trading`, `USDC`

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
pytest crates/adapters/bybit/test_data/http_get_instruments_option.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.498518Z*
