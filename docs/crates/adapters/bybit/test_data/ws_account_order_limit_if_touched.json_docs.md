# Documentation: `crates/adapters/bybit/test_data/ws_account_order_limit_if_touched.json`
**Generated:** 2025-11-15T19:40:00.717913Z
**File Size:** 1352 bytes
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

- **Path:** `crates/adapters/bybit/test_data/ws_account_order_limit_if_touched.json`
- **Size:** 1,352 bytes
- **Lines:** 52
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd93",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "BTCUSDT",
      "orderId": "test-lit-001",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "UNKNOWN",
      "price": "55500.00",
      "qty": "0.100",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Untriggered",
      "orderLinkId": "test-client-lit-001",
      "lastPriceOnCreated": "50000.00",
      "reduceOnly": false,
      "leavesQty": "0.100",
      "leavesValue": "5550.00",
      "cumExecQty": "0",
      "cumExecValue": "0",
      "avgPrice": "",
      "blockTradeId": "",
      "positionIdx": 0,
      "cumExecFee": "0",
      "createdTime": "1672364262444",
      "updatedTime": "1672364262457",
      "rejectReason": "",
      "stopOrderType": "Stop",
      "tpslMode": "",
      "triggerPrice": "55000.00",
      "takeProfit": "",
      "stopLoss": "",
      "tpTriggerBy": "",
      "slTriggerBy": "",
      "tpLimitPrice": "",
      "slLimitPrice": "",
      "triggerDirection": 2,
      "triggerBy": "LastPrice",
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

This file is located at `crates/adapters/bybit/test_data/ws_account_order_limit_if_touched.json` within the repository.

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


