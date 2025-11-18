# Documentation: v4_accounts_channel_data.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data.json`
- **Size**: 2,048 bytes
- **Lines**: 64
- **Language**: JSON

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 9


**Identifiers**: `BUY`, `Buffer`, `C84B0BBCA8E713A2D46EFBA07F2D0A32C1F6E2440794A366B888503935E0EF40`, `ETH`, `FILLED`, `IOC`, `LIMIT`, `TAKER`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.449317Z*
