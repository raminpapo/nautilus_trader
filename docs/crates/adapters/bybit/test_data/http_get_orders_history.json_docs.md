# Documentation: `crates/adapters/bybit/test_data/http_get_orders_history.json`
**Generated:** 2025-11-15T19:40:00.707266Z
**File Size:** 1398 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_orders_history.json`
- **Size:** 1,398 bytes
- **Lines:** 54
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "list": [
      {
        "orderId": "abcdef123456",
        "orderLinkId": "client-1",
        "blockTradeId": null,
        "symbol": "BTCUSDT",
        "price": "30000",
        "qty": "0.010",
        "side": "Buy",
        "isLeverage": "1",
        "positionIdx": 0,
        "orderStatus": "Cancelled",
        "cancelType": "CancelByUser",
        "rejectReason": "",
        "avgPrice": null,
        "leavesQty": "0.010",
        "leavesValue": "300",
        "cumExecQty": "0",
        "cumExecValue": "0",
        "cumExecFee": "0",
        "timeInForce": "GTC",
        "orderType": "Limit",
        "stopOrderType": "StopLoss",
        "orderIv": null,
        "triggerPrice": "0",
        "takeProfit": "0",
        "stopLoss": "0",
        "tpTriggerBy": "MarkPrice",
        "slTriggerBy": "LastPrice",
        "triggerDirection": 0,
        "triggerBy": "MarkPrice",
        "lastPriceOnCreated": "0",
        "reduceOnly": false,
        "closeOnTrigger": false,
        "smpType": "None",
        "smpGroup": 0,
        "smpOrderId": "0",
        "tpslMode": "Full",
        "tpLimitPrice": "0",
        "slLimitPrice": "0",
        "placeType": "order",
        "createdTime": "1700000000000",
        "updatedTime": "1700000005000"
      }
    ],
    "nextPageCursor": ""
  },
  "retExtInfo": {},
  "time": 1700000006000
}
```


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_orders_history.json` within the repository.

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


