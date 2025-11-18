# Documentation: http_futures_tickers.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/http_futures_tickers.json`
- **Size**: 1,720 bytes
- **Lines**: 57
- **Language**: JSON

## Original Source

```json
{
    "result": "success",
    "serverTime": "2025-11-17T00:34:37.524Z",
    "tickers": [
        {
            "symbol": "PI_XBTUSD",
            "last": 91415.0,
            "lastTime": "2025-11-17T00:31:01.835715Z",
            "tag": "perpetual",
            "pair": "BTC:USD",
            "markPrice": 91506.6009839176,
            "bid": 91415.0,
            "bidSize": 4960.0,
            "ask": 91490.5,
            "askSize": 5020.0,
            "vol24h": 21118140.0,
            "volumeQuote": 260138.8647,
            "openInterest": 21279580.0,
            "open24h": 90000.0,
            "high24h": 92000.0,
            "low24h": 89000.0,
            "lastSize": 3240.0,
            "fundingRate": -3.995839963e-09,
            "fundingRatePrediction": 6.272058425e-08,
            "suspended": false,
            "indexPrice": 91468.38,
            "postOnly": false,
            "change24h": 1.57
        },
        {
            "symbol": "PF_ETHUSD",
            "last": 3200.5,
            "lastTime": "2025-11-17T00:30:00.000000Z",
            "tag": "perpetual",
            "pair": "ETH:USD",
            "markPrice": 3205.25,
            "bid": 3200.0,
            "bidSize": 100.0,
            "ask": 3210.5,
            "askSize": 150.0,
            "vol24h": 500000.0,
            "volumeQuote": 1600000.0,
            "openInterest": 1000000.0,
            "open24h": 3150.0,
            "high24h": 3250.0,
            "low24h": 3100.0,
            "lastSize": 50.0,
            "fundingRate": 1.5e-05,
            "fundingRatePrediction": 1.2e-05,
            "suspended": false,
            "indexPrice": 3202.75,
            "postOnly": false,
            "change24h": 1.6
        }
    ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 5


**Identifiers**: `BTC`, `ETH`, `PF_ETHUSD`, `PI_XBTUSD`, `USD`

## Related Files

This file is located in `crates/adapters/kraken/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/kraken/test_data/http_futures_tickers.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.232625Z*
