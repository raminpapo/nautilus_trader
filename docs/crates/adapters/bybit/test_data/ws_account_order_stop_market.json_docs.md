# Documentation: `crates/adapters/bybit/test_data/ws_account_order_stop_market.json`
**Generated:** 2025-11-15T19:40:00.722661Z
**File Size:** 1362 bytes
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

- **Path:** `crates/adapters/bybit/test_data/ws_account_order_stop_market.json`
- **Size:** 1,362 bytes
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
      "orderId": "test-stop-market-001",
      "side": "Sell",
      "orderType": "Market",
      "cancelType": "UNKNOWN",
      "price": "",
      "qty": "0.100",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Untriggered",
      "orderLinkId": "test-client-stop-market-001",
      "lastPriceOnCreated": "50000.00",
      "reduceOnly": false,
      "leavesQty": "0.100",
      "leavesValue": "5000.00",
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
      "triggerPrice": "45000.00",
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

This file is located at `crates/adapters/bybit/test_data/ws_account_order_stop_market.json` within the repository.

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


