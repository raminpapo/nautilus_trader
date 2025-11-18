# Documentation: http_futures_account_trades.json

## File Metadata

- **Path**: `tests/integration_tests/adapters/binance/resources/http_responses/http_futures_account_trades.json`
- **Size**: 896 bytes
- **Lines**: 37
- **Language**: JSON

## Original Source

```json
[
    {
        "symbol": "ETHUSDT",
        "id": 82357626,
        "orderId": 831238666,
        "side": "SELL",
        "price": "2778.35",
        "qty": "0.005",
        "realizedPnl": "0",
        "marginAsset": "USDT",
        "quoteQty": "13.89175",
        "commission": "0.00555670",
        "commissionAsset": "USDT",
        "time": 1645930322371,
        "positionSide": "BOTH",
        "buyer": false,
        "maker": false
    },
    {
        "symbol": "ETHUSDT",
        "id": 82357629,
        "orderId": 831238690,
        "side": "BUY",
        "price": "2779",
        "qty": "0.005",
        "realizedPnl": "-0.00325000",
        "marginAsset": "USDT",
        "quoteQty": "13.89500",
        "commission": "0.00555800",
        "commissionAsset": "USDT",
        "time": 1645930333910,
        "positionSide": "BOTH",
        "buyer": true,
        "maker": false
    }
]

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BOTH`, `BUY`, `ETHUSDT`, `SELL`, `USDT`

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
pytest tests/integration_tests/adapters/binance/resources/http_responses/http_futures_account_trades.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:06.608446Z*
