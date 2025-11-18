# Documentation: book_snapshot.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/book_snapshot.json`
- **Size**: 497 bytes
- **Lines**: 31
- **Language**: JSON

## Original Source

```json
{
  "type": "book_snapshot",
  "symbol": "XBTUSD",
  "exchange": "bitmex",
  "name": "book_snapshot_2_50ms",
  "depth": 2,
  "interval": 50,
  "bids": [
    {
      "price": 7633.5,
      "amount": 1906067
    },
    {
      "price": 7633,
      "amount": 65319
    }
  ],
  "asks": [
    {
      "price": 7634,
      "amount": 1467849
    },
    {
      "price": 7634.5,
      "amount": 67939
    }
  ],
  "timestamp": "2019-10-25T13:39:46.950Z",
  "localTimestamp": "2019-10-25T13:39:46.961Z"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `XBTUSD`

## Related Files

This file is located in `crates/adapters/tardis/src/tests/data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/tardis/src/tests/data/book_snapshot.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.746630Z*
