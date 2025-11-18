# Documentation: betting_replace_orders_success.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success.json`
- **Size**: 1,019 bytes
- **Lines**: 40
- **Language**: JSON

## Original Source

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "1628815542932-1.186291565-rpl-0",
    "marketId": "1.186291565",
    "instructionReports": [
      {
        "cancelInstructionReport": {
          "instruction": {
            "betId": "1"
          },
          "sizeCancelled": 5.0,
          "cancelledDate": "2021-08-13T00:45:43.000Z",
          "status": "SUCCESS"
        },
        "placeInstructionReport": {
          "instruction": {
            "selectionId": 40521960,
            "limitOrder": {
              "size": 5.0,
              "price": 50.0,
              "persistenceType": "LAPSE"
            },
            "orderType": "LIMIT",
            "side": "BACK"
          },
          "betId": "240808766933",
          "placedDate": "2021-08-13T00:45:43.000Z",
          "averagePriceMatched": 0.0,
          "sizeMatched": 0.0,
          "status": "SUCCESS",
          "orderStatus": "EXECUTABLE"
        },
        "status": "SUCCESS"
      }
    ],
    "status": "SUCCESS"
  }
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BACK`, `EXECUTABLE`, `LAPSE`, `LIMIT`, `SUCCESS`

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
pytest tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.224777Z*
