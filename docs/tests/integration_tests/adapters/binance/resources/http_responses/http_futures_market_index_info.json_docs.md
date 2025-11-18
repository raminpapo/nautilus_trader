# Documentation: http_futures_market_index_info.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/http_responses/http_futures_market_index_info.json`
- **Size**: 444 bytes
- **Lines**: 22
- **Language**: JSON

## Original Source

```json
[
  {
    "symbol": "DEFIUSDT",
    "time": 1589437530011,
    "component": "baseAsset",
    "baseAssetList": [
      {
        "baseAsset": "BAL",
        "quoteAsset": "USDT",
        "weightInQuantity": "1.04406228",
        "weightInPercentage": "0.02783900"
      },
      {
        "baseAsset": "BAND",
        "quoteAsset": "USDT",
        "weightInQuantity": "3.53782729",
        "weightInPercentage": "0.03935200"
      }
    ]
  }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BAL`, `BAND`, `DEFIUSDT`, `USDT`

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
pytest tests/integration_tests/adapters/binance/resources/http_responses/http_futures_market_index_info.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.624311Z*
