# Documentation: v4_accounts_channel_data_transfers.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_accounts_channel_data_transfers.json`
- **Size**: 874 bytes
- **Lines**: 27
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_subaccounts",
    "connection_id": "c941e384-e3ac-48a9-8420-a5c39eede3ae",
    "contents": {
        "blockHeight": "19079256",
        "transfers": {
            "createdAt": "2024-08-16T08:43:22.999Z",
            "createdAtHeight": "19079256",
            "recipient": {
                "address": "dydx14zzueazeh0hj67cghhf9jypslcf9sh2n5k6art"
            },
            "sender": {
                "address": "dydx14zzueazeh0hj67cghhf9jypslcf9sh2n5k6art",
                "subaccountNumber": 0
            },
            "size": "10",
            "symbol": "USDC",
            "transactionHash": "C0A42DABFC98F8B51D0F092A9B8EB48BA189B3B77128D8A453FCD69D4365BD9C",
            "type": "WITHDRAWAL"
        }
    },
    "id": "dydx14zzueazeh0hj67cghhf9jypslcf9sh2n5k6art/0",
    "message_id": 135,
    "type": "channel_data",
    "version": "3.0.0"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `C0A42DABFC98F8B51D0F092A9B8EB48BA189B3B77128D8A453FCD69D4365BD9C`, `USDC`, `WITHDRAWAL`

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
pytest tests/test_data/dydx/websocket/v4_accounts_channel_data_transfers.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.460002Z*
