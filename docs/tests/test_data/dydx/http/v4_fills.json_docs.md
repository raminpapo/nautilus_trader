# Documentation: v4_fills.json

## File Metadata

- **Path**: `tests/test_data/dydx/http/v4_fills.json`
- **Size**: 623 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
    "fills": [
        {
            "affiliateRevShare": "0",
            "clientMetadata": "0",
            "createdAt": "2024-10-12T15:09:16.874Z",
            "createdAtHeight": "22883718",
            "fee": "0.000496",
            "id": "ac2df5fb-b135-5bd6-bb5a-62487d9f67d3",
            "liquidity": "MAKER",
            "market": "ETH-USD",
            "marketType": "PERPETUAL",
            "orderId": "bdfa3018-6054-5a11-b4af-8873a0b3f801",
            "price": "2477.6",
            "side": "SELL",
            "size": "0.002",
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


**Identifiers**: `ETH`, `LIMIT`, `MAKER`, `PERPETUAL`, `SELL`, `USD`

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
pytest tests/test_data/dydx/http/v4_fills.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.440570Z*
