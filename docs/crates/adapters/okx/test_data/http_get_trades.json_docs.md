# Documentation: http_get_trades.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_trades.json`
- **Size**: 386 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "instId": "BTC-USDT",
      "side": "sell",
      "sz": "0.00013669",
      "px": "102537.9",
      "tradeId": "734864333",
      "ts": "1747087163557"
    },
    {
      "instId": "BTC-USDT",
      "side": "buy",
      "sz": "0.0000125",
      "px": "102537.9",
      "tradeId": "734864332",
      "ts": "1747087161666"
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
pytest crates/adapters/okx/test_data/http_get_trades.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.560523Z*
