# Documentation: streaming_ocm_UPDATE.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_UPDATE.json`
- **Size**: 1,355 bytes
- **Lines**: 59
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 12345,
  "clk": "AOkVAIMZALsQAKsQAO8M",
  "pt": 1478546671115,
  "oc": [
    {
      "id": "1.180604981",
      "orc": [
        {
          "id": 1209555,
          "uo": [
            {
              "id": "78996704480",
              "p": 1.02,
              "s": 2,
              "side": "L",
              "status": "E",
              "pt": "L",
              "ot": "L",
              "pd": 1478546670000,
              "cd": 1478546670001,
              "sm": 0,
              "sr": 2,
              "sl": 0,
              "sc": 0,
              "sv": 0,
              "rac": "",
              "rc": "REG_GGC",
              "rfo": "O-20210408-062924-001-001-2",
              "rfs": "BetfairTestStrategy-001"
            },
            {
              "id": "78996704480",
              "p": 1.02,
              "s": 2,
              "side": "L",
              "status": "EC",
              "pt": "L",
              "ot": "L",
              "pd": 1478546670000,
              "cd": 1478546670001,
              "sm": 0,
              "sr": 0,
              "sl": 0,
              "sc": 2,
              "sv": 0,
              "rac": "",
              "rc": "REG_GGC",
              "rfo": "O-20210408-062924-001-001-2",
              "rfs": "BetfairTestStrategy-001"
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


**Identifiers**: `AOkVAIMZALsQAKsQAO8M`, `BetfairTestStrategy`, `REG_GGC`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_UPDATE.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.537663Z*
