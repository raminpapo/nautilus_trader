# Documentation: `crates/adapters/bybit/test_data/ws_account_order_partially_filled_rejected.json`
**Generated:** 2025-11-15T19:40:00.719893Z
**File Size:** 1380 bytes
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

- **Path:** `crates/adapters/bybit/test_data/ws_account_order_partially_filled_rejected.json`
- **Size:** 1,380 bytes
- **Lines:** 52
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "id": "5923240c6880ab-c59f-420b-9adb-3639adc9dd91",
  "topic": "order",
  "creationTime": 1672364262474,
  "data": [
    {
      "symbol": "APEXUSDT",
      "orderId": "5cf98598-39a7-459e-97bf-76ca765ee021",
      "side": "Buy",
      "orderType": "Limit",
      "cancelType": "UNKNOWN",
      "price": "1.500",
      "qty": "100.0",
      "orderIv": "",
      "timeInForce": "GTC",
      "orderStatus": "Rejected",
      "orderLinkId": "O-20251001-164609-APEX-000-49",
      "lastPriceOnCreated": "1.485",
      "reduceOnly": false,
      "leavesQty": "50.0",
      "leavesValue": "75.0",
      "cumExecQty": "50.0",
      "cumExecValue": "75.0",
      "avgPrice": "1.500",
      "blockTradeId": "",
      "positionIdx": 0,
      "cumExecFee": "0.0413",
      "createdTime": "1672364262444",
      "updatedTime": "1672364262457",
      "rejectReason": "UNKNOWN",
      "stopOrderType": "",
      "tpslMode": "Full",
      "triggerPrice": "",
      "takeProfit": "",
      "stopLoss": "",
      "tpTriggerBy": "",
      "slTriggerBy": "",
      "tpLimitPrice": "0",
      "slLimitPrice": "0",
      "triggerDirection": 0,
      "triggerBy": "",
      "closeOnTrigger": false,
      "category": "spot",
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

This file is located at `crates/adapters/bybit/test_data/ws_account_order_partially_filled_rejected.json` within the repository.

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


