# Documentation: betting_place_order_bsp.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/requests/betting_place_order_bsp.json`
- **Size**: 509 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "method": "SportsAPING/v1.0/placeOrders",
  "params": {
    "marketId": "1.179082386",
    "instructions": [
      {
        "customerOrderRef": "O-20210410-022422-001",
        "selectionId": "50214",
        "handicap": null,
        "marketOnCloseOrder": {
          "liability": "10.0"
        },
        "orderType": "MARKET_ON_CLOSE",
        "side": "BACK"
      }
    ],
    "customerStrategyRef": "S-001",
    "customerRef": "be7dffa046f2fce5d820c7634d022ca1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `BACK`, `MARKET_ON_CLOSE`, `SportsAPING`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/requests/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/requests/betting_place_order_bsp.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.206573Z*
