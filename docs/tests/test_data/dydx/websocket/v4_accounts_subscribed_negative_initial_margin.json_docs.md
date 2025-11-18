# Documentation: v4_accounts_subscribed_negative_initial_margin.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_subscribed_negative_initial_margin.json`
- **Size**: 7,078 bytes
- **Lines**: 184
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "fb3dc232-802e-4447-b30c-13d333493f6e",
    "contents": {
        "blockHeight": "19083216",
        "orders": [
            {
                "clientId": "123",
                "clientMetadata": "0",
                "clobPairId": "1",
                "createdAtHeight": "18260746",
                "goodTilBlock": "18260746",
                "id": "ae9e64e1-1cb4-5ad2-baaa-d51773562a84",
                "orderFlags": "0",
                "postOnly": false,
                "price": "90000",
                "reduceOnly": false,
                "side": "BUY",
                "size": "0.01",
                "status": "BEST_EFFORT_CANCELED",
                "subaccountId": "8586bcf6-1f58-5ec9-a0bc-e53db273e7b0",
                "subaccountNumber": 0,
                "ticker": "ETH-USD",
                "timeInForce": "IOC",
                "totalFilled": "0.01",
                "type": "LIMIT",
                "updatedAt": "2024-08-05T12:12:40.696Z",
                "updatedAtHeight": "18260746"
            },
            {
                "clientId": "0",
                "clientMetadata": "0",
                "clobPairId": "0",
                "createdAtHeight": "13489890",
                "goodTilBlock": "17276346",
                "id": "a5eb3913-6c2d-5c35-8cfe-708aeb3e6ae5",
                "orderFlags": "0",
                "postOnly": false,
                "price": "3509",
                "reduceOnly": false,
                "side": "SELL",
                "size": "97700000",
                "status": "BEST_EFFORT_CANCELED",
                "subaccountId": "8586bcf6-1f58-5ec9-a0bc-e53db273e7b0",
                "subaccountNumber": 0,
                "ticker": "BTC-USD",
                "timeInForce": "IOC",
                "totalFilled": "0.0394",
                "type": "LIMIT",
                "updatedAt": "2024-07-23T11:41:10.601Z",
                "updatedAtHeight": "17276337"
            },
            {
                "clientId": "2050958613",
                "clientMetadata": "0",
                "clobPairId": "1",
                "createdAtHeight": "1143797",
                "goodTilBlock": "1143806",
                "id": "02e7c5bb-75dc-5327-91be-cc6aadced911",
                "orderFlags": "0",
                "postOnly": false,
                "price": "1850",
                "reduceOnly": false,
                "side": "SELL",
                "size": "0.01",
                "status": "BEST_EFFORT_CANCELED",
                "subaccountId": "8586bcf6-1f58-5ec9-a0bc-e53db273e7b0",
                "subaccountNumber": 0,
                "ticker": "ETH-USD",
                "timeInForce": "GTT",
                "totalFilled": "0.01",
                "type": "LIMIT",
                "updatedAt": "2023-11-05T18:31:55.836Z",
                "updatedAtHeight": "1143797"
            },
            {
                "clientId": "1780278110",
                "clientMetadata": "0",
                "clobPairId": "1",
                "createdAtHeight": "1143792",
                "goodTilBlock": "1143801",
                "id": "0123a72b-54c9-564b-b833-86b676747def",
                "orderFlags": "0",
                "postOnly": false,
                "price": "1850",
                "reduceOnly": false,
                "side": "SELL",
                "size": "0.01",
                "status": "BEST_EFFORT_CANCELED",
                "subaccountId": "8586bcf6-1f58-5ec9-a0bc-e53db273e7b0",
                "subaccountNumber": 0,
                "ticker": "ETH-USD",
                "timeInForce": "GTT",
                "totalFilled": "0.01",
                "type": "LIMIT",
                "updatedAt": "2023-11-05T18:31:48.972Z",
                "updatedAtHeight": "1143792"
            },
            {
                "clientId": "147339483",
                "clientMetadata": "0",
                "clobPairId": "0",
                "createdAtHeight": "951762",
                "goodTilBlock": "951763",
                "id": "d459eead-79a4-5133-88ec-7b5762dedbd4",
                "orderFlags": "0",
                "postOnly": false,
                "price": "10000",
                "reduceOnly": false,
                "side": "SELL",
                "size": "0.1",
                "status": "BEST_EFFORT_CANCELED",
                "subaccountId": "8586bcf6-1f58-5ec9-a0bc-e53db273e7b0",
                "subaccountNumber": 0,
                "ticker": "BTC-USD",
                "timeInForce": "GTT",
                "totalFilled": "0.0248",
                "type": "LIMIT",
                "updatedAt": "2023-11-02T16:38:54.575Z",
                "updatedAtHeight": "951763"
            }
        ],
        "subaccount": {
            "address": "dydx14zzueazeh0hj67cghhf9jypslcf9sh2n5k6art",
            "assetPositions": {
                "USDC": {
                    "assetId": "0",
                    "side": "SHORT",
                    "size": "5768.816478",
                    "subaccountNumber": 0,
                    "symbol": "USDC"
                }
            },
            "equity": "304.384048054",
            "freeCollateral": "0.1986661447",
            "latestProcessedBlockHeight": "19083216",
            "marginEnabled": true,
            "openPerpetualPositions": {
                "BTC-USD": {
                    "closedAt": null,
                    "createdAt": "2024-08-05T12:12:10.337Z",
                    "createdAtHeight": "18260718",
                    "entryPrice": "58308.13962472406181015453",
                    "exitPrice": "56755.1978021978021978022",
                    "market": "BTC-USD",
                    "maxSize": "0.3102",
                    "netFunding": "0",
                    "realizedPnl": "-367.426035209713024282561278",
                    "side": "LONG",
                    "size": "0.1036",
                    "status": "OPEN",
                    "subaccountNumber": 0,
                    "sumClose": "0.2366",
                    "sumOpen": "0.3624",
                    "unrealizedPnl": "37.730816998587196467990692"
                },
                "ETH-USD": {
                    "closedAt": null,
                    "createdAt": "2024-08-16T09:28:08.307Z",
                    "createdAtHeight": "19081558",
                    "entryPrice": "2618.8",
                    "exitPrice": null,
                    "market": "ETH-USD",
                    "maxSize": "-0.001",
                    "netFunding": "0",
                    "realizedPnl": "0",
                    "side": "SHORT",
                    "size": "-0.002",
                    "status": "OPEN",
                    "subaccountNumber": 0,
                    "sumClose": "0",
                    "sumOpen": "0.002",
                    "unrealizedPnl": "-0.015956066"
                }
            },
            "subaccountNumber": 0,
            "updatedAtHeight": "19083216"
        }
    },
    "id": "dydx14zzueazeh0hj67cghhf9jypslcf9sh2n5k6art/0",
    "message_id": 1,
    "type": "subscribed"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 13


**Identifiers**: `BEST_EFFORT_CANCELED`, `BTC`, `BUY`, `ETH`, `GTT`, `IOC`, `LIMIT`, `LONG`, `OPEN`, `SELL`, `SHORT`, `USD`, `USDC`

## Related Files

This file is located in `tests/test_data/dydx/websocket/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/websocket/v4_accounts_subscribed_negative_initial_margin.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.466204Z*
