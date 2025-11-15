# Documentation: `tests/test_data/dydx/websocket/v4_accounts_fills.json`
**Generated:** 2025-11-15T19:40:08.256107Z
**File Size:** 3676 bytes
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

- **Path:** `tests/test_data/dydx/websocket/v4_accounts_fills.json`
- **Size:** 3,676 bytes
- **Lines:** 96
- **Extension:** `.json`
- **Type:** text

---

## Source Code

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "61fefb6d-60e7-44cf-9604-375c133eb25a",
    "contents": {
        "blockHeight": "18794557",
        "fills": [
            {
                "clientMetadata": "1",
                "clobPairId": "1",
                "createdAt": "2024-08-12T14:06:01.172Z",
                "createdAtHeight": "18794557",
                "eventId": "011ec83d000000020000000b",
                "fee": "0.001311",
                "id": "aec07db3-d668-5b77-8508-0f50a28bb303",
                "liquidity": "TAKER",
                "orderId": "70dbcf99-214e-54f5-9ddd-3c5e1a46b95e",
                "price": "2620.1",
                "quoteAmount": "2.6201",
                "side": "BUY",
                "size": "0.001",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "ticker": "ETH-USD",
                "transactionHash": "D1A40972B706E85EEADC0A2B299F8DE975907D93CA4A0D4810DC54FC7E6B4B69",
                "type": "LIMIT"
            },
            {
                "clientMetadata": "1",
                "clobPairId": "1",
                "createdAt": "2024-08-12T14:06:01.172Z",
                "createdAtHeight": "18794557",
                "eventId": "011ec83d000000020000000e",
                "fee": "0.001313",
                "id": "d013c6fe-4c2e-5e40-86ca-26067d061ad1",
                "liquidity": "TAKER",
                "orderId": "70dbcf99-214e-54f5-9ddd-3c5e1a46b95e",
                "price": "2624.7",
                "quoteAmount": "2.6247",
                "side": "BUY",
                "size": "0.001",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "ticker": "ETH-USD",
                "transactionHash": "D1A40972B706E85EEADC0A2B299F8DE975907D93CA4A0D4810DC54FC7E6B4B69",
                "type": "LIMIT"
            }
        ],
        "orders": [
            {
                "clientId": "1497046405",
                "clientMetadata": "1",
                "clobPairId": "1",
                "createdAtHeight": "18794557",
                "goodTilBlock": "18794564",
                "goodTilBlockTime": null,
                "id": "70dbcf99-214e-54f5-9ddd-3c5e1a46b95e",
                "orderFlags": "0",
                "postOnly": false,
                "price": "2752.3",
                "reduceOnly": false,
                "side": "BUY",
                "size": "0.002",
                "status": "FILLED",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "ticker": "ETH-USD",
                "timeInForce": "IOC",
                "totalFilled": "0.002",
                "triggerPrice": null,
                "type": "LIMIT",
                "updatedAt": "2024-08-12T14:06:01.172Z",
                "updatedAtHeight": "18794557"
            }
        ],
        "perpetualPositions": [
            {
                "address": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5",
                "entryPrice": "2955.62",
                "exitPrice": null,
                "market": "ETH-USD",
                "maxSize": "0.005",
                "netFunding": "0",
                "positionId": "389cf77f-5faa-53f2-8a76-b06685d63eb0",
                "realizedPnl": "0",
                "side": "LONG",
                "size": "0.005",
                "status": "OPEN",
                "subaccountNumber": 0,
                "sumClose": "0",
                "sumOpen": "0.005",
                "unrealizedPnl": "-1.683806695"
            }
        ]
    },
    "id": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5/0",
    "message_id": 6,
    "type": "channel_data",
    "version": "3.0.0"
}
```


---

## Overview

This file is located at `tests/test_data/dydx/websocket/v4_accounts_fills.json` within the repository.

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


