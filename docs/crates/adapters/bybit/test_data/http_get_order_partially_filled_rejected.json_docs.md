# Documentation: `crates/adapters/bybit/test_data/http_get_order_partially_filled_rejected.json`
**Generated:** 2025-11-15T19:40:00.706257Z
**File Size:** 1439 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_order_partially_filled_rejected.json`
- **Size:** 1,439 bytes
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
        "orderId": "5cf98598-39a7-459e-97bf-76ca765ee021",
        "orderLinkId": "O-20251001-164609-APEX-000-49",
        "blockTradeId": null,
        "symbol": "BTCUSDT",
        "price": "30000",
        "qty": "0.010",
        "side": "Buy",
        "isLeverage": "0",
        "positionIdx": 0,
        "orderStatus": "Rejected",
        "cancelType": "UNKNOWN",
        "rejectReason": "INSUFFICIENT_MARGIN",
        "avgPrice": "30000",
        "leavesQty": "0.005",
        "leavesValue": "150",
        "cumExecQty": "0.005",
        "cumExecValue": "150",
        "cumExecFee": "0.0825",
        "timeInForce": "GTC",
        "orderType": "Limit",
        "stopOrderType": "",
        "orderIv": null,
        "triggerPrice": "0",
        "takeProfit": "0",
        "stopLoss": "0",
        "tpTriggerBy": "",
        "slTriggerBy": "",
        "triggerDirection": 0,
        "triggerBy": "",
        "lastPriceOnCreated": "29950",
        "reduceOnly": false,
        "closeOnTrigger": false,
        "smpType": "None",
        "smpGroup": 0,
        "smpOrderId": "0",
        "tpslMode": "Full",
        "tpLimitPrice": "0",
        "slLimitPrice": "0",
        "placeType": "order",
        "createdTime": "1672364262444",
        "updatedTime": "1672364262457"
      }
    ],
    "nextPageCursor": ""
  },
  "retExtInfo": {},
  "time": 1672364262500
}
```


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_order_partially_filled_rejected.json` within the repository.

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


