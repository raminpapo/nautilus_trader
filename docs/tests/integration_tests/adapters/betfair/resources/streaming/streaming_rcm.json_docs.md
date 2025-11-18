# Documentation: streaming_rcm.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/betfair/resources/streaming/streaming_rcm.json`
- **Size**: 706 bytes
- **Lines**: 43
- **Language**: JSON

## Original Source

```json
{
  "op":"rcm",
  "id":2,
  "clk":12,
  "pt":1518626764,
  "rc": [
    {
      "id": "28587288.1650",
      "mid": "1.1234567",
      "rrc": [
        {
          "ft":1518626674,
          "id":7390417,
          "lat":51.4189543,
          "long":-0.4058491,
          "spd":17.8,
          "prg":2051,
          "sfq":2.07
        }
      ],
      "rpc": {
        "ft":1518626674,
        "g":"1f",
        "st":10.6,
        "rt":46.7,
        "spd":17.8,
        "prg":87.5,
        "ord": [
          7390417,
          5600338,
          11527189,
          6395118,
          8706072
        ],
        "J": [
          {"J":2,"L":370.1},
          {"J":1,"L":203.8}
        ]
      }
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 0

*No keywords extracted*

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
pytest tests/integration_tests/adapters/betfair/resources/streaming/streaming_rcm.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.554552Z*
