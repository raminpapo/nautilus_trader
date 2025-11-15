# Documentation: `tests/test_data/dydx/websocket/v4_accounts_channel_data.json`
**Generated:** 2025-11-15T19:40:08.247687Z
**File Size:** 2048 bytes
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

- **Path:** `tests/test_data/dydx/websocket/v4_accounts_channel_data.json`
- **Size:** 2,048 bytes
- **Lines:** 63
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "a00edbe8-095a-4da1-8a9d-ff1f91467258",
    "contents": {
        "fills": [
            {
                "clobPairId": "1",
                "createdAt": "2023-04-04T19:09:24.869Z",
                "createdAtHeight": "61169",
                "eventId": {
                    "data": [
                        0,
                        0,
                        238,
                        241,
                        0,
                        0,
                        0,
                        2,
                        0,
                        0,
                        0,
                        77
                    ],
                    "type": "Buffer"
                },
                "id": "c5030bd3-cd85-5046-8f2a-518bbba6ec45",
                "liquidity": "TAKER",
                "orderId": "64fe30a2-006d-5108-a156-cb0c8443546c",
                "price": "1854.25",
                "quoteAmount": "1854.25",
                "side": "BUY",
                "size": "1",
                "subaccountId": "db535c19-b298-5ee8-bb59-e96c659a8bd4",
                "ticker": "ETH-USD",
                "transactionHash": "C84B0BBCA8E713A2D46EFBA07F2D0A32C1F6E2440794A366B888503935E0EF40",
                "type": "LIMIT"
            }
        ],
        "orders": [
            {
                "goodTilBlock": "61186",
                "goodTilBlockTime": null,
                "id": "64fe30a2-006d-5108-a156-cb0c8443546c",
                "orderFlags": "0",
                "postOnly": false,
                "price": "1948.65",
                "reduceOnly": false,
                "side": "BUY",
                "size": "1",
                "status": "FILLED",
                "ticker": "ETH-USD",
                "timeInForce": "IOC",
                "totalFilled": "1",
                "type": "LIMIT"
            }
        ]
    },
    "id": "dydx1zsw8fczav25uvc8rg3zcv6zy9j7yhnktpq374m/0",
    "message_id": 4,
    "type": "channel_data",
    "version": "2.1.0"
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/v4_accounts_channel_data.json` within the repository.

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


