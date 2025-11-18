# Documentation: streaming_ocm_SUB_IMAGE.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_SUB_IMAGE.json`
- **Size**: 481 bytes
- **Lines**: 29
- **Language**: JSON

## Original Source

```json
{
  "op": "ocm",
  "id": 12345,
  "initialClk": "Lfj28Y4CiQayxLyUAlDysIqUAkfx6qyNAq8Gpd6fjgI=",
  "clk": "AAAAAAAAAAAAAA==",
  "conflateMs": 0,
  "heartbeatMs": 5000,
  "pt": 1478543329252,
  "ct": "SUB_IMAGE",
  "oc": [
    {
      "closed": true,
      "id": "1.180612579",
      "orc": [
        {
          "fullImage": true,
          "id": 25200510,
          "mb": [
            [
              80,
              0.08
            ]
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


**Identifiers**: `AAAAAAAAAAAAAA`, `Lfj28Y4CiQayxLyUAlDysIqUAkfx6qyNAq8Gpd6fjgI`, `SUB_IMAGE`

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_ocm_SUB_IMAGE.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.536323Z*
