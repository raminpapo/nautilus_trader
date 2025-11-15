# Documentation: `crates/adapters/okx/test_data/ws_orders_trigger.json`
**Generated:** 2025-11-15T19:40:01.405629Z
**File Size:** 1378 bytes
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

- **Path:** `crates/adapters/okx/test_data/ws_orders_trigger.json`
- **Size:** 1,378 bytes
- **Lines:** 60
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
  "arg": {
    "channel": "orders",
    "instType": "SWAP"
  },
  "data": [
    {
      "accFillSz": "0.01",
      "avgPx": "101950.0",
      "cTime": "1737400200000",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "normal",
      "ccy": "USDT",
      "clOrdId": "706620792746729474_0",
      "execType": "T",
      "fee": "-0.020390",
      "feeCcy": "USDT",
      "fillPx": "101950.0",
      "fillSz": "0.01",
      "fillTime": "1737400200100",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "isTpLimit": "false",
      "lever": "2.0",
      "linkedAlgoOrd": {
        "algoId": "706620792746729474"
      },
      "ordId": "706620792746729999",
      "ordType": "trigger",
      "pnl": "10.5",
      "posSide": "long",
      "px": "",
      "pxType": "",
      "pxUsd": "",
      "pxVol": "",
      "quickMgnType": "",
      "rebate": "0",
      "rebateCcy": "USDT",
      "reduceOnly": "true",
      "side": "sell",
      "slOrdPx": "",
      "slTriggerPx": "",
      "slTriggerPxType": "",
      "source": "algo",
      "state": "filled",
      "stpId": "",
      "stpMode": "cancel_maker",
      "sz": "0.01",
      "tag": "",
      "tdMode": "isolated",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905530",
      "uTime": "1737400200100"
    }
  ]
}
```


---

## Overview

This file is located at `crates/adapters/okx/test_data/ws_orders_trigger.json` within the repository.

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


