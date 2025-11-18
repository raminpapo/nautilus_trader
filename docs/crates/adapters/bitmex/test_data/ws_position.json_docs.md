# Documentation: ws_position.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_position.json`
- **Size**: 2,293 bytes
- **Lines**: 88
- **Language**: JSON

## Original Source

```json
{
    "account": 1234567,
    "symbol": "XBTUSD",
    "currency": "XBT",
    "underlying": "XBT",
    "quoteCurrency": "USD",
    "commission": 0.00075,
    "initMarginReq": 0.01,
    "maintMarginReq": 0.005,
    "riskLimit": 20000000000,
    "leverage": 100,
    "crossMargin": false,
    "deleveragePercentile": 0.9999,
    "rebalancedPnl": 0,
    "prevRealisedPnl": 0,
    "prevUnrealisedPnl": 0,
    "prevClosePrice": 98000.0,
    "openingTimestamp": "2024-11-25T00:00:00.000Z",
    "openingQty": 0,
    "openingCost": 0,
    "openingComm": 0,
    "openOrderBuyQty": 0,
    "openOrderBuyCost": 0,
    "openOrderBuyPremium": 0,
    "openOrderSellQty": 0,
    "openOrderSellCost": 0,
    "openOrderSellPremium": 0,
    "execBuyQty": 1000,
    "execBuyCost": -1020408,
    "execSellQty": 0,
    "execSellCost": 0,
    "execQty": 1000,
    "execCost": -1020408,
    "execComm": 765,
    "currentTimestamp": "2024-11-25T10:35:00.789Z",
    "currentQty": 1000,
    "currentCost": -1020408,
    "currentComm": 765,
    "realisedCost": 0,
    "unrealisedCost": -1020408,
    "grossOpenCost": 0,
    "grossOpenPremium": 0,
    "grossExecCost": 1020408,
    "isOpen": true,
    "markPrice": 98500.0,
    "markValue": -1015228,
    "riskValue": 1015228,
    "homeNotional": 0.01015228,
    "foreignNotional": 1000.0,
    "posState": "",
    "posCost": -1020408,
    "posCost2": -1020408,
    "posCross": 10204,
    "posInit": 10204,
    "posComm": 765,
    "posLoss": 0,
    "posMargin": 10969,
    "posMaint": 5867,
    "posAllowance": 0,
    "taxableMargin": 0,
    "initMargin": 0,
    "maintMargin": 15949,
    "sessionMargin": 0,
    "targetExcessMargin": 0,
    "varMargin": 0,
    "realisedGrossPnl": 0,
    "realisedTax": 0,
    "realisedPnl": -765,
    "unrealisedGrossPnl": 5180,
    "longBankrupt": 0,
    "shortBankrupt": 0,
    "taxBase": 0,
    "indicativeTaxRate": 0,
    "indicativeTax": 0,
    "unrealisedTax": 0,
    "unrealisedPnl": 5180,
    "unrealisedPnlPcnt": 0.5074,
    "unrealisedRoePcnt": 50.7353,
    "avgCostPrice": 98039.5,
    "avgEntryPrice": 98039.5,
    "breakEvenPrice": 98117.0,
    "marginCallPrice": 2509.5,
    "liquidationPrice": 1255.0,
    "bankruptPrice": 0,
    "timestamp": "2024-11-25T10:35:00.789Z",
    "lastPrice": 98500.0,
    "lastValue": -1015228
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 3


**Identifiers**: `USD`, `XBT`, `XBTUSD`

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
pytest crates/adapters/bitmex/test_data/ws_position.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.121159Z*
