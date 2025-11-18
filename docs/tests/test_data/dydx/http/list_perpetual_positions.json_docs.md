# Documentation: list_perpetual_positions.json

## File Metadata

- **Path**: `tests/test_data/dydx/http/list_perpetual_positions.json`
- **Size**: 630 bytes
- **Lines**: 23
- **Language**: JSON

## Original Source

```json
{
    "positions": [
        {
            "closedAt": null,
            "createdAt": "2024-08-01T07:09:25.767Z",
            "createdAtHeight": "17933806",
            "entryPrice": "3177.76666666666666666667",
            "exitPrice": null,
            "market": "ETH-USD",
            "maxSize": "0.003",
            "netFunding": "0",
            "realizedPnl": "0",
            "side": "LONG",
            "size": "0.003",
            "status": "OPEN",
            "subaccountNumber": 0,
            "sumClose": "0",
            "sumOpen": "0.003",
            "unrealizedPnl": "-0.85556049500000000000001"
        }
    ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `ETH`, `LONG`, `OPEN`, `USD`

## Related Files

This file is located in `tests/test_data/dydx/http/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/http/list_perpetual_positions.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.436283Z*
