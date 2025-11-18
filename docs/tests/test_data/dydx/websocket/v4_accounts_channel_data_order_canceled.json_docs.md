# Documentation: v4_accounts_channel_data_order_canceled.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_canceled.json`
- **Size**: 1,271 bytes
- **Lines**: 37
- **Language**: JSON

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `BUY`, `CANCELED`, `ETH`, `GTT`, `LIMIT`, `ORDER_REMOVAL_REASON_USER_CANCELED`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data_order_canceled.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.455251Z*
