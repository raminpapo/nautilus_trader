# Documentation: http_get_klines_linear.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/http_get_klines_linear.json`
- **Size**: 317 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "retCode": 0,
  "retMsg": "OK",
  "result": {
    "category": "linear",
    "symbol": "BTCUSDT",
    "list": [
      [
        "1709891679000",
        "27450",
        "27460",
        "27440",
        "27455",
        "123.45",
        "3390000"
      ]
    ]
  },
  "retExtInfo": {},
  "time": 1709891679050
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `BTCUSDT`

## Related Files

This file is located in `crates/adapters/bybit/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bybit/test_data/http_get_klines_linear.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.500676Z*
