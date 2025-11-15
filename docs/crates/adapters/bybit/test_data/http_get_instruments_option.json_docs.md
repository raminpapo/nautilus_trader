# Documentation: `crates/adapters/bybit/test_data/http_get_instruments_option.json`
**Generated:** 2025-11-15T19:40:00.703662Z
**File Size:** 715 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_instruments_option.json`
- **Size:** 715 bytes
- **Lines:** 32
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


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_instruments_option.json` within the repository.

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


