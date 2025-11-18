# Documentation: streaming_ocm_filled_different_price.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_filled_different_price.json`
- **Size**: 1,059 bytes
- **Lines**: 51
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 2,
  "clk": "APcKAKYHAJ0VAIcPAPEL",
  "pt": 1635217898600,
  "oc": [
    {
      "fullImage": true,
      "id": "1.189731772",
      "orc": [
        {
          "fullImage": true,
          "id": 6023845,
          "uo": [
            {
              "id": "248485109136",
              "p": 1.3,
              "s": 20,
              "side": "B",
              "status": "EC",
              "pt": "P",
              "ot": "L",
              "pd": 1635217893000,
              "md": 1635217898000,
              "avp": 1.2,
              "sm": 20,
              "sr": 0,
              "sl": 0,
              "sc": 0,
              "sv": 0,
              "rac": "",
              "rc": "REG_LGA",
              "rfo": "O-20211026-031132-000",
              "rfs": "TestStrategy-1."
            }
          ],
          "smc": {
            "KobeStrategy-1.": {
              "mb": [
                [
                  1.33,
                  20
                ]
              ]
            }
          }
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

Total unique keywords extracted: 4


**Identifiers**: `APcKAKYHAJ0VAIcPAPEL`, `KobeStrategy`, `REG_LGA`, `TestStrategy`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_filled_different_price.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.550853Z*
