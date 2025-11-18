# Documentation: http_get_executions.json

## File Metadata

- **Path**: `crates/adapters/bitmex/test_data/http_get_executions.json`
- **Size**: 3,261 bytes
- **Lines**: 100
- **Language**: JSON

## Original Source

```json
[
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
        "settlCurrency": "XBt",
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
    },
    {
        "execID": "550e8400-e29b-41d4-a716-446655440011",
        "orderID": "550e8400-e29b-41d4-a716-446655440002",
        "clOrdID": "mm_bitmex_2b/oemUeQ4CAJZgP3fjHsB",
        "clOrdLinkID": null,
        "account": 1234567,
        "symbol": "XBTUSD",
        "side": "Sell",
        "lastQty": 100,
        "lastPx": 98951.0,
        "underlyingLastPx": null,
        "lastMkt": "XBME",
        "lastLiquidityInd": "Removed",
        "simpleOrderQty": null,
        "orderQty": 200,
        "price": 99000,
        "displayQty": null,
        "stopPx": null,
        "pegOffsetValue": null,
        "pegPriceType": null,
        "currency": "USD",
        "settlCurrency": "XBt",
        "execType": "Trade",
        "ordType": "Limit",
        "timeInForce": "GoodTillCancel",
        "execInst": "ParticipateDoNotInitiate",
        "contingencyType": null,
        "exDestination": "XBME",
        "ordStatus": "Filled",
        "triggered": null,
        "workingIndicator": false,
        "ordRejReason": null,
        "simpleLeavesQty": null,
        "leavesQty": 0,
        "simpleCumQty": null,
        "cumQty": 200,
        "avgPx": 98950.5,
        "commission": 0.00075,
        "tradePublishIndicator": "PublishTrade",
        "multiLegReportingType": "SingleSecurity",
        "text": "Submitted via API.",
        "trdMatchID": "00000000-006d-1000-0000-000e8737d541",
        "execCost": -101055,
        "execComm": 151,
        "homeNotional": -0.00101055,
        "foreignNotional": 100.0,
        "transactTime": "2024-11-25T10:35:01.123Z",
        "timestamp": "2024-11-25T10:35:01.123Z"
    }
]
```

## High-Level Overview

This file is part of the NautilusTrader repository. This is a JSON data file.

## Detailed Walkthrough

This file contains implementation details. See the source code above for complete information.


## Keywords and Identifiers

Total unique keywords extracted: 17


**Identifiers**: `API`, `Added`, `Filled`, `GoodTillCancel`, `Limit`, `PartiallyFilled`, `ParticipateDoNotInitiate`, `PublishTrade`, `Removed`, `Sell`, `SingleSecurity`, `Submitted`, `Trade`, `USD`, `XBME`, `XBTUSD`, `XBt`

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
pytest crates/adapters/bitmex/test_data/http_get_executions.json

# For Rust
cargo test --package <package-name>
```

## Performance and Security Considerations

No specific security or performance concerns identified. Follow general best practices.

---
*Generated on 2025-11-18T21:54:59.102491Z*
