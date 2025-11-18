# Documentation: streaming_ocm_error_fill.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_error_fill.json`
- **Size**: 1,286 bytes
- **Lines**: 58
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 2,
  "clk": "AOyKCwDVjQgAvq8JAL2VCwDS8wc=",
  "pt": 1634172533141,
  "oc": [
    {
      "closed": true,
      "id": "1.189080949",
      "orc": [
        {
          "id": 8622709,
          "uo": [
            {
              "id": "247177945217",
              "p": 11.5,
              "s": 2,
              "side": "L",
              "status": "EC",
              "pt": "P",
              "ot": "L",
              "pd": 1634167607000,
              "sm": 0,
              "sr": 0,
              "sl": 2,
              "sc": 0,
              "sv": 0,
              "rac": "",
              "rc": "REG_LGA",
              "rfo": "O-20211013-232646-000",
              "rfs": "TestStrategy-1."
            },
            {
              "id": "247177946234",
              "p": 11.5,
              "s": 2,
              "side": "L",
              "status": "EC",
              "pt": "P",
              "ot": "L",
              "pd": 1634167609000,
              "sm": 0,
              "sr": 0,
              "sl": 2,
              "sc": 0,
              "sv": 0,
              "rac": "",
              "rc": "REG_LGA",
              "rfo": "O-20211013-232648-000",
              "rfs": "TestStrategy-1."
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


**Identifiers**: `AOyKCwDVjQgAvq8JAL2VCwDS8wc`, `REG_LGA`, `TestStrategy`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_error_fill.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.549596Z*
