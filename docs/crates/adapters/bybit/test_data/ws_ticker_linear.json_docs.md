# Documentation: ws_ticker_linear.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_ticker_linear.json`
- **Size**: 838 bytes
- **Lines**: 29
- **Language**: JSON

## Original Source

```json
{
    "topic": "tickers.BTCUSDT",
    "type": "snapshot",
    "data": {
        "symbol": "BTCUSDT",
        "tickDirection": "PlusTick",
        "price24hPcnt": "0.017103",
        "lastPrice": "17216.00",
        "prevPrice24h": "16926.50",
        "highPrice24h": "17281.50",
        "lowPrice24h": "16915.00",
        "prevPrice1h": "17238.00",
        "markPrice": "17217.33",
        "indexPrice": "17227.36",
        "openInterest": "68744.761",
        "openInterestValue": "1183601235.91",
        "turnover24h": "1570383121.943499",
        "volume24h": "91705.276",
        "nextFundingTime": "1673280000000",
        "fundingRate": "-0.000212",
        "bid1Price": "17215.50",
        "bid1Size": "84.489",
        "ask1Price": "17216.00",
        "ask1Size": "83.020"
    },
    "cs": 24987956059,
    "ts": 1673272861686
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 2


**Identifiers**: `BTCUSDT`, `PlusTick`

## Related Files

This file is located in `crates/adapters/bybit/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bybit/test_data/ws_ticker_linear.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.535220Z*
