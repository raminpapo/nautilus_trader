# Documentation: v4_markets_oracle_price.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_markets_oracle_price.json`
- **Size**: 452 bytes
- **Lines**: 18
- **Language**: JSON

## Original Source

```json
{
    "channel": "v4_markets",
    "connection_id": "2805e661-5377-4fe7-8457-7b9dc45bfd92",
    "contents": {
        "oraclePrices": {
            "FTM-USD": {
                "effectiveAt": "2024-08-17T17:50:25.837Z",
                "effectiveAtHeight": "19183704",
                "marketId": 82,
                "oraclePrice": "0.3866273177"
            }
        }
    },
    "message_id": 7,
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


**Identifiers**: `FTM`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_markets_oracle_price.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.510605Z*
