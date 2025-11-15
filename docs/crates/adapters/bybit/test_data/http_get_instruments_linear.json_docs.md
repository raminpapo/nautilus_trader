# Documentation: `crates/adapters/bybit/test_data/http_get_instruments_linear.json`
**Generated:** 2025-11-15T19:40:00.702743Z
**File Size:** 1983 bytes
**Extension:** .json
**Type:** text

---

## Table of Contents

1. [File Metadata](#file-metadata)
2. [Source Code](#source-code)
3. [Overview](#overview)
4. [Detailed Analysis](#detailed-analysis)
5. [Usage Examples](#usage-examples)
6. [Related Files](#related-files)
7. [Notes](#notes)

---

## File Metadata

- **Path:** `crates/adapters/bybit/test_data/http_get_instruments_linear.json`
- **Size:** 1,983 bytes
- **Lines:** 75
- **Extension:** `.json`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_instruments_linear.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bybit/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


