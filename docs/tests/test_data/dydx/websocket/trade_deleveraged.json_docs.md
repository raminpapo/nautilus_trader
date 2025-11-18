# Documentation: trade_deleveraged.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/trade_deleveraged.json`
- **Size**: 1,070 bytes
- **Lines**: 37
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_trades",
    "connection_id": "796abe49-c178-417e-b3d1-7da7de91b931",
    "contents": {
        "trades": [
            {
                "createdAt": "2024-08-05T01:09:28.338Z",
                "id": "015034b9000000020000000e",
                "price": "2322.8",
                "side": "BUY",
                "size": "4.303",
                "type": "LIMIT"
            },
            {
                "createdAt": "2024-08-05T01:09:28.338Z",
                "id": "015034b90000000200000011",
                "price": "2322.8",
                "side": "BUY",
                "size": "4.303",
                "type": "LIMIT"
            },
            {
                "createdAt": "2024-08-05T01:09:28.338Z",
                "id": "015034b90000000200000026",
                "price": "2340.7442700369913687",
                "side": "SELL",
                "size": "0.811",
                "type": "DELEVERAGED"
            }
        ]
    },
    "id": "ETH-USD",
    "message_id": 14299286,
    "type": "channel_data",
    "version": "2.1.0"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `BUY`, `DELEVERAGED`, `ETH`, `LIMIT`, `SELL`, `USD`

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
pytest tests/test_data/dydx/websocket/trade_deleveraged.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.444954Z*
