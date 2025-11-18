# Documentation: betting_place_order_success.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_success.json`
- **Size**: 765 bytes
- **Lines**: 31
- **Language**: JSON

## Original Source

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "O-20210327-090738-001-001-2",
    "status": "SUCCESS",
    "marketId": "1.181005744",
    "instructionReports": [
      {
        "status": "SUCCESS",
        "instruction": {
          "selectionId": 86362,
          "handicap": 0.0,
          "limitOrder": {
            "size": 10.0,
            "price": 2.58,
            "persistenceType": "PERSIST"
          },
          "customerOrderRef": "O-20210327-090738-001-001-2",
          "orderType": "LIMIT",
          "side": "LAY"
        },
        "betId": "228302937743",
        "placedDate": "2021-03-27T09:07:38.000Z",
        "averagePriceMatched": 0.0,
        "sizeMatched": 0.0,
        "orderStatus": "EXECUTABLE"
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

Total unique keywords extracted: 5


**Identifiers**: `EXECUTABLE`, `LAY`, `LIMIT`, `PERSIST`, `SUCCESS`

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
pytest tests/integration_tests/adapters/betfair/resources/responses/betting_place_order_success.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.223441Z*
