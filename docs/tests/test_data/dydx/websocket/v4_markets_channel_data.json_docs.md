# Documentation: v4_markets_channel_data.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_markets_channel_data.json`
- **Size**: 456 bytes
- **Lines**: 18
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_markets",
    "connection_id": "36c85c46-69e8-4c1b-85e5-7412a54354a7",
    "contents": {
        "oraclePrices": {
            "JASMY-USD": {
                "effectiveAt": "2024-08-17T17:24:36.330Z",
                "effectiveAtHeight": "19182358",
                "marketId": 87,
                "oraclePrice": "0.02069413882"
            }
        }
    },
    "message_id": 11,
    "type": "channel_data",
    "version": "1.0.0"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `JASMY`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_markets_channel_data.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.507175Z*
