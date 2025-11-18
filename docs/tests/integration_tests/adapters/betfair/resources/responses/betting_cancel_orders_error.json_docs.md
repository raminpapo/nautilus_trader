# Documentation: betting_cancel_orders_error.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/betting_cancel_orders_error.json`
- **Size**: 339 bytes
- **Lines**: 18
- **Language**: JSON

## Original Source

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "customerRef": "d32e64db841763cb0e207d9f7a385b1e",
    "status": "SUCCESS",
    "marketId": "1.179082386",
    "instructionReports": [
      {
        "status": "FAILURE",
        "errorCode": "ERROR_IN_ORDER",
        "instruction": {
          "betId": "1"
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

Total unique keywords extracted: 3


**Identifiers**: `ERROR_IN_ORDER`, `FAILURE`, `SUCCESS`

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
pytest tests/integration_tests/adapters/betfair/resources/responses/betting_cancel_orders_error.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.219650Z*
