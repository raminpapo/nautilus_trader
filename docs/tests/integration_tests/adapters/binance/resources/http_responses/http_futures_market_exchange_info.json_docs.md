# Documentation: http_futures_market_exchange_info.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/http_responses/http_futures_market_exchange_info.json`
- **Size**: 6,641 bytes
- **Lines**: 284
- **Language**: JSON

## Original Source

```json
{
  "timezone": "UTC",
  "serverTime": 1645233611962,
  "futuresType": "U_MARGINED",
  "rateLimits": [
    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 6000
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 1200
    },
    {
      "rateLimitType": "ORDERS",
      "interval": "SECOND",
      "intervalNum": 10,
      "limit": 300
    }
  ],
  "exchangeFilters": [],
  "assets": [
    {
      "asset": "USDT",
      "marginAvailable": true,
      "autoAssetExchange": "-100"
    },
    {
      "asset": "BTC",
      "marginAvailable": true,
      "autoAssetExchange": "-0.00100000"
    },
    {
      "asset": "BNB",
      "marginAvailable": true,
      "autoAssetExchange": "-0.00100000"
    },
    {
      "asset": "ETH",
      "marginAvailable": true,
      "autoAssetExchange": "-0.00100000"
    },
    {
      "asset": "BUSD",
      "marginAvailable": true,
      "autoAssetExchange": "-100"
    }
  ],
  "symbols": [
    {
      "symbol": "BTCUSDT",
      "pair": "BTCUSDT",
      "contractType": "PERPETUAL",
      "deliveryDate": 4133404802000,
      "onboardDate": 1569398400000,
      "status": "TRADING",
      "maintMarginPercent": "2.5000",
      "requiredMarginPercent": "5.0000",
      "baseAsset": "BTC",
      "quoteAsset": "USDT",
      "marginAsset": "USDT",
      "pricePrecision": 2,
      "quantityPrecision": 3,
      "baseAssetPrecision": 8,
      "quotePrecision": 8,
      "underlyingType": "COIN",
      "underlyingSubType": [],
      "settlePlan": 0,
      "triggerProtect": "0.0500",
      "liquidationFee": "0.012000",
      "marketTakeBound": "0.30",
      "filters": [
        {
          "minPrice": "402",
          "maxPrice": "1246396.60",
          "filterType": "PRICE_FILTER",
          "tickSize": "0.10"
        },
        {
          "stepSize": "0.001",
          "filterType": "LOT_SIZE",
          "maxQty": "1000",
          "minQty": "0.001"
        },
        {
          "stepSize": "0.001",
          "filterType": "MARKET_LOT_SIZE",
          "maxQty": "1000",
          "minQty": "0.001"
        },
        {
          "limit": 200,
          "filterType": "MAX_NUM_ORDERS"
        },
        {
          "limit": 10,
          "filterType": "MAX_NUM_ALGO_ORDERS"
        },
        {
          "notional": "10",
          "filterType": "MIN_NOTIONAL"
        },
        {
          "multiplierDown": "0.5454",
          "multiplierUp": "1.1000",
          "multiplierDecimal": "4",
          "filterType": "PERCENT_PRICE"
        }
      ],
      "orderTypes": [
        "LIMIT",
        "MARKET",
        "STOP",
        "STOP_MARKET",
        "TAKE_PROFIT",
        "TAKE_PROFIT_MARKET",
        "TRAILING_STOP_MARKET"
      ],
      "timeInForce": [
        "GTC",
        "IOC",
        "FOK",
        "GTX"
      ]
    },
    {
      "symbol": "ETHUSDT",
      "pair": "ETHUSDT",
      "contractType": "PERPETUAL",
      "deliveryDate": 4133404800000,
      "onboardDate": 1569398400000,
      "status": "TRADING",
      "maintMarginPercent": "2.5000",
      "requiredMarginPercent": "5.0000",
      "baseAsset": "ETH",
      "quoteAsset": "USDT",
      "marginAsset": "USDT",
      "pricePrecision": 2,
      "quantityPrecision": 3,
      "baseAssetPrecision": 8,
      "quotePrecision": 8,
      "underlyingType": "COIN",
      "underlyingSubType": [],
      "settlePlan": 0,
      "triggerProtect": "0.0500",
      "liquidationFee": "0.030000",
      "marketTakeBound": "0.10",
      "filters": [
        {
          "minPrice": "28.23",
          "maxPrice": "144004.03",
          "filterType": "PRICE_FILTER",
          "tickSize": "0.01"
        },
        {
          "stepSize": "0.001",
          "filterType": "LOT_SIZE",
          "maxQty": "10000",
          "minQty": "0.001"
        },
        {
          "stepSize": "0.001",
          "filterType": "MARKET_LOT_SIZE",
          "maxQty": "10000",
          "minQty": "0.001"
        },
        {
          "limit": 200,
          "filterType": "MAX_NUM_ORDERS"
        },
        {
          "limit": 10,
          "filterType": "MAX_NUM_ALGO_ORDERS"
        },
        {
          "notional": "10",
          "filterType": "MIN_NOTIONAL"
        },
        {
          "multiplierDown": "0.9000",
          "multiplierUp": "1.1000",
          "multiplierDecimal": "4",
          "filterType": "PERCENT_PRICE"
        }
      ],
      "orderTypes": [
        "LIMIT",
        "MARKET",
        "STOP",
        "STOP_MARKET",
        "TAKE_PROFIT",
        "TAKE_PROFIT_MARKET",
        "TRAILING_STOP_MARKET"
      ],
      "timeInForce": [
        "GTC",
        "IOC",
        "FOK",
        "GTX"
      ]
    },
    {
      "symbol": "BTCUSDT_220325",
      "pair": "BTCUSDT",
      "contractType": "CURRENT_QUARTER",
      "deliveryDate": 1648195200000,
      "onboardDate": 1640332800000,
      "status": "TRADING",
      "maintMarginPercent": "2.5000",
      "requiredMarginPercent": "5.0000",
      "baseAsset": "BTC",
      "quoteAsset": "USDT",
      "marginAsset": "USDT",
      "pricePrecision": 1,
      "quantityPrecision": 3,
      "baseAssetPrecision": 8,
      "quotePrecision": 8,
      "underlyingType": "COIN",
      "underlyingSubType": [],
      "settlePlan": 0,
      "triggerProtect": "0.0500",
      "liquidationFee": "0.010000",
      "marketTakeBound": "0.05",
      "filters": [
        {
          "minPrice": "1093.3",
          "maxPrice": "1822332.8",
          "filterType": "PRICE_FILTER",
          "tickSize": "0.1"
        },
        {
          "stepSize": "0.001",
          "filterType": "LOT_SIZE",
          "maxQty": "500",
          "minQty": "0.001"
        },
        {
          "stepSize": "0.001",
          "filterType": "MARKET_LOT_SIZE",
          "maxQty": "500",
          "minQty": "0.001"
        },
        {
          "limit": 200,
          "filterType": "MAX_NUM_ORDERS"
        },
        {
          "limit": 10,
          "filterType": "MAX_NUM_ALGO_ORDERS"
        },
        {
          "notional": "10",
          "filterType": "MIN_NOTIONAL"
        },
        {
          "multiplierDown": "0.9500",
          "multiplierUp": "1.0500",
          "multiplierDecimal": "4",
          "filterType": "PERCENT_PRICE"
        }
      ],
      "orderTypes": [
        "LIMIT",
        "MARKET",
        "STOP",
        "STOP_MARKET",
        "TAKE_PROFIT",
        "TAKE_PROFIT_MARKET",
        "TRAILING_STOP_MARKET"
      ],
      "timeInForce": [
        "GTC",
        "IOC",
        "FOK",
        "GTX"
      ]
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 36


**Identifiers**: `BNB`, `BTC`, `BTCUSDT`, `BTCUSDT_220325`, `BUSD`, `COIN`, `CURRENT_QUARTER`, `ETH`, `ETHUSDT`, `FOK`, `GTC`, `GTX`, `IOC`, `LIMIT`, `LOT_SIZE`, `MARKET`, `MARKET_LOT_SIZE`, `MAX_NUM_ALGO_ORDERS`, `MAX_NUM_ORDERS`, `MINUTE`, `MIN_NOTIONAL`, `ORDERS`, `PERCENT_PRICE`, `PERPETUAL`, `PRICE_FILTER`, `REQUEST_WEIGHT`, `SECOND`, `STOP`, `STOP_MARKET`, `TAKE_PROFIT` *(+6 more)*

## Related Files

This file is located in `tests/integration_tests/adapters/binance/resources/http_responses/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/resources/http_responses/http_futures_market_exchange_info.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.618732Z*
