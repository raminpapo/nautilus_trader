# Documentation: `crates/adapters/bybit/test_data/ws_account_order.json`
**Generated:** 2025-11-15T19:40:00.715103Z
**File Size:** 1351 bytes
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

- **Path:** `crates/adapters/bybit/test_data/ws_account_order.json`
- **Size:** 1,351 bytes
- **Lines:** 52
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "topic": "order",
  "id": "9b8d7cf0-1234-4567-8abc-00d0beef0001",
  "creationTime": 1700000007000,
  "data": [
    {
      "category": "linear",
      "symbol": "BTCUSDT",
      "orderId": "abcdef123456",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "CancelByUser",
      "price": "30000",
      "qty": "0.010",
      "orderIv": "0",
      "timeInForce": "GTC",
      "orderStatus": "Cancelled",
      "orderLinkId": "client-1",
      "lastPriceOnCreated": "0",
      "reduceOnly": false,
      "leavesQty": "0.010",
      "leavesValue": "300",
      "cumExecQty": "0",
      "cumExecValue": "0",
      "avgPrice": "0",
      "blockTradeId": "0",
      "positionIdx": 0,
      "cumExecFee": "0",
      "createdTime": "1700000000000",
      "updatedTime": "1700000005000",
      "rejectReason": "",
      "triggerPrice": "0",
      "takeProfit": "0",
      "stopLoss": "0",
      "tpTriggerBy": "MarkPrice",
      "slTriggerBy": "LastPrice",
      "tpLimitPrice": "0",
      "slLimitPrice": "0",
      "closeOnTrigger": false,
      "placeType": "order",
      "smpType": "None",
      "smpGroup": 0,
      "smpOrderId": "0",
      "feeCurrency": "USDT",
      "triggerBy": "MarkPrice",
      "stopOrderType": "StopLoss",
      "triggerDirection": 0,
      "tpslMode": "Full",
      "createType": "CreateByUser"
    }
  ]
}
```


---

## Overview

This file is located at `crates/adapters/bybit/test_data/ws_account_order.json` within the repository.

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


