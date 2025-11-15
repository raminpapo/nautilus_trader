# Documentation: `tests/test_data/dydx/websocket/v4_accounts_subscribed.json`
**Generated:** 2025-11-15T19:40:08.258077Z
**File Size:** 1863 bytes
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

- **Path:** `tests/test_data/dydx/websocket/v4_accounts_subscribed.json`
- **Size:** 1,863 bytes
- **Lines:** 54
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "3c285b7e-04b6-491f-9a70-458fb04edad2",
    "contents": {
        "blockHeight": "22079023",
        "orders": [
            {
                "clientId": "2043599281",
                "clientMetadata": "1",
                "clobPairId": "1",
                "createdAtHeight": "17933806",
                "goodTilBlock": "17933813",
                "id": "05009670-3fba-5ec7-8447-efb81a03cd9f",
                "orderFlags": "0",
                "postOnly": false,
                "price": "3335.3",
                "reduceOnly": false,
                "side": "BUY",
                "size": "0.003",
                "status": "OPEN",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "subaccountNumber": 0,
                "ticker": "ETH-USD",
                "timeInForce": "IOC",
                "totalFilled": "0.003",
                "type": "LIMIT",
                "updatedAt": "2024-08-01T07:09:25.767Z",
                "updatedAtHeight": "17933806"
            }
        ],
        "subaccount": {
            "address": "dydx1m5kup0427wptegfek4kygtu0av5wm76a034q",
            "assetPositions": {
                "USDC": {
                    "assetId": "0",
                    "side": "LONG",
                    "size": "11.623325",
                    "subaccountNumber": 0,
                    "symbol": "USDC"
                }
            },
            "equity": "11.623325",
            "freeCollateral": "11.623325",
            "latestProcessedBlockHeight": "22079024",
            "marginEnabled": true,
            "openPerpetualPositions": {},
            "subaccountNumber": 0,
            "updatedAtHeight": "21716452"
        }
    },
    "id": "dydx1m5kup0427wptegfed9k4kygtu0avm76a034q/0",
    "message_id": 1,
    "type": "subscribed"
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/v4_accounts_subscribed.json` within the repository.

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


