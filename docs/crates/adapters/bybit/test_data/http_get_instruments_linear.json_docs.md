# Documentation: http_get_instruments_linear.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_instruments_linear.json`
- **Size**: 1,983 bytes
- **Lines**: 76
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
        "symbol": "BTCUSDT",
        "contractType": "LinearPerpetual",
        "status": "Trading",
        "baseCoin": "BTC",
        "quoteCoin": "USDT",
        "launchTime": "1699990000000",
        "deliveryTime": "1702592000000",
        "deliveryFeeRate": "0.0005",
        "priceScale": "2",
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
          "maxOrderQty": "100.0",
          "minOrderQty": "0.001",
          "qtyStep": "0.001",
          "postOnlyMaxOrderQty": "100.0",
          "maxMktOrderQty": "50.0",
          "minNotionalValue": "5"
        },
        "unifiedMarginTrade": true,
        "fundingInterval": 8,
        "settleCoin": "USDT"
      },
      {
        "symbol": "ETHUSDT",
        "contractType": "LinearPerpetual",
        "status": "Trading",
        "baseCoin": "ETH",
        "quoteCoin": "USDT",
        "launchTime": "1699990000000",
        "deliveryTime": "1702592000000",
        "deliveryFeeRate": "0.0005",
        "priceScale": "2",
        "leverageFilter": {
          "minLeverage": "1",
          "maxLeverage": "100",
          "leverageStep": "1"
        },
        "priceFilter": {
          "minPrice": "0.1",
          "maxPrice": "100000",
          "tickSize": "0.05"
        },
        "lotSizeFilter": {
          "maxOrderQty": "1000.0",
          "minOrderQty": "0.01",
          "qtyStep": "0.01",
          "postOnlyMaxOrderQty": "1000.0",
          "maxMktOrderQty": "500.0",
          "minNotionalValue": "5"
        },
        "unifiedMarginTrade": true,
        "fundingInterval": 8,
        "settleCoin": "USDT"
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

Total unique keywords extracted: 7


**Identifiers**: `BTC`, `BTCUSDT`, `ETH`, `ETHUSDT`, `LinearPerpetual`, `Trading`, `USDT`

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
pytest crates/adapters/bybit/test_data/http_get_instruments_linear.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.497343Z*
