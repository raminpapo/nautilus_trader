# Documentation: fills.json

## File Metadata

- **Path**: `tests/test_data/dydx/http/fills.json`
- **Size**: 1,144 bytes
- **Lines**: 37
- **Language**: JSON

## Original Source

```json
{
    "fills": [
        {
            "clientMetadata": "1",
            "createdAt": "2024-08-01T07:09:25.767Z",
            "createdAtHeight": "17933806",
            "fee": "0.003179",
            "id": "55d7fc68-4b92-5c81-a73d-a3395e0124cb",
            "liquidity": "TAKER",
            "market": "ETH-USD",
            "marketType": "PERPETUAL",
            "orderId": "05009670-3fba-5ec7-8447-efb81a03cd9f",
            "price": "3178.5",
            "side": "BUY",
            "size": "0.002",
            "subaccountNumber": 0,
            "type": "LIMIT"
        },
        {
            "clientMetadata": "1",
            "createdAt": "2024-08-01T07:09:25.767Z",
            "createdAtHeight": "17933806",
            "fee": "0.001589",
            "id": "77641277-0f93-5c7c-ba22-c36b58498f52",
            "liquidity": "TAKER",
            "market": "ETH-USD",
            "marketType": "PERPETUAL",
            "orderId": "05009670-3fba-5ec7-8447-efb81a03cd9f",
            "price": "3176.3",
            "side": "BUY",
            "size": "0.001",
            "subaccountNumber": 0,
            "type": "LIMIT"
        }
    ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `BUY`, `ETH`, `LIMIT`, `PERPETUAL`, `TAKER`, `USD`

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
pytest tests/test_data/dydx/http/fills.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.418176Z*
