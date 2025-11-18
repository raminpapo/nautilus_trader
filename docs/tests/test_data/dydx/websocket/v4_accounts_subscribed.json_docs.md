# Documentation: v4_accounts_subscribed.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_subscribed.json`
- **Size**: 1,863 bytes
- **Lines**: 55
- **Language**: JSON

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 8


**Identifiers**: `BUY`, `ETH`, `IOC`, `LIMIT`, `LONG`, `OPEN`, `USD`, `USDC`

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
pytest tests/test_data/dydx/websocket/v4_accounts_subscribed.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.463478Z*
