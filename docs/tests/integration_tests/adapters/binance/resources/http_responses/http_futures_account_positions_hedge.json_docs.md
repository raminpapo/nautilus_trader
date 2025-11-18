# Documentation: http_futures_account_positions_hedge.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/http_responses/http_futures_account_positions_hedge.json`
- **Size**: 840 bytes
- **Lines**: 33
- **Language**: JSON

## Original Source

```json
[
  {
    "entryPrice": "6563.66500",
    "marginType": "isolated",
    "isAutoAddMargin": "false",
    "isolatedMargin": "15517.54150468",
    "leverage": "10",
    "liquidationPrice": "5930.78",
    "markPrice": "6679.50671178",
    "maxNotionalValue": "20000000",
    "positionAmt": "20.000",
    "symbol": "BTCUSDT",
    "unRealizedProfit": "2316.83423560",
    "positionSide": "LONG",
    "updateTime": 1625474304765
  },
  {
    "entryPrice": "0.00000",
    "marginType": "isolated",
    "isAutoAddMargin": "false",
    "isolatedMargin": "5413.95799991",
    "leverage": "10",
    "liquidationPrice": "7189.95",
    "markPrice": "6679.50671178",
    "maxNotionalValue": "20000000",
    "positionAmt": "-10.000",
    "symbol": "BTCUSDT",
    "unRealizedProfit": "-1156.46711780",
    "positionSide": "SHORT",
    "updateTime": 0
  }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `BTCUSDT`, `LONG`, `SHORT`

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
pytest tests/integration_tests/adapters/binance/resources/http_responses/http_futures_account_positions_hedge.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.604632Z*
