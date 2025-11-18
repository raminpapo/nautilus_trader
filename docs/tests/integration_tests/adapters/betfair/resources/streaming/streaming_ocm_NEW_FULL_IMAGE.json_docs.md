# Documentation: streaming_ocm_NEW_FULL_IMAGE.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_NEW_FULL_IMAGE.json`
- **Size**: 883 bytes
- **Lines**: 37
- **Language**: JSON

## Original Source

```json
{
    "op": "ocm",
    "id": 6,
    "initialClk": "GpOH0JwBH762w50BHKKomJ0BGpzR5ZoBH5mWsJwB",
    "clk": "AAAAAAAAAAAAAA==",
    "conflateMs": 0,
    "heartbeatMs": 5000,
    "pt": 1468943673782,
    "ct": "SUB_IMAGE",
    "oc": [{
        "id": "1.179082386",
        "orc": [{
            "fullImage": true,
            "id": 50214,
            "uo": [{
                "id": "71352090695",
                "p": 12,
                "s": 5,
                "side": "B",
                "status": "E",
                "pt": "L",
                "ot": "L",
                "pd": 1468919099000,
                "md": 1468933833000,
                "avp": 12,
                "sm": 4.75,
                "sr": 0.25,
                "sl": 0,
                "sc": 0,
                "sv": 0
            }],
            "mb": [
                [12, 4.75]
            ]
        }]
    }]
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `AAAAAAAAAAAAAA`, `GpOH0JwBH762w50BHKKomJ0BGpzR5ZoBH5mWsJwB`, `SUB_IMAGE`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_NEW_FULL_IMAGE.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.534891Z*
