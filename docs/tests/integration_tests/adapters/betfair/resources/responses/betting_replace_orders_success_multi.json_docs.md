# Documentation: betting_replace_orders_success_multi.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success_multi.json`
- **Size**: 1,433 bytes
- **Lines**: 60
- **Language**: JSON

## Original Source

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "op": "ocm",
    "id": 2,
    "clk": "ADIAYgA7ADcAUQ==",
    "pt": 1617237424262,
    "oc": [
      {
        "id": "1.181300531",
        "orc": [
          {
            "id": 448,
            "uo": [
              {
                "id": "228703177738",
                "p": 1.1,
                "s": 10,
                "side": "L",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1617237424000,
                "sm": 0,
                "sr": 10,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20210401-003703-001-001-2",
                "rfs": "BetfairTestStrategy-001"
              },
              {
                "id": "228703177752",
                "p": 1.22,
                "s": 10,
                "side": "B",
                "status": "E",
                "pt": "P",
                "ot": "L",
                "pd": 1617237424000,
                "sm": 0,
                "sr": 10,
                "sl": 0,
                "sc": 0,
                "sv": 0,
                "rac": "",
                "rc": "REG_LGA",
                "rfo": "O-20210401-003703-001-001-1",
                "rfs": "BetfairTestStrategy-001"
              }
            ]
          }
        ]
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


**Identifiers**: `ADIAYgA7ADcAUQ`, `BetfairTestStrategy`, `REG_LGA`

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
pytest tests/integration_tests/adapters/betfair/resources/responses/betting_replace_orders_success_multi.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.226104Z*
