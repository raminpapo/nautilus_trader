# Documentation: http_futures_account_symbol_config.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/http_responses/http_futures_account_symbol_config.json`
- **Size**: 297 bytes
- **Lines**: 17
- **Language**: JSON

## Original Source

```json
[
  {
    "symbol": "ETHUSDT",
    "marginType": "CROSSED",
    "isAutoAddMargin": false,
    "leverage": 20,
    "maxNotionalValue": "1000000"
  },
  {
    "symbol": "BTCUSDT",
    "marginType": "ISOLATED",
    "isAutoAddMargin": true,
    "leverage": 25,
    "maxNotionalValue": "2000000"
  }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BTCUSDT`, `CROSSED`, `ETHUSDT`, `ISOLATED`

## Related Files

This file is located in `tests/integration_tests/adapters/binance/resources/http_responses/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/integration_tests/adapters/binance/resources/http_responses/http_futures_account_symbol_config.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.607147Z*
