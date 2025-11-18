# Documentation: v4_markets_channel_data_v8.json

## File Metadata

- **Path**: `tests/test_data/dydx/websocket/v4_markets_channel_data_v8.json`
- **Size**: 1,226 bytes
- **Lines**: 36
- **Language**: JSON

## Original Source

```json
{
    "type": "channel_data",
    "connection_id": "207fc648-5bbe-4a6a-a347-c1dae4e4b07c",
    "message_id": 3535525,
    "channel": "v4_markets",
    "version": "1.0.0",
    "contents": {
        "trading": {
            "TRY-USD": {
                "id": "143",
                "clobPairId": "143",
                "ticker": "TRY-USD",
                "marketId": 143,
                "status": "ACTIVE",
                "quantumConversionExponent": -9,
                "atomicResolution": -4,
                "subticksPerTick": 1000000,
                "stepBaseQuantums": 1000000,
                "marketType": "ISOLATED",
                "initialMarginFraction": "0.01",
                "maintenanceMarginFraction": "0.005",
                "openInterestLowerCap": "500000",
                "openInterestUpperCap": "1000000",
                "tickSize": "0.00001",
                "stepSize": "100",
                "priceChange24H": "0.00002296872",
                "volume24H": "0",
                "trades24H": 0,
                "nextFundingRate": "0",
                "openInterest": "1257800",
                "baseOpenInterest": "408800",
                "defaultFundingRate1H": "0"
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


**Identifiers**: `ACTIVE`, `ISOLATED`, `TRY`, `USD`

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
pytest tests/test_data/dydx/websocket/v4_markets_channel_data_v8.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.508303Z*
