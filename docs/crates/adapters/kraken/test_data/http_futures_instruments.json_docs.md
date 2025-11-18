# Documentation: http_futures_instruments.json

## File Metadata

- **Path**: `crates/adapters/kraken/test_data/http_futures_instruments.json`
- **Size**: 1,165 bytes
- **Lines**: 39
- **Language**: JSON

## Original Source

```json
{
    "result": "success",
    "instruments": [
        {
            "symbol": "PI_XBTUSD",
            "type": "futures_inverse",
            "underlying": "rr_xbtusd",
            "tickSize": 0.5,
            "contractSize": 1,
            "tradeable": true,
            "impactMidSize": 1000.0,
            "maxPositionSize": 75000000.0,
            "openingDate": "2018-08-31T00:00:00Z",
            "marginLevels": [
                {
                    "contracts": 0,
                    "initialMargin": 0.02,
                    "maintenanceMargin": 0.01
                },
                {
                    "contracts": 500000,
                    "initialMargin": 0.04,
                    "maintenanceMargin": 0.02
                }
            ],
            "fundingRateCoefficient": 24,
            "maxRelativeFundingRate": 0.0025,
            "isin": "GB00J62YGL67",
            "contractValueTradePrecision": 0,
            "postOnly": false,
            "feeScheduleUid": "a6cbc326-9477-4a6c-911a-d4cb3ed7481e",
            "mtf": true,
            "base": "BTC",
            "quote": "USD",
            "pair": "BTC:USD"
        }
    ]
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `BTC`, `GB00J62YGL67`, `PI_XBTUSD`, `USD`

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
pytest crates/adapters/kraken/test_data/http_futures_instruments.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.230644Z*
