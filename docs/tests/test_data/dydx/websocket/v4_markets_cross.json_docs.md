# Documentation: v4_markets_cross.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_markets_cross.json`
- **Size**: 1,193 bytes
- **Lines**: 36
- **Language**: JSON

## Original Source

```json
{
    "type": "channel_data",
    "connection_id": "3f42a31a-07a0-4c4b-b74e-bfa3dbf03012",
    "message_id": 768900,
    "channel": "v4_markets",
    "version": "1.0.0",
    "contents": {
        "trading": {
            "FTM-USD": {
                "id": "86",
                "clobPairId": "86",
                "ticker": "FTM-USD",
                "marketId": 86,
                "status": "FINAL_SETTLEMENT",
                "quantumConversionExponent": -9,
                "atomicResolution": -5,
                "subticksPerTick": 1000000,
                "stepBaseQuantums": 1000000,
                "marketType": "CROSS",
                "initialMarginFraction": "0.2",
                "maintenanceMarginFraction": "0.1",
                "openInterestLowerCap": "5000000",
                "openInterestUpperCap": "10000000",
                "tickSize": "0.0001",
                "stepSize": "10",
                "priceChange24H": "-0.0036333222",
                "volume24H": "292953.744",
                "trades24H": 2656,
                "nextFundingRate": "0",
                "openInterest": "564710",
                "baseOpenInterest": "263330"
            }
        }
    }
}

```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 4


**Identifiers**: `CROSS`, `FINAL_SETTLEMENT`, `FTM`, `USD`

## Related Files

This file is located in `tests/test_data/dydx/websocket/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/websocket/v4_markets_cross.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.509429Z*
