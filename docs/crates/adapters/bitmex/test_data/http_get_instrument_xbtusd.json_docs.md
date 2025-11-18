# Documentation: http_get_instrument_xbtusd.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/http_get_instrument_xbtusd.json`
- **Size**: 2,421 bytes
- **Lines**: 82
- **Language**: JSON

## Original Source

```json
{
    "symbol": "XBTUSD",
    "rootSymbol": "XBT",
    "state": "Open",
    "typ": "FFWCSX",
    "listing": "2016-05-13T12:00:00.000Z",
    "front": "2016-05-13T12:00:00.000Z",
    "positionCurrency": "USD",
    "underlying": "XBT",
    "quoteCurrency": "USD",
    "underlyingSymbol": "XBT=",
    "reference": "BMEX",
    "referenceSymbol": ".BXBT",
    "maxOrderQty": 10000000,
    "maxPrice": 1000000,
    "lotSize": 100,
    "tickSize": 0.1,
    "multiplier": -100000000,
    "settlCurrency": "XBt",
    "underlyingToSettleMultiplier": -100000000,
    "isQuanto": false,
    "isInverse": true,
    "initMargin": 0.01,
    "maintMargin": 0.005,
    "riskLimit": 20000000000,
    "riskStep": 15000000000,
    "taxed": true,
    "deleverage": true,
    "makerFee": 0.0005,
    "takerFee": 0.0005,
    "settlementFee": 0,
    "fundingBaseSymbol": ".XBTBON8H",
    "fundingQuoteSymbol": ".USDBON8H",
    "fundingPremiumSymbol": ".XBTUSDPI8H",
    "fundingTimestamp": "2024-11-25T04:00:00.000Z",
    "fundingInterval": "2000-01-01T08:00:00.000Z",
    "fundingRate": 0.00011,
    "indicativeFundingRate": 0.000125,
    "prevClosePrice": 97409.63,
    "limitDownPrice": null,
    "limitUpPrice": null,
    "prevTotalVolume": 3868480147789,
    "totalVolume": 3868507398889,
    "volume": 27251100,
    "volume24h": 419742700,
    "prevTotalTurnover": 37667656761390205,
    "totalTurnover": 37667684492745237,
    "turnover": 27731355032,
    "turnover24h": 431762899194,
    "homeNotional24h": 4317.62899194,
    "foreignNotional24h": 419742700,
    "prevPrice24h": 97655,
    "vwap": 97216.6863,
    "highPrice": 98743.5,
    "lowPrice": 95802.9,
    "lastPrice": 97893.7,
    "lastPriceProtected": 97912.5054,
    "lastTickDirection": "PlusTick",
    "lastChangePcnt": 0.0024,
    "bidPrice": 97882.5,
    "midPrice": 97884.8,
    "askPrice": 97887.1,
    "impactBidPrice": 97882.7951,
    "impactMidPrice": 97884.7,
    "impactAskPrice": 97886.6277,
    "hasLiquidity": true,
    "openInterest": 411647400,
    "openValue": 420691293378,
    "fairMethod": "FundingRate",
    "fairBasisRate": 0.12045,
    "fairBasis": 5.99,
    "fairPrice": 97849.76,
    "markMethod": "FairPrice",
    "markPrice": 97849.76,
    "indicativeSettlePrice": 97843.77,
    "instantPnl": true,
    "timestamp": "2024-11-24T23:33:19.034Z",
    "minTick": 0.01,
    "fundingBaseRate": 0.0003,
    "fundingQuoteRate": 0.0006,
    "capped": false
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 14


**Identifiers**: `BMEX`, `BXBT`, `FFWCSX`, `FairPrice`, `FundingRate`, `Open`, `PlusTick`, `USD`, `USDBON8H`, `XBT`, `XBTBON8H`, `XBTUSD`, `XBTUSDPI8H`, `XBt`

## Related Files

This file is located in `crates/adapters/bitmex/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/bitmex/test_data/http_get_instrument_xbtusd.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.103791Z*
