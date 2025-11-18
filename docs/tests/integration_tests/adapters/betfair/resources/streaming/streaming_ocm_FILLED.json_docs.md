# Documentation: streaming_ocm_FILLED.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_FILLED.json`
- **Size**: 796 bytes
- **Lines**: 39
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 2,
  "clk": "AIsCAHgAZwCrAQCHAQ==",
  "pt": 1617863371576,
  "oc": [
    {
      "id": "1.180604981",
      "orc": [
        {
          "id": 1209555,
          "uo": [
            {
              "id": "229430281339",
              "p": 1.1,
              "s": 10,
              "side": "L",
              "status": "EC",
              "pt": "P",
              "ot": "L",
              "pd": 1617863365000,
              "sm": 10,
              "sr": 0,
              "sl": 0,
              "sc": 0,
              "sv": 0,
              "rac": "",
              "rc": "REG_LGA",
              "rfo": "O-20210408-062924-001-001-2",
              "rfs": "BetfairTestStrategy-001",
              "md": 1617863371000
            }
          ]
        }
      ]
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `AIsCAHgAZwCrAQCHAQ`, `BetfairTestStrategy`, `REG_LGA`

## Related Files

This file is located in `tests/integration_tests/adapters/betfair/resources/streaming/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_FILLED.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.528788Z*
