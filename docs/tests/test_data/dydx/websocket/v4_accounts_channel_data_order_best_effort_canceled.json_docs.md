# Documentation: v4_accounts_channel_data_order_best_effort_canceled.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_best_effort_canceled.json`
- **Size**: 1,130 bytes
- **Lines**: 34
- **Language**: JSON

## Original Source

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

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 7


**Identifiers**: `BEST_EFFORT_CANCELED`, `ETH`, `IOC`, `LIMIT`, `ORDER_REMOVAL_REASON_REDUCE_ONLY_RESIZE`, `SELL`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data_order_best_effort_canceled.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.453800Z*
