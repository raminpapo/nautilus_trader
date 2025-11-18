# Documentation: bar.json

## File Metadata

- **Path**: `crates/adapters/tardis/src/tests/data/bar.json`
- **Size**: 506 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "type": "trade_bar",
  "symbol": "XBTUSD",
  "exchange": "bitmex",
  "name": "trade_bar_10000ms",
  "interval": 10000,
  "kind": "time",
  "open": 7623.5,
  "high": 7623.5,
  "low": 7623,
  "close": 7623.5,
  "volume": 37034,
  "buyVolume": 24244,
  "sellVolume": 12790,
  "trades": 9,
  "vwap": 7623.327320840309,
  "openTimestamp": "2019-10-25T13:11:31.574Z",
  "closeTimestamp": "2019-10-25T13:11:39.212Z",
  "localTimestamp": "2019-10-25T13:11:40.369Z",
  "timestamp": "2019-10-25T13:11:40.000Z"
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
pytest crates/adapters/tardis/src/tests/data/bar.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.743037Z*
