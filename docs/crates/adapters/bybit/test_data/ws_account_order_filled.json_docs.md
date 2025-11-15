# Documentation: `crates/adapters/bybit/test_data/ws_account_order_filled.json`
**Generated:** 2025-11-15T19:40:00.716951Z
**File Size:** 1428 bytes
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

- **Path:** `crates/adapters/bybit/test_data/ws_account_order_filled.json`
- **Size:** 1,428 bytes
- **Lines:** 52
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd90",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderId": "5cf98598-39a7-459e-97bf-76ca765ee020",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "UNKNOWN",
      "price": "30000.50",
      "qty": "0.100",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Filled",
      "orderLinkId": "test-client-order-001",
      "lastPriceOnCreated": "29950.00",
      "reduceOnly": false,
      "leavesQty": "0",
      "leavesValue": "0",
      "cumExecQty": "0.100",
      "cumExecValue": "3000.05",
      "avgPrice": "30000.50",
      "blockTradeId": "",
      "positionIdx": 0,
      "cumExecFee": "1.650028",
      "createdTime": "1672364262444",
      "updatedTime": "1672364262457",
      "rejectReason": "",
      "stopOrderType": "Stop",
      "tpslMode": "Full",
      "triggerPrice": "29500.00",
      "takeProfit": "31000.00",
      "stopLoss": "29000.00",
      "tpTriggerBy": "MarkPrice",
      "slTriggerBy": "LastPrice",
      "tpLimitPrice": "0",
      "slLimitPrice": "0",
      "triggerDirection": 0,
      "triggerBy": "MarkPrice",
      "closeOnTrigger": false,
      "category": "linear",
      "placeType": "order",
      "smpType": "None",
      "smpGroup": 0,
      "smpOrderId": "",
      "feeCurrency": "USDT",
      "createType": "CreateByUser"
    }
  ]
}
```


---

## Overview

This file is located at `crates/adapters/bybit/test_data/ws_account_order_filled.json` within the repository.

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


