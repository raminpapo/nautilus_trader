# Documentation: `crates/adapters/okx/test_data/ws_orders_algo.json`
**Generated:** 2025-11-15T19:40:01.403649Z
**File Size:** 3513 bytes
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

- **Path:** `crates/adapters/okx/test_data/ws_orders_algo.json`
- **Size:** 3,513 bytes
- **Lines:** 138
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "arg": {
    "channel": "orders-algo",
    "instType": "SWAP"
  },
  "data": [
    {
      "algoId": "706620792746729472",
      "algoClOrdId": "STOP001BTCUSDT20250120",
      "clOrdId": "",
      "ordId": "",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "live",
      "side": "sell",
      "posSide": "long",
      "sz": "0.01",
      "triggerPx": "95000",
      "triggerPxType": "last",
      "ordPx": "-1",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "true",
      "actualPx": "",
      "actualSz": "0",
      "notionalUsd": "950",
      "triggerTime": "",
      "tag": "",
      "cTime": "1737400000000",
      "uTime": "1737400000000"
    },
    {
      "algoId": "706620792746729473",
      "algoClOrdId": "STOP002BTCUSDT20250120",
      "clOrdId": "",
      "ordId": "",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "live",
      "side": "buy",
      "posSide": "short",
      "sz": "0.02",
      "triggerPx": "105000",
      "triggerPxType": "mark",
      "ordPx": "106000",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "false",
      "actualPx": "",
      "actualSz": "0",
      "notionalUsd": "2100",
      "triggerTime": "",
      "tag": "",
      "cTime": "1737400100000",
      "uTime": "1737400100000"
    },
    {
      "algoId": "706620792746729474",
      "algoClOrdId": "STOP003BTCUSDT20250120",
      "clOrdId": "706620792746729474_0",
      "ordId": "706620792746729999",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "order_placed",
      "side": "sell",
      "posSide": "long",
      "sz": "0.01",
      "triggerPx": "102000",
      "triggerPxType": "last",
      "ordPx": "-1",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "true",
      "actualPx": "101950",
      "actualSz": "0.01",
      "notionalUsd": "1020",
      "triggerTime": "1737400200000",
      "tag": "",
      "cTime": "1737400050000",
      "uTime": "1737400200000"
    },
    {
      "algoId": "706620792746729475",
      "algoClOrdId": "STOP004BTCUSDT20250120",
      "clOrdId": "",
      "ordId": "",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "canceled",
      "side": "buy",
      "posSide": "short",
      "sz": "0.015",
      "triggerPx": "98000",
      "triggerPxType": "index",
      "ordPx": "98500",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "false",
      "actualPx": "",
      "actualSz": "0",
      "notionalUsd": "1470",
      "triggerTime": "",
      "tag": "user_cancel",
      "cTime": "1737399900000",
      "uTime": "1737400300000"
    },
    {
      "algoId": "706620792746729476",
      "algoClOrdId": "STOP005BTCUSDT20250120",
      "clOrdId": "706620792746729476_0",
      "ordId": "706620792746730000",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "ordType": "trigger",
      "state": "filled",
      "side": "sell",
      "posSide": "long",
      "sz": "0.005",
      "triggerPx": "103000",
      "triggerPxType": "last",
      "ordPx": "102900",
      "tdMode": "isolated",
      "lever": "2.0",
      "reduceOnly": "true",
      "actualPx": "102920",
      "actualSz": "0.005",
      "notionalUsd": "514.60",
      "triggerTime": "1737400400000",
      "tag": "",
      "cTime": "1737399800000",
      "uTime": "1737400400000"
    }
  ]
}
```


---

## Overview

This file is located at `crates/adapters/okx/test_data/ws_orders_algo.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/okx/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


