# Documentation: ws_spot_ticker_book.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_ticker_book.json`
- **Size**: 231 bytes
- **Lines**: 14
- **Language**: JSON

## Original Source

```json
{
  "stream":"ethusdt@bookTicker",
  "data":{
    "u":12711621188,
    "s":"ETHUSDT",
    "b":"4507.24000000",
    "B":"2.35950000",
    "a":"4507.25000000",
    "A":"2.84570000",
    "T":1646199228121,
    "E":1646199228123
  }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `ETHUSDT`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/resources/ws_messages/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_ticker_book.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.722111Z*
