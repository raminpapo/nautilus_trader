# Documentation: http_get_instruments_swap.json

## File Metadata

- **Path**: `crates/adapters/okx/test_data/http_get_instruments_swap.json`
- **Size**: 3,423 bytes
- **Lines**: 135
- **Language**: JSON

## Original Source

```json
{
  "code": "0",
  "msg": "",
  "data": [
    {
      "alias": "",
      "auctionEndTime": "",
      "baseCcy": "",
      "category": "1",
      "contTdSwTime": "",
      "ctMult": "1",
      "ctType": "inverse",
      "ctVal": "100",
      "ctValCcy": "USD",
      "expTime": "",
      "futureSettlement": false,
      "instFamily": "BTC-USD",
      "instId": "BTC-USD-SWAP",
      "instIdCode": 10458,
      "instType": "SWAP",
      "lever": "100",
      "listTime": "1535424203000",
      "lotSz": "1",
      "maxIcebergSz": "100000000.0000000000000000",
      "maxLmtAmt": "20000000",
      "maxLmtSz": "100000000",
      "maxMktAmt": "",
      "maxMktSz": "30000",
      "maxPlatOILmt": "",
      "maxStopSz": "30000",
      "maxTriggerSz": "100000000.0000000000000000",
      "maxTwapSz": "100000000.0000000000000000",
      "minSz": "1",
      "openType": "",
      "optType": "",
      "posLmtAmt": "",
      "posLmtPct": "",
      "preMktSwTime": "",
      "quoteCcy": "",
      "ruleType": "normal",
      "settleCcy": "BTC",
      "state": "live",
      "stk": "",
      "tickSz": "0.1",
      "tradeQuoteCcyList": [],
      "uly": "BTC-USD"
    },
    {
      "alias": "",
      "auctionEndTime": "",
      "baseCcy": "",
      "category": "1",
      "contTdSwTime": "",
      "ctMult": "1",
      "ctType": "linear",
      "ctVal": "0.1",
      "ctValCcy": "ETH",
      "expTime": "",
      "futureSettlement": false,
      "instFamily": "ETH-USDT",
      "instId": "ETH-USDT-SWAP",
      "instIdCode": 10461,
      "instType": "SWAP",
      "lever": "100",
      "listTime": "1573557408000",
      "lotSz": "0.01",
      "maxIcebergSz": "100000000.0000000000000000",
      "maxLmtAmt": "20000000",
      "maxLmtSz": "100000000",
      "maxMktAmt": "",
      "maxMktSz": "20000",
      "maxPlatOILmt": "",
      "maxStopSz": "20000",
      "maxTriggerSz": "100000000.0000000000000000",
      "maxTwapSz": "100000000.0000000000000000",
      "minSz": "0.01",
      "openType": "",
      "optType": "",
      "posLmtAmt": "",
      "posLmtPct": "",
      "preMktSwTime": "",
      "quoteCcy": "",
      "ruleType": "normal",
      "settleCcy": "USDT",
      "state": "live",
      "stk": "",
      "tickSz": "0.01",
      "tradeQuoteCcyList": [],
      "uly": "ETH-USDT"
    },
    {
      "alias": "",
      "auctionEndTime": "",
      "baseCcy": "",
      "category": "1",
      "contTdSwTime": "",
      "ctMult": "1",
      "ctType": "linear",
      "ctVal": "0.01",
      "ctValCcy": "BTC",
      "expTime": "",
      "futureSettlement": false,
      "instFamily": "BTC-USDT",
      "instId": "BTC-USDT-SWAP",
      "instIdCode": 10459,
      "instType": "SWAP",
      "lever": "100",
      "listTime": "1573557408000",
      "lotSz": "0.01",
      "maxIcebergSz": "100000000.0000000000000000",
      "maxLmtAmt": "20000000",
      "maxLmtSz": "100000000",
      "maxMktAmt": "",
      "maxMktSz": "12000",
      "maxPlatOILmt": "",
      "maxStopSz": "12000",
      "maxTriggerSz": "100000000.0000000000000000",
      "maxTwapSz": "100000000.0000000000000000",
      "minSz": "0.01",
      "openType": "",
      "optType": "",
      "posLmtAmt": "",
      "posLmtPct": "",
      "preMktSwTime": "",
      "quoteCcy": "",
      "ruleType": "normal",
      "settleCcy": "USDT",
      "state": "live",
      "stk": "",
      "tickSz": "0.1",
      "tradeQuoteCcyList": [],
      "uly": "BTC-USDT"
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


**Identifiers**: `BTC`, `ETH`, `SWAP`, `USD`, `USDT`

## Related Files

This file is located in `crates/adapters/okx/test_data/`. Related files may include:
- Other files in the same directory
- Test files in corresponding `tests/` directory
- Parent module files (`__init__.py`, `mod.rs`, etc.)

See the folder documentation for complete context.

## Testing and Usage

This appears to be a test file. Run tests using:
```bash
# For Python
pytest crates/adapters/okx/test_data/http_get_instruments_swap.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:55:00.544770Z*
