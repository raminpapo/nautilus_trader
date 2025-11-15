# Documentation: `crates/adapters/bitmex/test_data/http_get_orders.json`
**Generated:** 2025-11-15T19:40:00.403989Z
**File Size:** 2214 bytes
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

- **Path:** `crates/adapters/bitmex/test_data/http_get_orders.json`
- **Size:** 2,214 bytes
- **Lines:** 72
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
[
    {
        "orderID": "550e8400-e29b-41d4-a716-446655440001",
        "clOrdID": "mm_bitmex_1a/oemUeQ4CAJZgP3fjHsA",
        "clOrdLinkID": null,
        "account": 1234567,
        "symbol": "XBTUSD",
        "side": "Buy",
        "simpleOrderQty": null,
        "orderQty": 100,
        "price": 98000,
        "displayQty": null,
        "stopPx": null,
        "pegOffsetValue": null,
        "pegPriceType": null,
        "currency": "USD",
        "settlCurrency": "XBt",
        "ordType": "Limit",
        "timeInForce": "GoodTillCancel",
        "execInst": null,
        "contingencyType": null,
        "exDestination": "XBME",
        "ordStatus": "New",
        "triggered": null,
        "workingIndicator": true,
        "ordRejReason": null,
        "simpleLeavesQty": null,
        "leavesQty": 100,
        "simpleCumQty": null,
        "cumQty": 0,
        "avgPx": null,
        "multiLegReportingType": "SingleSecurity",
        "text": "Submitted via API.",
        "transactTime": "2024-11-25T10:30:00.000Z",
        "timestamp": "2024-11-25T10:30:00.123Z"
    },
    {
        "orderID": "550e8400-e29b-41d4-a716-446655440002",
        "clOrdID": "mm_bitmex_2b/oemUeQ4CAJZgP3fjHsB",
        "clOrdLinkID": null,
        "account": 1234567,
        "symbol": "XBTUSD",
        "side": "Sell",
        "simpleOrderQty": null,
        "orderQty": 200,
        "price": 99000,
        "displayQty": null,
        "stopPx": null,
        "pegOffsetValue": null,
        "pegPriceType": null,
        "currency": "USD",
        "settlCurrency": "XBt",
        "ordType": "Limit",
        "timeInForce": "GoodTillCancel",
        "execInst": "ParticipateDoNotInitiate",
        "contingencyType": null,
        "exDestination": "XBME",
        "ordStatus": "Filled",
        "triggered": null,
        "workingIndicator": false,
        "ordRejReason": null,
        "simpleLeavesQty": null,
        "leavesQty": 0,
        "simpleCumQty": null,
        "cumQty": 200,
        "avgPx": 98950.5,
        "multiLegReportingType": "SingleSecurity",
        "text": "Submitted via API.",
        "transactTime": "2024-11-25T10:25:00.000Z",
        "timestamp": "2024-11-25T10:35:00.456Z"
    }
]
```


---

## Overview

This file is located at `crates/adapters/bitmex/test_data/http_get_orders.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `crates/adapters/bitmex/test_data`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


