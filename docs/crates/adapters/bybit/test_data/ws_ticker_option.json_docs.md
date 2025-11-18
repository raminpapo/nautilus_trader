# Documentation: ws_ticker_option.json

## File Metadata

- **Path**: `crates/adapters/bybit/test_data/ws_ticker_option.json`
- **Size**: 957 bytes
- **Lines**: 34
- **Language**: JSON

## Original Source

```json
{
    "id": "tickers.BTC-6JAN23-17500-C-2480334983-1672917511074",
    "topic": "tickers.BTC-6JAN23-17500-C",
    "ts": 1672917511074,
    "data": {
        "symbol": "BTC-6JAN23-17500-C",
        "bidPrice": "0",
        "bidSize": "0",
        "bidIv": "0",
        "askPrice": "10",
        "askSize": "5.1",
        "askIv": "0.514",
        "lastPrice": "10",
        "highPrice24h": "25",
        "lowPrice24h": "5",
        "markPrice": "7.86976724",
        "indexPrice": "16823.73",
        "markPriceIv": "0.4896",
        "underlyingPrice": "16815.1",
        "openInterest": "49.85",
        "turnover24h": "446802.8473",
        "volume24h": "26.55",
        "totalVolume": "86",
        "totalTurnover": "1437431",
        "delta": "0.047831",
        "gamma": "0.00021453",
        "vega": "0.81351067",
        "theta": "-19.9115368",
        "predictedDeliveryPrice": "0",
        "change24h": "-0.33333334"
    },
    "type": "snapshot"
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 1


**Identifiers**: `BTC`

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
pytest crates/adapters/bybit/test_data/ws_ticker_option.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.536469Z*
