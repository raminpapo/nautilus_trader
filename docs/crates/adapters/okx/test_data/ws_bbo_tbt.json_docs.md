# Documentation: ws_bbo_tbt.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/ws_bbo_tbt.json`
- **Size**: 376 bytes
- **Lines**: 29
- **Language**: JSON

## Original Source

```json
{
  "arg": {
    "channel": "bbo-tbt",
    "instId": "BTC-USDT"
  },
  "data": [
    {
      "asks": [
        [
          "8476.98",
          "415",
          "0",
          "13"
        ]
      ],
      "bids": [
        [
          "8476.97",
          "256",
          "0",
          "12"
        ]
      ],
      "ts": "1597026383085",
      "seqId": 123456
    }
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `BTC`, `USDT`

## Related Files

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/ws_bbo_tbt.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.571698Z*
