# Documentation: `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_canceled.json`
**Generated:** 2025-11-15T19:40:08.251407Z
**File Size:** 1271 bytes
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

- **Path:** `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_canceled.json`
- **Size:** 1,271 bytes
- **Lines:** 36
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "643c68a7-d84c-4929-97c2-23f471931825",
    "contents": {
        "blockHeight": "18786404",
        "orders": [
            {
                "clientId": "1053905556",
                "clientMetadata": "0",
                "clobPairId": "1",
                "createdAtHeight": "18786007",
                "goodTilBlockTime": "2024-09-09T11:19:22.000Z",
                "id": "e628b62f-2623-5192-a22f-d9ce042bd5be",
                "orderFlags": "64",
                "postOnly": false,
                "price": "2666.4",
                "reduceOnly": false,
                "removalReason": "ORDER_REMOVAL_REASON_USER_CANCELED",
                "side": "BUY",
                "size": "0.001",
                "status": "CANCELED",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "ticker": "ETH-USD",
                "timeInForce": "GTT",
                "totalFilled": "0",
                "type": "LIMIT",
                "updatedAt": "2024-08-12T11:27:02.651Z",
                "updatedAtHeight": "18786405"
            }
        ]
    },
    "id": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5/0",
    "message_id": 3,
    "type": "channel_data",
    "version": "3.0.0"
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_canceled.json` within the repository.

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


