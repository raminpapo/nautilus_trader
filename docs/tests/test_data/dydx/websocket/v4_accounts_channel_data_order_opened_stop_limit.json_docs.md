# Documentation: v4_accounts_channel_data_order_opened_stop_limit.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_opened_stop_limit.json`
- **Size**: 1,049 bytes
- **Lines**: 33
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "820fbfcd-6994-42c0-bb13-253d51d8a414",
    "contents": {
        "blockHeight": "18846067",
        "orders": [
            {
                "clientId": "1885399800",
                "clientMetadata": "1",
                "clobPairId": "1",
                "goodTilBlock": "18846077",
                "id": "09a4bd71-66b5-5eb6-886f-8c91b0e6d7bf",
                "orderFlags": "0",
                "postOnly": false,
                "price": "2791.6",
                "reduceOnly": false,
                "side": "BUY",
                "size": "0.002",
                "status": "BEST_EFFORT_OPENED",
                "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
                "ticker": "ETH-USD",
                "timeInForce": "IOC",
                "triggerPrice": "2791.9",
                "type": "STOP_LIMIT"
            }
        ]
    },
    "id": "dydx1kzsvkf2ghjqlysuffdkhcdctknl4rsvcx5hkm5/0",
    "message_id": 2,
    "type": "channel_data",
    "version": "3.0.0"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `BEST_EFFORT_OPENED`, `BUY`, `ETH`, `IOC`, `STOP_LIMIT`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data_order_opened_stop_limit.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.458746Z*
