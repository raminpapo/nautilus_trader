# Documentation: betting_replace_order.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/requests/betting_replace_order.json`
- **Size**: 285 bytes
- **Lines**: 15
- **Language**: JSON

## Original Source

```json
{
  "method": "SportsAPING/v1.0/replaceOrders",
  "params": {
    "marketId": "1.179082386",
    "instructions": [
      {
        "betId": "240718603398",
        "newPrice": 2.0
      }
    ],
    "customerRef": "038990c619d2b5c837a6fe91f9b7b9ed"
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

Total unique keywords extracted: 1


**Identifiers**: `SportsAPING`

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
pytest tests/integration_tests/adapters/betfair/resources/requests/betting_replace_order.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.209696Z*
