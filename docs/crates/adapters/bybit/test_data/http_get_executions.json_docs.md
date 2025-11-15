# Documentation: `crates/adapters/bybit/test_data/http_get_executions.json`
**Generated:** 2025-11-15T19:40:00.699855Z
**File Size:** 2029 bytes
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

- **Path:** `crates/adapters/bybit/test_data/http_get_executions.json`
- **Size:** 2,029 bytes
- **Lines:** 72
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "nextPageCursor": "132766%3A2%2C132766%3A2",
    "category": "linear",
    "list": [
      {
        "symbol": "BTCUSDT",
        "orderId": "8c065341-7b52-4ca9-ac2c-37e31ac55c94",
        "orderLinkId": "test-order-001",
        "side": "Buy",
        "orderPrice": "50000.00",
        "orderQty": "0.100",
        "leavesQty": "0.000",
        "createType": "CreateByUser",
        "orderType": "Limit",
        "stopOrderType": "",
        "execFee": "0.0150",
        "execId": "e0cbe81d-0f18-5866-9415-cf319b5dab3b",
        "execPrice": "50000.00",
        "execQty": "0.100",
        "execType": "Trade",
        "execValue": "5000.00",
        "execTime": "1672282722429",
        "feeCurrency": "USDT",
        "isMaker": true,
        "feeRate": "0.0003",
        "tradeIv": "",
        "markIv": "",
        "markPrice": "50010.50",
        "indexPrice": "50005.25",
        "underlyingPrice": "",
        "blockTradeId": "",
        "closedSize": "0.000",
        "seq": 4688002127
      },
      {
        "symbol": "ETHUSDT",
        "orderId": "7b954230-6a41-3ba8-bc20-26d20ab44b83",
        "orderLinkId": "test-order-002",
        "side": "Sell",
        "orderPrice": "3000.00",
        "orderQty": "1.000",
        "leavesQty": "0.500",
        "createType": "CreateByUser",
        "orderType": "Limit",
        "stopOrderType": "",
        "execFee": "0.9000",
        "execId": "f1dce92e-1g29-6977-a526-dg420c6ecb4c",
        "execPrice": "3000.00",
        "execQty": "0.500",
        "execType": "Trade",
        "execValue": "1500.00",
        "execTime": "1672282822529",
        "feeCurrency": "USDT",
        "isMaker": false,
        "feeRate": "0.0006",
        "tradeIv": "",
        "markIv": "",
        "markPrice": "2998.75",
        "indexPrice": "2999.50",
        "underlyingPrice": "",
        "blockTradeId": "",
        "closedSize": "0.000",
        "seq": 4688002128
      }
    ]
  },
  "retExtInfo": {},
  "time": 1672283754510
}
```


---

## Overview

This file is located at `crates/adapters/bybit/test_data/http_get_executions.json` within the repository.

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


