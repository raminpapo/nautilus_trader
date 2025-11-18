# Documentation: ws_spot_agg_trade.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_agg_trade.json`
- **Size**: 259 bytes
- **Lines**: 16
- **Language**: JSON

## Original Source

```json
{
  "stream":"ethusdt@aggTrade",
  "data":{
    "e":"aggTrade",
    "E":1675759520848,
    "s":"ETHUSDT",
    "a":226532,
    "p":"1632.46000000",
    "q":"0.34305000",
    "f":228423,
    "l":228423,
    "T":1675759520847,
    "m":false,
    "M":true
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
pytest tests/integration_tests/adapters/binance/resources/ws_messages/ws_spot_agg_trade.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.681188Z*
