# Documentation: ws_book_update.json

## File Metadata

- **Path**: `crates/adapters/coinbase_intx/test_data/ws_book_update.json`
- **Size**: 259 bytes
- **Lines**: 20
- **Language**: JSON

## Original Source

```json
{
  "channel": "LEVEL2",
  "type": "UPDATE",
  "product_id": "BTC-PERP",
  "sequence": 1,
  "time": "2025-03-14T23:09:44.095Z",
  "changes": [
    [
      "BUY",
      "84296.2",
      "0"
    ],
    [
      "BUY",
      "84296.3",
      "0.1779"
    ]
  ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BTC`, `BUY`, `LEVEL2`, `PERP`, `UPDATE`

## Related Files

This file is located in `crates/adapters/coinbase_intx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/coinbase_intx/test_data/ws_book_update.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.664224Z*
