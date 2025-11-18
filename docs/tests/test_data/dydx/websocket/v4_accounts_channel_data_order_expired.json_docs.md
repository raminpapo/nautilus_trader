# Documentation: v4_accounts_channel_data_order_expired.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data_order_expired.json`
- **Size**: 733 bytes
- **Lines**: 24
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "2454e5fc-fcbb-4e8c-a435-e5f19d5a0180",
    "contents": {
        "blockHeight": "19090305",
        "orders": [
            {
                "clientId": "1964904710",
                "clobPairId": "1",
                "id": "5a1c10aa-66bb-5cf2-a106-32d6470eb43e",
                "orderFlags": "0",
                "removalReason": "ORDER_REMOVAL_REASON_EXPIRED",
                "status": "CANCELED",
                "subaccountId": "8586bcf6-1f58-5ec9-a0bc-e53db273e7b0",
                "ticker": "ETH-USD"
            }
        ]
    },
    "id": "dydx14zzueazeh0hj67cghhf9jypslcf9sh2n5k6art/0",
    "message_id": 50,
    "type": "channel_data",
    "version": "3.0.0"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `CANCELED`, `ETH`, `ORDER_REMOVAL_REASON_EXPIRED`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data_order_expired.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.456374Z*
