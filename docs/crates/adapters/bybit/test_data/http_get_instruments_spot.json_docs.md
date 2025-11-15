# Documentation: `crates/adapters/bybit/test_data/http_get_instruments_spot.json`
**Generated:** 2025-11-15T19:40:00.704549Z
**File Size:** 648 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_instruments_spot.json`
- **Size:** 648 bytes
- **Lines:** 30
- **Extension:** `.json`
- **Type:** text

---

## Source Code

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


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_instruments_spot.json` within the repository.

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


