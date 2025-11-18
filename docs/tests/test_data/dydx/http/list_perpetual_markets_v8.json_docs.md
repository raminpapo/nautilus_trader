# Documentation: list_perpetual_markets_v8.json

## File Metadata

- **Path**: `tests/test_data/dydx/http/list_perpetual_markets_v8.json`
- **Size**: 836 bytes
- **Lines**: 29
- **Language**: JSON

## Original Source

```json
{
    "markets":{
       "BTC-USD":{
          "clobPairId":"0",
          "ticker":"BTC-USD",
          "status":"ACTIVE",
          "oraclePrice":"104952.44975",
          "priceChange24H":"2545.6996",
          "volume24H":"96146.1767",
          "trades24H":7366,
          "nextFundingRate":"0",
          "initialMarginFraction":"0.02",
          "maintenanceMarginFraction":"0.012",
          "openInterest":"44.8741",
          "atomicResolution":-10,
          "quantumConversionExponent":-9,
          "tickSize":"1",
          "stepSize":"0.0001",
          "stepBaseQuantums":1000000,
          "subticksPerTick":100000,
          "marketType":"CROSS",
          "openInterestLowerCap":"0",
          "openInterestUpperCap":"0",
          "baseOpenInterest":"50.3776",
          "defaultFundingRate1H":"0"
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


**Identifiers**: `ACTIVE`, `BTC`, `CROSS`, `USD`

## Related Files

This file is located in `tests/test_data/dydx/http/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest tests/test_data/dydx/http/list_perpetual_markets_v8.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:08.435067Z*
