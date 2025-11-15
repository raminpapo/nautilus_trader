# Documentation: `crates/adapters/bybit/test_data/http_get_instruments_inverse.json`
**Generated:** 2025-11-15T19:40:00.701671Z
**File Size:** 1025 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_instruments_inverse.json`
- **Size:** 1,025 bytes
- **Lines:** 42
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


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_instruments_inverse.json` within the repository.

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


