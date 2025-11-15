# Documentation: `crates/adapters/okx/test_data/ws_orders_liquidation.json`
**Generated:** 2025-11-15T19:40:01.404676Z
**File Size:** 1445 bytes
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

- **Path:** `crates/adapters/okx/test_data/ws_orders_liquidation.json`
- **Size:** 1,445 bytes
- **Lines:** 64
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
      "accFillSz": "0.5",
      "algoClOrdId": "",
      "algoId": "",
      "attachAlgoClOrdId": "",
      "attachAlgoOrds": [],
      "avgPx": "40000.0",
      "cTime": "1746947317401",
      "cancelSource": "",
      "cancelSourceReason": "",
      "category": "full_liquidation",
      "ccy": "USDT",
      "clOrdId": "",
      "execType": "T",
      "fee": "-20.0",
      "feeCcy": "USDT",
      "fillPx": "40000.0",
      "fillSz": "0.5",
      "fillTime": "1746947317402",
      "instId": "BTC-USDT-SWAP",
      "instType": "SWAP",
      "isTpLimit": "false",
      "lever": "10.0",
      "linkedAlgoOrd": {
        "algoId": ""
      },
      "ordId": "2497956918703120999",
      "ordType": "market",
      "pnl": "-5000",
      "posSide": "long",
      "px": "",
      "pxType": "",
      "pxUsd": "",
      "pxVol": "",
      "quickMgnType": "",
      "rebate": "0",
      "rebateCcy": "USDT",
      "reduceOnly": "false",
      "side": "sell",
      "slOrdPx": "",
      "slTriggerPx": "",
      "slTriggerPxType": "",
      "source": "",
      "state": "filled",
      "stpId": "",
      "stpMode": "cancel_maker",
      "sz": "0.5",
      "tag": "",
      "tdMode": "isolated",
      "tgtCcy": "",
      "tpOrdPx": "",
      "tpTriggerPx": "",
      "tpTriggerPxType": "",
      "tradeId": "1518905999",
      "uTime": "1746947317402"
    }
  ]
}
```


---

## Overview

This file is located at `crates/adapters/okx/test_data/ws_orders_liquidation.json` within the repository.

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


