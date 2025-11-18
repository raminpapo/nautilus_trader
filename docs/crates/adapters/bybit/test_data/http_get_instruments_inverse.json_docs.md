# Documentation: http_get_instruments_inverse.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_instruments_inverse.json`
- **Size**: 1,025 bytes
- **Lines**: 43
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
        "symbol": "BTCUSD",
        "contractType": "InversePerpetual",
        "status": "Trading",
        "baseCoin": "BTC",
        "quoteCoin": "USD",
        "launchTime": "1699980000000",
        "deliveryTime": "1702582000000",
        "deliveryFeeRate": "0.0005",
        "priceScale": "1",
        "leverageFilter": {
          "minLeverage": "1",
          "maxLeverage": "100",
          "leverageStep": "1"
        },
        "priceFilter": {
          "minPrice": "1",
          "maxPrice": "1000000",
          "tickSize": "0.5"
        },
        "lotSizeFilter": {
          "maxOrderQty": "1000000",
          "minOrderQty": "1",
          "qtyStep": "1",
          "postOnlyMaxOrderQty": "1000000",
          "maxMktOrderQty": "500000"
        },
        "unifiedMarginTrade": true,
        "fundingInterval": 8,
        "settleCoin": "BTC"
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

Total unique keywords extracted: 5


**Identifiers**: `BTC`, `BTCUSD`, `InversePerpetual`, `Trading`, `USD`

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
pytest crates/adapters/bybit/test_data/http_get_instruments_inverse.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.495839Z*
