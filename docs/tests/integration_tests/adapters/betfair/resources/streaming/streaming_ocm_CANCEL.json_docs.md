# Documentation: streaming_ocm_CANCEL.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_CANCEL.json`
- **Size**: 793 bytes
- **Lines**: 39
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 2,
  "clk": "AM4HAJwMAJILAMwFANwJ",
  "pt": 1617231693896,
  "oc": [
    {
      "id": "1.179082386",
      "orc": [
        {
          "id": 448,
          "uo": [
            {
              "id": "240564968665",
              "p": 1.19,
              "s": 10,
              "side": "B",
              "status": "EC",
              "pt": "P",
              "ot": "L",
              "pd": 1617231644000,
              "sm": 0,
              "sr": 0,
              "sl": 0,
              "sc": 10,
              "sv": 0,
              "rac": "",
              "rc": "REG_LGA",
              "rfo": "O-20210331-230044-001-001-3",
              "rfs": "BetfairTestStrategy-001",
              "cd": 1617231693000
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


**Identifiers**: `AM4HAJwMAJILAMwFANwJ`, `BetfairTestStrategy`, `REG_LGA`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_CANCEL.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.524890Z*
