# Documentation: ws_execution.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/ws_execution.json`
- **Size**: 1,435 bytes
- **Lines**: 49
- **Language**: JSON

## Original Source

```json
{
    "execID": "550e8400-e29b-41d4-a716-446655440010",
    "orderID": "550e8400-e29b-41d4-a716-446655440002",
    "clOrdID": "mm_bitmex_2b/oemUeQ4CAJZgP3fjHsB",
    "clOrdLinkID": null,
    "account": 1234567,
    "symbol": "XBTUSD",
    "side": "Sell",
    "lastQty": 100,
    "lastPx": 98950.0,
    "underlyingLastPx": null,
    "lastMkt": "XBME",
    "lastLiquidityInd": "Added",
    "simpleOrderQty": null,
    "orderQty": 200,
    "price": 99000,
    "displayQty": null,
    "stopPx": null,
    "pegOffsetValue": null,
    "pegPriceType": null,
    "currency": "USD",
    "settlCurrency": "XBT",
    "execType": "Trade",
    "ordType": "Limit",
    "timeInForce": "GoodTillCancel",
    "execInst": "ParticipateDoNotInitiate",
    "contingencyType": null,
    "exDestination": "XBME",
    "ordStatus": "PartiallyFilled",
    "triggered": null,
    "workingIndicator": true,
    "ordRejReason": null,
    "simpleLeavesQty": null,
    "leavesQty": 100,
    "simpleCumQty": null,
    "cumQty": 100,
    "avgPx": 98950.0,
    "commission": 0.00075,
    "tradePublishIndicator": "PublishTrade",
    "multiLegReportingType": "SingleSecurity",
    "text": "Submitted via API.",
    "trdMatchID": "00000000-006d-1000-0000-000e8737d540",
    "execCost": -101065,
    "execComm": 76,
    "homeNotional": -0.00101065,
    "foreignNotional": 100.0,
    "transactTime": "2024-11-25T10:35:00.789Z",
    "timestamp": "2024-11-25T10:35:00.789Z"
}
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 15


**Identifiers**: `API`, `Added`, `GoodTillCancel`, `Limit`, `PartiallyFilled`, `ParticipateDoNotInitiate`, `PublishTrade`, `Sell`, `SingleSecurity`, `Submitted`, `Trade`, `USD`, `XBME`, `XBT`, `XBTUSD`

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
pytest crates/adapters/bitmex/test_data/ws_execution.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.110800Z*
