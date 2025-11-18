# Documentation: conditional_order.json

## File Metadata

- **Path**: `tests/test_data/dydx/http/conditional_order.json`
- **Size**: 660 bytes
- **Lines**: 25
- **Language**: JSON

## Original Source

```json
{
    "clientId": "2043599281",
    "clientMetadata": "1",
    "clobPairId": "1",
    "createdAtHeight": "17933806",
    "goodTilBlock": "17933813",
    "id": "05009670-3fba-5ec7-8447-efb81a03cd9f",
    "orderFlags": "0",
    "postOnly": false,
    "price": "3335.3",
    "triggerPrice": "2791.9",
    "reduceOnly": false,
    "side": "BUY",
    "size": "0.003",
    "status": "FILLED",
    "subaccountId": "4484a830-fa43-5b04-ba00-3621a33ef89d",
    "subaccountNumber": 0,
    "ticker": "ETH-USD",
    "timeInForce": "IOC",
    "totalFilled": "0.003",
    "type": "STOP_LIMIT",
    "updatedAt": "2024-08-01T07:09:25.767Z",
    "updatedAtHeight": "17933806"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `BUY`, `ETH`, `FILLED`, `IOC`, `STOP_LIMIT`, `USD`

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
pytest tests/test_data/dydx/http/conditional_order.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.416930Z*
