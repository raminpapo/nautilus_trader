# Documentation: `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_best_effort_canceled.json`
**Generated:** 2025-11-15T19:40:08.250514Z
**File Size:** 1130 bytes
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

- **Path:** `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_best_effort_canceled.json`
- **Size:** 1,130 bytes
- **Lines:** 33
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "94b32a3c-29a1-454b-850f-b37edc5bf73f",
    "contents": {
        "blockHeight": "18847075",
        "orders": [
            {
                "clientId": "1560051747",
                "clientMetadata": "1",
                "clobPairId": "1",
                "goodTilBlock": "18847084",
                "id": "1a28b05a-eb97-5945-a786-12ba7320eb30",
                "orderFlags": "0",
                "postOnly": false,
                "price": "2519.4",
                "reduceOnly": true,
                "removalReason": "ORDER_REMOVAL_REASON_REDUCE_ONLY_RESIZE",
                "side": "SELL",
                "size": "0.003",
                "status": "BEST_EFFORT_CANCELED",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "ticker": "ETH-USD",
                "timeInForce": "IOC",
                "totalOptimisticFilled": "0.003",
                "type": "LIMIT"
            }
        ]
    },
    "id": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5/0",
    "message_id": 5,
    "type": "channel_data",
    "version": "3.0.0"
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_best_effort_canceled.json` within the repository.

This is a configuration file.


---

## Detailed Analysis

*No structured code elements detected in this file.*


---

## Usage Examples

*Usage examples are specific to the file type and context.*


---

## Related Files

**Directory:** `tests/test_data/dydx/websocket`

See [folder index](./index.md) for related files.


---

## Notes

**Testing:** This appears to be a test file. Ensure it's run as part of the test suite.


