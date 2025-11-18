# Documentation: ws_book_snapshot.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/ws_book_snapshot.json`
- **Size**: 443 bytes
- **Lines**: 21
- **Language**: JSON

## Original Source

```json
{
  "channel": "book",
  "type": "snapshot",
  "data": [
    {
      "symbol": "BTC/USD",
      "bids": [
        {"price": 105944.20, "qty": 0.136},
        {"price": 105935.40, "qty": 0.024},
        {"price": 105920.10, "qty": 0.052}
      ],
      "asks": [
        {"price": 105944.30, "qty": 0.136},
        {"price": 105946.90, "qty": 0.095},
        {"price": 105955.80, "qty": 0.003}
      ],
      "checksum": 2439117997
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


**Identifiers**: `BTC`, `USD`

## Related Files

This file is located in `crates/adapters/kraken/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/kraken/test_data/ws_book_snapshot.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.268057Z*
