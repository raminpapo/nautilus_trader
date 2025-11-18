# Documentation: betting_place_order_error.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_error.json`
- **Size**: 655 bytes
- **Lines**: 28
- **Language**: JSON

## Original Source

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "O-20210331-202018-001-001-2",
    "status": "FAILURE",
    "errorCode": "PERMISSION_DENIED",
    "marketId": "1.181106170",
    "instructionReports": [
      {
        "status": "FAILURE",
        "errorCode": "ERROR_IN_ORDER",
        "instruction": {
          "selectionId": 235,
          "handicap": 0.0,
          "limitOrder": {
            "size": 10.0,
            "price": 1.8,
            "persistenceType": "PERSIST"
          },
          "customerOrderRef": "O-20210331-202018-001-001-2",
          "orderType": "LIMIT",
          "side": "LAY"
        }
      }
    ]
  }
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 6


**Identifiers**: `ERROR_IN_ORDER`, `FAILURE`, `LAY`, `LIMIT`, `PERMISSION_DENIED`, `PERSIST`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/responses/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_error.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.222100Z*
